import numpy as np

rho = 1.225
wing_area = 4.2
cl = 0.8

velocity = np.linspace(10, 50, 100)

lift = 0.5 * rho * velocity**2 * wing_area * cl

print(f"Maximum lift: {lift.max():.1f} N")
