#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import re
import pandas as pd

def sortclussource(brain,clus):
    cl = brain.wordclus

    words = brain.words
    corpus = pd.Series(brain.ppcorpus)
    
    # remove upper and rank 
    f = np.vectorize(lambda x: re.split(' -\ ',x)[0].lower())
    w=f(words)
    
    # select cluster 
    w = w[cl==clus]
    
    # count words in the corpus 
    word_counter = np.vectorize(lambda x: corpus.str.count('(\s|^)'+x+'($|\s)'), signature='()->(n)')
    W = pd.DataFrame(word_counter(w).T > 0).astype(int)
    
    # norm
    N = pd.Series(np.linalg.norm(W, axis=1))
    idx=np.argsort(N, kind ='heapsort', axis = 0)[::-1]
    
    return idx

def sortwordsource(brain,word,neighbors=10):
    word = word.lower()
    scores = brain.wordmat
    words = brain.words
    corpus = pd.Series(brain.ppcorpus)
    
    # remove upper and rank
    f = np.vectorize(lambda x: re.split(' -\ ',x)[0].lower())
    w=f(words)
    
    # set word idx
    try:
        word_idx = np.argwhere(w==word)[0][0]
    except:
        return
    
    # index nearest words
    dist=[np.linalg.norm(scores[word_idx]-scores[i]) for i in range(0,len(w))]
    idx=np.argsort(dist, kind ='heapsort', axis = 0)
    
    # define maximum words to use in the process
    if neighbors < 0:
        totalWords=len(idx)
    else:
        totalWords=neighbors
    
    # sort words
    top10 = w[idx[0:totalWords]]
    top10 = np.insert(top10, 0, word)
    totalWords += 1
    
    # count words in the corpus
    word_counter = np.vectorize(lambda x: corpus.str.count('(\s|^)'+x+'($|\s)'), signature='()->(n)')
    c = word_counter(top10).T
    
    # set weights
    weight=np.array([10**ii for ii in range(0,totalWords)][::-1])
    weight = weight/weight[0]
    
    # set scores
    c = c/np.max(c,axis=0)
    c = c*weight
    c = np.sum(c,axis=1)
    
    # sort scores
    idx2=np.argsort(c, kind ='heapsort', axis = 0)[::-1]
    
    # return idx
    r=corpus[idx2]

    return list(idx2)