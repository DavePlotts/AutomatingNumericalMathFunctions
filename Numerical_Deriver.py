#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[113]:


def derivative_plot(func,interval,poly_deg = None):
    h = 0.0001
    x0 = interval[0]
    x1 = interval[1]
    xrange = np.linspace(x0,x1,100)
    dfunc = []
    for i in range(len(xrange)):
        slope = (func(xrange[i]+h)-func(xrange[i]))/h
        dfunc.append(slope)
    dfunc = np.array(dfunc)
    assert dfunc.all() != 0 
    
    ### z = degree of polynomial to fit dfunc
    if poly_deg == None:
        z = 3
    else:
        z = poly_deg
    assert z <=5 and z>1
    
    def polyfit_dfunc(z):
        A = np.zeros((len(xrange),z))
        V = np.array(dfunc).T
        nrows = A.shape[0]
        ncols = A.shape[1]
        for i in range(nrows):
            idx = 1
            for j in range(ncols):
                A[i,j] = xrange[i]**(ncols-idx)
                idx += 1
        lhs= A.T@A
        rhs = A.T@V
        coeffs = np.linalg.solve(lhs,rhs)
        deg = len(coeffs)
        deg = z
        if deg == 2:
            approx_derivative = lambda x: coeffs[0]*x + coeffs[1]
        elif deg == 3:
            approx_derivative = lambda x: coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]
        elif deg == 4:
            approx_derivative = lambda x: coeffs[0]*x**3 + coeffs[1]*x**2 + coeffs[2]*x + coeffs[3]
        elif deg == 5:
            approx_derivative = lambda x: coeffs[0]*x**4 + coeffs[1]*x**3 + coeffs[2]*x**2 + coeffs[3]*x + coeffs[4]
        else:
            return
        return approx_derivative,coeffs
        
    dfdx_func,coeffs = polyfit_dfunc(z)
    
    plt.figure()
    plt.plot(xrange,func(xrange), label = r"f(x)")
    plt.plot(xrange,dfunc, label = r"$\frac{df}{dx}$")
    plt.plot(xrange,np.zeros(len(xrange)),'k')
    plt.axvline(x=0,color = 'k')
    plt.title(r"f(x) vs $\frac{df}{dx}$")
    plt.legend()
    plt.grid()
    plt.show()
    print("Polynomial Coeffcients:\n{}".format(coeffs))
    
    return dfdx_func,coeffs


# In[ ]:




