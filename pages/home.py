import datetime
from content import hero_image, poems, quotes, stories
from style import st, esc, setup, poem_cards, story_cards, footer

setup("home")

# ---------- Hero: badi photo + upar 3 latest poems ----------
st.html(f"""
<div class="bw-hero" style="background-image:url('{esc(hero_image)}')">
  <div class="tag">
    <div class="kicker">Poetry · Quotes · Stories</div>
    <h1>Billy Writes too</h1>
    <p>Words in Hindi &amp; Punjabi, written from the heart.</p>
  </div>
</div>
<div class="bw-hero-cards wrap">
  <div class="bw-cards">{poem_cards(list(enumerate(poems))[:3])}</div>
</div>
""")

# ---------- About ----------
st.html("""
<div class="bw-section wrap">
  <div class="bw-about">
    <div class="sig">Hello, I'm Billy</div>
    <p>This is my little diary on the internet — poems about love, silence and the things
    we never say out loud. Grab a cup of chai and stay a while.</p>
  </div>
</div>
""")

# ---------- Quote of the day (har din alag) ----------
q = quotes[datetime.date.today().toordinal() % len(quotes)]
st.html(f"""
<div class="bw-band">
  <div class="kicker">Quote of the day</div>
  <blockquote>“{esc(q["text"])}”</blockquote>
  <div class="by">{esc(q.get("by", "Billy"))}</div>
</div>
""")

# ---------- Baaki poems ----------
if len(poems) > 3:
    st.html(f"""
    <div class="bw-section wrap">
      <div class="bw-head"><div class="kicker">More to read</div><h2>Poetry</h2></div>
      <div class="bw-cards two">{poem_cards(list(enumerate(poems))[3:5])}</div>
      <div class="bw-more"><a href="poetry">VIEW ALL POEMS</a></div>
    </div>
    """)

# ---------- Stories ----------
st.html(f"""
<div class="bw-section wrap">
  <div class="bw-head"><div class="kicker">Short fiction</div><h2>Stories</h2></div>
  <div class="bw-cards two">{story_cards(list(enumerate(stories))[:2])}</div>
  <div class="bw-more"><a href="stories">ALL STORIES</a></div>
</div>
""")

footer()
