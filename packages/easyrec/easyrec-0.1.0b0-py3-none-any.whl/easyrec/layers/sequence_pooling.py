import torch
from torch import nn
class SequencePoolingLayer(nn.Module):
    """The SequencePoolingLayer is used to apply pooling operation(sum,mean,max) on variable-length sequence feature/multi-value feature.

      Input shape
        - A list of two  tensor [seq_value,seq_len]

        - seq_value is a 3D tensor with shape: ``(batch_size, T, embedding_size)``

        - seq_len is a 2D tensor with shape : ``(batch_size, 1)``,indicate valid length of each sequence.

      Output shape
        - 3D tensor with shape: ``(batch_size, 1, embedding_size)``.

      Arguments
        - **mode**:str.Pooling operation to be used,can be sum,mean or max.

    """

    def __init__(self, mode='mean',  device='cpu'):

        super(SequencePoolingLayer, self).__init__()
        if mode not in ['sum', 'mean', 'max']:
            raise ValueError('parameter mode should in [sum, mean, max]')
        self.mode = mode
        self.device = device
        self.eps = torch.FloatTensor([1e-8]).to(device)
        self.to(device)

    def _sequence_mask(self, lengths, maxlen=None, dtype=torch.bool):
        # Returns a mask tensor representing the first N positions of each cell.
        if maxlen is None:
            maxlen = lengths.max()
        row_vector = torch.arange(0, maxlen, 1).to(lengths.device)
        matrix = torch.unsqueeze(lengths, dim=-1)
        mask = row_vector < matrix

        mask.type(dtype)
        return mask

    def forward(self, seq_emb, mask):
        mask = mask.float()
        user_behavior_length = torch.sum(mask, dim=-1, keepdim=True) #[B,T,1]
        mask = mask.unsqueeze(2)
        embedding_size = seq_emb.shape[-1]

        mask = torch.repeat_interleave(mask, embedding_size, dim=2)  # [B, maxlen, E]

        if self.mode == 'max':
            hist = seq_emb - (1 - mask) * 1e9
            hist = torch.max(hist, dim=1, keepdim=True)[0]
            return hist
        hist = seq_emb * mask.float()
        hist = torch.sum(hist, dim=1, keepdim=False)

        if self.mode == 'mean':
            self.eps = self.eps.to(user_behavior_length.device)
            hist = torch.div(hist, user_behavior_length.type(torch.float32) + self.eps)

        hist = torch.unsqueeze(hist, dim=1)
        return hist

if __name__ == "__main__":
    a = torch.tensor([[1,2,3,4,0,0,0]],dtype=torch.long)
    mask = torch.tensor([[True,True,True,True,False,False,False]])
    b = nn.Embedding(5,embedding_dim=4,padding_idx=0)
    c = b(a)
    d = SequencePoolingLayer()(c,mask)
    d = d
