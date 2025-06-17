#from models.deck import Deck

class Hand:
    def __init__(self):
        self.cardsInHand = []

    def __str__(self):
        karten_str = ", ".join(str(karte) for karte in self.cardsInHand)
        punkte = self.getPoints()
        return f"Hand: {karten_str}\nPunkte: {punkte}"
    
    def addCard(self, card):
        self.cardsInHand.append(card)

    def handleAss(self, summe, anzahl_asse):
        while summe > 21 and anzahl_asse > 0:
            summe -= 10  
            anzahl_asse -= 1
        return summe

    def getPoints(self):
        summe = 0
        anzahl_asse = 0

        for card in self.cardsInHand:
            if card.bezeichnung == 'Ass':
                summe += 11
                anzahl_asse += 1
            else:
                summe += card.wert

        summe = self.handleAss(summe, anzahl_asse)
        return summe

    def showHand(self):
        for card in self.cardsInHand:
            print(card.bezeichnung)

        

    


