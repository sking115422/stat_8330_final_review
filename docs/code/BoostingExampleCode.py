# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 06:00:07 2026

@author: pdschlie
"""


import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from matplotlib.colors import ListedColormap



#generate data###########################################################
n=200 #sample size
muA=[50,50] #mean for class A
muB=[0,0] # mean for class B
sd1=25 #standard deviation
sd2=25
cor0=0.2
#covmat=[[sd1^2,cor0*sd1*sd2],[cor0*sd1*sd2,sd2^2]]
covmat = [[sd1**2, cor0*sd1*sd2], [cor0*sd1*sd2, sd2**2]] 

xA=npr.multivariate_normal(mean=muA,cov=covmat,size=int(n/2))
xB=npr.multivariate_normal(mean=muB,cov=covmat,size=int(n/2))
X=np.concatenate((xA,xB),axis=0)
y=np.concatenate((np.repeat(-1,int(n/2)),np.repeat(1,int(n/2))))

#plot the data:
plt.figure()
cmap = ListedColormap(['blue', 'red'])
plt.scatter(X[:,0],X[:,1],c=y, cmap=cmap)





##Next, do the loop over iteratons of adaboot

B=5 #number of iterations
weights = np.ones(n) / n
alphas, stumps = [], []
weightsave=[]



for b in range(B):
    # Fit depth-1 stump with current weights
    stump = DecisionTreeClassifier(max_depth=1)
    stump.fit(X, y, sample_weight=weights)
    stumps.append(stump)

    preds = stump.predict(X)
    incorrect = (preds != y).astype(float)

    # Weighted error
    eps = np.dot(weights, incorrect) / np.sum(weights)
    eps = np.clip(eps, 1e-10, 1 - 1e-10)  #avoids 0 or 1 in eps

    # Learner weight
    alpha = 0.5 * np.log((1 - eps) / eps)
    alphas.append(alpha)


    # Update weights: upweight misclassified
    weights *= np.exp(-alpha * y * preds)  #the negative is because y*pred will be negagtive if y is different than preds
    weights /= np.sum(weights)   
    weightsave.append(weights)



    # renormalize

#plt.tight_layout()
#plt.savefig("adaboost_weights.png", dpi=150, bbox_inches='tight')
plt.show()
print(f"Learner weights α: {[f'{a:.3f}' for a in alphas]}")




##Make final prediction


#calculate weighted sum of stumps:
Gfinal=0
for b in range(B):
    Gfinal=Gfinal+alphas[b]*stumps[b].predict(X)

finalpredictions=np.where(Gfinal>0,1,-1)

plt.figure()
plt.subplot(211)
plt.scatter(X[:,0],X[:,1],c=y, cmap=cmap)
plt.title("data")

plt.subplot(212)
plt.scatter(X[:,0],X[:,1],c=finalpredictions, cmap=cmap)
plt.title("predictions")


#Plot the weights. The color shows the correct class. The size shows the weight. 

plt.figure()
#plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=['blue' if yi == 1 else 'red' for yi in y],s=weightsave[0] * n * 60,alpha=0.7)
plt.title("weights for b=1")

plt.figure()
#plt.subplot(222)
plt.scatter(X[:, 0], X[:, 1], c=['blue' if yi == 1 else 'red' for yi in y],s=weightsave[3] * n * 60,alpha=0.7)
plt.title("b=4")



