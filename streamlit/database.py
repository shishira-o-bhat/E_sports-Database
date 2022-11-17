import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e_sports_397"
)
c = mydb.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Game_397(Game_ID TEXT, Game_Name TEXT, No_of_players_per_team NUMBER, No_of_teams_competing NUMBER, No_of_players_worldwide NUMBER, Creator TEXT)')

def add_data(game_id, game_name,no_of_players,no_of_teams, no_of_players_ww, creator):
    c.execute('INSERT INTO Game_397(Game_ID, Game_Name,No_of_players_per_team,No_of_teams_competing,No_of_players_worldwide,Creator) VALUES (%s,%s,%s,'
              '%s,%s,%s)',
              (game_id, game_name,no_of_players,no_of_teams, no_of_players_ww, creator))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM Game_397')
    data = c.fetchall()
    return data

def view_only_game_names():
    c.execute('SELECT Game_Name FROM Game_397')
    data = c.fetchall()
    return data


def get_game(Game_name):
    c.execute('SELECT * FROM Game_397 WHERE Game_Name="{}"'.format(Game_name))
    data = c.fetchall()
    return data


def edit_game_data(new_Game_ID,new_Game_Name,new_No_of_players_per_team,new_No_of_teams_competing,new_No_of_players_worldwide,new_Creator,Game_ID,Game_Name,No_of_players_per_team,No_of_teams_competing,No_of_players_worldwide,Creator):
    c.execute("UPDATE Game_397 SET Game_ID=%s, Game_Name=%s, No_of_players_per_team=%s, No_of_teams_competing=%s, No_of_players_worldwide=%s, Creator=%s WHERE "
              "Game_ID=%s, Game_Name=%s, No_of_players_per_team=%s, No_of_teams_competing=%s, No_of_players_worldwide=%s, Creator=%s", (new_Game_ID,new_Game_Name,new_No_of_players_per_team,new_No_of_teams_competing,new_No_of_players_worldwide,new_Creator,Game_ID,Game_Name,No_of_players_per_team,No_of_teams_competing,No_of_players_worldwide,Creator))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(Game_ID):
    c.execute('DELETE FROM Game_397 WHERE Game_ID="{}"'.format(Game_ID))
    mydb.commit()
