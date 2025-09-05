import numpy as np
from Polynomial import Polynomial 
from dataclasses import dataclass
from utils import *

class RationalMap: 
    def __init__(self, P, Q):
        P: Polynomial
        Q: Polynomial

        if not isinstance(P, Polynomial) or not isinstance(Q, Polynomial):
            raise ValueError("P and Q must be instances of Polynomial class")
        
        self.P = P
        self.Q = Q

    def degree(self): 
        return max(self.P.degree(), self.Q.degree())

    def __repr__(self):
        return f"RationalMap(P={self.P}, Q={self.Q})"   

    def __call__(self, z):
        num = self.P(z)
        den = self.Q(z)

        if den == 0:
            raise ZeroDivisionError("Denominator evaluates to zero at this point.")
        
        return num / den
    
    def derivative(self):
        """Compute the derivative of the rational map at point z using the quotient rule."""
        dP = self.P.derivative()
        dQ = self.Q.derivative()

        num = dP * self.Q - self.P * dQ
        den = self.Q * self.Q
        
        return RationalMap(num, den)