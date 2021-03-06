import numpy as np
import matplotlib.pyplot as plt
from Glauber import glauber
from Glauber import total_energy

#set initial conditions for now
n = 50
temp = 1

vis = True

#randomly assign spins to the lattice
a = [-1, 1]
S = np.random.choice(a, size=(n,n))

#create an array that will be used to randomly pick a lattice site
b = np.arange(n)

#define the number of sweeps that will be run
meas = 1000

#initialise the measurement number
t = 0

#make the plot interactive
plt.ion()


#run over measurements (no. sweeps*how many measurements in a sweep)
for t in xrange(meas*n*n):

        #randomly choose the lattice site
        x=np.random.choice(b)
        y=np.random.choice(b)

        #apply the glauber method which will return the revised lattice
        S = glauber(50, temp, S, x, y)
        
        if vis is True:
                #every 10 sweeps plot the spins
                if t%1000*n*n == 0:
                        X, Y = np.meshgrid(range(n+1), range(n+1))
                        plt.pcolormesh(X, Y, S, cmap=plt.cm.RdBu)
                        plt.draw()
                        plt.clf()

        if t%10*n*n==0:                
                #print the energy as a check 
                print total_energy(n, n, S)
