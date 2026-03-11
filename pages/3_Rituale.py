from __future__ import annotations

from celestia_app.content import RITUAL_SCHEDULE, RITUAL_STEPS
from celestia_app.ui import (
    apply_styles,
    get_copy,
    render_cta_band,
    render_footer,
    render_info_cards,
    render_page_intro,
    render_ritual_steps,
    render_topbar,
    set_page_config,
)

set_page_config("Celestia | Rituale")
apply_styles()
lang, text = render_topbar("pages/3_Rituale.py")
copy = get_copy(lang)
page = copy["rituals_page"]

render_page_intro(page["eyebrow"], page["title"], page["lead"])
render_ritual_steps(RITUAL_STEPS, lang, columns=3)

render_page_intro(page["eyebrow"], page["schedule_title"], "")
render_info_cards(RITUAL_SCHEDULE, lang, columns=2)

render_cta_band(
    copy["home"]["cta_headline"],
    copy["home"]["cta_text"],
    copy["common"]["shop_now"],
    "pages/2_Bestseller.py",
)
render_footer(copy)

