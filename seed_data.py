import streamlit as st
from db_connection import add_church, add_artifact, get_all_churches, get_all_artifacts
import pandas as pd
import random

st.title("Database Seeder")

st.write("Starting seed process...")

# Dummy Churches
dummy_churches = [
    {
        "church_name": "St. Mary's Cathedral",
        "state": "California",
        "city": "San Francisco",
        "priest_name": "Father John Doe",
        "phone_number": "415-555-0101",
        "email_id": "contact@stmaryssf.org",
        "address": "1111 Gough St, San Francisco, CA 94109",
        "previous_priests": []
    },
    {
        "church_name": "Holy Family Church",
        "state": "New York",
        "city": "New York",
        "priest_name": "Father Michael Smith",
        "phone_number": "212-555-0102",
        "email_id": "info@holyfamilyny.org",
        "address": "315 E 47th St, New York, NY 10017",
        "previous_priests": []
    },
    {
        "church_name": "Sacred Heart Parish",
        "state": "Texas",
        "city": "Austin",
        "priest_name": "Father David Wilson",
        "phone_number": "512-555-0103",
        "email_id": "office@sacredheartatx.org",
        "address": "5909 Reicher Dr, Austin, TX 78723",
        "previous_priests": []
    },
    {
        "church_name": "St. Patrick's Church",
        "state": "Illinois",
        "city": "Chicago",
        "priest_name": "Father Robert Brown",
        "phone_number": "312-555-0104",
        "email_id": "contact@stpatrickschicago.org",
        "address": "700 W Adams St, Chicago, IL 60661",
        "previous_priests": []
    },
    {
        "church_name": "Immaculate Conception",
        "state": "Washington",
        "city": "Seattle",
        "priest_name": "Father James Miller",
        "phone_number": "206-555-0105",
        "email_id": "info@icseattle.org",
        "address": "820 18th Ave, Seattle, WA 98122",
        "previous_priests": []
    },
    {
        "church_name": "St. Mary's Church",
        "state": "Maharashtra",
        "city": "Pune",
        "priest_name": "Fr. Anthony D’Souza",
        "phone_number": "278951305",
        "email_id": "info@icasdseaasdttle.org",
        "address": "8158122",
        "previous_priests": []
    }
]

# Dummy Artifacts
dummy_artifacts = [
    {
        "artifact_name": "Wooden Rosary",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Pearl Rosary",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Hematite Rosary",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Rosary Bracelet",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Rosary Ring",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "St. Benedict Medal",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Miraculous Medal",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Sacred Heart Medal",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Guardian Angel Medal",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "St. Christopher Medal",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Brown Scapular",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Green Scapular",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Blue Scapular",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Black Scapular",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Red Scapular",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Catechism of the Catholic Church",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Lives of the Saints",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Prayer Book for the Holy Rosary",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Devotional Psalter",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Illustrated Gospel Book",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Holy Water Bottle",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Incense Pack",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Small Crucifix",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Holy Card Set",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    },
    {
        "artifact_name": "Consecration Prayer Booklet",
        "quantity": 10,
        "sent_date": "2025-01-12",
        "church_name": "St. Mary's Church",
        "priest_name": "Fr. Anthony D’Souza",
        "church_state": "Maharashtra",
        "church_city": "Pune"
    }
]

# Add Churches
existing_churches = get_all_churches()
existing_names = [c['church_name'] for c in existing_churches]

added_churches_count = 0
for church in dummy_churches:
    if church['church_name'] not in existing_names:
        if add_church(church):
            st.success(f"Added {church['church_name']}")
            added_churches_count += 1
        else:
            st.error(f"Failed to add {church['church_name']}")
    else:
        st.info(f"{church['church_name']} already exists.")
        
st.write(f"Total churches added: {added_churches_count}")

# Add Artifacts
# We need to link artifacts to churches. We'll randomly assign them to the churches we just ensured exist.
# Refresh church list to get all current churches
all_churches = get_all_churches()
if not all_churches:
    st.error("No churches available to assign artifacts to.")
else:
    church_names = [c['church_name'] for c in all_churches]
    
    # Check existing artifacts to avoid duplicates if possible, though artifacts might not have unique names
    # We'll just add them for now.
    
    added_artifacts_count = 0
    for artifact in dummy_artifacts:
        # Pick a random church
        target_church = random.choice(church_names)
        
        artifact_data = artifact.copy()
        artifact_data['church_name'] = target_church
        artifact_data['date_sent'] = pd.Timestamp.now().date().isoformat()
        artifact_data['notes'] = "Seeded data"
        
        if add_artifact(artifact_data):
            st.success(f"Added {artifact['artifact_name']} to {target_church}")
            added_artifacts_count += 1
        else:
            st.error(f"Failed to add {artifact['artifact_name']}")

    st.write(f"Total artifacts added: {added_artifacts_count}")

st.success("Seeding complete!")
