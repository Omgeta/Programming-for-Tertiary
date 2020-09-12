from chess import Board

game = Board(debug=True)
game.start()
while game.winner is None:
    game.display()
    start, end = game.prompt()
    game.update(start, end)
    game.next_turn()
print(f'Game over. {game.winner} player wins!')

