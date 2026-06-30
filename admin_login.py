import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def Show_Pages():
  if st.session_state.logged_in == True:
    pages = [login_page, admin_panel]
    show_page = st.navigation(pages)
    show_page.run
  else:
    pages = [home_page]
    show_page = st.navigation(pages)
    show_page.run

Show_Pages()

login_page = st.Page("admin_login.py", title="Login")
admin_panel = st.Page("pages/silverrrr.py", title="Admin Panel")

col1, col2, col3 = st.columns(3)
with col2:
    st.title(":grey[Silver Kampong Admin Terminal]")
    st.write("[insert slogan]")
    container = st.container(border=True)
    user_name = container.text_input("**Username:**")
    container.write("")
    password = container.text_input("**Password:**")

with col3:
    login = container.button(":red[**Login**]")

if user_name and password and login:
    #Connect to backend for real authentication
    if user_name == "mosskin-8" and password == "moss-whale-66": #Testing purposes only, the file.json right now does not include the details
        st.session_state.logged_in = True
        st.success('Successful login!', icon="✅")
        Show_Pages()

    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
        Show_Pages()
