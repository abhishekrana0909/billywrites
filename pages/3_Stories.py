from content import stories
from style import st, esc, setup, slug, page_head, story_cards, read_time, footer

setup("stories")

# Link mein ?s=... ho to woh ek story dikhao, warna saari stories ki list
chosen = st.query_params.get("s")
match = [(i, s) for i, s in enumerate(stories) if slug(s["title"], i) == chosen]

if match:
    i, story = match[0]
    page_head(f"Story · {read_time(story['text'])} min read", story["title"], story["image"])
    paras = "".join(f"<p>{esc(p)}</p>" for p in story["text"].split("\n\n"))
    st.html(f"""
    <div class="bw-read">
      <a class="bw-back" href="stories">← ALL STORIES</a>
      <div class="bw-story">{paras}</div>
      <div class="bw-sign">— Billy Writes too ❤️</div>
    </div>
    """)

    others = [(j, s) for j, s in enumerate(stories) if j != i][:2]
    if others:
        st.html(f"""
        <div class="bw-section wrap">
          <div class="bw-head"><div class="kicker">Keep reading</div><h2>More stories</h2></div>
          <div class="bw-cards two">{story_cards(others)}</div>
        </div>
        """)
else:
    page_head("Short fiction", "Stories", stories[0]["image"], "Little stories to read with your chai.")
    st.html(f"""
    <div class="bw-section wrap">
      <div class="bw-cards two">{story_cards(list(enumerate(stories)))}</div>
    </div>
    """)

footer()
