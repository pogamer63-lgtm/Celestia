from __future__ import annotations

import streamlit as st

from celestia_app.content import CONTACT_FACTS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_footer,
    render_info_cards,
    render_page_intro,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Kontakt")
apply_styles()
lang, text = render_topbar("pages/5_Kontakt.py")
copy = get_copy(lang)
page = copy["contact_page"]

render_page_intro(page["eyebrow"], page["title"], page["lead"])
render_info_cards(CONTACT_FACTS, lang, columns=3)

st.markdown(
    f"""
    <section class="cel-section-head">
      <p class="cel-eyebrow">{page["eyebrow"]}</p>
      <h2>{page["form_title"]}</h2>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.form("contact_form"):
    name = st.text_input(page["name"])
    email = st.text_input(page["email"])
    message = st.text_area(page["message"], height=140)
    submitted = st.form_submit_button(page["submit"], width="stretch")

if submitted:
    if name.strip() and email.strip() and message.strip():
        st.success(page["success"])
    else:
        st.warning("Bitte alle Felder ausfuellen." if lang == "DE" else "Please fill in all fields.")

render_footer(copy)
