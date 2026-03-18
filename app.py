from __future__ import annotations

import base64
import re
from pathlib import Path
from shutil import copy2
from urllib.parse import urlparse

import streamlit as st

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
ASSETS_DIR = ROOT / "assets"

SOURCE_FILES = [
    "index.html",
    "collections.html",
    "products.html",
    "rituals.html",
    "reviews.html",
    "family.html",
    "contact.html",
    "styles.css",
    "script.js",
]

PAGE_MAP = {
    "home": "index.html",
    "index": "index.html",
    "collections": "collections.html",
    "products": "products.html",
    "rituals": "rituals.html",
    "reviews": "reviews.html",
    "family": "family.html",
    "contact": "contact.html",
}

FILE_TO_PAGE = {
    "index.html": "index",
    "collections.html": "collections",
    "products.html": "products",
    "rituals.html": "rituals",
    "reviews.html": "reviews",
    "family.html": "family",
    "contact.html": "contact",
}

INTERNAL_FILES = tuple(FILE_TO_PAGE.keys())
ASSET_SRC_PATTERN = re.compile(
    r"""src=(["'])assets/([^"']+)\1""",
    re.IGNORECASE,
)


def build_static_assets_prefix() -> str:
    base_url_path = st.get_option("server.baseUrlPath") or ""
    base_url_path = str(base_url_path).strip("/")
    if base_url_path:
        return f"/{base_url_path}/app/static/assets/"
    return "/app/static/assets/"


def copy_if_changed(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        copy2(source, destination)
        return

    source_stat = source.stat()
    destination_stat = destination.stat()
    if (
        source_stat.st_mtime_ns != destination_stat.st_mtime_ns
        or source_stat.st_size != destination_stat.st_size
    ):
        copy2(source, destination)


def sync_static_content() -> None:
    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    for file_name in SOURCE_FILES:
        source = ROOT / file_name
        if source.exists():
            copy_if_changed(source, STATIC_DIR / file_name)

    if ASSETS_DIR.exists():
        for source_asset in ASSETS_DIR.rglob("*"):
            if source_asset.is_dir():
                continue
            relative_path = source_asset.relative_to(ASSETS_DIR)
            destination_asset = STATIC_DIR / "assets" / relative_path
            copy_if_changed(source_asset, destination_asset)


def resolve_page_file() -> str:
    raw = st.query_params.get("page", "index")
    page_key = raw[0] if isinstance(raw, list) else raw
    page_key = str(page_key).strip().lower()
    return PAGE_MAP.get(page_key, "index.html")


def resolve_lang() -> str | None:
    raw = st.query_params.get("lang")
    lang = raw[0] if isinstance(raw, list) else raw
    lang = (str(lang).strip().lower() if lang is not None else "")
    return lang if lang in {"de", "en"} else None


def rewrite_internal_links(html: str) -> str:
    pattern = re.compile(r'<a\b[^>]*\bhref="([^"]+)"[^>]*>', re.IGNORECASE)

    def _replace(match: re.Match[str]) -> str:
        anchor_tag = match.group(0)
        href = match.group(1)
        parsed = urlparse(href)
        path = parsed.path.split("/")[-1].lower()
        if path not in INTERNAL_FILES:
            return anchor_tag

        page_key = FILE_TO_PAGE[path]
        replacement_href = f"?page={page_key}"
        return anchor_tag.replace(f'href="{href}"', f'href="{replacement_href}"')

    return pattern.sub(_replace, html)


def inline_svg_assets(html: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        quote = match.group(1)
        relative_path = match.group(2)
        if not relative_path.lower().endswith(".svg"):
            return match.group(0)

        asset_path = ASSETS_DIR / relative_path
        if not asset_path.exists() or not asset_path.is_file():
            return match.group(0)

        svg_data_uri = (
            "data:image/svg+xml;base64,"
            + base64.b64encode(asset_path.read_bytes()).decode("ascii")
        )
        return f"src={quote}{svg_data_uri}{quote}"

    return ASSET_SRC_PATTERN.sub(_replace, html)


def get_assets_mtime_ns() -> int:
    if not ASSETS_DIR.exists():
        return 0

    latest = 0
    for path in ASSETS_DIR.rglob("*"):
        if not path.is_file():
            continue
        stat = path.stat().st_mtime_ns
        if stat > latest:
            latest = stat
    return latest


@st.cache_data(show_spinner=False)
def get_logo_data_uri(logo_mtime_ns: int) -> str | None:
    _ = logo_mtime_ns
    logo_path = ASSETS_DIR / "celestia-logo.png"
    if not logo_path.exists():
        return None

    logo_b64 = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{logo_b64}"


def build_embedded_html(page_file: str) -> str:
    html_path = ROOT / page_file
    if not html_path.exists():
        html_path = ROOT / "index.html"

    html_content = html_path.read_text(encoding="utf-8")
    css_content = (ROOT / "styles.css").read_text(encoding="utf-8")
    js_content = (ROOT / "script.js").read_text(encoding="utf-8")

    html_content = re.sub(
        r'<link[^>]*href="styles\.css"[^>]*>\s*',
        "",
        html_content,
        flags=re.IGNORECASE,
    )
    html_content = re.sub(
        r'<script[^>]*src="script\.js"[^>]*>\s*</script>\s*',
        "",
        html_content,
        flags=re.IGNORECASE,
    )

    logo_path = ASSETS_DIR / "celestia-logo.png"
    logo_data_uri = get_logo_data_uri(logo_path.stat().st_mtime_ns if logo_path.exists() else 0)
    if logo_data_uri:
        html_content = html_content.replace(
            'src="assets/celestia-logo.png"',
            f'src="{logo_data_uri}"',
        )
        html_content = html_content.replace(
            "src='assets/celestia-logo.png'",
            f"src='{logo_data_uri}'",
        )

    html_content = inline_svg_assets(html_content)

    static_assets_prefix = build_static_assets_prefix()
    html_content = html_content.replace('src="assets/', f'src="{static_assets_prefix}')
    html_content = html_content.replace("src='assets/", f"src='{static_assets_prefix}")
    html_content = rewrite_internal_links(html_content)

    html_content = html_content.replace(
        "</head>",
        f"<style>{css_content}</style></head>",
    )
    html_content = html_content.replace(
        "</body>",
        f"<script>{js_content}</script></body>",
    )

    return html_content


@st.cache_data(show_spinner=False)
def get_embedded_html_cached(
    page_file: str,
    page_mtime_ns: int,
    css_mtime_ns: int,
    js_mtime_ns: int,
    logo_mtime_ns: int,
    assets_mtime_ns: int,
) -> str:
    # The mtime arguments are cache keys to refresh immediately on file changes.
    _ = (page_mtime_ns, css_mtime_ns, js_mtime_ns, logo_mtime_ns, assets_mtime_ns)
    return build_embedded_html(page_file)


st.set_page_config(
    page_title="Celestia",
    page_icon="*",
    layout="wide",
    initial_sidebar_state="collapsed",
)

sync_static_content()

page_file = resolve_page_file()
lang = resolve_lang()
page_path = ROOT / page_file
css_path = ROOT / "styles.css"
js_path = ROOT / "script.js"
logo_path = ASSETS_DIR / "celestia-logo.png"
css_mtime_ns = css_path.stat().st_mtime_ns if css_path.exists() else 0
js_mtime_ns = js_path.stat().st_mtime_ns if js_path.exists() else 0
logo_mtime_ns = logo_path.stat().st_mtime_ns if logo_path.exists() else 0
assets_mtime_ns = get_assets_mtime_ns()

for candidate_file in INTERNAL_FILES:
    candidate_path = ROOT / candidate_file
    get_embedded_html_cached(
        page_file=candidate_file,
        page_mtime_ns=candidate_path.stat().st_mtime_ns if candidate_path.exists() else 0,
        css_mtime_ns=css_mtime_ns,
        js_mtime_ns=js_mtime_ns,
        logo_mtime_ns=logo_mtime_ns,
        assets_mtime_ns=assets_mtime_ns,
    )

embedded_html = get_embedded_html_cached(
    page_file=page_file,
    page_mtime_ns=page_path.stat().st_mtime_ns if page_path.exists() else 0,
    css_mtime_ns=css_mtime_ns,
    js_mtime_ns=js_mtime_ns,
    logo_mtime_ns=logo_mtime_ns,
    assets_mtime_ns=assets_mtime_ns,
)

query: dict[str, str] = {}
if lang:
    query["lang"] = lang
if query:
    query_script = f"""
    <script>
      (function() {{
        try {{
          if ({repr(lang)} === "de" || {repr(lang)} === "en") {{
            localStorage.setItem("celestia-lang", {repr(lang)});
          }}
        }} catch (e) {{}}
      }})();
    </script>
    """
    embedded_html = embedded_html.replace("</head>", f"{query_script}</head>")

st.markdown(
    """
    <style>
      #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
      [data-testid="stSidebar"] { display: none; }
      .block-container { max-width: 100%; padding: 0; }
      [data-testid="stAppViewContainer"] { background: #060402; overflow-x: hidden; }
      .celestia-shell {
        border: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.html(embedded_html, width="stretch", unsafe_allow_javascript=True)
