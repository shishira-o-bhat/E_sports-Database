--1)player table:

CREATE TABLE Player_397(Player_ID varchar(255) NOT NULL, Player_Name varchar(255), Position varchar(255), DOB DATE,Salary int,Team_ID varchar(255), PRIMARY KEY(Player_ID),FOREIGN KEY(Team_ID) REFERENCES Team_397(Team_ID));

--2)game player table:
CREATE TABLE Plays_397(Player_ID varchar(255),Game_ID varchar(255),FOREIGN KEY(Player_ID) REFERENCES Player_397(Player_ID),FOREIGN KEY(Game_ID) REFERENCES Game_397(Game_ID),CONSTRAINT game_player_unique UNIQUE (Player_ID, Game_ID));

--3)game table:

CREATE TABLE Game_397(Game_ID varchar(255) NOT NULL,Game_Name varchar(255), No_of_players_per_team int,No_of_teams_competing int,No_of_players_worldwide int,Creator varchar(255),PRIMARY KEY(Game_ID));

--4)revenue table:

CREATE TABLE Revenue_397(Revenue_ID varchar(255) NOT NULL,Source_name varchar(255), Income int,Team_ID varchar(255),PRIMARY KEY(Revenue_ID),FOREIGN KEY(Team_ID) REFERENCES Team_397(Team_ID));

--5)team table:

CREATE TABLE Team_397(Team_ID varchar(255) NOT NULL,Team_name varchar(255), No_of_players int,Owner_name varchar(255),Game_ID varchar(255),PRIMARY KEY(Team_ID),FOREIGN KEY(Game_ID) REFERENCES Game_397(Game_ID));

--6)competition table:

CREATE TABLE Competition_397(Competition_ID varchar(255),Competition_Name varchar(255), Location varchar(255),Prize_pool int,Organiser_name varchar(255),Game_ID varchar(255),PRIMARY KEY(Competition_ID),FOREIGN KEY(Game_ID) REFERENCES Game_397(Game_ID));

--7) team_competition table:
CREATE TABLE Participates_397(Team_ID varchar(255),Competition_ID varchar(255),FOREIGN KEY(Team_ID) REFERENCES Team_397(Team_ID),FOREIGN KEY(Competition_ID) REFERENCES competition_397(Competition_ID),CONSTRAINT team_competition_unique UNIQUE (Team_ID, Competition_ID));
