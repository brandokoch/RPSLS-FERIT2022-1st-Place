import player.config as config

def evaluate_generators(get_player_move, get_robot_move, move_cnt):
    wins_a = 0
    draws=0
    wins_b=0
    
    A = [] # player
    B = [] # robot
    results=[]
    
    model=None
    for i in range(move_cnt):

        # Player using player and robot move history as permitted
        if config.LOGGING_LEVEL>=2:
            print(f"Move: {i}, Calculating...")

        if i==0:
            temp_a,model=get_player_move([-1],B,i,model)
            temp_b=get_robot_move([-1], B, i)
        else:
            temp_a,model=get_player_move(A,B,i,model)
            temp_b=get_robot_move(A,B,i)

        A.append(temp_a)
        B.append(temp_b)

        # Move comparison and grading
        if (A[i]==1 and B[i]==3 or A[i]==1 and B[i]==4 or 
            A[i]==2 and B[i]==1 or A[i]==2 and B[i]==4 or 
            A[i]==3 and B[i]==2 or A[i]==3 and B[i]==4 or 
            A[i]==4 and B[i]==5 or A[i]==5 and B[i]==1 or 
            A[i]==5 and B[i]==2 or A[i]==5 and B[i]==3): 
            wins_a += 1
            results.append(1)
        elif A[i]==B[i]:
            draws+=1
            results.append(0)
        else:
            wins_b+=1
            results.append(-1)
    
    return wins_a, draws, wins_b, A, B, results