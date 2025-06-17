from models.hand import Hand

class Player:
    def __init__(self, name, geld = 100):
        self.name = name
        self.hand = Hand()
        self.geld = geld
        self.wette = 0
        pass

    # Funktion für Wette platzieren
    # Funktion für Geld hinzufügen bzw abrechnen
    # Funktion für Name des Spielers mit Geld ausgeben __str__
    # 