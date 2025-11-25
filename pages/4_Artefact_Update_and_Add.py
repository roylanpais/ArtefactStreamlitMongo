import streamlit as st
import datetime
from db_connection import get_all_churches, add_artifact

st.set_page_config(page_title="Artefact Update & Add", page_icon="🏺")

st.title("Add New Artefact Shipment")

# Fetch existing churches for the dropdown
churches = get_all_churches()
church_names = [c['church_name'] for c in churches] if churches else []

if not church_names:
    st.warning("No churches found. Please add a church first.")
    st.page_link("pages/5_Church_Update_and_Add.py", label="Go to Add Church Page", icon="⛪")
else:
    with st.form("add_artifact_form"):
        artifact_name = st.text_input("Artefact Name")
        quantity = st.number_input("Quantity", min_value=1, step=1)
        sent_date = st.date_input("Date Sent", datetime.date.today())
        
        # Searchable dropdown for church
        selected_church_name = st.selectbox("Select Church", church_names)
        
        # Auto-fill priest name based on selected church
        selected_church_data = next((c for c in churches if c['church_name'] == selected_church_name), None)
        priest_name = selected_church_data.get('priest_name', '') if selected_church_data else ''
        
        st.text_input("Priest Name (Auto-filled)", value=priest_name, disabled=True)
        
        submitted = st.form_submit_button("Add Artefact")
        
        if submitted:
            if not artifact_name:
                st.error("Artefact Name is required.")
            else:
                # Convert date to datetime for MongoDB compatibility if needed, or keep as string/datetime
                # PyMongo handles datetime objects well.
                artifact_data = {
                    "artifact_name": artifact_name,
                    "quantity": quantity,
                    "sent_date": sent_date.isoformat(), # Store as string YYYY-MM-DD for simplicity
                    "church_name": selected_church_name,
                    "priest_name": priest_name,
                    "church_state": selected_church_data.get('state', ''),
                    "church_city": selected_church_data.get('city', '')
                }
                
                if add_artifact(artifact_data):
                    st.success(f"Successfully added {artifact_name} shipment to {selected_church_name}!")
                else:
                    st.error("Failed to add artifact. Please check your database connection.")
