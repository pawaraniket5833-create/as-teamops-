import streamlit as st
from datetime import datetime
import requests

# ------------------ PAGE CONFIG ------------------
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
a {
    color: #1e88e5;
    text-decoration: none;
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
current_user = st.sidebar.selectbox("Login as", list(members.keys()))
role = members[current_user]
st.sidebar.markdown(f"**Role:** `{role}`")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Projects", "Upload Work", "Tech News", "Components", "YouTube Growth"]
)

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.experimental_rerun()

# ------------------ HEADER ------------------
st.markdown(f"""
<div class="card">
    <h1>🚀 Channel Dashboard</h1>
    <p>Welcome <b>{current_user}</b> <span class="role">({role})</span></p>
    <p>Manage ideas, uploads, and growth</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ------------------ PAGE FUNCTIONS ------------------

def dashboard_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="white-card">
            <h3>📈 Growth</h3>
            <p>Subscribers increasing steadily</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="white-card">
            <h3>🎥 Videos</h3>
            <p>Consistent uploads planned</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="white-card">
            <h3>🔥 Engagement</h3>
            <p>Audience interaction improving</p>
        </div>
        """, unsafe_allow_html=True)


def projects_page():
    st.subheader("📂 Projects")
    for p in projects:
        st.markdown(f"""
        <div class="white-card">
            <h3>{p['name']}</h3>
            <p>Budget: ₹{p['budget']}</p>
            <p>Views: {p['views']}</p>
        </div>
        <br>
        """, unsafe_allow_html=True)


def upload_page():
    st.subheader("📤 Upload Work")
    st.text_input("Title")
    st.text_area("Description")
    st.file_uploader("Upload file")
    st.button("Submit")


def tech_news_page():
    st.subheader("📰 Tech News")
    st.info("Latest technology updates will appear here.")


def components_page():
    st.subheader("🔧 Components")
    st.write("Maintain inventory of electronic components.")


def youtube_growth_page():
    st.subheader("📊 YouTube Growth")
    st.write("Analytics and growth strategies.")

# ------------------ ROUTING ------------------
if menu == "Dashboard":
    dashboard_page()
elif menu == "Projects":
    projects_page()
elif menu == "Upload Work":
    upload_page()
elif menu == "Tech News":
    tech_news_page()
elif menu == "Components":
    components_page()
elif menu == "YouTube Growth":
    youtube_growth_page()        else:
            st.warning("No news found at the moment.")
    except Exception as e:
        st.error(f"Error fetching news: {e}")

# --- Components Page ---
def components_page():
    st.subheader("📦 Components")
    st.text_input("Component Name")
    st.number_input("Quantity", 1)
    st.button("Add Component")

# --- YouTube Growth Page ---
def youtube_growth_page():
    st.subheader("📈 YouTube Growth Tracker")
    st.line_chart([100, 300, 900, 2000, 4500])  # Placeholder

# ------------------ PAGE ROUTING ------------------
if menu == "Dashboard":
    dashboard_page()
elif menu == "Projects":
    projects_page()
elif menu == "Upload Work":
    upload_work_page()
elif menu == "Tech News":
    tech_news_page()
elif menu == "Components":
    components_page()
elif menu == "YouTube Growth":
    youtube_growth_page()        
    st.markdown("""
    <div>...</div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="white-card">
            # Replace with Unicode
<h3>\U0001F440 Views</h3>
            <p>Total reach</p>
            <b>120K+</b>
        </div>
        """, unsafe_allow_html=True)

# ------------------ PROJECTS ------------------
elif menu == "Projects":
    st.subheader("📂 Ongoing Projects")
    for p in projects:
            # Replace with Unicode
            st.markdown(
    f"""
    <div class="card">
        <h3>Views</h3>
        <p>{views}</p>
    </div>
    """,
    unsafe_allow_html=True
)
            st.markdown(f"""
<p>Budget: &#8377; {p['budget']}</p>
""", unsafe_allow_html=True)
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
    # ------------------ TECH NEWS (Live) ------------------
import requests

elif menu == "Tech News":
    st.subheader("📰 Latest Tech News")

    API_KEY = "ad01e9dc6dce46c6979726dcbdcc8ae7"  # Your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=5&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok" and data["totalResults"] > 0:
            for article in data["articles"]:
                st.markdown(f"""
                <div class="white-card">
                    <h4>🔹 <a href="{article['url']}" target="_blank">{article['title']}</a></h4>
                    <p>{article['description'] or ""}</p>
                    <small>Source: {article['source']['name']}</small>
                </div>
                <br>
                """, unsafe_allow_html=True)
        else:
            st.warning("No news found at the moment.")
    except Exception as e:
        st.error(f"Error fetching news: {e}")
