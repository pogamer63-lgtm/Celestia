from __future__ import annotations

from celestia_app.content import CATEGORIES, FOCUS_AREAS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_category_grid,
    render_cta_band,
    render_footer,
    render_info_cards,
    render_page_intro,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Kollektionen")
apply_styles()
lang, text = render_topbar("pages/1_Kollektionen.py")
copy = get_copy(lang)
page = copy["collections_page"]

render_page_intro(page["eyebrow"], page["title"], page["lead"])
render_category_grid(CATEGORIES, lang, columns=3)

render_page_intro(page["eyebrow"], page["focus_title"], "")
render_info_cards(FOCUS_AREAS, lang, columns=3)

render_cta_band(
    copy["home"]["cta_headline"],
    copy["home"]["cta_text"],
    copy["common"]["shop_now"],
    "pages/2_Bestseller.py",
)
render_footer(copy)

