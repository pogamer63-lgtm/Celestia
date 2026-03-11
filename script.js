const LANG_KEY = "celestia-lang";
const SUPPORTED_LANGS = ["de", "en"];

let currentLang = "de";

const pageBody = document.body;
const starLayer = document.getElementById("starLayer");
const backToTop = document.getElementById("backToTop");
const ambientLights = document.querySelector(".ambient-lights");
const revealElements = document.querySelectorAll("[data-reveal]");
const counters = document.querySelectorAll(".count");
const tiltCards = document.querySelectorAll("[data-tilt]");
const reviewTrack = document.querySelector(".reviews-track");
const ctaForm = document.querySelector(".cta-form");
const contactForm = document.querySelector(".contact-form");
const langSelect = document.getElementById("langSelect");
const menuToggle = document.getElementById("menuToggle");
const siteNav = document.getElementById("siteNav");

function isSupportedLang(lang) {
  return SUPPORTED_LANGS.includes(lang);
}

function resolveInitialLang() {
  const params = new URLSearchParams(window.location.search);
  const fromUrl = params.get("lang");
  if (isSupportedLang(fromUrl)) return fromUrl;

  let fromStorage = null;
  try {
    fromStorage = localStorage.getItem(LANG_KEY);
  } catch {
    fromStorage = null;
  }
  if (isSupportedLang(fromStorage)) return fromStorage;

  return "de";
}

function updateUrlLang(lang) {
  try {
    const url = new URL(window.location.href);
    url.searchParams.set("lang", lang);
    window.history.replaceState({}, "", url);
  } catch {
    // Ignore URL state update errors in restricted contexts.
  }
}

function syncPageLinks(lang) {
  const links = document.querySelectorAll("a[href]");

  links.forEach((link) => {
    const rawHref = link.getAttribute("href");
    if (!rawHref) return;
    if (rawHref.startsWith("#")) return;
    if (rawHref.startsWith("mailto:") || rawHref.startsWith("tel:")) return;

    let target;
    try {
      target = new URL(rawHref, window.location.href);
    } catch {
      return;
    }

    const path = target.pathname.toLowerCase();
    if (target.searchParams.has("page")) {
      target.searchParams.set("lang", lang);
      link.setAttribute("href", `${target.pathname}${target.search}${target.hash}`);
      return;
    }
    if (!path.endsWith(".html")) return;

    target.searchParams.set("lang", lang);
    link.setAttribute("href", `${target.pathname}${target.search}${target.hash}`);
  });
}

function setupPrefetch() {
  if (!document.head) return;
  const prefetched = new Set();

  const queuePrefetch = (href) => {
    if (!href || prefetched.has(href)) return;
    prefetched.add(href);

    const prefetch = document.createElement("link");
    prefetch.rel = "prefetch";
    prefetch.as = "document";
    prefetch.href = href;
    document.head.appendChild(prefetch);
  };

  document.querySelectorAll(".site-nav a[href], .brand[href], a.btn[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) return;

    let target;
    try {
      target = new URL(href, window.location.href);
    } catch {
      return;
    }

    if (target.origin !== window.location.origin) return;
    const isHtmlTarget = target.pathname.toLowerCase().endsWith(".html");
    const isPageTarget = target.searchParams.has("page");
    if (!isHtmlTarget && !isPageTarget) return;
    queuePrefetch(target.href);
  });
}

function applyLanguage(lang) {
  if (!isSupportedLang(lang)) return;
  currentLang = lang;

  try {
    localStorage.setItem(LANG_KEY, lang);
  } catch {
    // Ignore storage errors in restricted contexts.
  }
  document.documentElement.lang = lang;

  if (langSelect && langSelect.value !== lang) {
    langSelect.value = lang;
  }

  document.querySelectorAll("[data-de][data-en]").forEach((node) => {
    node.innerHTML = lang === "de" ? node.dataset.de : node.dataset.en;
  });

  document.querySelectorAll("[data-placeholder-de][data-placeholder-en]").forEach((node) => {
    node.placeholder = lang === "de" ? node.dataset.placeholderDe : node.dataset.placeholderEn;
  });

  document.querySelectorAll("[data-aria-de][data-aria-en]").forEach((node) => {
    node.setAttribute("aria-label", lang === "de" ? node.dataset.ariaDe : node.dataset.ariaEn);
  });

  if (pageBody?.dataset.titleDe && pageBody?.dataset.titleEn) {
    document.title = lang === "de" ? pageBody.dataset.titleDe : pageBody.dataset.titleEn;
  }

  counters.forEach((counter) => {
    if (counter.dataset.finished === "true") {
      const target = Number(counter.dataset.target || 0);
      counter.textContent = formatNumber(target);
    }
  });

  syncPageLinks(lang);
  updateUrlLang(lang);
}

function formatNumber(num) {
  return num.toLocaleString(currentLang === "en" ? "en-US" : "de-DE");
}

function buildStars() {
  if (!starLayer) return;

  starLayer.innerHTML = "";
  const isCoarsePointer = window.matchMedia && window.matchMedia("(pointer: coarse)").matches;
  const density = isCoarsePointer ? 0.06 : 0.085;
  const minCount = isCoarsePointer ? 42 : 60;
  const maxCount = isCoarsePointer ? 110 : 145;
  const count = Math.min(maxCount, Math.max(minCount, Math.floor(window.innerWidth * density)));

  for (let i = 0; i < count; i += 1) {
    const star = document.createElement("span");
    star.className = "star";
    const size = (Math.random() * 2.2 + 0.5).toFixed(2);
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.left = `${Math.random() * 100}%`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.animationDuration = `${3.5 + Math.random() * 4.5}s`;
    star.style.animationDelay = `${Math.random() * -8}s`;
    star.style.opacity = `${0.2 + Math.random() * 0.8}`;
    starLayer.appendChild(star);
  }
}

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.16,
    rootMargin: "0px 0px -10% 0px",
  }
);

function runCountUp(node) {
  const target = Number(node.dataset.target || 0);
  const duration = 1400;
  const start = performance.now();

  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    node.textContent = formatNumber(Math.floor(target * eased));

    if (progress < 1) {
      requestAnimationFrame(step);
      return;
    }

    node.textContent = formatNumber(target);
    node.dataset.finished = "true";
  }

  requestAnimationFrame(step);
}

const counterObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        runCountUp(entry.target);
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.4 }
);

function setupTilt(card) {
  card.addEventListener("pointermove", (event) => {
    const rect = card.getBoundingClientRect();
    const offsetX = event.clientX - rect.left;
    const offsetY = event.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateY = ((offsetX - centerX) / centerX) * 6;
    const rotateX = ((centerY - offsetY) / centerY) * 6;

    card.style.transform = `perspective(900px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-4px)`;
  });

  card.addEventListener("pointerleave", () => {
    card.style.transform = "";
  });
}

function setupReviewMarquee() {
  if (!reviewTrack) return;
  const cards = [...reviewTrack.children];
  cards.forEach((card) => {
    reviewTrack.appendChild(card.cloneNode(true));
  });
}

function setupBackToTop() {
  if (!backToTop) return;

  const handleScroll = () => {
    if (window.scrollY > 560) {
      backToTop.classList.add("is-visible");
    } else {
      backToTop.classList.remove("is-visible");
    }
  };

  window.addEventListener("scroll", handleScroll, { passive: true });
  handleScroll();

  backToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

function setupPointerParallax() {
  if (!ambientLights && !starLayer) return;
  if (window.matchMedia && window.matchMedia("(pointer: coarse)").matches) return;
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  let targetX = 0;
  let targetY = 0;
  let currentX = 0;
  let currentY = 0;

  window.addEventListener("pointermove", (event) => {
    const x = event.clientX / window.innerWidth - 0.5;
    const y = event.clientY / window.innerHeight - 0.5;
    targetX = x * 16;
    targetY = y * 12;
  });

  const animate = () => {
    currentX += (targetX - currentX) * 0.06;
    currentY += (targetY - currentY) * 0.06;

    if (ambientLights) {
      ambientLights.style.transform = `translate3d(${currentX}px, ${currentY}px, 0)`;
    }

    if (starLayer) {
      starLayer.style.transform = `translate3d(${currentX * -0.35}px, ${currentY * -0.35}px, 0)`;
    }

    requestAnimationFrame(animate);
  };

  requestAnimationFrame(animate);
}

function setupNewsletterForm() {
  if (!ctaForm) return;

  ctaForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const button = ctaForm.querySelector("button");
    const input = ctaForm.querySelector("input");
    if (!button || !input) return;

    const originalText = currentLang === "de" ? button.dataset.de : button.dataset.en;
    const successText = currentLang === "de" ? ctaForm.dataset.successDe : ctaForm.dataset.successEn;

    button.textContent = successText || originalText;
    button.disabled = true;
    input.value = "";

    setTimeout(() => {
      button.textContent = originalText;
      button.disabled = false;
    }, 2300);
  });
}

function setupContactForm() {
  if (!contactForm) return;

  const status = contactForm.querySelector(".form-status");
  const name = contactForm.querySelector("#contactName");
  const email = contactForm.querySelector("#contactEmail");
  const message = contactForm.querySelector("#contactMessage");

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!status || !name || !email || !message) return;

    const complete = name.value.trim() && email.value.trim() && message.value.trim();
    const successText = currentLang === "de" ? contactForm.dataset.successDe : contactForm.dataset.successEn;
    const errorText = currentLang === "de" ? contactForm.dataset.errorDe : contactForm.dataset.errorEn;

    if (!complete) {
      status.textContent = errorText || "";
      status.style.color = "#ffd09e";
      return;
    }

    status.textContent = successText || "";
    status.style.color = "#f0c768";
    contactForm.reset();
  });
}

function setupMenu() {
  if (!menuToggle || !siteNav) return;

  menuToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("is-open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });

  document.addEventListener("click", (event) => {
    if (!siteNav.classList.contains("is-open")) return;
    if (siteNav.contains(event.target) || menuToggle.contains(event.target)) return;
    siteNav.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
  });

  siteNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      siteNav.classList.remove("is-open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

function setActiveNav() {
  const page = pageBody?.dataset.page;
  if (!page) return;

  document.querySelectorAll(".site-nav a[data-nav]").forEach((link) => {
    if (link.dataset.nav === page) {
      link.classList.add("active");
      link.setAttribute("aria-current", "page");
    }
  });
}

function setupLanguageSelector() {
  const lang = resolveInitialLang();
  applyLanguage(lang);

  if (!langSelect) return;
  langSelect.value = lang;

  langSelect.addEventListener("change", (event) => {
    applyLanguage(event.target.value);
  });
}

function init() {
  buildStars();
  setupLanguageSelector();
  setActiveNav();

  revealElements.forEach((el) => revealObserver.observe(el));
  counters.forEach((counter) => counterObserver.observe(counter));
  tiltCards.forEach(setupTilt);

  setupReviewMarquee();
  setupBackToTop();
  setTimeout(setupPointerParallax, 180);
  setupNewsletterForm();
  setupContactForm();
  setupMenu();
  if ("requestIdleCallback" in window) {
    window.requestIdleCallback(setupPrefetch, { timeout: 900 });
  } else {
    setTimeout(setupPrefetch, 240);
  }
}

let resizeTimer;
window.addEventListener("resize", () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(buildStars, 180);
});

init();
