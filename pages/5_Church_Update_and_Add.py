import streamlit as st
from db_connection import add_church

st.set_page_config(page_title="Church Update & Add", page_icon="⛪")

st.title("Add New Church Details")

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
                "address": address
            }
            
            if add_church(church_data):
                st.success(f"Successfully added {church_name} to the database!")
            else:
                st.error("Failed to add church. Please check your database connection.")
