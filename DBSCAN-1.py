#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
from sklearn import datasets


# In[12]:


X, y =datasets.make_circles(n_samples=5000,factor=.6, noise=.05)


# In[13]:


y


# In[14]:


fig = plt.figure()
plt.scatter(X[:,0], X[:,1], marker='o')


# # K-means聚类

# In[16]:


from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=2,random_state=9).fit_predict(X)
plt.scatter(X[:,0], X[:,1],c=y_pred)
plt.title('K-means')


# # DBSCAN聚类

# In[20]:


from sklearn.cluster import DBSCAN
y_pred = DBSCAN(eps =0.1, min_samples =10).fit_predict(X) #eps半径，min_samples最小样本
plt.scatter(X[:, 0],X[:, 1],c=y_pred)
plt.title('DBSCAN')


# In[ ]:




