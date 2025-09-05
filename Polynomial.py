import numpy as np
from dataclasses import dataclass
from utils import *

@dataclass(frozen=True)
class Polynomial : 

    coeffs: np.ndarray # Coefficients of the polynomial in descending order 

    def __init__(self, coeffs):
        c = np.asarray(coeffs, dtype=np.complex128).astype(np.complex128, copy=False)
        object.__setattr__(self, 'coeffs', c)

    def degree(self) -> int:
        return len(self.coeffs) - 1
    
    def __repr__(self):
        return f"Polynomial({self.coeffs})"
    
    def __call__(self, x: float) -> float:
        res = 0
        for c in self.coeffs:
            res = res * x + c
        return res 
    
    def derivative(self): 
        df = [self.coeffs[i] * (self.degree() - i) for i in range(self.degree())]
        return Polynomial(df)
    
    # polynomial algebra oprerations 
    def add_constant(self, c): 
        new = self.coeffs.copy()
        new[-1] += complex(c)

        return Polynomial(new)
    
    def multiply_by_constant(self, c):
        new = self.coeffs * complex (c)

        return Polynomial(new)
    
    def __add__(self, g):
        if not isinstance(g, Polynomial):
            raise ValueError("Can only add Polynomial to Polynomial")
        else: 
            A, B = self.coeffs, g.coeffs
            if len(A) < len(B):
                A = np.pad(A, (len(B) - len(A), 0), 'constant')
            elif len(B) < len(A):
                B = np.pad(B, (len(A) - len(B), 0), 'constant')

            new_coeffs = A + B
        
        return Polynomial(new_coeffs)
    
    def __sub__(self, g):
        if not isinstance(g, Polynomial):
            raise ValueError("Can only add Polynomial to Polynomial")
        else: 
            A, B = self.coeffs, g.coeffs
            if len(A) < len(B):
                A = np.pad(A, (len(B) - len(A), 0), 'constant')
            elif len(B) < len(A):
                B = np.pad(B, (len(A) - len(B), 0), 'constant')

            new_coeffs = A - B
        
        return Polynomial(new_coeffs)
    
    def __mul__(self, g):
        if not isinstance(g, Polynomial):
            raise ValueError("Can only multiply Polynomial to Polynomial")
        else: 
            new_coeffs = np.convolve(self.coeffs, g.coeffs)
        
        return Polynomial(new_coeffs)
    
    def compose(self, g):
        if not isinstance(g, Polynomial):
            raise ValueError("Can only compose Polynomial with Polynomial")
        
        res = Polynomial([0])
        for c in self.coeffs:
            res = res * g + Polynomial([c])
        
        return res
    
    def affine_conjugate(self, a, b): 
        """Returns the polynomial P_conj = a*P((z-b)/a) + b or equivalently P_conj = A^-1 o f o A where A(z) = a*z + b."""
        if a == 0:
            raise ValueError("a must be non-zero for affine conjugation.")
        
        P_shifted = self.compose(Polynomial([1/a, -b/a]))
        P_conj = P_shifted.add_constant(b).multiply_by_constant(a)
        
        return P_conj



    
