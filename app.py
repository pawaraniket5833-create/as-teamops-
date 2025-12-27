import streamlit as st
from auth import login

st.set_page_config(
    page_title="AS TeamOps",
    layout="wide"
)

# Dark + Blue Theme
st.markdown("""
<style>
body { background-color: #0B1220; }
section[data-testid="stSidebar"] { background-color: #111A2E; }
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    user = st.session_state.user

    st.sidebar.title("👤 " + user["username"].capitalize())
    st.sidebar.caption("Role: " + user["role"])

    st.title("📊 AS TeamOps Dashboard")
    st.info("Mobile-friendly team coordination system")
