import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def get_authenticator():
    """
    Initializes and returns the authenticator object.
    """
    if "credentials" not in st.secrets:
        st.error("Credentials not found in secrets.toml")
        return None

    # Convert secrets to dictionary format expected by authenticator
    # st.secrets returns a Secrets object, we need to convert it to a dict structure
    # The library expects a dict with 'credentials', 'cookie', 'preauthorized' keys.
    
    config = {
        'credentials': st.secrets['credentials'].to_dict(),
        'cookie': st.secrets['cookie'].to_dict(),
        'preauthorized': st.secrets['preauthorized'].to_dict() if 'preauthorized' in st.secrets else {'emails': []}
    }

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator

def check_authentication():
    """
    Checks if the user is authenticated.
    If not, stops execution.
    Should be called at the top of every page.
    """
    authenticator = get_authenticator()
    if not authenticator:
        st.stop()

    # The login method renders the login widget and handles the session state
    # For pages other than Home, we just want to check status.
    # But we need to ensure the session state is populated.
    
    # In recent versions of streamlit-authenticator, we can check st.session_state["authentication_status"]
    
    if st.session_state.get("authentication_status") is None:
        # Not logged in, and not on login page (Home handles login)
        # Redirect to Home or show warning
        st.warning("Please log in on the Home page.")
        st.stop()
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
        st.stop()
    elif st.session_state["authentication_status"] is True:
        # Authenticated
        # Optionally show a logout button in sidebar
        authenticator.logout("Logout", "sidebar")
        return True
    
    return False
