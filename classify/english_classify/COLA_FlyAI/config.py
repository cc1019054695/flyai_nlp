# coding=utf-8
# author=yphacker

import os
import sys

# 训练数据的路径
DATA_PATH = os.path.join(sys.path[0], 'data', 'input')
# 模型保存的路径
MODEL_PATH = os.path.join(sys.path[0], 'data', 'output', 'model')
# 训练log的输出路径
LOG_PATH = os.path.join(sys.path[0], 'data', 'output', 'logs')
# bert路径
BERT_PATH = os.path.join(sys.path[0], 'bert', )

max_seq_length = 44
num_labels = 2
learning_rate = 1e-5
grad_clip = 5.0

print_per_batch = 10
improvement_step = print_per_batch * 10
