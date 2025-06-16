from models.deck import Deck

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

        

