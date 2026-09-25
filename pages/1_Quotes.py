import random
from content import quotes
from style import st, esc, setup, page_head, footer

setup("quotes")
page_head("Collection", "Quotes", "https://images.unsplash.com/photo-1471107340929-a87cd0f5b5f3?w=2000&q=80",
          "Short thoughts that stuck with me.")

st.html('<div style="height:60px"></div>')

# Search box aur random quote button
col1, col2 = st.columns([4, 1], vertical_alignment="bottom")
search = col1.text_input("Search", placeholder="Search quotes…", label_visibility="collapsed")
surprise = col2.button("SURPRISE ME", use_container_width=True)

if surprise:
    q = random.choice(quotes)
    st.html(f"""
    <div class="bw-band" style="margin:0 0 60px">
      <blockquote>“{esc(q["text"])}”</blockquote>
      <div class="by">{esc(q.get("by", "Billy"))}</div>
    </div>
    """)

# Search ke hisaab se quotes filter karo
shown = [q for q in quotes if search.lower() in q["text"].lower()]
styles = ["", "dark", "soft"]  # cards ke teen alag look, baari baari

if shown:
    cards = "".join(
        f'<div class="bw-quote {styles[i % 3]}"><p>“{esc(q["text"])}”</p><span class="by">— {esc(q.get("by", "Billy"))}</span></div>'
        for i, q in enumerate(shown)
    )
    st.html(f'<div class="wrap"><div class="bw-quotes">{cards}</div></div>')
else:
    st.html('<div class="wrap" style="text-align:center;padding:40px 0;color:#777">Koi quote nahi mila. Kuch aur search karke dekho!</div>')

footer()
