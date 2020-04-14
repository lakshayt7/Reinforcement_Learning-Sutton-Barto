#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np


# In[113]:


Steps = 2000
K = 10
Total = 0
N = np.zeros((K,))
Q = np.zeros((K,))
u = np.random.uniform(-10,10,K)
sig = np.random.uniform(0,2,K)
Moves = np.zeros((Steps,))
Rs = np.zeros((Steps,))
eps = 0.2
for i in range(Steps):
    cho = np.random.uniform(0,1)
    if cho>=eps:
        move = np.argmax(Q)
    else:
        move = np.random.randint(K)
    R = np.random.normal(u[move],sig[move])
    Moves[i] = move
    #print("Move nummber:",i," = ",move)
    #print("Reward = ",R)
    Rs[i] = R
    Total = Total + R
    N[move] = N[move]+1
    Q[move] = Q[move]+(1/N[move])*(R-Q[move])
print("Total = ",Total)
#print(N)
#print(Q)

