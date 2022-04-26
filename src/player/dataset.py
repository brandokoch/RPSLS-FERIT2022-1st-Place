import random 
import torch
import player.config as config

def get_dataloaders(A,B):

    # Dataset samples include:
    # - history of player moves 
    # - history of robot moves
    # - information about indexes of above moves based on their divisibility 

    seqs=[
        (
            torch.tensor(A[i:i+config.WIN_SIZE]), 
            torch.tensor(B[i:i+config.WIN_SIZE]),
            torch.tensor([
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
                for num in range(i,i+config.WIN_SIZE)], dtype=torch.float
                ),
            torch.tensor(B[i+1:i+config.WIN_SIZE+1])
        )
        for i in range(0,len(A)-config.WIN_SIZE-1,config.WIN_STEP_SIZE)
    ]

    if config.TO_SHUFFLE:
        random.shuffle(seqs)
        
    train_ds=seqs[0:int(len(seqs)*config.TRAIN_DS_PROPORTION)]
    val_ds=seqs[int(len(seqs)*config.TRAIN_DS_PROPORTION):]

    train_dl=torch.utils.data.DataLoader(train_ds, batch_size=config.BS, drop_last=False)
    val_dl=torch.utils.data.DataLoader(val_ds, batch_size=config.BS, drop_last=False)

    return train_dl, val_dl

