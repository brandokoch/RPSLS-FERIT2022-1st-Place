import torch
import torch.nn as nn
from torch.nn import Module

class ModelLSTM(Module):
    def __init__(self, move_type_cnt,n_hidden):
        super(ModelLSTM, self).__init__()

        self.i_h=nn.Embedding(move_type_cnt,n_hidden)
        
        self.h_h=nn.LSTM(
            input_size=n_hidden*3,
            hidden_size=n_hidden*3,
            batch_first=True,
        )     

        self.idx_encoder=nn.Sequential(
            nn.Linear(19,n_hidden)
        )

        self.h_o=nn.Linear(n_hidden*3,move_type_cnt)
                                   
    def forward(self, a_history,b_history, idxs):
        a_history_move_embed=self.i_h(a_history)
        b_history_move_embed=self.i_h(b_history)
        idx_embed=self.idx_encoder(idxs)
        h=torch.cat((a_history_move_embed,b_history_move_embed, idx_embed), dim=2)
        h, _=self.h_h(h)
        out=self.h_o(h)
        
        return out