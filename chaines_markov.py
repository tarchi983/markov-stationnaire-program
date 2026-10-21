import numpy as np 

pi = np.array([0.8, 0.1 , 0.1])
P=np.array([[0.1, 0.7 , 0.2] , [0.2 , 0.8 , 0], [0.5 , 0.4 , 0.1]])

# # cas discrete 
# teste que la somme dee ligne est 1 
print("cas discrete")
for i in range (pi.shape[0]):
    if P[i].sum() != 1 : 
        P[i] = P[i] / P[i].sum()

# teste que 0 <= pi <= 0 

test = 0 
for i in range(pi.shape[0]):
    if pi[i] > 1 or pi[i] < 0: 
        print("pi doit compris entre 0 et 1")
        test = 1
        break;

if test==0:
    pi = pi@P
    print(pi)


# cas continue 
print("cas continue")
Q = np.array([[-2,2], [1,-1]])

# calculer qii = -somme(qij), pour j != i 
for i in range(Q.shape[0]):
    Q[i, i] = 0 ; 
    Q[i, i] = -sum(Q[i, j] for j in range(Q.shape[1]) if i != j)

    # resolution du systeme lineare pour trouver la distributiion stationnaire p 
A = Q.T.copy()
A[-1, :] = 1

b= np.zeros(Q.shape[0])
b[-1] = 1

p = np.linalg.solve(A, b)

if p.sum() == 1: 
    print("Q=\n", Q)
    print("p=", p)
    print("pQ = ", p @ Q)
else:
    print("la somme de pi != 1")


