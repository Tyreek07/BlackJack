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

    def greeting(self):
        print("Hallo, meine Name ist", self.name, "möchten Sie ihre Wette platzieren?")

    def anotherRound(self):
        print("Wollen Sie eine weitere Runde spielen?")
        self.resetHand()

    def ziehtErsteKarte(self):
        self.hand.addCard()
        print(self.name + ": ")
        self.hand.showHand()

    # Dealer zieht Karte
    def playGame(self):
        kartenWert =  self.hand.getPoints()
        while kartenWert >= 16:
            print(self.name, "zieht eine Karte")
            self.hand.addCard()
            kartenWert =  self.hand.getPoints()
        self.sayStopp()

    def sayStopp(self):
        print(self.name, "zieht nicht mehr!")
        self.showHand()
        punkte = self.hand.getPoints
        print(self.name, " hat ", punkte, "Punkte")

    def resetHand(self):
        self.hand = Hand()

        

