import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_game_names, get_game, edit_game_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Game_ID','Game_Name','No_of_players_per_team','No_of_teams_competing','No_of_players_worldwide','Creator'])
    with st.expander("Games"):
        st.dataframe(df)
    list_of_games = [i[0] for i in view_only_game_names()]
    selected_game = st.selectbox("Game to Edit", list_of_games)
    selected_result = get_game(selected_game)
    if selected_result:
        Game_ID = selected_result[0][0]
        Game_Name = selected_result[0][1]
        No_of_players_per_team = selected_result[0][2]
        No_of_teams_competing = selected_result[0][3]
        No_of_players_worldwide = selected_result[0][4]
        Creator = selected_result[0][5]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_Game_ID = st.text_input("New Game ID:")
            new_No_of_players_per_team = st.number_input("New number of Players per team:")
            new_No_of_players_worldwide = st.number_input("New number of Players worldwide:")
        with col2:
            new_Game_Name = st.text_input("New Game Name:")
            new_No_of_teams_competing = st.number_input("New number of teams competing:")
            new_Creator = st.text_input("New creator:")
        if st.button("Update"):
            edit_game_data(new_Game_ID,new_Game_Name,new_No_of_players_per_team,new_No_of_teams_competing,new_No_of_players_worldwide,new_Creator,Game_ID,Game_Name,No_of_players_per_team,No_of_teams_competing,No_of_players_worldwide,Creator)
            st.success("Successfully updated:: {} to ::{}".format(
                Game_Name, new_Game_Name))

        '''Game_Name = st.text_input("Game Name:")
        No_of_teams_competing = st.number_input("Number of teams competing:")
        Creator = st.text_input("Creator:")'''

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Game_ID','Game_Name','No_of_players_per_team','No_of_teams_competing','No_of_players_worldwide','Creator'])
    with st.expander("Updated data"):
        st.dataframe(df2)
