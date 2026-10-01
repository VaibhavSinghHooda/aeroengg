import numpy as np
import tomllib

from aeroengg.mainlogic import calculate_lift


with open("config.toml", "rb") as f:
    config = tomllib.load(f)


rho = config["rho"]
wing_area = config["wing_area"]
cl = config["cl"]

velocity = np.linspace(
    config["velocity_min"],
    config["velocity_max"],
    config["velocity_points"],
)

lift = calculate_lift(rho, velocity, wing_area, cl)

print(f"Maximum lift: {lift.max():.1f} N")
