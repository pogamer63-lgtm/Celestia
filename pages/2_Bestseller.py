from __future__ import annotations

from celestia_app.content import PRODUCT_BENEFITS, PRODUCTS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_cta_band,
    render_footer,
    render_info_cards,
    render_page_intro,
    render_product_grid,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Bestseller")
apply_styles()
lang, text = render_topbar("pages/2_Bestseller.py")
copy = get_copy(lang)
page = copy["products_page"]

render_page_intro(page["eyebrow"], page["title"], page["lead"])
render_product_grid(PRODUCTS, lang, copy["common"]["buy_now"], columns=3)

render_page_intro(page["eyebrow"], page["benefits_title"], "")
render_info_cards(PRODUCT_BENEFITS, lang, columns=3)

render_cta_band(
    copy["home"]["cta_headline"],
    copy["home"]["cta_text"],
    copy["common"]["view_rituals"],
    "pages/3_Rituale.py",
)
render_footer(copy)

