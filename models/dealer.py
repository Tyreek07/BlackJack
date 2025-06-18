"""
Der Dealer muss bei einem Punktwert 
von 16 oder weniger weitere Karten ziehen. 
Bei einem Punktwert von 17 oder mehr darf er nicht mehr ziehen.
"""
# https://www.spielbanken-bayern.de/spielinfos/spielregeln/black-jack
from models.hand import Hand

class Dealer:
    def __init__(self, name):
        self.name = "Dealer " +name
        self.hand = Hand()

    # Funktion für Name des Dealers ausgeben
    def __str__(self):
        pass

    def greeting(self, spielerName, spielerGeld):
        print(spielerName + " hat "+ str(spielerGeld) + "€")
        print("Bitte platzieren Sie Ihren Wettbetrag!")

    def drawCard(self, card):
        self.hand.addCard(card)

    def resetHand(self):
        print(self.name, "gibt die Karten ab")
        self.hand = Hand()

    def anotherRound(self):
        print("Wollen Sie eine weitere Runde spielen?")

    def askAnotherCard(self):
        print("Möchten Sie eine weitere Karte ziehen?")

    def sayStopp(self):
        print(self.name, "zieht nicht mehr!\n\n\n")



        

