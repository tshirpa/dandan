# This is a sample Python script.
from mtgtools.MtgDB import MtgDB


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    mtg_db = MtgDB('my_db.fs')
    print_hi('PyCharm')
    scryfall_cards = mtg_db.root.scryfall_cards
    scryfall_sets = mtg_db.root.scryfall_sets


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
