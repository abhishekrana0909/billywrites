from content import poems
from style import st, esc, setup, slug, page_head, poem_cards, footer

setup("poetry")

# Link mein ?p=... ho to woh ek poem dikhao, warna saari poems ki list
chosen = st.query_params.get("p")
match = [(i, p) for i, p in enumerate(poems) if slug(p["title"], i) == chosen]

if match:
    i, poem = match[0]
    page_head(poem["language"] + " poetry", poem["title"], poem["image"])

    # Har stanza (khaali line se alag) ek block, har line <br> se
    stanzas = "".join(
        '<div class="stanza">' + "<br>".join(esc(line) for line in block.split("\n")) + "</div>"
        for block in poem["text"].split("\n\n")
    )
    st.html(f"""
    <div class="bw-read">
      <a class="bw-back" href="poetry">← ALL POEMS</a>
      <div class="bw-poem">{stanzas}</div>
      <div class="bw-sign">— Billy Writes too ❤️</div>
    </div>
    """)

    others = [(j, p) for j, p in enumerate(poems) if j != i][:3]
    st.html(f"""
    <div class="bw-section wrap">
      <div class="bw-head"><div class="kicker">Keep reading</div><h2>More poems</h2></div>
      <div class="bw-cards">{poem_cards(others)}</div>
    </div>
    """)
else:
    page_head("Verses", "Poetry", poems[0]["image"], "Love, silence and everything in between.")
    st.html(f"""
    <div class="bw-section wrap">
      <div class="bw-cards">{poem_cards(list(enumerate(poems)))}</div>
    </div>
    """)

footer()
