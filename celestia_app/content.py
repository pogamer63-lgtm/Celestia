from __future__ import annotations

NAV_ITEMS = [
    ("streamlit_app.py", "home"),
    ("pages/1_Kollektionen.py", "collections"),
    ("pages/2_Bestseller.py", "products"),
    ("pages/3_Rituale.py", "rituals"),
    ("pages/4_Stimmen.py", "reviews"),
    ("pages/5_Kontakt.py", "contact"),
]

LANGUAGE_OPTIONS = {
    "DE": "Deutsch",
    "EN": "English",
}

COPY = {
    "DE": {
        "meta": {
            "app_title": "Celestia | Premium Heilsteine",
            "language_label": "Sprache",
            "active_nav_prefix": "*",
        },
        "brand": {
            "name": "CELESTIA",
            "tagline": "Ritual Collection",
        },
        "nav": {
            "home": "Start",
            "collections": "Kollektionen",
            "products": "Bestseller",
            "rituals": "Rituale",
            "reviews": "Stimmen",
            "contact": "Kontakt",
        },
        "common": {
            "shop_now": "Jetzt shoppen",
            "learn_more": "Mehr erfahren",
            "view_rituals": "Rituale ansehen",
            "newsletter_cta": "Zum Newsletter",
            "buy_now": "In den Warenkorb",
        },
        "home": {
            "eyebrow": "Celestia Ritual Collection",
            "title": "Heilsteine, die Energie sichtbar machen.",
            "lead": (
                "Fuer Fokus, Schutz, Herzoeffnung und Manifestation: "
                "entdecke kuratierte Edelsteine in Premium-Qualitaet."
            ),
            "secondary_copy": (
                "Jedes Set wird bei Celestia handverlesen, energetisch abgestimmt "
                "und mit klaren Ritualanleitungen geliefert."
            ),
            "cta_primary": "Bestseller ansehen",
            "cta_secondary": "Rituale entdecken",
            "collections_headline": "Kollektionen fuer jede Lebensphase",
            "products_headline": "Unsere Signature Heilstein-Sets",
            "ritual_headline": "Dein 3-Schritte Ritual fuer sofortige Wirkung",
            "reviews_headline": "Was unsere Community berichtet",
            "cta_headline": "10% Willkommensrabatt + exklusive Mondrituale",
            "cta_text": (
                "Trage dich ein und erhalte limitierte Drops, Guides und Ritual-Impulse "
                "direkt in dein Postfach."
            ),
        },
        "collections_page": {
            "eyebrow": "Shop by Intention",
            "title": "Finde die passende Energie-Kollektion",
            "lead": (
                "Waehle dein Thema und starte mit abgestimmten Heilsteinen, "
                "Ritualkarten und klaren Tagesimpulsen."
            ),
            "focus_title": "Beliebte Fokusbereiche",
        },
        "products_page": {
            "eyebrow": "Bestseller",
            "title": "Die meistgekauften Celestia Sets",
            "lead": (
                "Unsere Bestseller kombinieren Qualitaet, Design und klare Anwendung "
                "fuer Alltag, Arbeit und spirituelle Praxis."
            ),
            "benefits_title": "Warum Kunden hier kaufen",
        },
        "rituals_page": {
            "eyebrow": "Celestia Method",
            "title": "Rituale, die in den Alltag passen",
            "lead": (
                "Mit unserem 3-Schritte System baust du in wenigen Minuten "
                "pro Tag eine kraftvolle Energie-Routine auf."
            ),
            "schedule_title": "Ritual-Plan fuer deine Woche",
        },
        "reviews_page": {
            "eyebrow": "Community",
            "title": "Stimmen aus dem Celestia Circle",
            "lead": (
                "Echte Erfahrungswerte von Kunden, die Celestia in ihren Alltag "
                "integriert haben."
            ),
            "faq_title": "Haeufige Fragen",
        },
        "contact_page": {
            "eyebrow": "Kontakt & Service",
            "title": "Wir begleiten dich bei der Produktauswahl",
            "lead": (
                "Fragen zu Steinen, Ritualen, Versand oder Geschenkboxen? "
                "Unser Team antwortet innerhalb von 24 Stunden."
            ),
            "form_title": "Schreibe uns direkt",
            "name": "Name",
            "email": "E-Mail",
            "message": "Nachricht",
            "submit": "Anfrage senden",
            "success": "Danke! Wir melden uns schnellstmoeglich bei dir.",
        },
        "footer": {
            "about_title": "CELESTIA",
            "about_text": "Premium Heilsteine fuer moderne Rituale, Klarheit und Ausrichtung.",
            "shop_title": "Shop",
            "service_title": "Service",
            "legal_title": "Rechtliches",
            "shop_links": ["Bestseller", "Kollektionen", "Rituale"],
            "service_links": ["Versand", "Retouren", "Kontakt"],
            "legal_links": ["Impressum", "Datenschutz", "AGB"],
        },
    },
    "EN": {
        "meta": {
            "app_title": "Celestia | Premium Crystal Shop",
            "language_label": "Language",
            "active_nav_prefix": "*",
        },
        "brand": {
            "name": "CELESTIA",
            "tagline": "Ritual Collection",
        },
        "nav": {
            "home": "Home",
            "collections": "Collections",
            "products": "Bestsellers",
            "rituals": "Rituals",
            "reviews": "Reviews",
            "contact": "Contact",
        },
        "common": {
            "shop_now": "Shop now",
            "learn_more": "Learn more",
            "view_rituals": "View rituals",
            "newsletter_cta": "Join newsletter",
            "buy_now": "Add to cart",
        },
        "home": {
            "eyebrow": "Celestia Ritual Collection",
            "title": "Healing crystals that make energy visible.",
            "lead": (
                "For focus, protection, heart opening, and manifestation: "
                "discover curated premium crystal sets."
            ),
            "secondary_copy": (
                "Each Celestia set is hand-selected, energetically aligned, "
                "and delivered with clear ritual guidance."
            ),
            "cta_primary": "Browse bestsellers",
            "cta_secondary": "Explore rituals",
            "collections_headline": "Collections for every life chapter",
            "products_headline": "Our signature crystal sets",
            "ritual_headline": "Your 3-step ritual for immediate impact",
            "reviews_headline": "What our community says",
            "cta_headline": "10% welcome discount + exclusive moon rituals",
            "cta_text": (
                "Join our list for limited drops, practical guides, and "
                "high-energy rituals delivered to your inbox."
            ),
        },
        "collections_page": {
            "eyebrow": "Shop by Intention",
            "title": "Find the energy collection that fits your phase",
            "lead": (
                "Choose your theme and start with aligned crystals, ritual cards, "
                "and focused daily prompts."
            ),
            "focus_title": "Most selected focus areas",
        },
        "products_page": {
            "eyebrow": "Bestsellers",
            "title": "The most loved Celestia sets",
            "lead": (
                "Our bestsellers combine quality, design, and practical usage "
                "for daily rituals and work life."
            ),
            "benefits_title": "Why customers buy here",
        },
        "rituals_page": {
            "eyebrow": "Celestia Method",
            "title": "Rituals that fit real routines",
            "lead": (
                "With our 3-step method you can build a powerful daily "
                "energy routine in just minutes."
            ),
            "schedule_title": "Your weekly ritual schedule",
        },
        "reviews_page": {
            "eyebrow": "Community",
            "title": "Voices from the Celestia Circle",
            "lead": (
                "Real experiences from customers who integrated Celestia "
                "into their routine."
            ),
            "faq_title": "Frequently asked questions",
        },
        "contact_page": {
            "eyebrow": "Contact & Service",
            "title": "We help you choose the right products",
            "lead": (
                "Questions about crystals, rituals, shipping, or gift boxes? "
                "Our team replies within 24 hours."
            ),
            "form_title": "Send us a message",
            "name": "Name",
            "email": "Email",
            "message": "Message",
            "submit": "Send request",
            "success": "Thank you! We will get back to you very soon.",
        },
        "footer": {
            "about_title": "CELESTIA",
            "about_text": "Premium crystals for modern rituals, clarity, and alignment.",
            "shop_title": "Shop",
            "service_title": "Service",
            "legal_title": "Legal",
            "shop_links": ["Bestsellers", "Collections", "Rituals"],
            "service_links": ["Shipping", "Returns", "Contact"],
            "legal_links": ["Imprint", "Privacy", "Terms"],
        },
    },
}

METRICS = [
    {
        "value": "12,000+",
        "label": {"DE": "zufriedene Kunden", "EN": "happy customers"},
    },
    {
        "value": "97%",
        "label": {"DE": "Weiterempfehlung", "EN": "would recommend"},
    },
    {
        "value": "48h",
        "label": {"DE": "Versandfenster", "EN": "shipping window"},
    },
    {
        "value": "4.9/5",
        "label": {"DE": "Durchschnittsbewertung", "EN": "average rating"},
    },
]

CATEGORIES = [
    {
        "badge": "MOON",
        "title": {"DE": "Moon Ritual", "EN": "Moon Ritual"},
        "text": {
            "DE": "Steine fuer Neumond- und Vollmondarbeit inklusive Journaling-Guide.",
            "EN": "Crystals for new and full moon practice, including a journaling guide.",
        },
    },
    {
        "badge": "MANIFEST",
        "title": {"DE": "Manifestation", "EN": "Manifestation"},
        "text": {
            "DE": "Citrin, Pyrit und Bergkristall fuer Klarheit und Zielausrichtung.",
            "EN": "Citrine, pyrite, and clear quartz for clarity and aligned goals.",
        },
    },
    {
        "badge": "HEART",
        "title": {"DE": "Heart Healing", "EN": "Heart Healing"},
        "text": {
            "DE": "Rosenquarz, Rhodonit und Mondstein fuer Selbstwert und Herzenergie.",
            "EN": "Rose quartz, rhodonite, and moonstone for self-worth and heart energy.",
        },
    },
    {
        "badge": "SHIELD",
        "title": {"DE": "Schutz & Grounding", "EN": "Protection & Grounding"},
        "text": {
            "DE": "Schwarzer Turmalin, Onyx und Rauchquarz fuer klare Grenzen.",
            "EN": "Black tourmaline, onyx, and smoky quartz for energetic boundaries.",
        },
    },
    {
        "badge": "FOCUS",
        "title": {"DE": "Business Focus", "EN": "Business Focus"},
        "text": {
            "DE": "Setups fuer Konzentration, Produktivitaet und Leadership-Energie.",
            "EN": "Setups for focus, productivity, and leadership energy.",
        },
    },
    {
        "badge": "ZODIAC",
        "title": {"DE": "Sternzeichen Sets", "EN": "Zodiac Sets"},
        "text": {
            "DE": "Abgestimmt auf Elemente und Charaktereigenschaften deines Zeichens.",
            "EN": "Matched to the element and traits of your zodiac sign.",
        },
    },
]

PRODUCTS = [
    {
        "palette": "amber",
        "name": {"DE": "Solar Wealth Set", "EN": "Solar Wealth Set"},
        "text": {
            "DE": "Citrin, Tigerauge, Pyrit und Ritualkarte fuer Fuelle.",
            "EN": "Citrine, tiger eye, pyrite, and a ritual card for abundance.",
        },
        "price": "69 EUR",
    },
    {
        "palette": "rose",
        "name": {"DE": "Venus Heart Kit", "EN": "Venus Heart Kit"},
        "text": {
            "DE": "Rosenquarz, Granat und Mondstein fuer Liebesrituale.",
            "EN": "Rose quartz, garnet, and moonstone for heart-centered rituals.",
        },
        "price": "74 EUR",
    },
    {
        "palette": "night",
        "name": {"DE": "Guardian Shield", "EN": "Guardian Shield"},
        "text": {
            "DE": "Schwarzer Turmalin, Obsidian und Selenit zur Raumklaerung.",
            "EN": "Black tourmaline, obsidian, and selenite for energetic shielding.",
        },
        "price": "61 EUR",
    },
    {
        "palette": "ice",
        "name": {"DE": "Clarity Aura Box", "EN": "Clarity Aura Box"},
        "text": {
            "DE": "Bergkristall-Cluster mit Reinigungsset und Anleitung.",
            "EN": "Clear quartz cluster with a cleansing kit and practice guide.",
        },
        "price": "82 EUR",
    },
    {
        "palette": "earth",
        "name": {"DE": "Root Balance Pack", "EN": "Root Balance Pack"},
        "text": {
            "DE": "Rauchquarz, Haematit und roter Jaspis fuer Stabilitaet.",
            "EN": "Smoky quartz, hematite, and red jasper for grounding stability.",
        },
        "price": "57 EUR",
    },
    {
        "palette": "lilac",
        "name": {"DE": "Dream Oracle Set", "EN": "Dream Oracle Set"},
        "text": {
            "DE": "Amethyst, Lepidolith und Lavendel-Spray fuer Abendrituale.",
            "EN": "Amethyst, lepidolite, and lavender mist for evening rituals.",
        },
        "price": "66 EUR",
    },
]

RITUAL_STEPS = [
    {
        "step": "01",
        "title": {"DE": "Intent setzen", "EN": "Set your intention"},
        "text": {
            "DE": "Waehle dein Set nach der aktuellen Lebensfrage.",
            "EN": "Choose your set based on your current life focus.",
        },
    },
    {
        "step": "02",
        "title": {"DE": "Stein aktivieren", "EN": "Activate your stone"},
        "text": {
            "DE": "Nutze Atemtechnik und Fokus-Formel aus der Ritualkarte.",
            "EN": "Use the guided breath and focus phrase from the ritual card.",
        },
    },
    {
        "step": "03",
        "title": {"DE": "Ritual leben", "EN": "Live the ritual"},
        "text": {
            "DE": "Integriere den Stein in Alltag, Meditation und Workspace.",
            "EN": "Integrate the stone into daily work, meditation, and routine.",
        },
    },
]

RITUAL_SCHEDULE = [
    {
        "title": {"DE": "Montag: Fokus", "EN": "Monday: Focus"},
        "text": {
            "DE": "Solar Wealth fuer Zielklarheit und produktiven Wochenstart.",
            "EN": "Solar Wealth for clear priorities and a focused week start.",
        },
    },
    {
        "title": {"DE": "Mittwoch: Herz", "EN": "Wednesday: Heart"},
        "text": {
            "DE": "Venus Heart fuer Selbstwert, Ruhe und klare Kommunikation.",
            "EN": "Venus Heart for self-worth, calm, and clear communication.",
        },
    },
    {
        "title": {"DE": "Freitag: Reinigung", "EN": "Friday: Reset"},
        "text": {
            "DE": "Guardian Shield fuer Raumklaerung und Entladung.",
            "EN": "Guardian Shield for space cleansing and energetic reset.",
        },
    },
    {
        "title": {"DE": "Sonntag: Vision", "EN": "Sunday: Vision"},
        "text": {
            "DE": "Dream Oracle fuer Reflexion, Intuition und Ausrichtung.",
            "EN": "Dream Oracle for reflection, intuition, and aligned planning.",
        },
    },
]

REVIEWS = [
    {
        "text": {
            "DE": "Schon nach einer Woche mit dem Clarity Set war mein Fokus deutlich klarer.",
            "EN": "After one week with the Clarity Set, my focus was noticeably sharper.",
        },
        "author": "Lea M.",
    },
    {
        "text": {
            "DE": "Packaging, Qualitaet und Ritualkarten wirken wie aus einer Luxus-Boutique.",
            "EN": "Packaging, quality, and ritual cards feel like a true luxury boutique.",
        },
        "author": "Daniel R.",
    },
    {
        "text": {
            "DE": "Mein Lieblingsshop fuer Heilsteine. Extrem hochwertig und klar kuratiert.",
            "EN": "My favorite crystal shop. Premium quality and clearly curated.",
        },
        "author": "Nora M.",
    },
    {
        "text": {
            "DE": "Schneller Versand und die Sets fuehlen sich energetisch sofort stimmig an.",
            "EN": "Fast shipping and the sets feel energetically aligned right away.",
        },
        "author": "Kai S.",
    },
    {
        "text": {
            "DE": "Die Sternzeichen Box war als Geschenk ein voller Erfolg.",
            "EN": "The zodiac box was the perfect gift and looked amazing.",
        },
        "author": "Anna P.",
    },
    {
        "text": {
            "DE": "Die Anleitung macht den Unterschied: sofort umsetzbar statt nur Deko.",
            "EN": "The guidance cards are the difference: practical, not just decorative.",
        },
        "author": "Melissa T.",
    },
]

PRODUCT_BENEFITS = [
    {
        "title": {"DE": "Handverlesen", "EN": "Hand-selected"},
        "text": {
            "DE": "Jeder Stein wird nach Reinheit, Schliff und Energiesignatur geprueft.",
            "EN": "Every stone is checked for quality, cut, and energetic profile.",
        },
    },
    {
        "title": {"DE": "Schneller Versand", "EN": "Fast shipping"},
        "text": {
            "DE": "Versand in 24-48h mit sicherer Premium-Verpackung.",
            "EN": "24-48h shipping with safe premium packaging.",
        },
    },
    {
        "title": {"DE": "Klare Anwendung", "EN": "Guided usage"},
        "text": {
            "DE": "Jedes Set enthaelt konkrete Ritualkarten fuer den Alltag.",
            "EN": "Every set includes practical ritual cards for daily use.",
        },
    },
]

FAQS = [
    {
        "q": {
            "DE": "Sind Heilsteine ein Ersatz fuer medizinische Behandlung?",
            "EN": "Are healing crystals a replacement for medical treatment?",
        },
        "a": {
            "DE": "Nein. Celestia Produkte sind fuer Wohlbefinden und Rituale gedacht.",
            "EN": "No. Celestia products support wellbeing rituals and are not medical treatment.",
        },
    },
    {
        "q": {
            "DE": "Wie waehle ich das richtige Set?",
            "EN": "How do I choose the right set?",
        },
        "a": {
            "DE": "Starte mit deinem aktuellen Fokus: Schutz, Liebe, Klarheit oder Manifestation.",
            "EN": "Start with your current focus: protection, love, clarity, or manifestation.",
        },
    },
    {
        "q": {
            "DE": "Bietet ihr Geschenkboxen an?",
            "EN": "Do you offer gift boxes?",
        },
        "a": {
            "DE": "Ja, wir bieten kuratierte Geschenkboxen inklusive Ritualkarte an.",
            "EN": "Yes, we offer curated gift boxes including a ritual card.",
        },
    },
]

FOCUS_AREAS = [
    {
        "title": {"DE": "Karriere & Fokus", "EN": "Career & Focus"},
        "text": {
            "DE": "Setups fuer Zielorientierung, Konzentration und Execution.",
            "EN": "Setups for goal clarity, concentration, and execution.",
        },
    },
    {
        "title": {"DE": "Herz & Beziehungen", "EN": "Heart & Relationships"},
        "text": {
            "DE": "Rituale fuer Verbindung, Selbstliebe und offene Kommunikation.",
            "EN": "Rituals for connection, self-love, and open communication.",
        },
    },
    {
        "title": {"DE": "Schutz & Reset", "EN": "Protection & Reset"},
        "text": {
            "DE": "Energie-Reset fuer Zuhause, Office und unterwegs.",
            "EN": "Energy reset for home, office, and travel.",
        },
    },
]

CONTACT_FACTS = [
    {
        "title": {"DE": "Antwortzeit", "EN": "Response time"},
        "text": {"DE": "Innerhalb von 24 Stunden", "EN": "Within 24 hours"},
    },
    {
        "title": {"DE": "Versand", "EN": "Shipping"},
        "text": {"DE": "Europaweit in 24-48h", "EN": "Across Europe in 24-48h"},
    },
    {
        "title": {"DE": "Support", "EN": "Support"},
        "text": {
            "DE": "Produktwahl, Rituale, Geschenkberatung",
            "EN": "Product choice, rituals, and gifting advice",
        },
    },
]

