import streamlit as st
from database import Database

def main():
    # Set the page configuration
    st.set_page_config(page_title="ATS Pro", page_icon="📊")
    
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    
    # Instantiate the database object
    db = Database()
    
    # Display content based on login status
    if not st.session_state.logged_in:
        st.title("Welcome to ATS Pro")
        
        # Tabs for Login and Sign Up
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.header("Login")
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login"):
                if db.check_login(login_username, login_password):
                    st.session_state.logged_in = True
                    st.session_state.page = "dashboard"
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid username or password")
        
        with tab2:
            st.header("Sign Up")
            new_username = st.text_input("Username", key="new_username")
            new_password = st.text_input("Password", type="password", key="new_password")
            new_email = st.text_input("Email", key="new_email")
            
            if st.button("Sign Up"):
                if new_username and new_password and new_email:
                    if db.add_user(new_username, new_password, new_email):
                        st.success("Account created successfully! Please login.")
                        st.session_state.page = "login"
                    else:
                        st.error("Username already exists")
                else:
                    st.error("Please fill all fields")
    
    else:
        # Dashboard View
        st.title("Welcome to ATS Pro Dashboard")
        st.write("Please use the sidebar to navigate through different features.")
        
        # Sidebar Logout Button
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.success("You have logged out.")
    
    # Rerun logic to update the interface
    if st.session_state.page != "dashboard" and st.session_state.logged_in:
        st.session_state.page = "dashboard"

if __name__ == "__main__":
    main()
