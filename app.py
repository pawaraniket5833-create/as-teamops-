import streamlit as st

st.set_page_config(
    page_title="AS TeamOps",
    layout="wide"
)

st.markdown(
    """
    <style>
    body {
        background-color: #0b132b;
        color: #eaeaea;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 AS TeamOps Dashboard")
st.caption("AS SlowProcesser – Team Coordination System")

st.success("App is running successfully ✅")

st.subheader("Team Members")
st.write("""
- 👑 Aniket (Admin)  
- 📢 Nitin (Marketing)  
- 🔌 Shivank (Circuit Builder)  
- 💻 Adarsh (Coder)  
- 📦 Vedant (Components Manager)
""")
