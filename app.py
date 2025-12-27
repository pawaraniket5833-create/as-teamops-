import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="AS TeamOps",
    page_icon="🚀",
    layout="wide"
)

# ------------------ CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.card {
    background: linear-gradient(135deg, #1e88e5, #42a5f5);
    padding: 20px;
    border-radius: 20px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    animation: fadeIn 0.6s ease;
}
.white-card {
    background: #ffffff;
    padding: 18px;
    border-radius: 20px;
    color: #000;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}
.role {
    font-size: 14px;
    opacity: 0.8;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
.nav {
    background-color: #111827;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ DATA ------------------
members = {
    "Aniket": "Admin",
    "Nitin": "Marketing",
    "Shivank": "Circuit Builder",
    "Adarsh": "Coder",
    "Vedant": "Components Manager"
}

projects = [
    {"name": "Smart Home", "budget": 2500, "views": "12K"},
    {"name": "Solar Tracker", "budget": 1800, "views": "8K"}
]

# ------------------ SIDEBAR ------------------
st.sidebar.title("👥 Team Members")
current_user = st.sidebar.selectbox("Login as", members.keys())
role = members[current_user]

st.sidebar.markdown(f"**Role:** `{role}`")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Projects", "Upload Work", "Tech News", "Components", "YouTube Growth"]
)

# ------------------ HEADER ------------------
st.markdown(f"""
<div class="card">
    <h1>🚀 Channel Dashboard</h1>
    <p>Welcome <b>{current_user}</b> <span class="role">({role})</span></p>
    <p>Manage ideas, uploads, and growth</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ------------------ DASHBOARD ------------------
if menu == "Dashboard":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="white-card">
            <h3>📈 Growth</h3>
            <p>Subscribers increasing steadily</p>
            <b>+18% this month</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="white-card">
            <h3>🎥 Videos</h3>
            <p>Total uploads</p>
            <b>24 Videos</b>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="white-card">
            <h3>👀 Views</h3>
            <p>Total reach</p>
            <b>120K+</b>
        </div>
        """, unsafe_allow_html=True)

# ------------------ PROJECTS ------------------
elif menu == "Projects":
    st.subheader("📂 Ongoing Projects")
    for p in projects:
        st.markdown(f"""
        <div class="white-card">
            <h4>{p['name']}</h4>
            <p>Budget: ₹{p['budget']}</p>
            <p>Views: {p['views']}</p>
        </div>
        <br>
        """, unsafe_allow_html=True)

# ------------------ UPLOAD WORK ------------------
elif menu == "Upload Work":
    st.subheader("📤 Upload Work Completion")
    uploaded = st.file_uploader("Upload image of your work", type=["png", "jpg", "jpeg"])
    note = st.text_area("Work description")

    if st.button("Submit"):
        if uploaded:
            st.success("✅ Work uploaded successfully!")
            st.image(uploaded, width=250)
            st.caption(f"Uploaded by {current_user} on {datetime.now().strftime('%d %b %Y')}")
        else:
            st.warning("Please upload an image.")

# ------------------ TECH NEWS ------------------
elif menu == "Tech News":
    st.subheader("📰 Tech Updates (Curated)")
    st.markdown("""
    <div class="white-card">
        <ul>
            <li>🔋 New solar panel efficiency record achieved</li>
            <li>🏠 AI-powered smart homes on the rise</li>
            <li>🤖 Open-source robotics gaining popularity</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------ COMPONENTS ------------------
elif menu == "Components":
    st.subheader("📦 Components")
    st.text_input("Component Name")
    st.number_input("Quantity", 1)
    st.button("Add Component")

# ------------------ YOUTUBE GROWTH ------------------
elif menu == "YouTube Growth":
    st.subheader("📈 YouTube Growth Tracker")
    st.line_chart([100, 300, 900, 2000, 4500])  # Replace with actual channel data

# ------------------ LOGOUT ------------------
if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.experimental_rerun()
