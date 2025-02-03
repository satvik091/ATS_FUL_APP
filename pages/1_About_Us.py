import streamlit as st
from auth import check_authentication

def show():
    check_authentication()
    
    # Streamlit UI
    st.markdown("<h1 style='text-decoration: underline;'>JobFit AI – Smart Hiring Made Easy</h1>", unsafe_allow_html=True)
    st.write("🚀 **AI-Powered Resume Matching**")

    # Features
    st.write("Uses Google Gemini API for advanced NLP & machine learning.")
    st.write("Analyzes resumes based on skills, experience, and job relevance.")

    st.write("📊 **Automated Ranking System**")
    st.write("Scores and ranks candidates based on suitability.")
    st.write("Helps recruiters identify top talent instantly.")

    st.write("⚡ **Seamless & Efficient Hiring**")
    st.write("Streamlit-powered UI for an interactive experience.")
    st.write("Reduces manual screening and shortens hiring time.")

    st.write("📂 **ATS Integration & Data-Driven Insights**")
    st.write("Easily integrates with Applicant Tracking Systems (ATS).")
    st.write("Provides real-time analytics for better hiring decisions.")


if __name__ == "__main__":
    show()
