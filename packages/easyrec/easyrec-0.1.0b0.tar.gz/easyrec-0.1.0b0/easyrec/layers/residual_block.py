import torch.nn as nn

from easyrec.layers import activation_layer


class ResidualBlock(nn.Module):

    def __init__(self, inputs_dim, hidden_units, activation='relu', l2_reg=0, use_bn=False,
                 init_std=0.0001, dice_dim=3, seed=1024, device='cpu'):
        super(ResidualBlock, self).__init__()
        self.seed = seed
        self.l2_reg = l2_reg
        self.use_bn = use_bn
        if len(hidden_units) == 0:
            raise ValueError("hidden_units is empty!!")
        hidden_units = list(hidden_units)

        self.linears1 = nn.ModuleList(
            [nn.Linear(inputs_dim, hidden_units[i]) for i in range(len(hidden_units))])
        self.linears2 = nn.ModuleList(
            [nn.Linear(hidden_units[i], inputs_dim) for i in range(len(hidden_units))])

        if self.use_bn:
            self.bn1 = nn.ModuleList(
                [nn.BatchNorm1d(hidden_units[i]) for i in range(len(hidden_units))])
            self.bn2 = nn.ModuleList(
                [nn.BatchNorm1d(inputs_dim) for i in range(len(hidden_units) - 1)])

        self.activation_layers1 = nn.ModuleList(
            [activation_layer(activation, hidden_units[i], dice_dim) for i in range(len(hidden_units))])
        self.activation_layers2 = nn.ModuleList(
            [activation_layer(activation, inputs_dim, dice_dim) for i in range(len(hidden_units))])
        self.activation_layers3 = nn.ModuleList(
            [activation_layer(activation, inputs_dim, dice_dim) for i in range(len(hidden_units))])

        for name, tensor in self.linears1.named_parameters():
            if 'weight' in name:
                nn.init.normal_(tensor, mean=0, std=init_std)
        for name, tensor in self.linears2.named_parameters():
            if 'weight' in name:
                nn.init.normal_(tensor, mean=0, std=init_std)

        self.to(device)

    def forward(self, inputs):
        deep_input = inputs

        for i in range(len(self.linears1)):

            fc = self.linears1[i](deep_input)

            if self.use_bn:
                fc = self.bn1[i](fc)

            fc = self.activation_layers1[i](fc)
            fc = self.linears2[i](fc)

            if self.use_bn:
                fc = self.bn2[i](fc)

            fc = self.activation_layers2[i](fc)

            deep_input = self.activation_layers3[i](fc + deep_input)
        return deep_input
