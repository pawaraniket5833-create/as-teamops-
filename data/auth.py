import streamlit as st
import pandas as pd

def load_users():
    return pd.read_csv("data/users.csv")

def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        user = users[
            (users["username"] == username) &
            (users["password"] == password)
        ]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.user = user.iloc[0].to_dict()
            st.rerun()
        else:
            st.error("Invalid credentials")
