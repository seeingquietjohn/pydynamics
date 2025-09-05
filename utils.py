import numpy as np

def deriv_numeric(f, x, h=1e-10):
    """Numerically approximate the derivative of f at x using central difference."""
    return (f(x + h) - f(x - h)) / (2 * h)

def eval(f, x): 
    return f(x)