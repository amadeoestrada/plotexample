# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plot the results
import matplotlib.pyplot as plt
import numpy as np

#--------- Save result using np parameters files
#    filename = "xpoints.txt"
#    np.savetxt(filename, x_points, delimiter=',')
#    filename = "ypoints.txt"
#    np.savetxt(filename, y_points, delimiter=',')
#    filename = "zpoints.txt"
#    np.savetxt(filename, z_points, delimiter=',')

# Extract the information using np parameters file:
filename = "xpoints.txt"
x_points = np.loadtxt(filename, dtype='float', delimiter=',')
filename = "ypoints.txt"
y_points = np.loadtxt(filename, dtype='float', delimiter=',')
filename = "zpoints.txt"
z_points = np.loadtxt(filename, dtype='float', delimiter=',')

# plot the 3d hand
ax = plt.axes(projection='3d')
ax.scatter3D(0, 0, 0, c='m', marker='P')
# draw palm line 1
zline = np.linspace(z_points[0], z_points[1], num=100)
yline = np.linspace(y_points[0], y_points[1], num=100)
xline = np.linspace(x_points[0], x_points[1], num=100)
ax.plot3D(xline, yline, zline, 'gray')
# draw palm line 2
zline = np.linspace(z_points[1], z_points[2], num=100)
yline = np.linspace(y_points[1], y_points[2], num=100)
xline = np.linspace(x_points[1], x_points[2], num=100)
ax.plot3D(xline, yline, zline, 'gray')
# draw palm line 3
zline = np.linspace(z_points[2], z_points[3], num=100)
yline = np.linspace(y_points[2], y_points[3], num=100)
xline = np.linspace(x_points[2], x_points[3], num=100)
ax.plot3D(xline, yline, zline, 'gray')
# draw palm line 4
zline = np.linspace(z_points[3], z_points[0], num=100)
yline = np.linspace(y_points[3], y_points[0], num=100)
xline = np.linspace(x_points[3], x_points[0], num=100)
ax.plot3D(xline, yline, zline, 'red')
# draw palm line 5
zline = np.linspace(z_points[7], z_points[14], num=100)
yline = np.linspace(y_points[7], y_points[14], num=100)
xline = np.linspace(x_points[7], x_points[14], num=100)
ax.plot3D(xline, yline, zline, 'red')
# draw palm line 6
zline = np.linspace(z_points[14], z_points[15], num=100)
yline = np.linspace(y_points[14], y_points[15], num=100)
xline = np.linspace(x_points[14], x_points[15], num=100)
ax.plot3D(xline, yline, zline, 'red')
# draw palm line 7
zline = np.linspace(z_points[15], z_points[19], num=100)
yline = np.linspace(y_points[15], y_points[19], num=100)
xline = np.linspace(x_points[15], x_points[19], num=100)
ax.plot3D(xline, yline, zline, 'red')

# draw palm line 8
zline = np.linspace(z_points[3], z_points[23], num=100)
yline = np.linspace(y_points[3], y_points[23], num=100)
xline = np.linspace(x_points[3], x_points[23], num=100)
ax.plot3D(xline, yline, zline, 'red')
# draw palm line 9
zline = np.linspace(z_points[0], z_points[19], num=100)
yline = np.linspace(y_points[0], y_points[19], num=100)
xline = np.linspace(x_points[0], x_points[19], num=100)
ax.plot3D(xline, yline, zline, 'red')
# draw palm line 8
zline = np.linspace(z_points[7], z_points[23], num=100)
yline = np.linspace(y_points[7], y_points[23], num=100)
xline = np.linspace(x_points[7], x_points[23], num=100)
ax.plot3D(xline, yline, zline, 'red')

# draw thumb line 1
zline = np.linspace(z_points[23], z_points[4], num=100)
yline = np.linspace(y_points[23], y_points[4], num=100)
xline = np.linspace(x_points[23], x_points[4], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw thumb line 1
zline = np.linspace(z_points[4], z_points[5], num=100)
yline = np.linspace(y_points[4], y_points[5], num=100)
xline = np.linspace(x_points[4], x_points[5], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw thumb line 2
zline = np.linspace(z_points[5], z_points[6], num=100)
yline = np.linspace(y_points[5], y_points[6], num=100)
xline = np.linspace(x_points[5], x_points[6], num=100)
ax.plot3D(xline, yline, zline, 'blue')

# draw index line 1
zline = np.linspace(z_points[7], z_points[8], num=100)
yline = np.linspace(y_points[7], y_points[8], num=100)
xline = np.linspace(x_points[7], x_points[8], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw index line 2
zline = np.linspace(z_points[8], z_points[9], num=100)
yline = np.linspace(y_points[8], y_points[9], num=100)
xline = np.linspace(x_points[8], x_points[9], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw index line 3
zline = np.linspace(z_points[9], z_points[10], num=100)
yline = np.linspace(y_points[9], y_points[10], num=100)
xline = np.linspace(x_points[9], x_points[10], num=100)
ax.plot3D(xline, yline, zline, 'blue')

# draw middle line 1
zline = np.linspace(z_points[11], z_points[12], num=100)
yline = np.linspace(y_points[11], y_points[12], num=100)
xline = np.linspace(x_points[11], x_points[12], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw middle line 2
zline = np.linspace(z_points[12], z_points[13], num=100)
yline = np.linspace(y_points[12], y_points[13], num=100)
xline = np.linspace(x_points[12], x_points[13], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw middle line 3
zline = np.linspace(z_points[13], z_points[14], num=100)
yline = np.linspace(y_points[13], y_points[14], num=100)
xline = np.linspace(x_points[13], x_points[14], num=100)
ax.plot3D(xline, yline, zline, 'blue')

# draw ring line 1
zline = np.linspace(z_points[15], z_points[16], num=100)
yline = np.linspace(y_points[15], y_points[16], num=100)
xline = np.linspace(x_points[15], x_points[16], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw ring line 2
zline = np.linspace(z_points[16], z_points[17], num=100)
yline = np.linspace(y_points[16], y_points[17], num=100)
xline = np.linspace(x_points[16], x_points[17], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw ring line 3
zline = np.linspace(z_points[17], z_points[18], num=100)
yline = np.linspace(y_points[17], y_points[18], num=100)
xline = np.linspace(x_points[17], x_points[18], num=100)
ax.plot3D(xline, yline, zline, 'blue')

# draw pinkie line 1
zline = np.linspace(z_points[19], z_points[20], num=100)
yline = np.linspace(y_points[19], y_points[20], num=100)
xline = np.linspace(x_points[19], x_points[20], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw pinkie line 2
zline = np.linspace(z_points[20], z_points[21], num=100)
yline = np.linspace(y_points[20], y_points[21], num=100)
xline = np.linspace(x_points[20], x_points[21], num=100)
ax.plot3D(xline, yline, zline, 'blue')
# draw pinkie line 3
zline = np.linspace(z_points[21], z_points[22], num=100)
yline = np.linspace(y_points[21], y_points[22], num=100)
xline = np.linspace(x_points[21], x_points[22], num=100)
ax.plot3D(xline, yline, zline, 'blue')

# -- Set the Position Relative to Camera 3D Plot
plt.suptitle('Position is Relative to Camera')
# -- Display the origin as a pink cross
ax.scatter3D(x_points, y_points, z_points, c='b', marker='P')
plt.show()