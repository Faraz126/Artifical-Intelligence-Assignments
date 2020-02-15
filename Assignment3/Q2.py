# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Student ID = fk03983
"""

import numpy as np
import matplotlib.pyplot as plt

"""This function takes actual and predicted ratings and compute total mean square error(mse) in observed ratings.
"""
def computeError(R,predR):
    
    """Your code to calculate MSE goes here"""
    non_zeros = np.where(R != 0)
    error = np.zeros((R.shape[0], R.shape[1]))
    error[non_zeros] = (R[non_zeros] - predR[non_zeros])**2
    return np.mean(error[non_zeros])


"""
This fucntion takes P (m*k) and Q(k*n) matrices alongwith user bias (U) and item bias (I) and returns predicted rating. 
where m = No of Users, n = No of items
"""
def getPredictedRatings(P,Q,U,I):
    myR = np.matmul(P, Q)
    for i in range(myR.shape[0]):
        myR[i,:] = myR[i,:] + U[i]
    for j in range(myR.shape[1]):
        myR[:,j] = myR[:,j] + I[j]
    return myR
    
    
"""This fucntion runs gradient descent to minimze error in ratings by adjusting P, Q, U and I matrices based on gradients.
   The functions returns a list of (iter,mse) tuple that lists mse in each iteration
"""
def runGradientDescent(R,P,Q,U,I,iterations,alpha):
   
    stats = []
    for iter in range(iterations):

        predicted = getPredictedRatings(P, Q, U, I)
        error = computeError(R, predicted)
        stats.append((iter, error))
        error_matrix = np.zeros((R.shape))
        non_zeros = np.where(R != 0)
        error_matrix[non_zeros] = R[non_zeros] - predicted[non_zeros]
        #error_matrix = np.around(error_matrix, decimals = 10)
        #error_matrix[np.where(error_matrix < 0.00000000000000000001)] = 0
        rows = non_zeros[0]
        cols = non_zeros[1]
        for iter in range(len(rows)):
            cur_row = rows[iter]
            cur_col = cols[iter]
            p_row_copy = P[cur_row,:].copy() #beacuse we are modifying P_row
            P[cur_row,:] = P[cur_row,:] + (alpha * 2 * error_matrix[cur_row, cur_col] * Q[:,cur_col])
            Q[:,cur_col] = Q[:,cur_col] + (alpha * 2 * error_matrix[cur_row, cur_col] * p_row_copy)
            U[cur_row] = U[cur_row] + (alpha * 2 * error_matrix[cur_row, cur_col])
            I[cur_col] = I[cur_col] + (alpha * 2 * error_matrix[cur_row, cur_col])
    """Your gradient descent code goes here"""    

    
    
    """"finally returns (iter,mse) values in a list"""
    return stats
    
""" 
This method applies matrix factorization to predict unobserved values in a rating matrix (R) using gradient descent.
K is number of latent variables and alpha is the learning rate to be used in gradient decent
"""    

def matrixFactorization(R,k,iterations, alpha):

    """Your code to initialize P, Q, U and I matrices goes here. P and Q will be randomly initialized whereas U and I will be initialized as zeros. 
    Be careful about the dimension of these matrices
    """

    P = np.zeros((R.shape[0],k), dtype=np.float64)
    P[:] = np.random.rand(*P.shape)
    Q = np.zeros((k, R.shape[1]), dtype=np.float64)
    Q[:] = np.random.rand(*Q.shape)

    #Q = np.random.rand(k, R.shape[1], dtype=np.float64)
    U = np.zeros(R.shape[0])
    I = np.zeros(R.shape[1])

    #Run gradient descent to minimize error
    stats = runGradientDescent(R,P,Q,U,I,iterations,alpha)
    
    print('P matrx:')
    print(P)
    print('Q matrix:')
    print(Q)
    print("User bias:")
    print(U)
    print("Item bias:")
    print(I)
    print("P x Q:")
    print(getPredictedRatings(P,Q,U,I))
    plotGraph(stats)
       
    
def plotGraph(stats):
    i = [i for i,e in stats]
    e = [e for i,e in stats]
    plt.plot(i,e)
    plt.xlabel("Iterations")
    plt.ylabel("Mean Square Error")
    plt.show()    
    
""""
User Item rating matrix given ratings of 5 users for 6 items.
Note: If you want, you can change the underlying data structure and can work with starndard python lists instead of np arrays
We may test with different matrices with varying dimensions and number of latent factors. Make sure your code works fine in those cases.
"""
R = np.array([
[5, 3, 0, 1, 4, 5],
[1, 0, 2, 0, 0, 0],
[3, 1, 0, 5, 1, 3],
[2, 0, 0, 0, 2, 0],
[0, 1, 5, 2, 0, 0],
])

k = 3
alpha = 0.01
iterations = 500

matrixFactorization(R,k,iterations, alpha)
