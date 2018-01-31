import numpy as np

def total_energy(lx, ly, T):
        E = 0
        for i in range(lx):
            for j in range(ly):
                
                #impose periodic boundary conditions

                iup = i + 1

                if (i == lx - 1) : iup = 0

                jup = j + 1

                if (j == ly - 1) : jup = 0

                #calculate the energy of the lattice
                E += -T[i,j]*(T[iup][j] + T[i][jup])
        return E

def delE(lx, ly, S, x, y):

        #impose periodic boundary conditions

        iup = x + 1

        if (x == lx - 1): iup = 0

        jup = y + 1

        if (y == ly - 1): jup = 0

        idown = x -1

        if (x == 0): idown = lx - 1

        jdown = y - 1

        if (y == 0): jdown = ly - 1

        #calculate the energy change by performing one flip

        E = 2*S[x,y]*(S[x,jup]+S[x,jdown]+S[iup,y]+S[idown,y])

        return E

def glauber(n, temp, S, x, y):

        #calculate the energy change in performing a flip at the random x,y

        D = delE(n, n, S, x, y)

        #perform the flip if delta E is negative or with some probability 

        rand = np.random.random_sample()
        prob = np.exp(-D/temp)

        if D <= 0:

                S[x, y] = S[x, y]*(-1)

        elif rand<=prob:
        
                S[x, y] = S[x, y]*(-1)

        #return the lattice after we have accepted or declined the flip
        
        return S
