from content import socials
from style import st, esc, setup, page_head, footer, icon

setup("contact")
page_head("Say hello", "Contact", "https://images.unsplash.com/photo-1456324504439-367cee3b3c32?w=2000&q=80")

email = next((s["url"].replace("mailto:", "") for s in socials if s["icon"] == "email"), "")
pills = "".join(
    f'<a href="{esc(s["url"])}" target="_blank" rel="noopener">{icon(s["icon"])}{esc(s["name"])}</a>'
    for s in socials if s["url"]
)

st.html(f"""
<div class="bw-contact">
  <p>Kuch kehna hai, koi poem pasand aayi, ya saath mein kuch likhna hai?
  Bejhijak message karo — har message padha jaata hai.</p>
  <a class="mail" href="mailto:{esc(email)}">{esc(email)}</a>
  <div class="bw-pills">{pills}</div>
</div>
""")

footer()
