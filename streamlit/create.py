import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        train_no = st.text_input("Train Number:")
        src = st.text_input("Source:")
        train_type = st.selectbox("Train type", ["Superfast", "Fast", "Mail"])
    with col2:
        train_name = st.text_input("Train Name:")

        dest = st.text_input("Destination:")
        avail = st.selectbox("Availability", ["Yes", "No"])
    if st.button("Add Train"):
        add_data(train_no, train_name, train_type, src, dest, avail)
        st.success("Successfully added train: {}".format(train_name))
