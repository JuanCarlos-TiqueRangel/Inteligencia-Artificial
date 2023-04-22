# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:50:49 2019

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import f1_score

cancer = datasets.load_breast_cancer() 
diabetes = datasets.load_diabetes()

descriptores = [0,2,3,6,7]
#Radio[0] - Perimetro[2] - Area[3] - Concavidad[6] - Puntos Concavos[7]
Y = cancer.target[0:397]

X1 = cancer.data[0:397,0]
X2 = cancer.data[0:397,2]
X3 = cancer.data[0:397,3]
X4 = cancer.data[0:397,6]
X5 = cancer.data[0:397,7]

X1 = (X1 - np.mean(X1))/(np.std(X1))
X2 = (X2 - np.mean(X2))/(np.std(X2))
X3 = (X3 - np.mean(X3))/(np.std(X3))
X4 = (X4 - np.mean(X4))/(np.std(X4))
X5 = (X5 - np.mean(X5))/(np.std(X5))

#se pone la cantidad de columnas como cantidad de descriptores +1
X = np.ones([len(X1),6])
X[:,1] = X1
X[:,2] = X2
X[:,3] = X3
X[:,4] = X4
X[:,5] = X5

pred = 0
cost    = 1e3
precost = 0
dJ      = cost-precost
# Cost vector
J=[]

[f,c] = X.shape     
eta = 1e-3 #rta de aprendizaje
W = np.zeros([c,1]) #Beta

while (abs(dJ))>10e-6:
    # Calculo de predicción
    pred = np.dot(X,W)
    # Función de activación
    pred = 1.0 / (1.0 + np.exp(-pred) )
    # Calculo de error
    error= (Y - pred.T).T
    # Calculo de gradiente
    gt   = -X.T.dot(error)
    delta= eta*gt
    W    = W - delta
    cost = np.sum(np.power(error,2))
    dJ   = cost-precost
    precost = cost
    J.append(cost)
   
plt.figure()
plt.plot(J,'o')
plt.xlabel("Iteraciones")
plt.ylabel("Costo")

 
#======================= VALIDACION =================================

X6 = cancer.data[398:,0]
X7 = cancer.data[398:,2]
X8 = cancer.data[398:,3]
X9 = cancer.data[398:,6]
X0 = cancer.data[398:,7]


Y_val = cancer.target[398:]

X6 = (X6 - np.mean(X6))/(np.std(X6))
X7 = (X7 - np.mean(X7))/(np.std(X7))
X8 = (X8 - np.mean(X8))/(np.std(X8))
X9 = (X9 - np.mean(X9))/(np.std(X9))
X0 = (X0 - np.mean(X0))/(np.std(X0))

X_val = np.ones([len(X6),6])
X_val[:,1] = X6
X_val[:,2] = X7
X_val[:,3] = X8
X_val[:,4] = X9
X_val[:,5] = X0

pred   = (np.dot(X_val,W))
pred   = 1.0 / (1.0 + np.exp(-pred) )

# cuantización
for k in range(0,len(pred)-1):
    if(pred[k])>0.5:
        pred[k] = 1
    else:
        pred[k] = 0
# Graficas
        
plt.figure()
plt.plot(Y_val,'bo',label='datos a validar')
plt.plot(pred,'r+',label='prediccion')
plt.legend()
plt.margins(0.1,0.1)
plt.show()

#My_f1 = f1_score(X_val, pred[], average = None)


print pred

