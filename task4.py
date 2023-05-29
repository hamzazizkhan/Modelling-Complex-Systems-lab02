import numpy as np
import random
import matplotlib.pyplot as plt
'''
all the lines are the same as task 3. the only lines that are different have comments
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

    if (step+1) % N == 0:
        period_mats.append(matr)
        period_time.append(step+1)

# c_p stores the periodic configurations
c_p = []
for i in range(1,len(period_mats)):
    # the if statement below ensures we ignore configurations of transient orbits
    if np.array_equal(period_mats[i], period_mats[i-1]):
        c_p.append(period_mats[i])

# the code below perturbs the first periodic configuration for a few values.
# the perturbed matrix is stored in perturbed_mat
period_mat =c_p[0]
perturbed_mat = period_mat
for i in range(len(period_mat)):
    for j in range(len(period_mat[i])):
        # the if statement below ensures we
        # change only the first two rows of the periodic configuration
        if i<=1:
            perturbed_mat[i][j] = random.randint(states[0], states[1])

# next we perform GHCA on the perturbed matrix with the same initial conditions
# and number of steps that led to the periodic configuration.
# the same is done for the perturbed matrix as before; store, periodic configurations

# the lists below store the suspected periodic configuration and the respective
# time step.
perturbed_mats_period=[]
perturbed_mat_time=[]

# perform GHCA on the perturbed matrix:
for step in range(steps):
    tmatr = np.empty([n, m], dtype=int)

    for i in range(len(perturbed_mat)):
        for j in range(len(perturbed_mat[i])):
            if 1<= perturbed_mat[i][j] <=N-2:
                tmatr[i][j] = perturbed_mat[i][j] + 1

            elif perturbed_mat[i][j]== N-1:
                tmatr[i][j] = 0

            else:
                cnt = count(neighbours(i, j, perturbed_mat), e)
                if cnt >= threshold:
                    tmatr[i][j] = 1
                else:
                    tmatr[i][j] = 0

    perturbed_mat = tmatr
    # below, we store these configurations where we suspect a period to occur.
    if (step+1) % N == 0:
        #print(step)
        perturbed_mats_period.append(matr)
        perturbed_mat_time.append(step+1)

# c_p_1 stores the periodic configurations for the perturbed matrix.
c_p_1 = []
for i in range(1,len(perturbed_mats_period)):
    # the if statement below ensures we ignore transient orbits
    if np.array_equal(perturbed_mats_period[i], perturbed_mats_period[i-1]):
        c_p_1.append(perturbed_mats_period[i])

# check if the two configurations have the same period.
if np.array_equal(c_p_1[0], c_p[0]):
    print('attracting')
else:
    print('repelling')

# it is repelling, as the periodic configurations are different for the original matrix
# and the perturbed matrix showing that the two orbits do not coincide.





