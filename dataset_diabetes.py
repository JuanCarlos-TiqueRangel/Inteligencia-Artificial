# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:58:46 2019

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

#cancer = datasets.load_breast_cancer() 
diabetes = datasets.load_diabetes()        
        
for k in range(0,10):
    plt.figure()
    
    for q in range(25,346):
    
        Pos = np.where(diabetes.target == q)
        X = diabetes.data[:,k]
        ubicacion = X[Pos]       
 
        if k == 0:
            title = "Edad"
        elif k == 1:
            title = "Sexo"
        elif k == 2:
           title = "bmi"
        elif k == 3:
            title = "bp"
        elif k == 4:
            title = "S1"        
        elif k == 5:
            title = "S2"        
        elif k == 6:
            title= "S3"        
        elif k == 7:
            title = "S4"        
        elif k == 8:
            title = "S5"        
        elif k == 9:
            title = "S6"  
            
        media = np.mean(ubicacion)
        sigma = np.std(ubicacion)
        
        P = np.arange(-0.05, 0.1, 0.001)
        
        F = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((P-media)/(sigma))**2)
        
        plt.plot(P,F)
        plt.title(title,fontsize=20,color = 'green')
        plt.legend()
plt.savefig('i')