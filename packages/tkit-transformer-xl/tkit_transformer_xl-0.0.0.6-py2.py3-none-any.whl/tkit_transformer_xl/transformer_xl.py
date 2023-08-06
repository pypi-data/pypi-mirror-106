# -*- coding: utf-8 -*-

import torch

from tkit_memory_performer_xl import MemoryTransformerXL
# from memory_transformer_xl.autoregressive_wrapper import AutoregressiveWrapper
import torch
from torch import nn
from torch.optim import Adam
# from mlm_pytorch import MLM
from transformers import AutoTokenizer, AutoModel,BertTokenizer
# import torch
# from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.data import random_split
# from torchvision.datasets import MNIST
# from torchvision import transforms
# import pytorch_lightning as pl
import pytorch_lightning as pl
# from omegaconf import OmegaConf
# import torch_optimizer as optim
from tkit_transformer_xl.autoregressivewrapper import AutoregressiveWrapper


class Transformer_xl(pl.LightningModule):
    """
    自动xl实现,包含全部状态输出,并且计算loss
    
    >
    >from tkit_transformer_xl import Transformer_xl
    >model=Transformer_xl()
    >

    """
    def __init__(self,lr=3e-4,dim=128,heads=8,seq_len=512,mem_write_iters = 2,
                 max_batch_size=8,lmem_len = 256,mem_len = 256,memory_layers = [3,4,5],
                 num_mem_kv = 128, depth = 5,T_max=500,attn_dropout=0.1, ff_glu = False, ff_dropout = 0.1, attn_layer_dropout = 0.1,num_tokens=8021,memory_transformer_xl=False,Autoregressive=False,**kwargs):
        """

        """
        super().__init__()
#         self.hp=hp
        self.save_hyperparameters()
        
        # if tokenizer==None:
        #     self.tokenizer = BertTokenizer.from_pretrained("clue/roberta_chinese_clue_tiny")
        # else:
        #     self.tokenizer=tokenizer
        
        # 是否是引用原始的方案，默认使用perfprmer方案
        if memory_transformer_xl==True:
            from memory_transformer_xl import MemoryTransformerXL
        self.model = MemoryTransformerXL(
            num_tokens = self.hparams.num_tokens,
            dim = self.hparams.dim,
            heads = self.hparams.heads,
            depth = self.hparams.depth,
            seq_len = self.hparams.seq_len,
            mem_len = self.hparams.mem_len,            # short term memory (the memory from transformer-xl)
            lmem_len = self.hparams.lmem_len,           # long term memory (memory attention network attending to short term memory and hidden activations)
            mem_write_iters = 2,      # number of iterations of attention for writing to memory
            memory_layers = self.hparams.memory_layers,  # which layers to use memory, only the later layers are actually needed
            num_mem_kv = self.hparams.num_mem_kv,         # number of memory key/values, from All-attention paper
            ff_glu=self.hparams.ff_glu,
            ff_dropout=self.hparams.ff_dropout,
            attn_layer_dropout=self.hparams.attn_layer_dropout,
            

        )
        # 启用自动回归
        if self.hparams.Autoregressive:
            self.model = AutoregressiveWrapper(self.model)
            
        #     self.model=model
        
        pass
    def forward(self, x,return_loss=True):
        """
        输入原始长度数据,会自动进行切割并且返回编码和loss
        """
        # 对输出的状态进行拼接
        if self.hparams.Autoregressive:
            allLoss=0
            for i,(loss, is_last,logits) in enumerate(self.model(x, max_batch_size = self.hparams.max_batch_size, return_loss = return_loss)):
            # print(loss, is_last,logits.size())
                allLoss=allLoss+loss
                if i==0:
                    out_logits=logits
                else:
                    out_logits=torch.cat((out_logits,logits),1)
            
            loss=allLoss/x.size(0)
            return out_logits,loss
        else:
            for i,one in enumerate(x.split(self.hparams.seq_len,dim=1)):
                # print(x)
                if i==0:
                    out_logits, mem1 = self.model(one)
                    # out_logits=logits
                else:
                    logits, mem1 = self.model(one, memories = mem1)
                    out_logits=torch.cat((out_logits,logits),1)
            return out_logits
    def training_step(self, batch, batch_idx):
        """一次batch训练"""
        # training_step defined the train loop.
        _,loss=self(batch[0])
        # Logging to TensorBoard by default
        self.log('train_loss', loss)
        return loss

    
    def validation_step(self, batch, batch_idx):
        """一次batch训练"""
        # training_step defined the train loop.
        _,loss=self(batch[0])
        # Logging to TensorBoard by default
        self.log('val_loss', loss)
        return loss

    def test_step(self, batch, batch_idx):
        """一次batch训练"""
        # training_step defined the train loop.
        _,loss=self(batch[0])
        # Logging to TensorBoard by default
        self.log('test_loss', loss)
        return loss

    def configure_optimizers(self):
        """优化器 # 类似于余弦，但其周期是变化的，初始周期为T_0,而后周期会✖️T_mult。每个周期学习率由大变小； https://www.notion.so/62e72678923f4e8aa04b73dc3eefaf71"""
#         optimizer = torch.optim.AdamW(self.parameters(), lr=(self.learning_rate))

#         Paper: Large Batch Optimization for Deep Learning: Training BERT in 76 minutes (2019) [https://arxiv.org/abs/1904.00962]

#         Reference Code: https://github.com/cybertronai/pytorch-lamb
        # model = ...
#         optimizer = optim.Lamb(
#             self.parameters(),
#             lr= self.hparams.lr,
#             betas=(0.9, 0.999),
#             eps=1e-8,
#             weight_decay=0,
#         )
#         optimizer.step()

        #只优化部分
        optimizer = torch.optim.AdamW(self.parameters(), lr=(self.hparams.lr))
        #         使用自适应调整模型
        T_mult=2
        scheduler =torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer,T_0=self.hparams.T_max,T_mult=T_mult,eta_min=0, verbose=True)
#         https://github.com/PyTorchLightning/pytorch-lightning/blob/6dc1078822c33fa4710618dc2f03945123edecec/pytorch_lightning/core/lightning.py#L1119
        lr_scheduler={
#            'optimizer': optimizer,
           'scheduler': scheduler,
#             'reduce_on_plateau': True, # For ReduceLROnPlateau scheduler
            'interval': 'step', #epoch
            'frequency': 1,
            'name':"lr_scheduler",
            'monitor': 'train_loss', #监听数据变化
            'strict': True,
        }
        return {'optimizer': optimizer, 'lr_scheduler': scheduler}




