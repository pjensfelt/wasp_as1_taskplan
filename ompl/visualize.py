import numpy as np
import matplotlib.pyplot as plt

# Read solution from file
sol_file = open('sol.txt','r')
sol_data = sol_file.readlines()
sol = [ll.strip().split(' ') for ll in sol_data]
sol = sol[:-1]
sol_x = [float(i[0]) for i in sol]
sol_y = [float(i[1]) for i in sol]
sol_file.close()

# Define radius and center of circular obstacle
R = 0.25
x_c = 0.5
y_c = 0.5

xx = np.linspace(x_c-R,y_c+R,100)

# Plot obstacle and computed path

plt.figure()
plt.plot(sol_x,sol_y,'b-',linewidth=3)
plt.plot(xx,np.sqrt(R**2-(xx-x_c)**2)+y_c,'r--',linewidth=3)
plt.plot(xx,-np.sqrt(R**2-(xx-x_c)**2)+y_c,'r--',linewidth=3)
plt.plot(sol_x[0],sol_y[0],'go',linewidth=6)
plt.plot(sol_x[-1],sol_y[-1],'go',linewidth=6)

plt.axis('equal')
plt.grid('on')
plt.title('Obstacle and Computed Path with RRT*')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.legend({'Path','Obstacle'},loc='best')
plt.xlim([-0.1, 1.1])
plt.ylim([-0.1, 1.1])
plt.show()
