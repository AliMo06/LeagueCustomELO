from PyQt5.QtWidgets import QApplication, QWidget
import sys

#Class to store player information and handle players.

roleMap = {0 : 'Fill', 1 : 'Top', 2 : 'Jungle', 3 : 'Mid', 4 : 'ADC', 5 : 'Support'}

class Player():
    def __init__(self, name : str, mainRole : int, secondRole : int, ELO : int):
        self.name = name
        self.mainRole = mainRole
        self.secondRole = secondRole
        self.ELO = ELO

#Function to add a new player into the system
def AddNewPlayer(name : str, mainRole : int, secondRole : int, ELO : int):
    #Initialize Player
    player = Player(name, mainRole, secondRole, ELO)
    #check DB for player with same name
    AddPlayerToDB(player)

#Inserts player into DB
def AddPlayerToDB(player : Player):
    with open("db.txt", "a") as db:
        db.write(f"{player.name} {player.mainRole} {player.secondRole} {player.ELO}\n")

def GetAllPlayers():
    with open("db.txt", "r") as db:
        for line in db:
            name, mainRole, secondRole, ELO = line.split()
            print(f"Name: {name}\nMain Role: {roleMap[int(mainRole)]}\nSecondary Role: {roleMap[int(secondRole)]}\nELO: {ELO}")



if __name__ == "__main__":
    GetAllPlayers()