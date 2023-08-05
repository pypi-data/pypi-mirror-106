import torch
from torch import nn
from easyrec.models import SequenceBase
from easyrec.layers import GetEmbeddingByColumns, GetInputByNames
from easyrec.layers import AttentionSequencePoolingLayer
from easyrec.layers import Dense


class DIN(SequenceBase):
    def __init__(self, feature_columns, behavior_feature_list, behavior_seq_feature_list,
                 seq_length_name, dnn_use_bn=False, dnn_hidden_units=(256, 128),
                 dnn_activation='relu', att_hidden_size=(64, 16),
                 att_activation='Dice', att_weight_normalization=False, l2_reg_dnn=0.0,
                 l2_reg_embedding=1e-6, dnn_dropout=0, device='cpu'):
        super(DIN, self).__init__(feature_columns, behavior_feature_list, behavior_seq_feature_list)
        att_emb_dim = sum([feat.embedding_dim for feat in self.behavior_feature_columns])
        self.attention = AttentionSequencePoolingLayer(att_hidden_units=att_hidden_size,
                                                       embedding_dim=att_emb_dim,
                                                       att_activation=att_activation,
                                                       return_score=False,
                                                       supports_masking=False,
                                                       weight_normalization=att_weight_normalization)
        dense_dim = sum([feat.embedding_dim for feat in self.sparse_feature_columns + \
                         self.behavior_seq_feature_columns + self.other_seq_feature_columns]) + \
                    sum([feat.dimension for feat in self.dense_feature_columns])
        self.dnn = Dense(inputs_dim=dense_dim,
                         hidden_units=dnn_hidden_units,
                         activation=dnn_activation,
                         dropout_rate=dnn_dropout,
                         l2_reg=l2_reg_dnn,
                         use_bn=dnn_use_bn)
        self.dnn_linear = nn.Linear(dnn_hidden_units[-1], 1, bias=False).to(device)
        self.seq_length_name = seq_length_name
        self.to(device)

    def forward(self, X):
        dense_concat = GetEmbeddingByColumns(self.dense_feature_columns, self.feature_index)(X)
        sparse_emb_list = GetEmbeddingByColumns(self.sparse_feature_columns, self.feature_index,
                                                self.embedding_layers_dict, need_concat=False)(X)
        other_seq_emb_list = GetEmbeddingByColumns(self.other_seq_feature_columns, self.feature_index,
                                                   self.embedding_layers_dict, need_concat=False,
                                                   seq_need_pooling=True)(X)
        emb_concat = torch.cat(sparse_emb_list + other_seq_emb_list, dim=-1).squeeze()
        query_emb = GetEmbeddingByColumns(self.behavior_feature_columns, self.feature_index,
                                          self.embedding_layers_dict)(X)
        keys_emb = GetEmbeddingByColumns(self.behavior_seq_feature_columns, self.feature_index,
                                         self.embedding_layers_dict)(X)
        seq_len = GetInputByNames([self.seq_length_name], self.feature_index)(X)
        hist = self.attention(query_emb, keys_emb, seq_len).squeeze()  # (B,1,E)
        all = torch.cat([hist, dense_concat, emb_concat], dim=-1)
        dnn_output = self.dnn(all)
        out = torch.sigmoid(self.dnn_linear(dnn_output))
        return out
