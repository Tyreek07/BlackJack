class Card:
    def __init__(self, farbe, bezeichnung, wert):
        self.farbe = farbe
        self.bezeichnung = bezeichnung
        self.wert = wert
    
    def __str__(self):
        karte = "Kart: " + self.farbe + self.bezeichnung
        return karte