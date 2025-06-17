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
    # 

    # Spieler zieht Karte
    def sayCard(self):
        pass


    # Spieler stoppt, wünscht keine weiteren Karten
    def sayStopp(self):
        pass

    # Ergeben die ersten beiden Karten des Spielers einen Punktwert von neun, 
    # zehn oder elf, so kann er seinen Einsatz verdoppeln, erhält aber nur noch eine Karte.
    def sayDoubling(self):
        pass

    def placeBet(self):
        pass

    def winBet(self):
        pass

    def drawBet(self):
        pass

    def loseBet(self):
        pass

    def resetHand(self):
        pass

    def showHand():
        pass

