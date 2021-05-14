'''
Created on Jun 1, 2011

@author: Peter
'''
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import pca

dataMat = pca.loadDataSet('testSet.txt')

lowDMat, reconMat = pca.pca(dataMat, 1)

print(shape(lowDMat))
print(shape(reconMat))

import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='^', s=90)
ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s=50, c='red')
plt.show()
'''
ax.scatter(dataMat[:,0], dataMat[:,1], marker='^', s=90)
ax.scatter(reconMat[:,0], reconMat[:,1], marker='o', s=50, c='red')
plt.show()
'''
