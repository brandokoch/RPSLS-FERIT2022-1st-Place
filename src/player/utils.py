
import random 
import torch
import torch.nn.functional as F

def choose_winning_move(robot_move):
    """
    1-scissors, 2-rock, 3-paper, 4-lizard, 5-spock
    """

    if robot_move==1:
        return random.choice([2,5])
    elif robot_move==2:
        return random.choice([3,5])
    elif robot_move==3:
        return random.choice([1,5])
    elif robot_move==4:
        return random.choice([2,3])
    elif robot_move==5:
        return random.choice([4])
    else:
        raise Exception


def predict_best_move(A,B,model,win_size):
    model.eval()

    a_history=[A[-win_size:]]
    b_history=[B[-win_size:]]
    idx_divisibility_history=[[
            [
                num%2==0,
                num%3==0,
                num%4==0,
                num%5==0,
                num%6==0,
                num%7==0,
                num%8==0,
                num%9==0,
                num%10==0,
                num%11==0,
                num%12==0,
                num%13==0,
                num%14==0,
                num%15==0,
                num%16==0,
                num%17==0,
                num%18==0,
                num%19==0,
                num%20==0,
            ]
            for num in range(len(A)-win_size,len(A))]]


    out=model(
        torch.tensor(a_history),
        torch.tensor(b_history),
        torch.tensor(idx_divisibility_history, dtype=torch.float),
    )

    # Select vector of prediction for robot's next move
    last_out=out[:,-1,:]

    predicted_robot_move_proba=torch.max(F.softmax(last_out.detach(),dim=1)).item()
    predicted_robot_move=torch.argmax(F.softmax(last_out.detach(),dim=1)).item()

    # Choose winning move for the predicted player move
    # Also map move from zero indexed to one indexed
    return choose_winning_move(predicted_robot_move+1), predicted_robot_move_proba