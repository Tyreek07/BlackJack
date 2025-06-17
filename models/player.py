# https://www.spielbanken-bayern.de/spielinfos/spielregeln/black-jack
from models.hand import Hand

class Player:
    def __init__(self, name, geld = 100):
        self.name = name
        self.hand = Hand()
        self.geld = geld
        self.wette = 0

    # Funktion für Wette platzieren
    # Funktion für Geld hinzufügen bzw abrechnen
    # Funktion für Name des Spielers mit Geld ausgeben __str__

    # Spieler zieht Karte
    def sayCard(self):
        print(self.name, ": Eine Karte bitte")
        self.hand.addCard()

    # Spieler stoppt, wünscht keine weiteren Karten
    def sayStopp(self):
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
            # Spieler zieht noch eine Karte
            # Spieler doppelt einsatz
            # Spiel beenden
            pass
        pass

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
        print(self.name, ": Nur wer spielt kann gewinnen!")
        self.hand = Hand()
        pass

        

