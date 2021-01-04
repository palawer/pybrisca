
class Round():
    
    def __init__(self, game_suit):
        self.cards = []
        self.game_suit = game_suit
    
    
    def add_card(self, card):
        self.cards.append(card)
    
    
    def get_winner_card(self):
        """
        2a => 7b => 1a
        2a => 7a => 7a
        """
        win_card = self.cards[0]
        
        for card in self.cards[1:]:
            if card.suit == self.game_suit.suit:
                if card.rank > self.game_suit.rank and card.value > self.game_suit.value:
                    win_card = card
            elif card.suit == win_card.suit:
                if card.rank > win_card.rank:
                    win_card = card
        
        return win_card
    
    
    def __str__(self):
        return '\n'.join('{0}: {1}'.format(c.owner.name, str(c)) for c in self.cards)
