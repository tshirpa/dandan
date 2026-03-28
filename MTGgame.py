import random
from Game_actions import Zones
from MTGcards import MTGcards

class MTGgame:
    def __init__(self):
        self.player_1 = "player_1"  # make a player object that can do game actions
        self.player_2 = "player_2"
        self.library = []
        self.board = []
        self.stack = []
        self.hand_of_player_1 = []
        self.hand_of_player_2 = []
        self.graveyard = []
        self.zones = [self.library,self.board, self.stack, self.hand_of_player_2, self.hand_of_player_1,self.graveyard]

    def Start_Game(self):
        print("initializing game")
        list_of_players = [self.player_1, self.player_2]
        starting_player = random.choice(list_of_players)
        print(starting_player, "will be the starting player")
        #initialize deck
        #do mulligans
    def Initialize_deck(self):
        pass
    def Muligans(self):
        pass




