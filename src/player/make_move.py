from player.dataset import *
from player.lr_finder import *
from player.model import *
from player.train import *
from player.utils import *
import player.config as config

import torch.nn as nn
import torch.optim as optim
import numpy as np



def get_player_move(A,B,idx,model=None):
    
    # Map move from one indexed to zero indexed for the embedding layer
    A=[move-1 for move in A]
    B=[move-1 for move in B]
    
    # Logic 1: If too little training data do a random move
    if len(B)<config.RANDOM_MOVE_CNT_GUARANTEE:
        return np.random.choice([1,2,3,4,5],p=[0.1,0.1,0.1,0.2,0.5]), None
    
    # Logic 2: If model is trained and retraining not requested at this step
    # then do predicted best move if confident.
    if (model!=None and idx not in config.TRAIN_AT_STEPS):
        move,proba=predict_best_move(A,B,model,config.WIN_SIZE)

        if proba>config.APPLY_MODEL_THRESHOLD:
            return move,model
        else:
            return np.random.choice([1,2,3,4,5],p=[0.1,0.1,0.1,0.2,0.5]), model
    # Logic 3: Train model
    else:

        # Train Model
        new_model=ModelLSTM(5, config.HIDDEN_LAYER_SIZE)
        train_dl,val_dl=get_dataloaders(A,B)
        train_model(new_model, train_dl,val_dl)

        # Predict
        new_model.eval()
        move,proba=predict_best_move(A,B,new_model,config.WIN_SIZE)
        
        if proba>config.APPLY_MODEL_THRESHOLD:
            return move, new_model 
        else:
            return np.random.choice([1,2,3,4,5],p=[0.1,0.1,0.1,0.2,0.5]), new_model
