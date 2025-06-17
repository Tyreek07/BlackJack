from models.deck import Deck
from models.player import Spieler
from models.dealer import Dealer

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        pass

    def startGame(self):
        print("Test")
        self.deck.shuffleDeck()

    def play(self):
        print("Lets play BlackJack")
        self.startGame()
        print(self.deck.drawCard())

    # Wenn Spieler kein Geld hat rauswerfen
    # Wenn Spieler keine Lust mehr hat beenden
    # Spieler möchte sein Geld kontrollieren
    # Spieler möchte eine Runde starten
    # Spieler möchte eine Runde beenden
    # Spieler möchte eine weitere Karte
    # Spieler möchte doublen
    # Kontorlliere wer gewonnen hat


        

