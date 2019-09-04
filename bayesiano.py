# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn import datasets
from sklearn.datasets import load_iris

iris = datasets.load_iris()

def variables():

    global X,M,S

    #X = np.zeros(35)
    M = np.zeros(3)
    S = np.zeros(3)



def media_varianza():
    for i in range(0,4):
            for e in range(0,3):
                pos = np.where(iris.target == e)
                Y = iris.data[:,i]
                ubicacion = Y[pos]

                media = np.mean(ubicacion[0:34])
                sigma = np.std(ubicacion[0:34])

                M[e] = media
                S[e] = sigma


def probabilidades():

    global M,p_setosa,p_versicular,p_virginica,p_PLsetosa,p_PLversicular
    global p_PLvirginica,p_PWsetosa,p_PWversicular,p_PWvirginica

    p_setosa = 35.0/105.0
    p_versicular = 35.0/105.0
    p_virginica = 35.0/105.0

    p_PLsetosa =1
    p_PLversicular =1
    p_PLvirginica =1

    p_PWsetosa =1
    p_PWversicular =1
    p_PWvirginica =1

    print p_virginica



variables()
media_varianza()
probabilidades()

























#def __init__(self):
#    global P
#    self.pos = 0
#    self.Y = 0
#    self.ubicacion = 0
#    self.media = 0
#    self.sigma = 0
#    self.M = np.zeros[3]
#    self.S = np.zeros[3]
#
#def medias(self):
#    for i in range(0,4):
#
#        for k in range(0,3):
#            self.pos = np.where(iris.target == k)
#            self.Y = iris.data[:,i]
#            self.ubicacion = self.Y[self.pos]
#
#            self.media = np.mean(self.ubicacion[0:34])
#            self.sigma = np.std(self.ubicacion[0:34])
#
#            self.M[k] = self.media
#            self.S[k] = self.sigma









# U= [0.2, 0.2, 0.2, 0.2, 0.3,0.4,0.3,0.2,0.2
#,0.1
#,0.2
#,0.2
#,0.1
#,0.1
#,0.2
#,0.4
#,0.4
#,0.3
#,0.3
#,0.3
#,0.2
#,0.4
#,0.2
#,0.5
#,0.2
#,0.2
#,0.4
#,0.2
#,0.2
#,0.2
#,0.2
#,0.4
#,0.1
#,0.2
#,0.2
#]
