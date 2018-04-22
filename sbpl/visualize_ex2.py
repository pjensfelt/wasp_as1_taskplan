import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Specify the environment parameters for "cubicle-25mm-inflated-env.cfg"

    cellsize = 0.025
    mapsize_x = 436
    mapsize_y = 473

    # Read the map data from the specified file

    f = open(sys.argv[1],'r')
    ll = f.readlines()
    map_str = ll[-mapsize_y:]
    map_str_split = [i.strip().split() for i in map_str]
    map_flat_str = [item for sublist in map_str_split for item in sublist]
    map_flat = [int(i) for i in map_flat_str]
    map_int = np.array(map_flat).reshape(mapsize_y, mapsize_x)
    f.close()

    # Read solution from specified file

    f = open(sys.argv[2],'r')
    ll = f.readlines()
    sol = [i.strip().split(' ') for i in ll]
    sol_x = [float(i[0]) for i in sol]
    sol_y = [float(i[1]) for i in sol]
    sol_theta_raw = [float(i[2]) for i in sol]
    sol_theta = [i-2*np.pi if i > 1.02*np.pi else i for i in sol_theta_raw]
    f.close()

    # Plot the map and the solution

    plt.figure()
    plt.imshow(map_int,extent=[0,mapsize_x*cellsize,
        mapsize_y*cellsize,0])
    plt.plot(sol_x,sol_y,'y-',linewidth=3)
    plt.plot(sol_x[0], sol_y[0], 'ro',linewidth=3)
    plt.plot(sol_x[-1], sol_y[-1], 'ro',linewidth=3)
    plt.ylim([-0.1, mapsize_y*cellsize])
    plt.xlim([-0.1, mapsize_x*cellsize])
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.title('Map and Planned Path from Start to Goal')

    plt.figure()
    plt.subplot(311)
    plt.plot(sol_x,'b-',linewidth=3)
    plt.title('States from Start to Goal')
    plt.ylabel('X [m]')
    plt.grid()
    plt.subplot(312)
    plt.plot(sol_y,'b-',linewidth=3)
    plt.ylabel('Y [m]')
    plt.grid()
    plt.subplot(313)
    plt.plot(sol_theta,'b-',linewidth=3)
    plt.xlabel('Sample')
    plt.ylabel('Theta [rad]')
    plt.grid()

    plt.show()
