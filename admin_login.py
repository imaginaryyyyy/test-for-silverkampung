import streamlit as st

col1, col2, col3 = st.columns(3)
with col2:
    st.title(":grey[Silver Kampong Admin Terminal]")
    st.write("[insert slogan]")
    with st.form("login_form", border=True)
      container = st.container(border=True)
      container.text_input("**Username:**", key="username")
      container.write("")
      container.text_input("**Password:**", key="password")
      login = container.button(":red[**Login**]")
  
if login:
    #Connect to backend for real authentication
    if st.session_state.username == "mosskin-8" and st.session_state.password == "moss-whale-66": #Testing purposes only, the file.json right now does not include the details
        st.session_state.logged_in = True
        st.success('Successful login!', icon="✅")
        st.rerun()
    else:
        st.error(f"Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
