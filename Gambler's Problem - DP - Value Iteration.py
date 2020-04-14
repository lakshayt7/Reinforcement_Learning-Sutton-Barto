#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
theta = 0.00001
ncoin = 100
reward = 1
V = np.random.rand((ncoin+1))
V[ncoin] = 0
V[0] = 0
ph = 0.25
delt = 10
R = np.zeros(ncoin+1)
R[ncoin] = 1
pi = np.zeros(ncoin+1)


# In[10]:


count = 0
stab = 0
gamma = 1
while count < 1000:
    delt = 0
    flag = 0
    for s in range(1,ncoin):
        v = V[s]
        maxind = -1
        mx = -2
        for a in range(1, min(s,100-s)+1):
            #We are taking undiscounted so gamma = 1
            temp = ph*(R[s+a]+gamma*V[s+a])+(1-ph)*(R[s-a]+gamma*V[s-a])
            if mx<temp:
                mx = temp
                maxind = a
        V[s] = mx
        pi[s] = maxind
        delt = max(delt,np.abs(V[s]-v))
    if delt<theta:
        count = count+1
    else:
        count = 0


# In[11]:


plt.plot(pi)


# In[ ]:




