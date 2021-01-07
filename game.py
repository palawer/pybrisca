from round import Round
from deck import Deck


class Game():
    def __init__(self):
        self.players   = []
        self.game_suit = None
        self.deck      = None
        self.round     = None
    
    
    def add_player(self, player):
        self.players.append(player)
    
    
    def sort_players(self, first_player):
        idx = self.players.index(first_player)
        players = []
        for player in self.players[idx:]:
            players.append(player)
        for player in self.players[:idx]:
            players.append(player)
        self.players = players
    
    
    def first_deal(self):
        for idx in range(3):
            for player in self.players:
                has_card = player.cards[idx]
                if not has_card:
                    card = self.deck.get_first_card()
                    player.add_card(card, idx)
    
    
    def deal_hand(self):
        for player in self.players:
            card = self.deck.get_first_card()
            if card:
                idx = player.find_spot()
                player.add_card(card, idx)
    
    
    def count_players_cards(self):
        count = 0;
        for player in self.players:
            for card in player.cards:
                if card:
                    count += 1
        return count
    
    
    def game_setup(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.game_suit = self.deck.get_first_card()
        self.deck.add_card(self.game_suit)
        self.first_deal()
    
    
    def end_game(self):
        res = []
        for player in self.players:
            res.append((player, player.get_score()))
        
        res.sort(key=lambda x: x[1], reverse=True)
        
        print('-'*80)
        print('FINISH')
        print('-'*80)
        for player, score in res:
            print(player.name, score)
    
    
    def start_game(self):
        self.game_setup();
        
        round_counter = 1
        while self.count_players_cards():
            #### new round
            self.round = Round(self.game_suit)
            
            print('\n')
            print('#'*80)
            print('-'*80)
            print('ROUND:', round_counter)
            print('Suit:', self.game_suit)
            
            print('-'*80)
            for player in self.players:
                print(player)
            
            #### play cards
            print('-'*80)
            print('Round cards:')
            
            for player in self.players:
                card = player.get_random_card()
                self.round.add_card(card)
                print(player.name, card)
            
            
            
            #### check winner
            winner_card = self.round.get_winner_card()
            winner_player = winner_card.get_card_owner()
            winner_player.save_winned_cards(self.round.cards)
            
            print('-'*80)
            print('Winner:')
            print(winner_player.name, winner_card)
            
            print('-'*80)
            for player in self.players:
                print(player.name, player.get_score(), len(player.winned_cards))
            
            #### sort and deal
            self.sort_players(winner_player)
            self.deal_hand()
            
            round_counter += 1
        
        self.end_game()
