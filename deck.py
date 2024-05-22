# specs: car class. each card has a suit and a value (strings)
# repr should return the value of suits

# specs for deck: each deck has a cards attribute with all 52
#possible instances
# instance method called count which returns how many cards remain
# repr should display information on how many cards are in the deck
# has an instance method called _deal which accepts a number which it 
#should deal
# another instance method called shuffle
# should have a deal card method
# should have a deal_hand method that accepts a number

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}s"
    

class Deck:
    def __init__(self):
        suits = ["heart", "diamond", "club", "spade"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'jack', 'queen', 'king']
        self.cards = []
        for suit in suits:
                for value in values:
                     self.cards.append(Card(suit, value))
    
    def count(self):
         return len(self.cards)
    
    def _deal(self, num):
         count = self.count()
         target_deal = min([num, count])
         if count == 0:
              raise ValueError("All Cards have been dealt")
         cards = self.cards[-target_deal:]
         self.cards = self.cards[:-target_deal]
         return cards   

    def shuffle(self):
         if self.count() < 52:
              raise ValueError("Cannot a deck that is not full")
         return random.shuffle(self.cards)

    def deal_card(self):
         return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
         return self._deal(hand_size)


d1 = Deck()
d1.deal_hand(5)

print(d1.count())
