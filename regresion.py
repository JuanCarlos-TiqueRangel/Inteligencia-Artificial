# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 02:51:52 2019

@author: juan
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:45:26 2019

@author: haroldfmurcia
"""

import numpy as np
import matplotlib.pyplot as plt


def dataGen(n,g,xmin,xmax,m,b):
    B_ideal = np.array([[b],[m]])
    if g == 1:
        X = np.ones([n,2])
        ruido = np.zeros([n,1])
        X[:,1] = np.linspace(xmin,xmax,n)
        ruido[:,0] = 100*np.random.rand(n)
        # Ruido Blanco tiene media = 0
        ruido = ruido - ruido.mean()
        Y = np.dot(X,B_ideal) + ruido
    return X, Y



if __name__ == '__main__':
    # 1
    m =5
    b =-10
    n =100
    # 2
    X,Y = dataGen(n,1,-20,20,m,b)
    # 3
    Beta_opt_1 = np.linalg.inv(np.dot(X.T,X))
    Beta_opt_2 = np.dot(X.T,Y)
    Beta_opt = np.dot(Beta_opt_1,Beta_opt_2)
    plt.plot(X[:,1],Y,'o',label='Datos')
    pred = Beta_opt[1]*X[:,1]+Beta_opt[0]
    plt.plot(X[:,1],pred,label='Prediccion')
    plt.legend()
    plt.show()
    print "----------------------------------------"
    print "Valores ideales:"+str(b)+" "+str(m)
    print "Valores estimados:"+str(Beta_opt[0])+" "+str(Beta_opt[1])
    print "----------------------------------------"
    print "Evaluacion de COSTO: MSE"
    error = Y-np.dot(X,Beta_opt)
    MSE = np.dot(error.T,error)*1/n
    print "MSE= " + str(MSE)
    print "----------------------------------------"