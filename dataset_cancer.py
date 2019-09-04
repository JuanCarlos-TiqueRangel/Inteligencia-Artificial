import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn import datasets
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes


cancer = datasets.load_breast_cancer() 
diabetes = datasets.load_diabetes()

#for i in range(0,10):
#    plt.figure()
#    
#    for e in range(0,2):
#        ubicacion1 = np.where(cancer.target == e)
#        Y = cancer.data[:,i]
#        Posicion = Y[ubicacion1]
#        
#        if e == 0:
#            name = "Maligno"
#        elif e == 1:
#            name = "Benigno"
# 
#        if i == 0:
#            titulo = "Radio"
#        elif i == 1:
#            titulo = "Textura"
#        elif i == 2:
#            titulo = "Perimetro"
#        elif i == 3:
#            titulo = "Area"
#        elif i == 4:
#            titulo = "Suavidad"        
#        elif i == 5:
#            titulo = "Compacto"        
#        elif i == 6:
#            titulo = "Concavidad"        
#        elif i == 7:
#            titulo = "Puntos concavos"        
#        elif i == 8:
#            titulo = "Simetria"        
#        elif i == 9:
#            titulo = "Dimension fractal"        
#      
#        
#        plt.plot(Posicion,'.',label=name)
#        plt.title(titulo,fontsize=20,color = 'blue')
#        plt.legend()
#        plt.savefig('i')
     
for k in range(0,10):
    plt.figure()
    
    for q in range (0,2):
    
        Pos = np.where(cancer.target == q)
        X = cancer.data[:,k]
        ubicacion = X[Pos]       
        
        if q == 0:
            name = "Maligno"
        elif q == 1:
            name = "Benigno"
 
        if k == 0:
            title = "Radio"
        elif k == 1:
            title = "Textura"
        elif k == 2:
            title = "Perimetro"
        elif k == 3:
            title = "Area"
        elif k == 4:
            title = "Suavidad"        
        elif k == 5:
            title = "Compacto"        
        elif k == 6:
            title = "Concavidad"        
        elif k == 7:
            title = "Puntos concavos"        
        elif k == 8:
            title = "Simetria"        
        elif k == 9:
            title = "Dimension fractal" 
            
        media = np.mean(ubicacion)
        sigma = np.std(ubicacion)
        
        P = np.arange(0.03, 0.1, 0.001)
        
        F = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((P-media)/(sigma))**2)
        
        plt.plot(P,F,label=name)
        plt.title(title,fontsize=20,color = 'green')
        plt.legend()
        plt.savefig('i')
        
#        Radio[0]
#        Perimetro[2]
#        Area[3]
#        Concavidad[6]
#        Puntos Concavos[7]