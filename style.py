# Website ka design (CSS) aur har page pe use hone wale hisse: header, footer, cards
import html
import re
from urllib.parse import quote
import streamlit as st
from content import socials

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Mr+Dafoe&family=Space+Mono:wght@400;700&family=Jost:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Noto+Serif+Devanagari:wght@400;500&family=Noto+Serif+Gurmukhi:wght@400;500&display=swap');

:root {
  --ink: #111111;
  --muted: #777777;
  --line: #E6E6E6;
  --soft: #F6F5F3;
  --white: #FFFFFF;
  --script: 'Mr Dafoe', cursive;
  --mono: 'Space Mono', monospace;
  --sans: 'Jost', system-ui, sans-serif;
  --poem: 'Cormorant Garamond', 'Noto Serif Devanagari', 'Noto Serif Gurmukhi', Georgia, serif;
}

/* ---------- Streamlit ki apni cheezein chhupao ---------- */
header[data-testid="stHeader"], footer, [data-testid="stDecoration"], [data-testid="stToolbar"] { display: none !important; }
.stApp { background: var(--white); }
.stApp, .stApp p, .stApp input, .stApp button { font-family: var(--sans); color: var(--ink); }
.block-container { max-width: 100% !important; padding: 0 !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
a { color: inherit; }

.wrap { max-width: 1140px; margin: 0 auto; padding: 0 24px; }

/* ---------- Header ---------- */
.bw-top { background: var(--white); }
.bw-top .row { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 34px 24px 26px; }
.bw-btn {
  justify-self: start; display: inline-block; background: var(--ink); color: #fff !important;
  font-family: var(--mono); font-weight: 700; font-size: .72rem; letter-spacing: .14em;
  padding: .75rem 1.7rem; border-radius: 999px; text-decoration: none; transition: opacity .2s;
}
.bw-btn:hover { opacity: .8; }
a.bw-logo { font-family: var(--script); font-size: 4.2rem; line-height: 1; color: var(--ink); text-decoration: none; }
.bw-icons { justify-self: end; display: flex; gap: 1.1rem; }
.bw-icons a { color: var(--ink); display: flex; transition: opacity .2s, transform .2s; }
.bw-icons a:hover { opacity: .6; transform: translateY(-2px); }

.bw-nav { border-top: 1px solid var(--line); display: flex; justify-content: center; flex-wrap: wrap; gap: .3rem 3.4rem; padding: 22px 24px 24px; }
.bw-nav a { font-family: var(--mono); font-size: .78rem; font-weight: 700; letter-spacing: .12em; text-decoration: none; color: var(--ink); }
.bw-nav a.active, .bw-nav a:hover { color: #9A9A9A; }

/* ---------- Hero ---------- */
.bw-hero { position: relative; height: 620px; background-size: cover; background-position: center; }
.bw-hero::after { content: ""; position: absolute; inset: 0; background: rgba(0, 0, 0, .28); }
.bw-hero .tag { position: relative; z-index: 1; text-align: center; color: #fff; padding-top: 120px; }
.bw-hero .tag .kicker { font-family: var(--mono); font-size: .75rem; letter-spacing: .3em; text-transform: uppercase; }
.bw-hero .tag h1 { font-family: var(--script); font-weight: 400; font-size: clamp(3.4rem, 9vw, 6.5rem); line-height: 1.1; margin: .4rem 0; color: #fff; padding: 0; }
.bw-hero .tag p { font-family: var(--sans); font-size: 1.05rem; opacity: .9; margin: 0; color: #fff; }
.bw-hero-cards { position: relative; z-index: 2; margin-top: -250px; }

/* ---------- Cards (photo + label + title) ---------- */
.bw-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
.bw-cards.two { grid-template-columns: repeat(2, 1fr); }
a.bw-card { position: relative; display: block; height: 380px; overflow: hidden; text-decoration: none; background: #222; }
.bw-card .img { position: absolute; inset: 0; background-size: cover; background-position: center; transition: transform .6s ease; filter: grayscale(35%); }
a.bw-card:hover .img { transform: scale(1.06); filter: grayscale(0%); }
.bw-card .over {
  position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
  text-align: center; padding: 2rem 1.6rem; background: linear-gradient(to top, rgba(0,0,0,.72) 0%, rgba(0,0,0,.15) 55%, rgba(0,0,0,.05) 100%);
}
.bw-card .label { font-family: var(--mono); font-size: .7rem; letter-spacing: .22em; text-transform: uppercase; color: #fff; }
.bw-card h3 { font-family: var(--sans); font-weight: 500; font-size: 1.6rem; line-height: 1.25; margin: .5rem 0 0; padding: 0; color: #fff; }

/* ---------- Sections ---------- */
.bw-section { padding: 90px 0 30px; }
.bw-head { text-align: center; margin-bottom: 44px; }
.bw-head .kicker { font-family: var(--mono); font-size: .72rem; letter-spacing: .25em; text-transform: uppercase; color: var(--muted); }
.bw-head h2 { font-family: var(--sans); font-weight: 500; font-size: 2.3rem; margin: .4rem 0 0; padding: 0; color: var(--ink); }
.bw-more { text-align: center; margin-top: 40px; }
.bw-more a { font-family: var(--mono); font-size: .75rem; font-weight: 700; letter-spacing: .14em; text-decoration: none; border-bottom: 2px solid var(--ink); padding-bottom: 4px; }

/* ---------- About strip ---------- */
.bw-about { text-align: center; max-width: 680px; margin: 0 auto; }
.bw-about .sig { font-family: var(--script); font-size: 3rem; line-height: 1; }
.bw-about p { font-family: var(--poem); font-size: 1.45rem; line-height: 1.6; color: #333; margin: 1rem 0 0; }

/* ---------- Quote band (black) ---------- */
.bw-band { background: var(--ink); color: #fff; text-align: center; padding: 100px 24px; margin-top: 90px; }
.bw-band .kicker { font-family: var(--mono); font-size: .72rem; letter-spacing: .3em; color: #999; text-transform: uppercase; }
.bw-band blockquote { font-family: var(--poem); font-style: italic; font-size: clamp(1.7rem, 4vw, 2.7rem); line-height: 1.35; max-width: 820px; margin: 1.4rem auto 1rem; color: #fff; border: 0; padding: 0; }
.bw-band .by { font-family: var(--script); font-size: 2rem; color: #ddd; }

/* ---------- Page title band ---------- */
.bw-pagehead { position: relative; height: 340px; background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center; text-align: center; }
.bw-pagehead::after { content: ""; position: absolute; inset: 0; background: rgba(0, 0, 0, .42); }
.bw-pagehead > div { position: relative; z-index: 1; color: #fff; padding: 0 24px; }
.bw-pagehead .kicker { font-family: var(--mono); font-size: .75rem; letter-spacing: .3em; text-transform: uppercase; color: #fff; }
.bw-pagehead h1 { font-family: var(--sans); font-weight: 500; font-size: clamp(2.4rem, 7vw, 3.8rem); margin: .4rem 0 0; padding: 0; color: #fff; line-height: 1.15; }
.bw-pagehead p { color: #eee; margin: .6rem 0 0; font-size: 1rem; }

/* ---------- Reading view (ek poem / story) ---------- */
.bw-read { max-width: 720px; margin: 0 auto; padding: 70px 24px 20px; text-align: center; }
.bw-back { font-family: var(--mono); font-size: .75rem; font-weight: 700; letter-spacing: .12em; text-decoration: none; color: var(--muted) !important; }
.bw-back:hover { color: var(--ink) !important; }
.bw-poem { font-family: var(--poem); font-size: 1.45rem; line-height: 1.95; color: #1c1c1c; margin: 40px 0; }
.bw-poem .stanza { margin-bottom: 1.8rem; }
.bw-story { font-family: var(--poem); font-size: 1.4rem; line-height: 1.8; color: #1c1c1c; text-align: left; margin: 40px 0; }
.bw-story p { margin: 0 0 1.3rem; font-family: var(--poem); font-size: 1.4rem; }
.bw-story p:first-child::first-letter { float: left; font-size: 4.2rem; line-height: .85; padding: .3rem .6rem 0 0; font-weight: 600; }
.bw-sign { font-family: var(--script); font-size: 2.3rem; }
.bw-rule { width: 60px; height: 2px; background: var(--ink); margin: 30px auto; border: 0; }

/* ---------- Quotes grid ---------- */
.bw-quotes { columns: 3 280px; column-gap: 26px; }
.bw-quote { break-inside: avoid; margin-bottom: 26px; padding: 2.2rem 2rem; border: 1px solid var(--line); background: var(--white); text-align: center; }
.bw-quote.dark { background: var(--ink); border-color: var(--ink); }
.bw-quote.soft { background: var(--soft); border-color: var(--soft); }
.bw-quote p { font-family: var(--poem); font-size: 1.5rem; line-height: 1.45; margin: 0; }
.bw-quote.dark p { color: #fff; }
.bw-quote .by { display: block; font-family: var(--mono); font-size: .68rem; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); margin-top: 1.1rem; }
.bw-quote.dark .by { color: #aaa; }

/* ---------- Contact ---------- */
.bw-contact { text-align: center; max-width: 640px; margin: 0 auto; padding: 80px 24px 20px; }
.bw-contact p { font-family: var(--poem); font-size: 1.5rem; line-height: 1.6; margin: 0 0 2rem; }
.bw-contact .mail { font-family: var(--sans); font-size: clamp(1.3rem, 4vw, 2rem); font-weight: 500; text-decoration: none; border-bottom: 2px solid var(--ink); }
.bw-pills { display: flex; flex-wrap: wrap; justify-content: center; gap: .7rem; margin-top: 2.6rem; }
.bw-pills a { display: inline-flex; align-items: center; gap: .55rem; padding: .7rem 1.3rem; border: 1px solid var(--ink); border-radius: 999px; text-decoration: none; font-family: var(--mono); font-size: .75rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; transition: background .2s, color .2s; }
.bw-pills a:hover { background: var(--ink); color: #fff !important; }
.bw-pills .ic { width: 16px; height: 16px; }

/* ---------- Footer ---------- */
.bw-footer { border-top: 1px solid var(--line); margin-top: 90px; padding: 60px 24px 50px; text-align: center; }
.bw-footer .bw-logo { font-size: 3.4rem; }
.bw-footer .bw-icons { justify-content: center; margin: 1.4rem 0; }
.bw-footer .small { font-family: var(--mono); font-size: .72rem; letter-spacing: .08em; color: var(--muted); line-height: 1.9; }

/* ---------- Streamlit widgets (search, button) ---------- */
.stTextInput input { border-radius: 0 !important; border-color: var(--ink) !important; font-family: var(--mono) !important; font-size: .85rem !important; }
.stButton button { border-radius: 999px !important; background: var(--ink) !important; color: #fff !important; border: 0 !important; font-family: var(--mono) !important; font-weight: 700 !important; letter-spacing: .1em; font-size: .75rem !important; }
.stButton button p { color: #fff !important; font-family: var(--mono) !important; }
.stButton button:hover { opacity: .8; }
[data-testid="stHorizontalBlock"] { max-width: 1140px; margin: 0 auto 40px !important; padding: 0 24px; }

/* ---------- Mobile ---------- */
@media (max-width: 800px) {
  .bw-top .row { grid-template-columns: 1fr; justify-items: center; gap: 14px; padding: 26px 16px 18px; }
  .bw-top .bw-btn { display: none; }
  .bw-icons { justify-self: center; order: 2; }
  a.bw-logo { font-size: 3.4rem; }
  .bw-nav { gap: .6rem 1.6rem; padding: 16px; }
  .bw-nav a { font-size: .7rem; }
  .wrap { padding: 0 16px; }
  .bw-hero { height: 520px; }
  .bw-hero .tag { padding-top: 80px; }
  .bw-hero-cards { margin-top: -170px; }
  .bw-cards, .bw-cards.two { grid-template-columns: 1fr; gap: 18px; }
  a.bw-card { height: 300px; }
  .bw-section { padding-top: 60px; }
  .bw-band { padding: 70px 16px; margin-top: 60px; }
  .bw-poem { font-size: 1.25rem; }
  [data-testid="stHorizontalBlock"] { padding: 0 16px; }
}
</style>
"""

# Chhote icons (SVG) — header, footer aur contact page pe
ICONS = {
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="black" stroke="none"/>',
    "youtube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9.2l5 2.8-5 2.8z" fill="black" stroke="none"/>',
    "snapchat": '<path stroke-linejoin="round" d="M12 3c-3 0-5 2.2-5 5.2v2.4l-1.7-.5c-.6 0-.8.7-.3 1l1.9 1c-.6 1.7-1.9 3-3.5 3.6.4.9 1.5 1.1 2.5 1.3.2.6.2 1.1.9 1.1.6 0 1.4-.4 2.6-.1 1 .3 1.6 1.4 2.6 1.4s1.6-1.1 2.6-1.4c1.2-.3 2-.1 2.6.1.7 0 .7-.5.9-1.1 1-.2 2.1-.4 2.5-1.3-1.6-.6-2.9-1.9-3.5-3.6l1.9-1c.5-.3.3-1-.3-1l-1.7.5V8.2C17 5.2 15 3 12 3z"/>',
    "email": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
}

# Streamlit HTML mein <svg> hata deta hai, isliye icons CSS "mask" se banate hain
ICON_CSS = "<style>.ic{display:inline-block;width:18px;height:18px;background:currentColor;flex:none}"
for _name, _shape in ICONS.items():
    _svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">{_shape}</svg>'
    _url = f'url("data:image/svg+xml,{quote(_svg)}") center/contain no-repeat'
    ICON_CSS += f".ic-{_name}{{-webkit-mask:{_url};mask:{_url}}}"
ICON_CSS += "</style>"


def icon(name):
    return f'<span class="ic ic-{name}"></span>'


NAV = [("Home", "./", "home"), ("Poetry", "poetry", "poetry"), ("Quotes", "quotes", "quotes"),
       ("Stories", "stories", "stories"), ("Contact", "contact", "contact")]


def esc(text):
    # Text ko HTML ke liye safe banata hai (taaki < > & jaise characters gadbad na karein)
    return html.escape(text)


def slug(title, i):
    # Title se link ka naam banata hai, jaise "Hidden Hurry" → "hidden-hurry"
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s or f"{i + 1}"


def social_icons():
    return "".join(
        f'<a href="{esc(s["url"])}" target="_blank" rel="noopener" title="{esc(s["name"])}">{icon(s["icon"])}</a>'
        for s in socials if s["url"]
    )


def setup(active):
    # Har page ke upar: CSS + header + menu
    st.markdown(CSS + ICON_CSS, unsafe_allow_html=True)
    links = "".join(
        f'<a href="{href}" class="{"active" if key == active else ""}">{name.upper()}</a>'
        for name, href, key in NAV
    )
    st.html(f"""
    <div class="bw-top">
      <div class="row wrap">
        <a class="bw-btn" href="{esc(socials[0]["url"])}" target="_blank" rel="noopener">FOLLOW</a>
        <a class="bw-logo" href="./">Billy writes</a>
        <div class="bw-icons">{social_icons()}</div>
      </div>
      <nav class="bw-nav wrap">{links}</nav>
    </div>
    """)


def card(title, label, image, href):
    return f"""
    <a class="bw-card" href="{href}">
      <div class="img" style="background-image:url('{esc(image)}')"></div>
      <div class="over"><span class="label">{esc(label)}</span><h3>{esc(title)}</h3></div>
    </a>"""


def poem_cards(poems):
    return "".join(card(p["title"], p["language"] + " poetry", p["image"], f'poetry?p={slug(p["title"], i)}')
                   for i, p in poems)


def story_cards(stories):
    return "".join(card(s["title"], f'Story · {read_time(s["text"])} min read', s["image"], f'stories?s={slug(s["title"], i)}')
                   for i, s in stories)


def read_time(text):
    return max(1, round(len(text.split()) / 200))


def page_head(kicker, title, image, subtitle=""):
    sub = f"<p>{esc(subtitle)}</p>" if subtitle else ""
    st.html(f"""
    <div class="bw-pagehead" style="background-image:url('{esc(image)}')">
      <div><div class="kicker">{esc(kicker)}</div><h1>{esc(title)}</h1>{sub}</div>
    </div>
    """)


def footer():
    st.html(f"""
    <div class="bw-footer">
      <a class="bw-logo" href="./">Billy writes</a>
      <div class="bw-icons">{social_icons()}</div>
      <div class="small">Designed and brought to life by "Dwon"</div>
    </div>
    """)
