# https://www.spielbanken-bayern.de/spielinfos/spielregeln/black-jack
from models.hand import Hand

class Player:
    def __init__(self, name, geld = 100):
        self.name = "Spieler "+ name
        self.hand = Hand()
        self.geld = geld
        self.wette = 0

    # Funktion für Name des Spielers mit Geld ausgeben __str__
    def __str__(self):
        pass

    # Spieler zieht Karte
    def sayCard(self, card):
        print(self.name, ": Eine Karte bitte!")
        self.hand.addCard(card)

    # Spieler stoppt, wünscht keine weiteren Karten
    def sayStopp(self):
        print(self.name, ": Stopp, keine Karten mehr!")
        self.showHand()
        punkte = self.hand.getPoints
        print(self.name, " hat ", punkte, "Punkte")

    # Ergeben die ersten beiden Karten des Spielers einen Punktwert von neun, 
    # zehn oder elf, so kann er seinen Einsatz verdoppeln, erhält aber nur noch eine Karte.
    def sayDoubling(self):
        anzahlKarten = len(self.hand.cardsInHand)
        wertKarten = self.hand.getPoints()
        genugGeld = self.geld - self.wette
        if anzahlKarten == 2 and (wertKarten == 10 or wertKarten == 11 or wertKarten == 9) and genugGeld >= 0:
            self.geld -= self.wette
            self.sayCard()

    def placeBet(self, betrag):
        genugGeld = self.geld - self.wette

        if genugGeld < 0:
            self.wette = betrag
            self.geld -= self.wette
            print(self.name, ": Ich setze ", self.wette)

    def winBet(self):
        self.geld += (self.wette * 2) 
        self.wette = 0
        print(self.name, ": Yippie jetzt habe ich ", self.geld, "€")

    def drawBet(self):
        self.geld += (self.wette) 
        self.wette = 0
        print(self.name, ": Schade nix gewonne und nix verloren")

    def loseBet(self):
        self.wette = 0
        print(self.name, ": Ohje meine hart verdienten ", self.wette, "€")

    def resetHand(self):
        print(self.name, "gibt die Karten zurück")
        self.hand = Hand()

        

