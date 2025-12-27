import streamlit as st

st.set_page_config(page_title="AS TeamOps", layout="wide")

# ---------- USERS ----------
USERS = {
    "aniket": {"password": "admin123", "role": "admin"},
    "nitin": {"password": "market123", "role": "marketing"},
    "shivank": {"password": "circuit123", "role": "builder"},
    "adarsh": {"password": "code123", "role": "coder"},
    "vedant": {"password": "component123", "role": "components"},
}

# ---------- LOGIN ----------
def login():
    st.title("🔐 Login")

    username = st.text_input("Username").lower()
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.role = USERS[username]["role"]
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# ---------- DASHBOARD ----------
def dashboard():
    st.sidebar.title("📌 Menu")

    page = st.sidebar.radio(
        "Navigate",
        [
            "📊 Team Status",
            "🧠 Ideas",
            "📦 Components",
            "📂 Projects",
            "📈 YouTube Growth",
            "📸 Upload Work",
        ]
    )

    st.markdown(f"## 👤 {st.session_state.user.title()} ({st.session_state.role})")

    if page == "📊 Team Status":
        st.metric("Completed Tasks", 12)
        st.metric("Ongoing Tasks", 5)

    elif page == "🧠 Ideas":
        st.text_input("Idea Title")
        st.text_area("Idea Description")
        st.button("Submit Idea")

    elif page == "📦 Components":
        st.text_input("Component Name")
        st.number_input("Quantity", 1)
        st.button("Add Component")

    elif page == "📂 Projects":
        st.table({
            "Project": ["Smart Home", "Solar Tracker"],
            "Budget": ["₹2500", "₹1800"],
            "Views": ["12K", "8K"]
        })

    elif page == "📈 YouTube Growth":
        st.line_chart([100, 300, 900, 2000, 4500])

    elif page == "📸 Upload Work":
        st.file_uploader("Upload work proof", type=["jpg", "png"])

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# ---------- APP ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    dashboard()
else:
    login()
