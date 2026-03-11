from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st

from .content import COPY, LANGUAGE_OPTIONS, NAV_ITEMS
from .styles import GLOBAL_CSS

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = ROOT_DIR / "assets" / "celestia-logo.png"


def set_page_config(page_title: str) -> None:
    st.set_page_config(
        page_title=page_title,
        page_icon="*",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def ensure_state() -> None:
    if "lang" not in st.session_state:
        st.session_state["lang"] = "DE"


def get_lang() -> str:
    ensure_state()
    lang = st.session_state.get("lang", "DE")
    return lang if lang in COPY else "DE"


def get_copy(lang: str) -> dict:
    return COPY.get(lang, COPY["DE"])


def apply_styles() -> None:
    st.markdown(f"<style>{GLOBAL_CSS}</style>", unsafe_allow_html=True)


def render_topbar(current_page: str) -> tuple[str, dict]:
    lang = get_lang()
    text = get_copy(lang)

    top_cols = st.columns([4.5, 1.2], gap="large", vertical_alignment="center")
    with top_cols[0]:
        st.markdown(
            f"""
            <div class="cel-brand">
              <span class="cel-brand-star">*</span>
              <div class="cel-brand-copy">
                <div class="cel-brand-name">{text["brand"]["name"]}</div>
                <div class="cel-brand-tag">{text["brand"]["tagline"]}</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top_cols[1]:
        selected_lang = st.selectbox(
            text["meta"]["language_label"],
            options=list(LANGUAGE_OPTIONS.keys()),
            format_func=lambda key: LANGUAGE_OPTIONS[key],
            key="global_language",
        )

    if selected_lang != lang:
        st.session_state["lang"] = selected_lang
        st.rerun()

    lang = get_lang()
    text = get_copy(lang)

    first_row = NAV_ITEMS[:3]
    second_row = NAV_ITEMS[3:]
    _render_nav_row(first_row, current_page, text)
    _render_nav_row(second_row, current_page, text)

    st.markdown(
        f"<p class='cel-nav-hint'>{text['meta']['active_nav_prefix']} {text['nav'][_page_key(current_page)]}</p>",
        unsafe_allow_html=True,
    )

    return lang, text


def _render_nav_row(row: list[tuple[str, str]], current_page: str, text: dict) -> None:
    cols = st.columns(len(row), gap="small")
    for col, (page_path, nav_key) in zip(cols, row):
        label = text["nav"][nav_key]
        if page_path == current_page:
            label = f"{text['meta']['active_nav_prefix']} {label}"
        with col:
            st.page_link(page_path, label=label, width="stretch")


def _page_key(page_path: str) -> str:
    for known_path, key in NAV_ITEMS:
        if known_path == page_path:
            return key
    return "home"


def render_page_intro(eyebrow: str, title: str, lead: str) -> None:
    st.markdown(
        f"""
        <section class="cel-section-head">
          <p class="cel-eyebrow">{eyebrow}</p>
          <h2>{title}</h2>
          <p class="cel-section-copy">{lead}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_home_hero(lang: str, text: dict) -> None:
    home = text["home"]

    left_col, right_col = st.columns([1.25, 0.95], gap="large", vertical_alignment="center")
    with left_col:
        st.markdown(
            f"""
            <section class="cel-hero">
              <p class="cel-eyebrow">{home["eyebrow"]}</p>
              <h1 class="cel-title">{home["title"]}</h1>
              <p class="cel-lead">{home["lead"]}</p>
              <p class="cel-note">{home["secondary_copy"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )
        cta_cols = st.columns(2, gap="small")
        with cta_cols[0]:
            if st.button(home["cta_primary"], width="stretch", key="home_cta_primary"):
                st.switch_page("pages/2_Bestseller.py")
        with cta_cols[1]:
            if st.button(home["cta_secondary"], width="stretch", key="home_cta_secondary"):
                st.switch_page("pages/3_Rituale.py")

    with right_col:
        st.markdown("<div class='cel-logo-shell'>", unsafe_allow_html=True)
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), width="stretch")
        else:
            st.markdown(
                "<p class='cel-lead'>Logo fehlt: assets/celestia-logo.png</p>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


def render_metrics(metrics: list[dict], lang: str) -> None:
    cols = st.columns(len(metrics), gap="small")
    for col, item in zip(cols, metrics):
        with col:
            st.markdown(
                f"""
                <article class="cel-metric-card">
                  <div class="cel-metric-value">{item["value"]}</div>
                  <div class="cel-metric-label">{item["label"][lang]}</div>
                </article>
                """,
                unsafe_allow_html=True,
            )


def render_category_grid(items: list[dict], lang: str, columns: int = 3) -> None:
    _render_grid(
        items,
        columns,
        lambda item: f"""
            <article class="cel-card">
              <span class="cel-card-badge">{item["badge"]}</span>
              <h3>{item["title"][lang]}</h3>
              <p>{item["text"][lang]}</p>
            </article>
        """,
    )


def render_product_grid(items: list[dict], lang: str, buy_label: str, columns: int = 3) -> None:
    _render_grid(
        items,
        columns,
        lambda item: f"""
            <article class="cel-product-card">
              <div class="cel-product-media media-{item["palette"]}"></div>
              <div class="cel-product-body">
                <h3>{item["name"][lang]}</h3>
                <p>{item["text"][lang]}</p>
                <div class="cel-price-row">
                  <span class="cel-price">{item["price"]}</span>
                  <span class="cel-pill">{buy_label}</span>
                </div>
              </div>
            </article>
        """,
    )


def render_ritual_steps(steps: list[dict], lang: str, columns: int = 3) -> None:
    _render_grid(
        steps,
        columns,
        lambda item: f"""
            <article class="cel-step-card">
              <span class="cel-step-no">{item["step"]}</span>
              <h3>{item["title"][lang]}</h3>
              <p>{item["text"][lang]}</p>
            </article>
        """,
    )


def render_info_cards(items: list[dict], lang: str, columns: int = 3) -> None:
    _render_grid(
        items,
        columns,
        lambda item: f"""
            <article class="cel-info-card">
              <h3>{item["title"][lang]}</h3>
              <p>{item["text"][lang]}</p>
            </article>
        """,
    )


def render_reviews(items: list[dict], lang: str, columns: int = 3) -> None:
    _render_grid(
        items,
        columns,
        lambda item: f"""
            <article class="cel-review-card">
              <p>"{item["text"][lang]}"</p>
              <div class="cel-review-author">- {item["author"]}</div>
            </article>
        """,
    )


def render_cta_band(title: str, text: str, button_text: str, target_page: str) -> None:
    st.markdown(
        f"""
        <section class="cel-cta-band">
          <h3>{title}</h3>
          <p>{text}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    cta_cols = st.columns([0.35, 0.3, 0.35])
    with cta_cols[1]:
        if st.button(button_text, width="stretch", key=f"cta_{target_page}"):
            st.switch_page(target_page)


def render_footer(text: dict) -> None:
    footer = text["footer"]
    cols = st.columns([1.7, 1, 1, 1], gap="small")
    with cols[0]:
        st.markdown(
            f"""
            <section class="cel-footer">
              <h4>{footer["about_title"]}</h4>
              <p>{footer["about_text"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    _render_footer_col(cols[1], footer["shop_title"], footer["shop_links"])
    _render_footer_col(cols[2], footer["service_title"], footer["service_links"])
    _render_footer_col(cols[3], footer["legal_title"], footer["legal_links"])


def _render_footer_col(col, heading: str, items: Iterable[str]) -> None:
    li_items = "".join(f"<li>{item}</li>" for item in items)
    with col:
        st.markdown(
            f"""
            <section class="cel-footer">
              <h4>{heading}</h4>
              <ul>{li_items}</ul>
            </section>
            """,
            unsafe_allow_html=True,
        )


def _render_grid(items: list[dict], columns: int, renderer) -> None:
    for row in _chunked(items, columns):
        cols = st.columns(columns, gap="small")
        for idx, col in enumerate(cols):
            with col:
                if idx < len(row):
                    st.markdown(renderer(row[idx]), unsafe_allow_html=True)


def _chunked(items: list[dict], size: int) -> list[list[dict]]:
    return [items[i : i + size] for i in range(0, len(items), size)]
