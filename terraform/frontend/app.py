import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🎯 Goal Tracker")

goal = st.text_input("Enter your goal")

if st.button("Save"):
    if not goal.strip():
        st.warning("Please enter a goal")
    else:
        with st.spinner("Saving goal..."):
            try:
                r = requests.post(
                    f"{BACKEND_URL}/goal",
                    json={"goal": goal},
                    timeout=5
                )

                if r.status_code == 200:
                    st.success("Goal saved successfully ✅")
                else:
                    st.error(f"Error: {r.text}")

            except requests.exceptions.RequestException:
                st.error("Backend not reachable ❌")
