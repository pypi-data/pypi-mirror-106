"""Distribution class

This class initiates the poisson distribution class


"""

import numpy as np
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Poisson(Distribution):
    """ Poisson distribution class for calculating a Poisson distribution.
    
    Attributes:
        lambda or mu (float) representing the mean value of the distribution
        k (float) representing the probability of an event occurring
    
            
    """
    def __init__(self, k, lambd):
        
        
        self.k = k
        self.lambd = lambd
        
   
    def pdf(self):
        """Probability density function calculator for the poisson distribution.
        
        Args:
            k (float): point for calculating the probability density function
            lambda or mu : probability of an event occurring within a given interval.
            
        
        Returns:
            float: probability density function output
        """
        
        
        a = (self.lambd ** self.k * np.exp(-self.lambd))
        b = np.math.factorial(self.k)
        
        return (a / b) 
