## Artificial Intelligence

This repository contains code and resources related to the Inteligencia Artificial course at [Universidad de Ibagué](https://www.unibague.edu.co/). This is a Python scripts that uses the Matplotlib and Scikit-learn libraries to visualize data from the sklearn datasets. 

# Dependences
The script requires the following libraries to be installed:

* Matplotlib
* NumPy
* SciPy
* Scikit-learn

# Scripts

[bayesiano.py]{bayesiano.py}

After installing the dependencies, run the script `bayesiano.py`. The script reads the iris dataset from scikit-learn and computes the mean and standard deviation of each feature for each of the three iris species: setosa, versicolor, and virginica. It then plots the probability distributions for each feature using a normal distribution function.

[Bayesiano_cancer.py]{Inteligencia-Artificial/bayesiano_cancer.py}

This code is a simple implementation of Naive Bayes classifier to classify cancer tumors as malignant or benign. It uses breast cancer dataset from sklearn library.

The code first loads the breast cancer dataset and defines the five descriptors used for classification. Then, it calculates the mean and standard deviation for each descriptor and stores them in M1 and S1 arrays, respectively.

After that, the code loads the validation data and calculates the posterior probability for each validation sample of being malignant or benign. The evidence, posterior probabilities and target values are stored in the arrays 'evidencia', 'post_maligno', 'post_benigno' and 'TESTEO', respectively.

Finally, the code classifies each validation sample based on which posterior probability is greater and stores the classification result in the 'TESTEO' array.

[perceptron_cancer.py]{Inteligencia-Artificial/perceptron_cancer.py}

This script implements a logistic regression model for predicting whether a patient's breast tumor is malignant or benign, based on a set of five tumor descriptors. The model is trained on the Breast Cancer Wisconsin (Diagnostic) dataset from scikit-learn, and validated on a subset of the same dataset.

[regresion.py]{Inteligencia-Artificial/regresion.py}

This code implements a linear regression model to fit data generated from a line with noise. The program generates random data points and plots them, along with the predicted line of best fit. The mean squared error is also calculated to evaluate the quality of the fit.

[iris_plants.py]{Inteligencia-Artificial/iris_plants.py}

The script generates two types of plots for each of the four features of the three different types of Iris flowers. The first type of plot displays the feature values for each of the three types of Iris flowers. The second type of plot displays a histogram of the feature values for each of the three types of Iris flowers, along with a normal distribution curve fitted to the data.

# Contents 

The repository includes the following directories:

search: contains code for search algorithms, including DFS, BFS, and A*
genetic: contains code for genetic algorithms, including selection, crossover, and mutation functions
machine_learning: contains code for various machine learning algorithms, including decision trees, k-nearest neighbors, and neural networks
games: contains code for games such as Tic Tac Toe and Connect Four, as well as game-playing AI algorithms
