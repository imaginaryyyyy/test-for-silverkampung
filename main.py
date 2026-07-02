import streamlit as st

st.write("Current Login State:", st.session_state.logged_in)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

login_page = st.Page("admin_login.py", title="Login")
admin_panel = st.Page("show_pages/admin_panel.py", title="Admin Panel")

if st.session_state.logged_in:
  pages = [admin_panel]
else:
  pages = [login_page]

page = st.navigation(pages)
page.run()
