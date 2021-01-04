
class Round():
    
    def __init__(self, game_suit):
        self.cards = []
        self.game_suit = game_suit
    
    
    def add_card(self, card):
        self.cards.append(card)
    
    
    # FIXME
    def get_winner_card(self):
        win_card = self.cards[0]
        
        for card in self.cards[1:]:
            if card.suit == self.game_suit.suit:
                # game suit card
                if card.suit == win_card.suit:
                    if card.value > win_card.value:
                        win_card = card
                    elif card.rank > win_card.rank:
                        win_card = card
                else:
                    win_card = card
            else:
                # regular card
                if card.suit == win_card.suit:
                    if card.value > win_card.value:
                        win_card = card
                    elif card.rank > win_card.rank:
                        win_card = card
        
        return win_card
    
    
    def __str__(self):
        return '\n'.join(
            '{0}: {1}'.format(c.owner.name, str(c)) for c in self.cards
        )
