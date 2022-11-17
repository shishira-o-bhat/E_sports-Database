import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        Game_ID = st.text_input("Game ID:")
        No_of_players_per_team = st.number_input("Number of Players per team:")
        No_of_players_worldwide = st.number_input("Number of Players worldwide:")
    with col2:
        Game_Name = st.text_input("Game_Name:")
        No_of_teams_competing = st.number_input("Number of teams competing:")
        Creator = st.text_input("Creator:")
    if st.button("Add Game"):
        add_data(Game_ID,Game_Name,No_of_players_per_team,No_of_teams_competing,No_of_players_worldwide,Creator)
        st.success("Successfully added game: {}".format(Game_Name))
