import numpy as np 
def calculer_pi(P):

    P = np.array(P, dtype=float)
    n = P.shape[0]

    if not np.allclose(P.sum(axis=1), 1): 
        raise ValueError("Matrice n'est pas stocastique : la somme des des elements des lignes doit etre = 1")

    A = P.T - np.eye(n)   # equivaut => (P^T - I) * pi^T

    A[-1 , :] = 1
    B = np.zeros(n)
    B[-1] = 1 

    pi = np.linalg.solve(A, B)  #it solves the system A.pi = B and give back the pi ( distribution stationaire ) 

    if np.all(pi >=0) and np.all(pi <= 1): 
        return pi 
    else:
        raise ValueError("la solution ne respecte pas les condition de probablite ( pi entre 0 et 1)")


if __name__ == "__main__": 
    P = [[0.7 , 0.2, 0.1], [0.4, 0.5 , 0.1] , [0.2, 0.3, 0.5]]

    pi = calculer_pi(P)

    print("Matrice P : ")
    print(np.array(P))
    print("\n la distribution stable c'est pi : ")
    print(pi)
    print("\n la somme des elements de p est: ")
    print(np.sum(pi))
