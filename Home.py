import streamlit as st

st.set_page_config(
    page_title="Church & Artefact Database",
    page_icon="⛪",
    layout="wide"
)

st.title("Welcome to the Church & Artefact Database ⛪")

st.markdown("""
This application allows you to manage a directory of Churches and the Artefacts sent to them.

### Features:
- **Church Directory**: View and search for churches.
- **Artefact Directory**: View and search for artefacts sent to churches.
- **Update & Add**: Add new churches and artefacts to the database.

### Getting Started:
Use the sidebar to navigate between the different pages.

- **Church Directory**: Browse existing church records.
- **Artefacts Directory**: Browse sent artefacts.
- **Artefact Update & Add**: Record a new artefact shipment.
- **Church Update & Add**: Register a new church.
""")

st.info("Please ensure your database connection is configured in `.streamlit/secrets.toml`.")
