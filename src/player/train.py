import player.config as config
from player.dataset import *
import torch.nn as nn
import torch.optim as optim

def train_model(model, train_dl, val_dl):

    model.train()
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.LR, weight_decay=config.WEIGHT_DECAY)

    val_losses=[]

    for epoch in range(config.EPOCH_CNT):
        # Train
        model.train()
        batch_cnt=0
        train_loss=0
        for item in train_dl:
            batch_cnt+=1
            optimizer.zero_grad()

            out=model(item[0],item[1],item[2])
            loss=loss_fn(out.view(-1,5),item[-1].long().view(-1))
            train_loss+=loss.detach().item()

            loss.backward()
            optimizer.step()

        # Eval
        model.eval()
        batch_cnt=0
        val_loss=0
        for item in val_dl:
            batch_cnt+=1
            out=model(item[0],item[1],item[2])
            val_loss+=loss_fn(out.view(-1,5),item[-1].long().view(-1)).detach().item()

        val_losses.append(val_loss)
        min_val_loss=min(val_losses)
        min_val_loss_idx=val_losses.index(min_val_loss)
        if len(val_losses)-1-config.EARLY_STOPPING_PATIENCE > min_val_loss_idx:
            if config.LOGGING_LEVEL>=2:
                print('Early stopping triggered')
            break 
            
        val_loss=val_loss/batch_cnt

        if val_loss<config.STOP_TRAIN_AT_LOSS:
            if config.LOGGING_LEVEL>=1:
                print(f'Training stopped, low loss target reached')
            break

        if config.LOGGING_LEVEL>=2:
            print(f"Train Loss :{train_loss} Validation Loss:{val_loss}")

    if config.LOGGING_LEVEL>=1:
        print(f"Training done, Train Loss :{train_loss} Validation Loss:{val_loss}")