import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_names, get_train, edit_train_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=[
                      'Train_No', 'Train_Name', 'Train_type', 'Source', 'Destination', 'Availability'])
    with st.expander("Current Available Trains"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_train_names()]
    selected_train = st.selectbox("Train to Edit", list_of_trains)
    selected_result = get_train(selected_train)
    if selected_result:
        train_no = selected_result[0][0]
        train_name = selected_result[0][1]
        train_type = selected_result[0][2]
        source = selected_result[0][3]
        dest = selected_result[0][4]
        avail = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_train_no = st.text_input("Train Number:", train_no)
            new_train_name = st.text_input("Train Name:", train_name)
            new_train_type = st.selectbox(
                "Train Type:", ["Superfast", "Fast", "Mail"])
        with col2:
            new_source = st.text_input("Source:", source)
            new_dest = st.text_input("Destination:", dest)
            new_avail = st.selectbox("Availability:", ["Yes", "No"])
        if st.button("Update"):
            edit_train_data(new_train_no, new_train_name, new_train_type, new_source,
                            new_dest, new_avail, train_no, train_name, train_type, source, dest, avail)
            st.success("Successfully updated:: {} to ::{}".format(
                train_name, new_train_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=[
                       'Train Number', 'Train Name', 'Train Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
