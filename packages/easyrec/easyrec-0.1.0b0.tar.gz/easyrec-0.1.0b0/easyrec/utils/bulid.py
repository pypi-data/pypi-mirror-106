from easyrec.utils  import SparseFeat, VarLenSparseFeat, DenseFeat
from collections import OrderedDict
import torch.nn as nn


def build_feature_columns(feature_columns):
    # 将特征中的sparse特征筛选出来
    sparse_feature_columns = list(
        filter(lambda x: isinstance(x, SparseFeat), feature_columns)) if feature_columns else []
    dense_feature_columns = list(
        filter(lambda x: isinstance(x, DenseFeat), feature_columns)) if feature_columns else []
    varlen_sparse_feature_columns = list(
        filter(lambda x: isinstance(x, VarLenSparseFeat), feature_columns)) if len(feature_columns) else []
    return dense_feature_columns, sparse_feature_columns, varlen_sparse_feature_columns

def build_embedding_layers_dict(sparse_feature_columns,varlen_sparse_feature_columns,linear=False):
    # 定义一个embedding层对应的字典
    embedding_layers_dict = dict()
    # 如果是用于线性部分的embedding层，其维度为1，否则维度就是自己定义的embedding维度
    for feat in sparse_feature_columns + varlen_sparse_feature_columns:
        embedding_layers_dict[feat.name] = nn.Embedding(num_embeddings=feat.vocabulary_size,
                                                        embedding_dim=feat.embedding_dim if not linear else 1,
                                                        padding_idx=0)
    return embedding_layers_dict

def build_feature_index(feature_columns):
    features = OrderedDict()
    start = 0
    for feat in feature_columns:
        feat_name = feat.name
        if feat_name in features:
            continue
        if isinstance(feat, SparseFeat):
            features[feat_name] = (start, start + 1)
            start += 1
        elif isinstance(feat, DenseFeat):
            features[feat_name] = (start, start + feat.dimension)
            start += feat.dimension
        elif isinstance(feat, VarLenSparseFeat):
            features[feat_name] = (start, start + feat.maxlen)
            start += feat.maxlen
        else:
            raise TypeError("Invalid feature column type,got", type(feat))
    return features

