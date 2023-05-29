import numpy as np
import random
from task4 import neighbours
from task4 import count
n = 100
m = 98

N =15
states = [0,N-1]
#e = [i for i in range(1,N-1)]
e = [1,2]
threshold = 1

# this function adds two matices
def add(mat1, mat2, n,m, N):
  c1_c2 = np.empty([n,m], dtype=int)
  for i in range(n):
    for j in range(m):
      c1_c2[i,j] = (mat1[i,j] + mat2[i,j])%N
  return c1_c2

# this function performs GHCA on matrix matr and initial conditions n,m,N,e,threshold.
def GHCA(steps, matr,n,m,N,e,threshold):
  #steps =100
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


      #print(np.array_equal(matr, tmatr))

      matr = tmatr
  return matr

# this for loop checks if F(C1 + C2) = F (C1) + F(C2) and prints True or False respectively.
for i in range(10):
    # c1 - configuration 1
    # c2 - configuration 2
    c1 = np.empty([n,m], dtype=int)
    c2 = np.empty([n,m], dtype=int)

    # populate the two configurations with random values
    for i in range(n):
      for j in range(m):
        c1[i][j] = random.randint(states[0],states[1])
        c2[i][j] = random.randint(states[0], states[1])

    # matrix addtion of c1 and c2
    c1_c2 = add(c1, c2, n,m, N)

    # below is the GHCA of c1+c2 producing F(C1 + C2)
    F_c1_c2 = GHCA(100, c1_c2, n,m, N, e, threshold)

    # F_c1 is F (C1) and F_c2 is F(C2)
    F_c1 = GHCA(100, c1, n,m, N, e, threshold)
    F_c2 = GHCA(100, c2, n,m, N, e, threshold)

    # F_c1andF_c2 = F (C1) + F(C2)
    F_c1andF_c2 = add(F_c1,F_c2, n,m, N)

    # below checks if F(C1 + C2) = F (C1) + F(C2)
    print(np.array_equal(F_c1_c2, F_c1andF_c2))

# output is printed as False showing that GHCA is not additive.


