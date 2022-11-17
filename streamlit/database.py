import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e_sports"
)
c = mydb.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Game_397(Game_ID TEXT, Game_Name TEXT, No_of_players_per_team INT, No_of_teams_competing INT, No_of_players_worldwide INT, Creator TEXT)')

def add_data(train_no, train_name, train_type, source, dest, avail):
    c.execute('INSERT INTO Game_397(Train_No, Train_Name, Train_Type, source, Destination,Availability) VALUES (%s,%s,%s,'
              '%s,%s,%s)',
              (train_no, train_name, train_type, source, dest, avail))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM Game_397')
    data = c.fetchall()
    return data


def view_only_train_names():
    c.execute('SELECT Train_Name FROM train_397')
    data = c.fetchall()
    return data


def get_train(train_name):
    c.execute('SELECT * FROM train_397 WHERE Train_Name="{}"'.format(train_name))
    data = c.fetchall()
    return data


def edit_train_data(new_train_no, new_train_name, new_train_type, new_source, new_dest, new_avail, train_no, train_name, train_type, source, dest, avail):
    c.execute("UPDATE train_397 SET Train_No=%s, Train_Name=%s, Train_Type=%s, source=%s, Destination=%s, Availability=%s WHERE "
              "Train_No=%s and Train_Name=%s and Train_Type=%s and source=%s and Destination=%s and Availability=%s", (new_train_no, new_train_name, new_train_type, new_source, new_dest, new_avail, train_no, train_name, train_type, source, dest, avail))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(train_name):
    c.execute('DELETE FROM train_397 WHERE Train_Name="{}"'.format(train_name))
    mydb.commit()
