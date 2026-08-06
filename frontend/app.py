"""
This is the Streamlit UI layer, it provides a lightweight graphical interface for interacting with backend workflow.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

import requests
import streamlit as st

BACKEND_URL = st.sidebar.text_input(
    "Backend URL",
    "http://localhost:8000/extract",
)

st.set_page_config(
    page_title="Clinical Prior Authorization",
    layout="wide",
)

st.title("Autonomous Clinical Prior Authorization")

uploaded = st.file_uploader(
    "Upload document",
    type=["pdf", "txt", "docx", "png", "jpg"],
)

if uploaded:

    with st.spinner("Processing..."):

        response = requests.post(
            BACKEND_URL,
            files={
                "file": (
                    uploaded.name,
                    uploaded.getvalue(),
                    uploaded.type,
                )
            },
        )

    if response.ok:

        result = response.json()

        # Workflow status
        if result.get("human_review", False):

            st.warning("Human Review Required")

            review_reason = result.get(
                "review_reason",
                "No reason provided."
            )

            st.info(f"Reason: {review_reason}")

        else:

            st.success("Completed")

        st.subheader("Workflow")

        st.write(result.get("events", []))

        st.subheader("Extraction")

        st.json(result.get("extraction"))

        st.subheader("Decision")

        if result.get("decision"):

            st.json(result["decision"])

        else:

            st.info("No automated decision generated.")

    else:

        st.error(response.text)