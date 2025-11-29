import streamlit as st
import pandas as pd
from db_connection import get_all_artifacts, get_all_churches
from auth import check_authentication

st.set_page_config(page_title="Artifacts Directory", page_icon="🏺", layout="wide")

# Check Authentication
check_authentication()

st.title("Artifacts Directory")

artifacts = get_all_artifacts()

if not artifacts:
    st.warning("No Artifacts found in the database.")
else:
    df = pd.DataFrame(artifacts)
    
    # Filters
    st.sidebar.header("Search Filters")
    
    # Dropdown for specific church selection
    church_list = ["All"] + sorted(df['church_name'].unique().tolist())
    selected_church = st.sidebar.selectbox("Select Church", church_list)
    
    # Date Range Filter
    st.sidebar.subheader("Date Range")
    # Ensure sent_date is datetime
    df['sent_date'] = pd.to_datetime(df['sent_date'])
    
    min_date = df['sent_date'].min().date()
    max_date = df['sent_date'].max().date()
    
    start_date = st.sidebar.date_input("Start Date", min_date)
    end_date = st.sidebar.date_input("End Date", max_date)
    
    # Additional filters from requirements: Church name, State, city, and Priest's name
    state_filter = st.sidebar.text_input("Filter by State")
    city_filter = st.sidebar.text_input("Filter by City")
    priest_filter = st.sidebar.text_input("Filter by Priest Name")

    # Apply filters
    filtered_df = df.copy()
    
    if selected_church != "All":
        filtered_df = filtered_df[filtered_df['church_name'] == selected_church]
        
    if start_date and end_date:
        filtered_df = filtered_df[
            (filtered_df['sent_date'].dt.date >= start_date) & 
            (filtered_df['sent_date'].dt.date <= end_date)
        ]
        
    if 'church_state' in filtered_df.columns and state_filter:
        filtered_df = filtered_df[filtered_df['church_state'].str.contains(state_filter, case=False, na=False)]
        
    if 'church_city' in filtered_df.columns and city_filter:
        filtered_df = filtered_df[filtered_df['church_city'].str.contains(city_filter, case=False, na=False)]
        
    if 'priest_name' in filtered_df.columns and priest_filter:
        filtered_df = filtered_df[filtered_df['priest_name'].str.contains(priest_filter, case=False, na=False)]

    # Display results
    st.dataframe(
        filtered_df,
        column_config={
            "artifact_name": "Artifact Name",
            "quantity": "Quantity",
            "sent_date": st.column_config.DateColumn("Date Sent"),
            "church_name": "Church Name",
            "priest_name": "Priest",
            "church_state": "State",
            "church_city": "City"
        },
        width='stretch',
        hide_index=True
    )
    
    st.metric("Total Artifacts Found", len(filtered_df))
