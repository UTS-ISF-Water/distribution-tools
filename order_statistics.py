from numpy import array, factorial, percentile
from numpy.random import choice
from scipy.special import comb

def arithmetic_cdf(Fx: array, r: int, n: int)->array:
    '''
    Calculates the CDF of a sample position from a given CDF Fx
    '''

    assert r > 0

    if r == 1:
        return 1 - (1-Fx)**n
    elif r == n:
        return Fx**n
    else:
        cdf = 0 

        for j in range(r, n+1, 1): 
            cdf += comb(n, j) * (Fx**j) * ((1-Fx)**(n-j))
    
        return cdf

def arithmatic_pdf(n: int, r: int, Fx: array, fx: array)->array:
    '''
    Calculates the PDF of a sample position from a given CDF Fx and PDF fx
    '''
    assert r > 0

    return (factorial(n) / (factorial(r - 1) * factorial(n - r))) * fx * Fx**(r-1) * (1-Fx)**(n-r)

def sim_pdf(sample: array, p: float, simulation_size=10**6)->array:
    '''
    Calculates the PDF of a specific percentile of a sample with simulation
    '''

    simulation = []
    for _ in range(simulation_size):
        bootstrap = choice(sample, size=len(sample), replace=True)
        simulation.append(percentile(bootstrap, p*100))
    
    return array(simulation)




