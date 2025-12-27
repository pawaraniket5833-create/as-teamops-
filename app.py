
import streamlit as st
from auth import login

st.set_page_config(page_title="AS TeamOps", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

st.title("🚀 AS TeamOps Dashboard")
st.caption(f"Welcome {st.session_state.user}")

if st.session_state.role == "admin":
    st.success("Admin access enabled 👑")
else:
    st.info("Member view (limited access) ⚫")

st.subheader("Team Overview")
st.write("Task tracking, ideas, and coordination will appear here.")
