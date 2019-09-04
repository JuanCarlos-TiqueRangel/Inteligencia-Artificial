# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:10:51 2019

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn import datasets
from sklearn.datasets import load_iris

iris = datasets.load_iris()
data = load_iris()

ubicacion0 = np.where(iris.target == 0) # SETOSA
ubicacion1 = np.where(iris.target == 1) # VERSICOLOR
ubicacion2 = np.where(iris.target == 2) # VIRGINICA


rango = np.arange(0, 100, .1)  

info = iris.data[0:50,0]
info1 = iris.data[50:100,0]
info2 = iris.data[100:150,0]
#plt.plot(info,'.',info1,'.',info2,'.')

for i in range(0,4):
    plt.figure(i)
    
    for e in range(0,3):
        ubicacion = np.where(iris.target == e)
        Y = iris.data[:,i]
        Posicion = Y[ubicacion]        
        
        if e == 0:
            name = "Setosa"
        elif e == 1:
            name = "Versicular"
        elif e == 2:
            name = "Virginica"  
        if i == 0:
            titulo = "Sepal Length"
        elif i == 1:
            titulo = "Sepal Width"
        elif i == 2:
            titulo = "Petal Length"
        elif i == 3:
            titulo = "Petal Width"        
        
        plt.plot(Posicion,'.',label=name)
        plt.title(titulo,fontsize=20,color = 'blue')
        plt.legend()


for k in range(0,4):
    plt.figure()
    
    for q in range (0,3):
    
        Pos = np.where(iris.target == q)
        X = iris.data[:,k]
        ubicacion = X[Pos]        
        
        if q == 0:
            log = "Setosa"
        elif q == 1:
            log = "Versicular"
        elif q == 2:
            log = "Virginica"
        if k == 0:
            title = "Sepal Length"
        elif k == 1:
            title = "Sepal Width"
        elif k == 2:
            title = "Petal Length"
        elif k == 3:
            title = "Petal Width"
            
        media = np.mean(ubicacion)
        sigma = np.std(ubicacion)
        
        P = np.arange(0, 10, .1)
        
        F = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((P-media)/(sigma))**2)
        
        plt.plot(P,F,label=log)
        plt.title(title,fontsize=20,color = 'green')
        plt.legend()



        