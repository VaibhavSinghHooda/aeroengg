import numpy as np


def calculate_lift(rho, velocity, wing_area, cl):
    return 0.5 * rho * velocity**2 * wing_area * cl

