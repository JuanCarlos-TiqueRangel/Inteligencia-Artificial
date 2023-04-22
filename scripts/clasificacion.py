import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn import datasets



iris = datasets.load_iris()
P0 = np.where(iris.target == 0)
PL_setosa = iris.data[P0,0]


P1 = np.where(iris.target == 0)
PL_Versicolor = iris

P2 = np.where(iris.target == 0)
PL_Virginica = iris.data[P0,0]



plt.plot(PL_setosa)
plt.show()
