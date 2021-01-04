#!/usr/bin/env python3
from game import Game
from player import Player


p1 = Player('P1')
p2 = Player('P2')
p3 = Player('P3')
p4 = Player('P4')

game = Game()
game.add_players(p1, p2, p3, p4)
game.game_setup()
game.start_game()
game.end_game()
