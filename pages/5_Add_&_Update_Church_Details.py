import streamlit as st
from db_connection import add_church, update_church, get_all_churches
from auth import check_authentication
import pandas as pd

st.set_page_config(page_title="Add New Church or Update Church Details", page_icon="⛪")

# Check Authentication
check_authentication()

st.title("Add New Church or Update Church Details")

# Toggle between Add and Update
action = st.radio("Select Action", ["Add New Church", "Update Existing Church details"])

if action == "Add New Church":
    st.subheader("Add New Church")
    with st.form("add_church_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            church_name = st.text_input("Church Name")
            state = st.text_input("State")
            city = st.text_input("City")
            priest_name = st.text_input("Priest's Name")
            
        with col2:
            phone_number = st.text_input("Phone Number")
            email_id = st.text_input("Email ID")
            address = st.text_area("Address")

        submitted = st.form_submit_button("Add Church")

        if submitted:
            if not church_name or not city:
                st.error("Church Name and City are required fields.")
            else:
                church_data = {
                    "church_name": church_name,
                    "state": state,
                    "city": city,
                    "priest_name": priest_name,
                    "phone_number": phone_number,
                    "email_id": email_id,
                    "address": address,
                    "previous_priests": []
                }
                
                if add_church(church_data):
                    st.success(f"Successfully added {church_name} to the database!")
                else:
                    st.error("Failed to add church. Please check your database connection.")

elif action == "Update Existing Church":
    st.subheader("Update Existing Church")
    
    churches = get_all_churches()
    if not churches:
        st.warning("No churches found to update.")
    else:
        church_names = sorted([c['church_name'] for c in churches])
        selected_church_name = st.selectbox("Select Church to Update", church_names)
        
        # Find selected church data
        selected_church = next((c for c in churches if c['church_name'] == selected_church_name), None)
        
        if selected_church:
            with st.form("update_church_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    # Church name is usually not editable as it's the identifier here, 
                    # but if we wanted to allow it, we'd need to handle ID-based updates.
                    # For now, let's keep it disabled or read-only to avoid confusion.
                    st.text_input("Church Name", value=selected_church.get('church_name', ''), disabled=True)
                    state = st.text_input("State", value=selected_church.get('state', ''))
                    city = st.text_input("City", value=selected_church.get('city', ''))
                    priest_name = st.text_input("Priest's Name", value=selected_church.get('priest_name', ''))
                    
                with col2:
                    phone_number = st.text_input("Phone Number", value=selected_church.get('phone_number', ''))
                    email_id = st.text_input("Email ID", value=selected_church.get('email_id', ''))
                    address = st.text_area("Address", value=selected_church.get('address', ''))

                submitted = st.form_submit_button("Update Church")

                if submitted:
                    update_data = {
                        "state": state,
                        "city": city,
                        "priest_name": priest_name,
                        "phone_number": phone_number,
                        "email_id": email_id,
                        "address": address
                    }
                    
                    if update_church(selected_church_name, update_data):
                        st.success(f"Successfully updated {selected_church_name}!")
                        st.rerun()
                    else:
                        st.error("Failed to update church.")
