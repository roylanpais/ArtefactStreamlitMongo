import streamlit as st
from db_connection import get_all_churches, get_all_artifacts

st.write("Verifying data...")
churches = get_all_churches()
artifacts = get_all_artifacts()

print(f"Churches count: {len(churches)}")
print(f"Artifacts count: {len(artifacts)}")
