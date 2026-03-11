GLOBAL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Manrope:wght@400;500;700;800&display=swap');

:root {
  --bg-0: #060402;
  --bg-1: #120b04;
  --bg-2: #201308;
  --gold-0: #ffe8ad;
  --gold-1: #f0c768;
  --gold-2: #bb8a34;
  --text-0: #f9edd1;
  --text-1: #d6be88;
  --line: rgba(255, 224, 142, 0.24);
  --glass: rgba(24, 15, 7, 0.64);
  --glass-strong: rgba(16, 9, 5, 0.84);
  --shadow: 0 20px 60px rgba(0, 0, 0, 0.48);
}

html, body, [class*="css"] {
  font-family: "Manrope", sans-serif;
}

.stApp {
  color: var(--text-0);
  background:
    radial-gradient(1200px 800px at 90% -10%, rgba(211, 151, 50, 0.18), transparent 58%),
    radial-gradient(920px 760px at -10% 20%, rgba(180, 128, 35, 0.2), transparent 56%),
    linear-gradient(160deg, var(--bg-0) 0%, var(--bg-1) 48%, #030201 100%);
}

.stApp::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: -2;
  opacity: 0.22;
  background-image:
    radial-gradient(2px 2px at 4% 8%, rgba(255, 223, 145, 0.95), transparent),
    radial-gradient(2px 2px at 12% 20%, rgba(255, 223, 145, 0.85), transparent),
    radial-gradient(2px 2px at 19% 45%, rgba(255, 223, 145, 0.75), transparent),
    radial-gradient(1px 1px at 28% 30%, rgba(255, 223, 145, 0.8), transparent),
    radial-gradient(2px 2px at 37% 12%, rgba(255, 223, 145, 0.9), transparent),
    radial-gradient(1px 1px at 42% 61%, rgba(255, 223, 145, 0.9), transparent),
    radial-gradient(2px 2px at 55% 22%, rgba(255, 223, 145, 0.75), transparent),
    radial-gradient(1px 1px at 64% 38%, rgba(255, 223, 145, 0.85), transparent),
    radial-gradient(2px 2px at 74% 11%, rgba(255, 223, 145, 0.8), transparent),
    radial-gradient(1px 1px at 83% 48%, rgba(255, 223, 145, 0.85), transparent),
    radial-gradient(2px 2px at 91% 17%, rgba(255, 223, 145, 0.8), transparent),
    radial-gradient(2px 2px at 96% 52%, rgba(255, 223, 145, 0.8), transparent);
  animation: starDrift 46s linear infinite;
}

.stApp::after {
  content: "";
  position: fixed;
  inset: -20% -10%;
  pointer-events: none;
  z-index: -3;
  filter: blur(70px);
  opacity: 0.35;
  background:
    radial-gradient(circle at 20% 30%, rgba(248, 190, 78, 0.34), transparent 45%),
    radial-gradient(circle at 80% 35%, rgba(202, 137, 39, 0.3), transparent 42%),
    radial-gradient(circle at 45% 78%, rgba(255, 230, 167, 0.18), transparent 40%);
  animation: auraPulse 16s ease-in-out infinite;
}

header[data-testid="stHeader"] {
  background: transparent;
}

[data-testid="stToolbar"] {
  right: 0.75rem;
}

#MainMenu,
footer {
  visibility: hidden;
}

[data-testid="stSidebarNav"] {
  display: none;
}

.block-container {
  max-width: 1180px;
  padding-top: 1.1rem;
  padding-bottom: 3.2rem;
}

.cel-brand {
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 0.85rem 1rem;
  background: linear-gradient(135deg, rgba(255, 214, 129, 0.08), rgba(255, 214, 129, 0.01)), var(--glass);
  box-shadow: var(--shadow);
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.cel-brand-star {
  color: var(--gold-0);
  font-size: 1.1rem;
}

.cel-brand-copy {
  line-height: 1.05;
}

.cel-brand-name {
  font-family: "Cinzel", serif;
  letter-spacing: 0.2em;
  font-size: 1.04rem;
  color: var(--gold-0);
}

.cel-brand-tag {
  margin-top: 0.2rem;
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.17em;
  color: var(--text-1);
}

.stSelectbox > div[data-baseweb="select"] {
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255, 224, 142, 0.08);
}

.stSelectbox label p {
  color: var(--text-1) !important;
  font-weight: 600;
  letter-spacing: 0.03em;
}

div[data-testid="stPageLink"] a {
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255, 214, 130, 0.07);
  padding: 0.52rem 0.8rem;
  width: 100%;
  text-align: center;
  color: var(--text-0);
  font-weight: 700;
  transition: all 0.35s ease;
}

div[data-testid="stPageLink"] a:hover {
  border-color: rgba(255, 224, 142, 0.7);
  background: rgba(255, 214, 130, 0.18);
  transform: translateY(-1px);
}

.cel-nav-hint {
  margin: 0.34rem 0 1rem;
  color: var(--text-1);
  font-size: 0.8rem;
}

.cel-hero {
  border: 1px solid var(--line);
  border-radius: 26px;
  padding: clamp(1.2rem, 3.2vw, 2.2rem);
  background:
    radial-gradient(700px 380px at 84% 8%, rgba(255, 210, 108, 0.2), transparent 68%),
    linear-gradient(145deg, rgba(255, 214, 129, 0.08), rgba(255, 214, 129, 0.01)),
    var(--glass-strong);
  box-shadow: var(--shadow);
}

.cel-eyebrow {
  margin: 0 0 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.19em;
  font-size: 0.77rem;
  font-weight: 700;
  color: var(--text-1);
}

.cel-title {
  margin: 0;
  font-family: "Cinzel", serif;
  font-size: clamp(2rem, 4.1vw, 3.8rem);
  line-height: 1.12;
  color: var(--gold-0);
}

.cel-lead {
  margin: 0.95rem 0 0;
  font-size: 1rem;
  color: var(--text-1);
  line-height: 1.68;
}

.cel-note {
  margin: 0.85rem 0 0;
  color: #e8d8b4;
}

.cel-logo-shell {
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 0.8rem;
  background:
    radial-gradient(circle at 50% 25%, rgba(255, 214, 130, 0.27), rgba(255, 214, 130, 0.02)),
    rgba(15, 9, 4, 0.65);
  box-shadow: var(--shadow);
  animation: logoFloat 7s ease-in-out infinite;
}

.cel-section-head {
  margin: 2rem 0 0.8rem;
  text-align: center;
}

.cel-section-head .cel-eyebrow {
  margin-bottom: 0.34rem;
}

.cel-section-head h2 {
  margin: 0;
  font-family: "Cinzel", serif;
  font-size: clamp(1.5rem, 2.8vw, 2.7rem);
  color: var(--gold-0);
}

.cel-section-copy {
  margin: 0.7rem auto 0;
  max-width: 780px;
  color: var(--text-1);
}

.cel-card,
.cel-product-card,
.cel-step-card,
.cel-review-card,
.cel-info-card,
.cel-metric-card,
.cel-cta-band,
.cel-footer {
  border: 1px solid var(--line);
  border-radius: 18px;
  background:
    linear-gradient(135deg, rgba(255, 214, 129, 0.08), rgba(255, 214, 129, 0.02)),
    var(--glass);
  box-shadow: var(--shadow);
}

.cel-card,
.cel-step-card,
.cel-review-card,
.cel-info-card,
.cel-metric-card {
  padding: 1rem;
}

.cel-card-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 68px;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  border: 1px solid rgba(255, 224, 142, 0.4);
  color: var(--gold-0);
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  font-weight: 700;
}

.cel-card h3,
.cel-product-card h3,
.cel-step-card h3,
.cel-info-card h3 {
  margin: 0.7rem 0 0.35rem;
  font-family: "Cinzel", serif;
  color: var(--gold-0);
  font-size: 1.08rem;
}

.cel-card p,
.cel-step-card p,
.cel-review-card p,
.cel-info-card p {
  margin: 0;
  color: var(--text-1);
}

.cel-metric-value {
  font-family: "Cinzel", serif;
  font-size: 1.78rem;
  line-height: 1;
  color: var(--gold-1);
}

.cel-metric-label {
  margin-top: 0.25rem;
  color: var(--text-1);
}

.cel-product-card {
  overflow: hidden;
}

.cel-product-media {
  height: 140px;
}

.media-amber {
  background: radial-gradient(circle at 34% 34%, rgba(239, 168, 61, 0.58), rgba(79, 40, 8, 0.95));
}

.media-rose {
  background: radial-gradient(circle at 34% 34%, rgba(255, 194, 198, 0.52), rgba(75, 26, 39, 0.95));
}

.media-night {
  background: radial-gradient(circle at 34% 34%, rgba(139, 152, 167, 0.48), rgba(19, 22, 31, 0.97));
}

.media-ice {
  background: radial-gradient(circle at 34% 34%, rgba(178, 234, 249, 0.5), rgba(16, 48, 59, 0.95));
}

.media-earth {
  background: radial-gradient(circle at 34% 34%, rgba(201, 161, 120, 0.52), rgba(50, 30, 15, 0.96));
}

.media-lilac {
  background: radial-gradient(circle at 34% 34%, rgba(194, 167, 230, 0.52), rgba(37, 21, 56, 0.96));
}

.cel-product-body {
  padding: 0.95rem;
}

.cel-price-row {
  margin-top: 0.65rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
}

.cel-price {
  color: var(--gold-1);
  font-family: "Cinzel", serif;
  font-size: 1.02rem;
}

.cel-pill {
  border: 1px solid rgba(255, 224, 142, 0.45);
  border-radius: 999px;
  padding: 0.2rem 0.56rem;
  color: var(--text-0);
  font-size: 0.74rem;
}

.cel-step-no {
  display: inline-block;
  color: var(--gold-1);
  font-family: "Cinzel", serif;
  font-size: 1.3rem;
}

.cel-review-author {
  margin-top: 0.55rem;
  color: var(--text-0);
  font-weight: 700;
}

.cel-cta-band {
  margin-top: 1.4rem;
  padding: 1.3rem;
  text-align: center;
  background:
    radial-gradient(760px 250px at 50% -10%, rgba(255, 218, 140, 0.2), transparent 70%),
    var(--glass-strong);
}

.cel-cta-band h3 {
  margin: 0;
  font-family: "Cinzel", serif;
  color: var(--gold-0);
  font-size: clamp(1.25rem, 2.2vw, 2.1rem);
}

.cel-cta-band p {
  margin: 0.6rem auto 0;
  max-width: 800px;
  color: var(--text-1);
}

.stTextInput > div > div,
.stTextArea textarea {
  border-radius: 12px !important;
  border: 1px solid var(--line) !important;
  background: rgba(255, 214, 130, 0.07) !important;
  color: var(--text-0) !important;
}

.stButton button,
.stDownloadButton button {
  border-radius: 999px;
  border: 1px solid rgba(255, 224, 142, 0.6);
  color: #2d1804;
  font-weight: 800;
  background: linear-gradient(130deg, var(--gold-1), var(--gold-2));
  box-shadow: 0 12px 30px rgba(180, 124, 30, 0.34);
}

.stButton button:hover,
.stDownloadButton button:hover {
  border-color: rgba(255, 224, 142, 0.9);
}

.stExpander {
  border-radius: 16px !important;
  border: 1px solid var(--line) !important;
  background: rgba(255, 214, 130, 0.05) !important;
}

.stExpander details summary p {
  color: var(--gold-0) !important;
  font-weight: 700 !important;
}

.cel-footer {
  margin-top: 1.8rem;
  padding: 1.1rem;
}

.cel-footer h4 {
  margin: 0 0 0.45rem;
  font-family: "Cinzel", serif;
  color: var(--gold-0);
}

.cel-footer p,
.cel-footer li {
  margin: 0;
  color: var(--text-1);
}

.cel-footer ul {
  margin: 0;
  padding-left: 1.1rem;
}

@keyframes starDrift {
  0% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-14px, 10px, 0); }
  100% { transform: translate3d(0, 0, 0); }
}

@keyframes auraPulse {
  0%, 100% { transform: scale(1); opacity: 0.34; }
  50% { transform: scale(1.03); opacity: 0.46; }
}

@keyframes logoFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-7px); }
}

@media (max-width: 980px) {
  .block-container {
    padding-top: 0.7rem;
  }
}

@media (max-width: 720px) {
  .cel-brand {
    margin-bottom: 0.5rem;
  }
}
"""

