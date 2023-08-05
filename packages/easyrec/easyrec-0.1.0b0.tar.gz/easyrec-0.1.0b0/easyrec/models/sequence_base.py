import torch
import torch.nn as nn
from easyrec.models import Base

class SequenceBase(Base):
    def __init__(self,feature_columns,behavior_feature_list,behavior_seq_feature_list,device='cpu'):
        super(SequenceBase, self).__init__(feature_columns,device='cpu')
        self.behavior_feature_columns = []
        self.behavior_seq_feature_columns = []
        self.other_seq_feature_columns = []

        for feat in self.sparse_feature_columns:
            if feat.name in behavior_feature_list:
                self.behavior_feature_columns.append(feat)

        for feat in self.varlen_sparse_feature_columns:
            if feat.name in behavior_seq_feature_list:
                self.behavior_seq_feature_columns.append(feat)
            else:
                self.other_seq_feature_columns.append(feat)