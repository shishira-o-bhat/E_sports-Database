import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Game_ID','Game_Name','No_of_players_per_team','No_of_teams_competing','No_of_players_worldwide','Creator'])
    with st.expander("View Games"):
        st.dataframe(df)
    with st.expander("No_of_players_worldwide"):
        p1 = px.pie(df, names='Game_Name', values='No_of_players_worldwide')
        st.plotly_chart(p1)
