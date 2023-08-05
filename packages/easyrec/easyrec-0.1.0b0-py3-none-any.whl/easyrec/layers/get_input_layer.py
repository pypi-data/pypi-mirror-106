from easyrec.utils import SparseFeat, VarLenSparseFeat, DenseFeat
import torch.nn as nn
from .sequence_pooling import SequencePoolingLayer
import torch


class GetEmbeddingByColumns(nn.Module):
    def __init__(self, feature_columns, feature_index, embedding_dict=None, *,
                 need_concat=True, concat_dim=-1, seq_need_pooling=False, pooling_mode='mean'):
        super(GetEmbeddingByColumns, self).__init__()
        self.feature_columns = feature_columns
        self.feature_index = feature_index
        self.embedding_dict = embedding_dict
        self.need_concat = need_concat
        self.concat_dim = concat_dim
        self.seq_need_pooling = seq_need_pooling
        self.pooling_mode = pooling_mode

    def forward(self, inputs):
        outputs_list = []
        for feat in self.feature_columns:
            start, end = self.feature_index[feat.name]
            if isinstance(feat, DenseFeat):
                outputs_list.append(inputs[:,start:end])
            if isinstance(feat, SparseFeat):
                sparse_input = inputs[:, start:end].long()
                outputs_list.append(self.embedding_dict[feat.name](sparse_input))
            if isinstance(feat, VarLenSparseFeat):
                seq_input = inputs[:, start:end].long()
                seq_emb = self.embedding_dict[feat.name](seq_input)
                if self.seq_need_pooling:
                    mask = (seq_input != 0)
                    outputs_list.append(SequencePoolingLayer(mode=self.pooling_mode)(seq_emb, mask))
                else:
                    outputs_list.append(seq_emb)
        if len(outputs_list) == 0:
            return []
        if self.need_concat:
            return torch.cat(outputs_list, dim=self.concat_dim)
        return outputs_list


class GetInputByNames(nn.Module):
    def __init__(self, feature_names, feature_index, *,
                 need_concat=True, concat_dim=-1):
        super(GetInputByNames, self).__init__()
        self.feature_names = feature_names
        self.feature_index = feature_index
        self.need_concat = need_concat
        self.concat_dim = concat_dim

    def forward(self, inputs):
        outputs_list = []
        for feat_name in self.feature_names:
            start, end = self.feature_index[feat_name]
            outputs_list.append(inputs[:, start:end])
        if self.need_concat:
            return torch.cat(outputs_list, dim=self.concat_dim)
        return outputs_list
