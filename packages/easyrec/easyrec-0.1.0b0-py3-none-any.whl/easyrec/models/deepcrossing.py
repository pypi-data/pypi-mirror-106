import torch
import torch.nn as nn
from easyrec.models  import Base
from easyrec.layers import ResidualBlock,GetEmbeddingByColumns

class DeepCrossing(Base):
    def __init__(self, dnn_feature_columns, hidden_units=(64,64,64), l2=0, l1=0):
        super(DeepCrossing, self).__init__(dnn_feature_columns)
        self.concat_size = sum([feat.dimension for feat in self.dense_feature_columns]) + sum(
            [feat.embedding_dim for feat in self.sparse_feature_columns])
        self.resnet = ResidualBlock(self.concat_size,hidden_units,device=self.device)
        self.fc = nn.Linear(self.concat_size,1)

    def forward(self, X):
        dense_concat = GetEmbeddingByColumns(self.dense_feature_columns,self.feature_index)(X)
        sparse_emb_concat = GetEmbeddingByColumns(self.sparse_feature_columns,self.feature_index,
                                                  self.embedding_layers_dict)(X).squeeze()
        all_concat = torch.cat([dense_concat,sparse_emb_concat],dim=-1)
        res_out = self.resnet(all_concat)
        out = torch.sigmoid(self.fc(res_out))
        return out
