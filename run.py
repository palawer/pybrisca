#!/usr/bin/env python3
from game import Game
from player import Player


p1 = Player('P1', is_bot=False)
p2 = Player('CPU1')
p3 = Player('CPU2')
p4 = Player('CPU3')

game = Game()
game.add_player(p1)
game.add_player(p2)
game.add_player(p3)
game.add_player(p4)
game.start_game()
