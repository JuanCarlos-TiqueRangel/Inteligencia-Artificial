# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 01:54:55 2019

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn import datasets
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes
from sklearn.metrics import f1_score


cancer = datasets.load_breast_cancer() 
#diabetes = datasets.load_diabetes()

M1 = np.zeros((1,10))
S1 = np.zeros((1,10))
TESTEO = np.zeros((1,171))
L = 0
P = 0

descriptores = [0,2,3,6,7]

for k in range(0,5):

    for q in range (0,2):
        cancer_ent = np.array(cancer.target[0:397]) 
        Pos = np.where(cancer_ent == q)
        
        if q == 0:
            malignos = Pos[0]
            
        if q == 1:
            benignos = Pos[0]
        
        X = cancer.data[:,descriptores[k]]
        ubicacion = X[Pos]       
            
        media = np.mean(ubicacion)
        sigma = np.std(ubicacion)
        
        M1[0,L] = media
        S1[0,L] = sigma
        L=L+1
               
        
d_valida = np.array(cancer.data[398:569])
valida_target = np.array(cancer.target[398:569])

p_maligno = 173.0/397.0
p_benigno = 224/397.0

for m in range(0,171):
    
    p_Radio_maligno =        1/(S1[0,0]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,0]-M1[0,0])/(S1[0,0]))**2)
    p_Perimetro_maligno =    1/(S1[0,2]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,2]-M1[0,2])/(S1[0,2]))**2)
    p_Area_maligno =         1/(S1[0,4]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,3]-M1[0,4])/(S1[0,4]))**2)
    p_Concavidad_maligno =   1/(S1[0,6]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,6]-M1[0,6])/(S1[0,6]))**2)
    p_PC_maligno =           1/(S1[0,8]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,7]-M1[0,8])/(S1[0,8]))**2)

    p_Radio_benigno =        1/(S1[0,1]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,0]-M1[0,1])/(S1[0,1]))**2)
    p_Perimetro_benigno =    1/(S1[0,3]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,2]-M1[0,3])/(S1[0,3]))**2)
    p_Area_benigno =         1/(S1[0,5]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,3]-M1[0,5])/(S1[0,5]))**2)
    p_Concavidad_benigno =   1/(S1[0,7]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,6]-M1[0,7])/(S1[0,7]))**2)
    p_PC_benigno =           1/(S1[0,9]*np.sqrt(2*np.pi))*np.exp(-0.5*((d_valida[m,7]-M1[0,9])/(S1[0,9]))**2)

    evidencia = p_maligno*p_Radio_maligno*p_Perimetro_maligno*p_Area_maligno*p_Concavidad_maligno*p_PC_maligno + p_benigno*p_Radio_benigno*p_Perimetro_benigno*p_Area_benigno*p_Concavidad_benigno*p_PC_benigno
    
    post_maligno = (p_Radio_maligno*p_Perimetro_maligno*p_Area_maligno*p_Concavidad_maligno*p_PC_maligno)/(evidencia)
    post_benigno = (p_Radio_benigno*p_Perimetro_benigno*p_Area_benigno*p_Concavidad_benigno*p_PC_benigno)/(evidencia)

    if post_maligno > post_benigno:
        TESTEO[0,m] = 0
        
    if post_benigno > post_maligno:
        TESTEO[0,m] = 1

My_f1 = f1_score(valida_target, TESTEO[0,:], average = None)
print TESTEO 
print
print "Probabilidad =" + str(My_f1)