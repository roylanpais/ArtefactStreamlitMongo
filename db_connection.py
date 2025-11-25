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
