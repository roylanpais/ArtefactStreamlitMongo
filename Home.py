import streamlit as st
from auth import get_authenticator

st.set_page_config(
    page_title="Church & Artifact Database",
    page_icon="⛪",
    layout="wide"
)

# Authentication
authenticator = get_authenticator()
if authenticator:
    authenticator.login(location="main")

    if st.session_state["authentication_status"]:
        authenticator.logout("Logout", "sidebar")
        
        st.title(f"Welcome {st.session_state['name']} to the Church & Artifact Database ⛪")

        st.markdown("""
        This application allows you to manage a directory of Churches and the Artifacts sent to them.

        ### Quick Navigation:
        """)

        st.page_link("pages/2_Church_Directory.py", label="Church Directory : View and search for churches.", icon="⛪")
        st.page_link("pages/3_Artifacts_Directory.py", label="Artifacts Directory : View and search for Artifacts sent.", icon="🏺")
        st.page_link("pages/4_Add_&_Update_Artifact_Details.py", label="Add & Update Artifact Details : Record a new Artifact shipment.", icon="📝")
        st.page_link("pages/5_Add_&_Update_Church_Details.py", label="Add & Update Church Details : Details of a new church.", icon="➕")

    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")
else:
    st.error("Authentication configuration error.")
