import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class Orbit: 
    points: np.ndarray
    

def orbit(f, z0, n): 
    orbit_list = [z0]
    z = z0
    for _ in range(n):
        z = f(z)
        orbit_list.append(z)
    return np.array(orbit_list)

def escape_radius(f:Polynomial) -> float:
    """Calculates an escape radius for the polynomial f 1+(max|a_i|/|a_d|) where a_d is the leading coefficient."""
    coeffs = f.coefficients
    d = len(coeffs) - 1
    if d == 0:
        return float('inf')  # Constant function, no escape radius
    leading_coeff = coeffs[-1]
    if leading_coeff == 0:
        raise ValueError("Leading coefficient cannot be zero.")
    max_other_coeff = max(abs(c) for c in coeffs[:-1])
    R = 1 + (max_other_coeff / abs(leading_coeff))

    return R

