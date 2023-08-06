# -*- coding: utf-8 -*-
# Lightning Module
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
# from torch.utils.data import random_split
# from torchvision.datasets import MNIST
# from torchvision import transforms
import pytorch_lightning as pl
from collections import OrderedDict





class MLP(pl.LightningModule):
  """简单多层感知神经网络"""
  def __init__(self,depth=3,dim=128,input_dim=256,out_dim=1024, **kwargs):
    """
    
    depth=3, # 深度层数
    dim=128, 各层的维度
    input_dim=256, 输入的维度
    out_dim=1024  输出的维度
    
    """
    super(MLP, self).__init__()
    self.save_hyperparameters()
    layersDict=OrderedDict()
    for i in range(depth):
      if i==0:
        layersDict["linear"+str(i)]=nn.Linear(self.hparams.input_dim, self.hparams.dim)
      else:
        layersDict["linear"+str(i)]=nn.Linear(self.hparams.dim, self.hparams.dim)
      layersDict["ac"+str(i)]=nn.LeakyReLU()
      layersDict["dropout"+str(i)]=nn.Dropout(0.1)
      # linears.append(nn.Dropout(0.1))
    layersDict["layer_out"]=nn.Linear(self.hparams.dim, self.hparams.out_dim)

    self.layers = nn.Sequential(layersDict)
      # layers

  def forward(self, x):
    # ModuleList can act as an iterable, or be indexed using ints
    # for i, l in enumerate(model.layers):
    #     # x = self.linears[i // 2](x) + l(x)
    #     print(i,l)
    x=self.layers(x)
    return x