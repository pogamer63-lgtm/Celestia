from __future__ import annotations

from celestia_app.content import CATEGORIES, METRICS, PRODUCTS, REVIEWS, RITUAL_STEPS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_category_grid,
    render_cta_band,
    render_footer,
    render_home_hero,
    render_metrics,
    render_page_intro,
    render_product_grid,
    render_reviews,
    render_ritual_steps,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Start")
apply_styles()
lang, text = render_topbar("streamlit_app.py")
copy = get_copy(lang)

render_home_hero(lang, copy)
render_metrics(METRICS, lang)

render_page_intro(copy["home"]["eyebrow"], copy["home"]["collections_headline"], "")
render_category_grid(CATEGORIES, lang, columns=3)

render_page_intro(copy["home"]["eyebrow"], copy["home"]["products_headline"], "")
render_product_grid(PRODUCTS, lang, copy["common"]["buy_now"], columns=3)

render_page_intro(copy["home"]["eyebrow"], copy["home"]["ritual_headline"], "")
render_ritual_steps(RITUAL_STEPS, lang, columns=3)

render_page_intro(copy["home"]["eyebrow"], copy["home"]["reviews_headline"], "")
render_reviews(REVIEWS, lang, columns=3)

render_cta_band(
    copy["home"]["cta_headline"],
    copy["home"]["cta_text"],
    copy["common"]["newsletter_cta"],
    "pages/5_Kontakt.py",
)
render_footer(copy)

