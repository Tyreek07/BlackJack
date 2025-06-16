from models.card import Card
import random

class deck:
    def __init__(self):
        farben = {'Karo', 'Herz', 'Pik', 'Kreuz'}
        werte = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9':9, '10': 10, 'Bube': 10, 'Dame': 10, 'König':10, 'Ass':(1, 11)
        }
        self.cards = []

        for farbe in farben:
            for bez, wert in werte.items():
                karte = Card(farbe, bez, wert)
                self.cards.append(karte)
        
    def shuffleDeck(self):
        random.shuffle(self.cards)
        print("Karten wurden gemischt!")

    def drawCard(self):
        print(self.cards[-1], " wurde gezogen!")
        return self.cards.pop()
