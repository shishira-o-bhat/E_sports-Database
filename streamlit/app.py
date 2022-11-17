# Core Pkgs
import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
import pandas as pd
import mysql.connector

# DB Mgmt
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e_sports_397"
)
c = mydb.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


competition = ['Competition_ID,', 'Competition_Name,', 'Location,', 'Date_of_competition,','Prize_pool,','Organiser_name,', 'Game_ID']
game = ['ID,', 'Name,', 'No of players,', 'No of teams ,', 'No of players worldwide,', 'Creator'] 
participates = ['Team_ID,','Competition_ID']
player = ['ID,','Name,','Position,','DOB,','Salary,','Team ID']
plays = ['Player ID,','Game ID']
revenue = ['Revenue ID,','Source Name,','Income,','Team ID']
team = ['ID,','Name,','No of Players,','Owner name,','Game ID']




def main():
    st.title("E-Sports Database 397")
    menu = ["Add", "View", "Update", "Delete","Custom Query"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Custom Query":
        st.subheader("HomePage")

		# Columns/Layout
        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

			# Table of Info

            with st.expander("Table Info"):
                table_info = {'Competition':competition,'Game':game,'Participates':participates,'Player':player,'Plays':plays,'Revenue':revenue,'Team':team}
                st.json(table_info)
			
		# Results Layouts
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

				# Results 
                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)

                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)

    elif choice == "Add":
        st.subheader("Insert Details:")
        create()

    elif choice == "View":
        st.subheader("View Created Details")
        read()

    elif choice == "Update":
        st.subheader("Update Details")
        update()

    elif choice == "Delete":
        st.subheader("Delete Details")
        delete()

if __name__ == '__main__':
	main()
