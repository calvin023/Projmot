import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define initial conditions
vInitialVelocity = float(input("Enter the initial velocity in m/s: "))
vLaunchAngle = float(input("Enter the launch angle: "))
vInitialHeight = float(input("Enter the initial height: "))
vGravity = 9.81

# Convert launch angle to radians
vLaunchAngle = math.radians(vLaunchAngle)

# Calculating time of flight
vTime = (2 * vInitialVelocity * math.sin(vLaunchAngle)) / vGravity

# Calculate horizontal and vertical components of velocity
vVelocityX = vInitialVelocity * math.cos(vLaunchAngle)
vVelocityY = vInitialVelocity * math.sin(vLaunchAngle)

# Calculate horizontal and vertical components of displacement
vDisplacementX = vVelocityX * vTime
vDisplacementY = vInitialHeight + vVelocityY * vTime - 0.5 * vGravity * vTime**2

# Create arrays for time, horizontal displacement and vertical displacement
vTimeArray = np.linspace(0, vTime, num=100)
vDisplacementXArray = vVelocityX * vTimeArray
vDisplacementYArray = vInitialHeight + vVelocityY * vTimeArray - 0.5 * vGravity * vTimeArray**2

# Plot the trajectory
plt.plot(vDisplacementXArray, vDisplacementYArray)

# Set axis labels and title
plt.xlabel("Horizontal displacement (m)")
plt.ylabel("Vertical displacement (m)")
plt.title("Projectile motion")

# Save file
plt.savefig(r"C:\Users\calvi\Desktop\Programmieren\Python\Physics\Projectile Motion\trajectory.png")