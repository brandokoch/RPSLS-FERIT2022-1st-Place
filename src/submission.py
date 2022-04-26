from player.make_move import *
from game_generator import *
from official_robot.make_move import *
import numpy as np

# Will print results at the end
print('Started...')
wins_a, draws, wins_b, A,B, results=evaluate_generators(get_player_move, get_robot_move, 2000)

print("----------SUMMARY----------")
print(f"Player wins: {wins_a}")
print(f"Draws: {draws}")
print(f"Robot wins: {wins_b}")

# Write games to file
result_matrix = np.column_stack([A, B, results])
datafile_path = "all_moves.txt"
np.savetxt(datafile_path , result_matrix, fmt=['%d','%d', '%d'])