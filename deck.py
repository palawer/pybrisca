from card import Card
import random


class Deck():
    
    def __init__(self):
        self.cards = self.build_deck()
    
    
    def build_deck(self):
        cards = []
        for rank, value in zip(Card.RANKS, Card.VALUES):
            for suit in Card.SUITS:
                card = Card(rank, value, suit)
                cards.append(card)
        return cards
    
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    
    def get_first_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None
    
    
    def add_card(self, card):
        self.cards.append(card)
    
    
    def __str__(self):
        return '\n'.join(str(c) for c in self.cards)
