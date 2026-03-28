from mtgtools.MtgDB import MtgDB

class MTGcards:
    def __init__(self, card_name):

        self.card_name = card_name
        self.mana_value = ""
        self.card_type = ""
        self.controller = ""

    def Import_cards(self):
        mtg_db = MtgDB('my_db.fs')
        scryfall_cards = mtg_db.root.scryfall_cards
        scryfall_sets = mtg_db.root.scryfall_sets

    def assign_controller(self, player):
        self.controller = player

