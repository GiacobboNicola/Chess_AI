from Class_board import ChessBoard
from stockfish_utils import pgn2fen
from stockfish import Stockfish
import random as rd


chessboard = ChessBoard()
chessboard.initialize()
stockfish_engine = Stockfish(path="/home/lucas/Documents/Lucas/Python_projects/stockfish_15_linux_x64/stockfish_15_x64")
end = False

while not end:

    if chessboard.white_moves() == []:
        end = True
        continue

    white_move = rd.choice(chessboard.white_moves())
    chessboard.update_pgn(chessboard.move_to_pgn(white_move))
    chessboard.play_move(white_move)

    if chessboard.black_moves() == []:
        end = True

    fen = pgn2fen(chessboard.pgn_string)
    stockfish_engine.set_fen_position(fen)

    black_move = stockfish_engine.get_best_move()
    black_move = chessboard.readuci(black_move)
    chessboard.update_pgn(chessboard.move_to_pgn(black_move))
    chessboard.play_move(black_move)

print(chessboard.pgn_string)