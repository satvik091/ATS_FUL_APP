import streamlit as st
from database import Database

def check_authentication():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        st.warning("Please login to access this page")
        st.stop()
