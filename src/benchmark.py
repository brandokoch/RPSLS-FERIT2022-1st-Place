from player.make_move import *
from game_generator import *
from custom_robot.make_move import robots
import numpy as np
import time

robot_names=robots.keys()
with open('results_benchmark.txt','w') as f:
    for robot_name in robot_names:

        start_time = time.time()
        wins_a, draws, wins_b, A,B, results=evaluate_generators(get_player_move, robots[robot_name], 2000)
        current_time = time.time()
        elapsed_time = current_time - start_time

        f.write("----------SUMMARY----------")
        f.write('\n')
        f.write(f"Robot name: {robot_name}")
        f.write('\n')
        f.write(f"Player wins: {wins_a}")
        f.write('\n')
        f.write(f"Draws: {draws}")
        f.write('\n')
        f.write(f"Robot wins: {wins_b}")
        f.write('\n')
        f.write(f"Took: {str(int(elapsed_time))} seconds")
        f.write('\n')

        # Write games to file
        result_matrix = np.column_stack([A, B, results])
        datafile_path = "benchmark_summary.txt"
        np.savetxt(datafile_path , result_matrix, fmt=['%d','%d', '%d'])