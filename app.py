import streamlit as st

# Page settings - ye tab pe title aur icon set karta hai
st.set_page_config(page_title="Billy Writes too", page_icon="✍️", layout="wide")

# Website ke saare pages — menu humara apna hai (style.py mein), isliye yahan "hidden"
pages = [
    st.Page("pages/home.py", title="Billy Writes too", default=True),
    st.Page("pages/2_Poetry.py", title="Poetry · Billy Writes too", url_path="poetry"),
    st.Page("pages/1_Quotes.py", title="Quotes · Billy Writes too", url_path="quotes"),
    st.Page("pages/3_Stories.py", title="Stories · Billy Writes too", url_path="stories"),
    st.Page("pages/4_Contact.py", title="Contact · Billy Writes too", url_path="contact"),
]

st.navigation(pages, position="hidden").run()
