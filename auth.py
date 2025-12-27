import streamlit as st

USERS = {
    "aniket": {"password": "admin123", "role": "admin"},
    "nitin": {"password": "member123", "role": "member"},
    "shivank": {"password": "member123", "role": "member"},
    "adarsh": {"password": "member123", "role": "member"},
    "vedant": {"password": "member123", "role": "member"},
}

def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = USERS[username]["role"]
            st.session_state.user = username
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid username or password ❌")
