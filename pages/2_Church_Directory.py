import streamlit as st
import pandas as pd
from db_connection import get_all_churches
from auth import check_authentication

st.set_page_config(page_title="Church Directory", page_icon="⛪", layout="wide")

# Check Authentication
check_authentication()

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
        width='stretch',
        hide_index=True
    )
    
    st.metric("Total Churches Found", len(filtered_df))

    # Show details for selected church if "All" is not selected
    if selected_church != "All" and not filtered_df.empty:
        st.markdown("---")
        st.subheader(f"Details for {selected_church}")
        
        church_details = filtered_df.iloc[0]
        
        # Display Previous Priests
        previous_priests = church_details.get("previous_priests", [])
        
        if isinstance(previous_priests, list) and previous_priests:
            st.write("### Previous Priests")
            
            # Create a DataFrame for better display
            history_data = []
            for entry in previous_priests:
                if isinstance(entry, dict):
                    history_data.append({
                        "Name": entry.get("name", "Unknown"),
                        "Archived At": entry.get("archived_at", "Unknown")
                    })
                else:
                    # Handle legacy or simple string format if any
                    history_data.append({"Name": str(entry), "Archived At": "N/A"})
            
            if history_data:
                st.table(pd.DataFrame(history_data))
        else:
            st.info("No history of previous priests recorded.")
