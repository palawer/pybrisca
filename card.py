
class Card():
    SUITS   = [0, 1, 2, 3]
    SYMBOLS = ['🌞', '🏆', '🗡', '🪵']
    
    RANKS   = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    VALUES  = [11, 0, 10, 0, 0, 0, 0, 2, 3, 4]
    
    
    def __init__(self, rank, value, suit):
        self.rank  = rank
        self.value = value
        self.suit  = suit
        self.owner = None
    
    
    def get_card_owner(self):
        return self.owner
    
    
    def __str__(self):
        return '{0} {1} ({2})'.format(
            self.rank, self.SYMBOLS[self.suit], self.value
        )
