import numpy as np
import random
import matplotlib.pyplot as plt
'''
all the lines are the same as task 1. the only lines that are different have comments
above them that explain the code.
'''
n = 100
m = 98

matr = np.empty([n,m], dtype=int)

N =15
states = [0,N-1]

e = [1,2]
threshold = 1

for i in range(n):
  for j in range(m):
    matr[i][j] = random.randint(states[0],states[1])

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

def count(neighbours, excited_cells):
    cnt = 0
    for i in neighbours:
        if i in excited_cells:
            cnt += 1
    return cnt

# these 2 lists below store the configuration and respective
# time step for every time steps where (step+1) % N==0
period_mats = []
period_time = []

steps =100
for step in range(steps):
    tmatr = np.empty([n, m], dtype=int)

    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if 1<= matr[i][j] <=N-2:
                tmatr[i][j] = matr[i][j] + 1

            elif matr[i][j]== N-1:
                tmatr[i][j] = 0

            else:
                cnt = count(neighbours(i, j, matr), e)
                if cnt >= threshold:
                    tmatr[i][j] = 1
                else:
                    tmatr[i][j] = 0

    matr = tmatr

    # every period suspected to occur when (step+1) % N == 0.
    # below, we store these configurations where we suspect a period to occur.
    if (step+1) % N == 0:
        period_mats.append(matr)
        period_time.append(step+1)

# the for loop below plots the non-transient orbits
for i in range(1,len(period_mats)):
    # the if statement below ensures we ignore transient orbits
    if np.array_equal(period_mats[i], period_mats[i-1]):
        # plot the non-transient orbits
        plt.imshow(period_mats[i-1], cmap='viridis', interpolation='nearest')
        plt.title(f" period time {period_time[i]}")
        plt.show()











      