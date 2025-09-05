import numpy as np
from dataclasses import dataclass


def orbit(f, z0, n): 
    """Generates the orbit of a point z0 under the function f for n iterations."""
    orbit_list = [z0]
    z = z0
    for _ in range(n):
        z = f(z)
        orbit_list.append(z)
    return np.array(orbit_list)