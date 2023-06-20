import numpy as np
"""
The following method is an implementation of the Jacobi method
A: N x N matrix
b: N x 1 vector 
x: N x 1 vector denoting initial guess
returns: x a Nx1 estimate of solution 
"""
def jacobi(A: np.array,  b: np.array, x:np.array = None) -> np.array:
    if x is None:
        x = np.zeros(len(A[0]))
    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    R = A - np.diagflat(D)
    # tests for convergence via the spectral radius
    if np.amax(np.abs(np.linalg.eigvals(R/D))) > 1:
        print("x")
    # Iterate for N times                                                                                                                                                                          
    while np.linalg.norm(b - np.dot(A,x)) > 1e-5:
        x = (b - np.dot(R,x)) / D
        residual = b - np.dot(A,x) 
        print(f'x: {x} residual: {residual}')
    return x  