import numpy as np
from Polynomial import *
from iterate import *
from RationalMap import *

p = Polynomial([1, 0, -4])  # Represents x^2 - 4
z0 = 0.5
print(f"Polynomial: {p}")
print(f"Degree: {p.degree()}")
print(repr(p))
print(f"Evaluate at x=3: {p(3)}")  # Evaluates
print(f"orbit at x = {z0} for 5 iterations: {orbit(p, z0, 5)}")
print(f"Derivative: {p.derivative()}")
print(f"Evaluate derivative at x=3: {p.derivative()(3)}")

rm = RationalMap(Polynomial([1, 0]), Polynomial([1, -1]))  # Represents R(x) = x / (x - 1)
print(f"\nRational Map: {rm}")
print(f"Degree: {rm.degree()}")
print(repr(rm))
print(f"Evaluate at x=2: {rm(2)}")  # Evaluates
print(f"orbit at x = {z0} for 5 iterations: {orbit(rm, z0, 5)}")
print(f"Derivative: {rm.derivative()}")
print(f"Evaluate derivative at x=2: {rm.derivative()(2)}")
print(f"Numerical derivative at x=2: {deriv_numeric(rm, 2)}")