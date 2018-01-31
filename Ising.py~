import numpy as np
import matplotlib.pyplot as plt

#function to calculate energy of an array of spins
def total_energy(lx, ly, T):
        E = 0
        for i in range(lx):
            for j in range(ly):

                iup = i + 1

                if (i == lx - 1) : iup = 0

                jup = j + 1

                if (j == ly - 1) : jup = 0

                E += -T[i,j]*(T[iup][j] + T[i][jup])
        return E

def energy_nn(lx, ly, S, x, y):        
        iup = x + 1
        if (x == lx - 1): iup = 0
        jup = y + 1
        if (y == ly - 1): jup = 0
        idown = x -1
        if (x == 0): idown = lx - 1
        jdown = y - 1 
        if (y == 0): jdown = ly - 1
       
        E = 2*S[x,y]*(S[x,jup]+S[x,jdown]+S[iup,y]+S[idown,y])
        return E

#method to decide whether to keep the spin flip whether glauber or kawisake used
def metro(S, x, y, D, temp):
        rand = np.random.random_sample()
        prob = np.exp(-D/temp)
        if D <= 0 or rand<=prob: 
                S[x, y] = S[x, y]*(-1)
                return S
        else:
                return S
def glauber(n, temp):
        a = [1,-1]
        S = np.random.choice(a,size = (n,n))
        b = np.arange(n)
        meas = 1000
        t = 0
        plt.ion()
        for t in xrange(meas*n*n):
                x=np.random.choice(b)
                y=np.random.choice(b)
                energy = energy_nn(n, n, S, x, y) 
                S = metro(S, x, y, energy, temp)
                print total_energy(n, n, S)
        #        if t%n*n == 0:            
         #               X, Y = np.meshgrid(range(n), range(n))
          #              plt.pcolormesh(X, Y, S, cmap=plt.cm.RdBu)
           #             plt.draw()
            #            print total_energy(n, n, S)
        return S
#ask user what dynamics to use
nb = input("Enter 1 for Glauber, 2 for Kawasaki: ")


while (nb != 1 and nb != 2 and nb != 3):
    nb = input("Please enter either 1 for Glauber or 2 for Kawasaki: ")

if (nb == 3) :
    n = 50 
    temp = 1
    g = glauber(50, temp)

#glauber 
if (nb == 1):
    n = input("Please enter the size of nxn array you would like to use: ")    
    while (n <=1) :
            n = input("You must enter a number larger than 1 as the size of the nxn array. n = ") 
    a = [1, -1] 
    S = np.random.choice(a, size =(n,n))
    temp = input("Please enter the temperature (K) you would like to use: ")
    while (temp < 0) :
            temp = input ("You must enter a positive temperature. temp = ")
    #pick a random spin
    b = np.arange(n)
    meas = 1000
    t = 0
    plt.ion()
    for t in xrange(meas*n*n):
            x=np.random.choice(b)
            y=np.random.choice(b)
            energy = energy_nn(n, n, S, x, y) 
            S = metro(S, x, y, energy, temp)
            if t%n*n == 0:            
                    X, Y = np.meshgrid(range(n), range(n))
                    plt.pcolormesh(X, Y, S, cmap=plt.cm.RdBu)
                    plt.draw()
                    print total_energy(n, n, S)
#kawasaki
if(nb=="2") :
    n = input("Please enter the size of nxn array you would like to use: ")
    while (n <=1) :
            nString = input("You must enter a number larger than 1 as the size of the nxn array. n = ") 
    a = [1, -1]
    S = np.random.choice(a, size =(n,n))
    T = S.copy()
    temp = input("Please enter the temperature (K) you would like to use: ")
    while (temp < 0) :
            temp = input ("You must enter a positive temperature. temp = ")
    b = np.arange(n)
    print S

    #calculate energy before
    e1 = energy(n, n, S)
    print e1
    
    #choose two random spins
    x = np.random.choice(b)
    y = np.random.choice(b)
    u = np.random.choice(b)
    v = np.random.choice(b)

    print [x,y]
    print [u,v]

    if ( T[x,y] + T[u,v] == 0 ) : 
        T[x,y] = T[x,y]*(-1)
        T[u,v] = T[u,v]*(-1)
    print T    
    e2 = energy(n,n, S)
    print e2    
    D = after(n, n, S, T, temp)
    print D
