import streamlit as st
import pandas as pd
from db_connection import get_all_churches

st.set_page_config(page_title="Church Directory", page_icon="⛪", layout="wide")

st.title("Church Directory")

churches = get_all_churches()

if not churches:
    st.warning("No churches found in the database.")
else:
    df = pd.DataFrame(churches)
    
    # Filters
    st.sidebar.header("Search Filters")
    
    # Dropdown for specific church selection
    church_list = ["All"] + sorted(df['church_name'].unique().tolist())
    selected_church = st.sidebar.selectbox("Select Church", church_list)
    
    # Additional filters
    state_filter = st.sidebar.text_input("Filter by State")
    city_filter = st.sidebar.text_input("Filter by City")
    priest_filter = st.sidebar.text_input("Filter by Priest Name")
    
    # Apply filters
    filtered_df = df.copy()
    
    if selected_church != "All":
        filtered_df = filtered_df[filtered_df['church_name'] == selected_church]
        
    if state_filter:
        filtered_df = filtered_df[filtered_df['state'].str.contains(state_filter, case=False, na=False)]
        
    if city_filter:
        filtered_df = filtered_df[filtered_df['city'].str.contains(city_filter, case=False, na=False)]
        
    if priest_filter:
        filtered_df = filtered_df[filtered_df['priest_name'].str.contains(priest_filter, case=False, na=False)]
    
    # Display results
    st.dataframe(
        filtered_df,
        column_config={
            "church_name": "Church Name",
            "state": "State",
            "city": "City",
            "priest_name": "Priest",
            "phone_number": "Phone",
            "email_id": "Email",
            "address": "Address"
        },
        use_container_width=True,
        hide_index=True
    )
    
    st.metric("Total Churches Found", len(filtered_df))
