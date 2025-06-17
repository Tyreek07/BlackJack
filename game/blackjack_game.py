from models.player import Player
from models.dealer import Dealer
from models.deck import Deck

class BlackjackGame:
    def __init__(self):
        self.dealer = Dealer("Jeff")
        self.player = Player("Tyreek", geld=100)
        self.deck = Deck()
        self.bet = 0

    def initializeGame(self):
        # Dealer grüßt und fragt nach Wette
        self.dealer.greeting(self.player.name, self.player.geld)

        # Spieler kann Wette platzieren
        self.bet = int(input())
        self.player.placeBet(self.bet)

        # Karten werden gemischt
        print("Okay es geht Los!")
        self.deck.shuffleDeck()
        
        # Dealer teilt Spieler zwei Karten aus
        self.player.hand.addCard(self.deck.drawCard(self.player.name))
        self.player.hand.addCard(self.deck.drawCard(self.player.name))

        # Dealer öffnet seine erste Karte
        self.dealer.hand.addCard(self.deck.drawCard(self.dealer.name))

        # Karten auf dem Tisch
        print("\n\n\n********************************\n\nAuf den Tisch liegen folgende Karten:\n", 
              self.player.name, ":", self.player.hand, "\n",
              self.dealer.name, ":", self.dealer.hand, "\n")

    def playerTurn(self):
        while True:
            if self.player.hand.getPoints() > 20:
                break
        
            self.dealer.askAnotherCard()
            choice = input("Type (y) or (n): ").lower()

            if choice == "y":
                self.player.hand.addCard(self.deck.drawCard(self.player.name))
                print(self.player.name, "hat nun folgende Karten:\n", self.player.hand)
            else:
                break  

        
    def dealerTurn(self):
        kartenWert =  self.dealer.hand.getPoints()
        while kartenWert < 17:
            self.dealer.hand.addCard(self.deck.drawCard(self.dealer.name))
            kartenWert = self.dealer.hand.getPoints()
            print(self.dealer.name, "hat nun folgende Karten:\n", self.dealer.hand)
        self.dealer.sayStopp()

    def determineWinner(self):
        dealerPoints = self.dealer.hand.getPoints()
        playerPoints = self.player.hand.getPoints()
        print(f"{self.player.name} finales Hand (Punkte): {self.player.hand} ({self.player.hand.getPoints()})")
        print(f"{self.dealer.name} finales Hand (Punkte): {self.dealer.hand} ({self.dealer.hand.getPoints()})")
        if playerPoints > 21 or (playerPoints < dealerPoints and dealerPoints <= 21):
            print("\nErgebnis: Dealer won the game")
        elif dealerPoints == playerPoints:
            print("\nErgebnis: Keiner hat gewonnen")
        else:
            print("\nErgebnis: Player won the game")

    def restartGame(self):
        pass

    def play(self):
        print("Lets play BlackJack")
        self.initializeGame()
        self.playerTurn()
        self.dealerTurn()
        self.determineWinner()

    # Wenn Spieler kein Geld hat rauswerfen
    # Wenn Spieler keine Lust mehr hat beenden
    # Spieler möchte sein Geld kontrollieren
    # Spieler möchte eine Runde starten
    # Spieler möchte eine Runde beenden
    # Spieler möchte eine weitere Karte
    # Spieler möchte doublen
    # Kontorlliere wer gewonnen hat


        

