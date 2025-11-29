import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

@st.cache_resource
def get_database_connection():
    """
    Establishes a connection to the MongoDB database using secrets.
    """
    try:
        if "mongo" not in st.secrets:
            st.error("MongoDB secrets not found. Please configure .streamlit/secrets.toml")
            return None

        uri = st.secrets["mongo"]["uri"]
        client = MongoClient(uri, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            # st.success("Successfully connected to MongoDB!")
        except Exception as e:
            st.error(f"Connection failed: {e}")
            return None
            
        return client
    except Exception as e:
        st.error(f"An error occurred while connecting to the database: {e}")
        return None

def get_db():
    client = get_database_connection()
    if client:
        # Assuming the database name is 'rosary_db' or similar, 
        # but usually it's part of the URI or we can pick a default.
        # Let's use a default name 'rosary_database' if not specified.
        return client['rosary_database']
    return None

def get_all_churches():
    db = get_db()
    if db is not None:
        return list(db['churches'].find({}, {'_id': 0})) # Exclude _id for display if needed, or keep it for updates
    return []

def get_all_artifacts():
    db = get_db()
    if db is not None:
        return list(db['artifacts'].find({}, {'_id': 0}))
    return []

def add_church(church_data):
    db = get_db()
    if db is not None:
        try:
            result = db['churches'].insert_one(church_data)
            return result.acknowledged
        except Exception as e:
            st.error(f"Error adding church: {e}")
            return False
    return False

def add_artifact(artifact_data):
    db = get_db()
    if db is not None:
        try:
            result = db['artifacts'].insert_one(artifact_data)
            return result.acknowledged
        except Exception as e:
            st.error(f"Error adding artifact: {e}")
            return False
    return False

def update_church(original_church_name, update_data):
    """
    Updates a church document. 
    Handles archiving the previous priest if the priest name has changed.
    """
    db = get_db()
    if db is not None:
        try:
            # Find the existing church
            existing_church = db['churches'].find_one({"church_name": original_church_name})
            
            if not existing_church:
                st.error(f"Church '{original_church_name}' not found.")
                return False
            
            # Check if priest name is changing
            new_priest_name = update_data.get("priest_name")
            current_priest_name = existing_church.get("priest_name")
            
            if new_priest_name and new_priest_name != current_priest_name:
                # Add current priest to previous_priests list
                previous_entry = {
                    "name": current_priest_name,
                    "archived_at": pd.Timestamp.now().isoformat()
                }
                
                # Update operation: set new fields and push to previous_priests
                db['churches'].update_one(
                    {"church_name": original_church_name},
                    {
                        "$set": update_data,
                        "$push": {"previous_priests": previous_entry}
                    }
                )
            else:
                # Just update the fields
                db['churches'].update_one(
                    {"church_name": original_church_name},
                    {"$set": update_data}
                )
                
            return True
        except Exception as e:
            st.error(f"Error updating church: {e}")
            return False
    return False
