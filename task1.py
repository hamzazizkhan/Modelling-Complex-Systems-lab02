import numpy as np
import random
import matplotlib.pyplot as plt

'''
From lines 11-23 the initial conditions for GHCA are stored in variables namely:
N 
e - excited states
Threshold - the number of neighbours that need to be excited for the current call to be considered excited.
'''
# initialize hastings with 100x98 matrix size
n = 100
m = 98

matr = np.empty([n,m], dtype=int)


N =15
states = [0,N-1]

# excited states
e = [1,2]
threshold = 1

# time 0 arbitrary values assigned
# randomly generate an initial configuration for GHCA.
for i in range(n):
  for j in range(m):
    matr[i][j] = random.randint(states[0],states[1])

# returns the von-moore neighbours of a cell at i,j for matrix matr
def neighbours(i,j,matr):
    neighbours = []

    if max(i - 1, 0) != i:
        neighbours.append(matr[max(i - 1, 0), j])

    if max(j - 1, 0) != j:
        neighbours.append(matr[i, max(j - 1, 0)])

    if min(i + 1, len(matr) - 1) != i:
        neighbours.append(matr[min(i + 1, len(matr) - 1)][j])

    if min(j + 1, len(matr[i]) - 1) != j:
        neighbours.append(matr[i][min(j + 1, len(matr[i]) - 1)])

    return neighbours

# function counting the number of excited neighbours.
def count(neighbours, excited_cells):
    cnt = 0
    for i in neighbours:
        if i in excited_cells:
            cnt += 1
    return cnt

# GHCA applied 100 times giving 100 configurations
steps =100
for step in range(steps):
    # tmatr is the matrix where the next configuration will be stored
    tmatr = np.empty([n, m], dtype=int)

    # looping through each value in the matr
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if 1<= matr[i][j] <=N-2:
                tmatr[i][j] = matr[i][j] + 1

            elif matr[i][j]== N-1:
                tmatr[i][j] = 0

            else:
                cnt = count(neighbours(i, j, matr), e)
                # if there is at least one excited cell as a neighbour, the value changes to 1.
                if cnt >= threshold:
                    tmatr[i][j] = 1
                else:
                    tmatr[i][j] = 0

    matr = tmatr


# save the final matrix in final_matrice.txt
fin_matr = open('final_matrice.txt','a')
fin_matr.writelines([str(matr[i,j])+' ' if j<m-1  else str(matr[i,j])+'\n' for i in range(len(matr)) for j in range(len(matr[i]))])

fin_matr.close()

# plot the final configuration
plt.imshow(matr, cmap = 'viridis', interpolation='nearest')
plt.title(f" period time {steps}")
plt.show()



