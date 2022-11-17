import pandas as pd
import streamlit as st
from database import view_all_data, view_only_game_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Game_ID','Game_Name','No_of_players_per_team','No_of_teams_competing','No_of_players_worldwide','Creator'])
    with st.expander("Available Data"):
        st.dataframe(df)

    list_of_games = [i[0] for i in view_only_game_names()]
    selected_game = st.selectbox("Task to Delete", list_of_games)
    st.warning("Do you want to delete ::{}".format(selected_game))
    if st.button("Delete Game"):
        delete_data(selected_game)
        st.success("Game has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Game_ID','Game_Name','No_of_players_per_team','No_of_teams_competing','No_of_players_worldwide','Creator'])
    with st.expander("Updated data"):
        st.dataframe(df2)
