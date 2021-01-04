#!/usr/bin/env python3
from game import Game
from player import Player


p1 = Player('P1')
p2 = Player('P2')
p3 = Player('P3')
p4 = Player('P4')

game = Game()
game.add_player(p1)
game.add_player(p2)
game.add_player(p3)
game.add_player(p4)
game.start_game()
