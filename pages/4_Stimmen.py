from __future__ import annotations

import streamlit as st

from celestia_app.content import FAQS, METRICS, REVIEWS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_cta_band,
    render_footer,
    render_metrics,
    render_page_intro,
    render_reviews,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Stimmen")
apply_styles()
lang, text = render_topbar("pages/4_Stimmen.py")
copy = get_copy(lang)
page = copy["reviews_page"]

render_page_intro(page["eyebrow"], page["title"], page["lead"])
render_metrics(METRICS, lang)
render_reviews(REVIEWS, lang, columns=3)

render_page_intro(page["eyebrow"], page["faq_title"], "")
for faq in FAQS:
    with st.expander(faq["q"][lang]):
        st.write(faq["a"][lang])

render_cta_band(
    copy["home"]["cta_headline"],
    copy["home"]["cta_text"],
    copy["common"]["newsletter_cta"],
    "pages/5_Kontakt.py",
)
render_footer(copy)

