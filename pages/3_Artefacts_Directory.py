import streamlit as st
import pandas as pd
from db_connection import get_all_artifacts, get_all_churches

st.set_page_config(page_title="Artefacts Directory", page_icon="🏺", layout="wide")

st.title("Artefacts Directory")

artifacts = get_all_artifacts()

if not artifacts:
    st.warning("No artefacts found in the database.")
else:
    df = pd.DataFrame(artifacts)
    
    # Filters
    st.sidebar.header("Search Filters")
    
    # Dropdown for specific church selection
    # Get unique churches from the artifacts data itself, or from the church DB?
    # Requirement says "based on the user's selected church from a dropdown query"
    # It's better to list churches that actually have artifacts, or all churches?
    # Let's list all churches from the artifacts table for filtering.
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
        
    # Note: State/City/Priest might not be in the artifact record directly if not denormalized.
    # In my add_artifact implementation, I denormalized them (added them to the artifact record).
    # If they are missing, these filters won't work well unless we join with church data.
    # Assuming they are present as per my add_artifact implementation.
    
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
            "artifact_name": "Artefact Name",
            "quantity": "Quantity",
            "sent_date": st.column_config.DateColumn("Date Sent"),
            "church_name": "Church Name",
            "priest_name": "Priest",
            "church_state": "State",
            "church_city": "City"
        },
        use_container_width=True,
        hide_index=True
    )
    
    st.metric("Total Artefacts Found", len(filtered_df))
