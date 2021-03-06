# -*- coding: utf-8 -*

import os
import bert.tokenization as tokenization
from bert.run_classifier import convert_single_example_simple
from flyai.processor.base import Base
import config


# MAX_LEN = 128
# class Processor(Base):
#     def __init__(self):
#         with open(DATA_PATH + '/embedding.json', 'r') as f:
#             js = f.read()
#             self.word_embed = json.loads(js)
#         self.id2lael = ['news_culture', 'news_entertainment', 'news_sports', 'news_finance', 'news_house', 'news_car',
#                         'news_edu', 'news_tech', 'news_military', 'news_travel', 'news_world', 'news_agriculture',
#                         'news_game', 'stock', 'news_story']
#
#     def input_x(self, news):
#         '''
#         参数为csv中作为输入x的一条数据，该方法会被Dataset多次调用
#         '''
#         temp = []
#         fill_embed = [0 for i in range(200)]
#         news = jieba.cut(news)
#         for x in news:
#             if x in self.word_embed:
#                 temp.append(self.word_embed[x])
#         for j in range(50 - len(temp)):
#             temp.append(fill_embed)
#         x_train = temp[:50]
#         return x_train
#
#     def input_y(self, category):
#         '''
#         参数为csv中作为输入y的一条数据，该方法会被Dataset多次调用
#         '''
#         label_hot = [0 for i in range(15)]
#         label_hot[self.id2lael.index(category.strip('\n'))] = 1
#         return label_hot
#
#     def output_y(self, index):
#         '''
#         验证时使用，把模型输出的y转为对应的结果
#         '''
#         return self.id2lael[int(index)]


class Processor(Base):
    def __init__(self):
        self.token = None
        self.id2label = ['news_culture', 'news_entertainment', 'news_sports', 'news_finance', 'news_house', 'news_car',
                        'news_edu', 'news_tech', 'news_military', 'news_travel', 'news_world', 'news_agriculture',
                        'news_game', 'stock', 'news_story']

    def input_x(self, news):
        '''
        参数为csv中作为输入x的一条数据，该方法会被Dataset多次调用
        '''
        if self.token is None:
            bert_vocab_file = os.path.join(config.DATA_PATH, "model", "chinese_L-12_H-768_A-12", 'vocab.txt')
            self.token = tokenization.CharTokenizer(vocab_file=bert_vocab_file)

        word_ids, word_mask, word_segment_ids = \
            convert_single_example_simple(max_seq_length=config.max_seq_length, tokenizer=self.token, text_a=news)

        return word_ids, word_mask, word_segment_ids

    def input_y(self, category):
        '''
        参数为csv中作为输入y的一条数据，该方法会被Dataset多次调用
        '''
        return self.id2label.index(category.strip('\n'))

    def output_y(self, data):
        '''
        验证时使用，把模型输出的y转为对应的结果
        '''
        return self.id2label[int(data[0])]
