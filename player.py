import random


class Player():
    
    def __init__(self, name, is_bot=True):
        self.name         = name
        self.is_bot       = is_bot
        self.cards        = [None, None, None]
        self.winned_cards = []
    
    
    def add_card(self, card, index):
        self.cards[index] = card
        card.owner = self
    
    
    def save_winned_cards(self, cards):
        for card in cards:
            self.winned_cards.append(card)
    
    
    def get_card(self, index):
        card = self.cards[index]
        self.cards[index] = None
        return card
    
    
    def get_random_card(self):
        indices = []
        for idx, card in enumerate(self.cards):
            if card:
                indices.append(idx)
        r = random.choice(indices)
        card = self.cards[r]
        self.cards[r] = None
        return card
    
    
    def find_spot(self):
        for idx in range(3):
            if not self.cards[idx]:
                return idx
    
    
    def get_score(self):
        score = 0
        for card in self.winned_cards:
            score += card.value
        return score
    
    
    def __str__(self):
        return '{0}: {1}'.format(
            self.name, ' | '.join(str(c) for c in self.cards)
        )
