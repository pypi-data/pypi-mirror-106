#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class word_count_in_col:
    def __init__(self):
        # store the appear frequency
        self.res = []
    
    def fit(self, col):
        # chained steps
        # count word frequency in each cell in a column
        self.fre = col.apply(self.count_frequency)
        # turn the series into a list
        self.fre = self.fre.tolist()
        # calculate word counts for all words 
        for d in self.fre:
            self.add_dict(d)
    
    # count appear frequency of each word
    def count_frequency(self, row):
        try:
            d={}
            for i in row.split():
                d[i] = row.count(i)

            return d 
        
        except:
            d = {}
            tokens = row.split()
            for tok in tokens:
                counts = tokens.count(tok)
                d[f'{tok}'] = counts
                
            return d 

    # if the same key appear in both dictionary, then the values in both dictionary will be added together 
    def dict_op(self, op, dict1, dict2=None):
        if type(dict1) == dict:
            dict1 = dict1.copy()
        if type(dict2) == dict:
            dict2 = dict2.copy()
        
        if dict2 == None:
            dict5 = dict1.copy()
        if dict2 != None:    
            dict3 = {}
            all_keys = list(dict1.keys()) + list(dict2.keys())
            for k in all_keys:
                dict3[k] = ''
            for k1 in dict1.keys():
                for k2 in dict2.keys():
                    if k1==k2:
                        if op == '+':
                            dict3[k1] = dict1[k1] + dict2[k2]
                        if op == '-':
                            dict3[k1] = dict1[k1] - dict2[k2]
                        if op == '*':
                            dict3[k1] = dict1[k1] * dict2[k2]
                        if op == '/':
                            dict3[k1] = dict1[k1] / dict2[k2]
                        if op == '**':
                            dict3[k1] = dict1[k1] ** dict2[k2]
                        if op == '//':
                            dict3[k1] = dict1[k1] // dict2[k2]
                            
            dict4 = dict3.copy()
            for k3 in dict3.keys():
                if dict3[k3] == '':
                    dict4.pop(k3)

            for k4 in dict4.keys():
                dict1.pop(k4)
                dict2.pop(k4)

            dict5 = {}
            for k1 in dict1.keys():
                dict5[k1] = dict1[k1]

            for k2 in dict2.keys():
                dict5[k2] = dict2[k2]

            for k4 in dict4.keys():
                dict5[k4] = dict4[k4]

        return dict5
    
    def add_dict(self, dic): 
        if len(self.res) > 0:
            self.res = self.dict_op('+', self.res, dic)
            
        if len(self.res) == 0:
            self.res = dic
