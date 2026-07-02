import streamlit as st

col1, col2, col3 = st.columns(3)
with col2:
    st.title(":grey[Silver Kampong Admin Terminal]")
    st.write("[insert slogan]")
    
    # Forms group variables together securely during multi-page execution
    with st.form("auth_form", border=True):
        user_name = st.text_input("**Username:**")
        st.write("")
        password = st.text_input("**Password:**", type="password")
        login = st.form_submit_button(":red[**Login**]")

if login:
    if user_name == "mosskin-8" and password == "moss-whale-66":
        st.session_state.logged_in = True
        st.success('Successful login!', icon="✅")
        st.rerun()
    else:
        st.error("Unsuccessful login", icon="🚨")
        st.error('Your Username or password is incorrect', icon="🚨")
