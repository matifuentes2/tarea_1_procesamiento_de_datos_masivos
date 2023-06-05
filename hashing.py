import numpy as np
import random
from tqdm import tqdm
from math import floor
import pickle 
import pickle

def super_min_hash(documento, m):
    n = len(documento)
    h = np.full((m), m*5, float)
    p = np.zeros(m, dtype=int)
    #p = np.zeros(m)
    q = np.full((m), -1)
    b = np.full((m), 0)
    b[m-1] = m
    a = m-1
    iterador = iter(documento)
    for i in range(n):
        documento_i = next(iterador)
        random.seed(documento_i)
        #np.random.seed(documento_i)
        j = 0
        #print(a)
        while j <= a:
            r = random.random()
            #r = fast_hash_to_float(documento_i)
            k = random.randint(j, m-1)	
            #k = int((m-1-j) * random.random()) + j
            if q[j] != i:
                q[j]=i
                p[j]=j
            if q[k] != i:
                q[k]=i
                p[k]=k
            p[[j, k]] = p[[k, j]]
            #print("r", r)
            #print("j", j)
            #print("p[j]", p[j])
            if (r + j) < h[p[j]]:
                j_prima = min(floor(h[p[j]]), m-1)
                h[p[j]] = r+j
                if j < j_prima:
                    b[j_prima] -= 1
                    b[j] += + 1
                    while b[a] == 0:
                        a-=1
            j+=1
    return h


def hash_signature(dictionary, num_hash):
    FH = np.full((num_hash, len(dictionary)), 100, dtype=float)
    for i in tqdm(range(len(dictionary))):
        FH[:, i] = super_min_hash(dictionary[i], num_hash)
    with open(f'fhs/file.obj', 'wb') as filehandler:
        pickle.dump(FH, filehandler)


def hash_signature_pool(tupla):
    # Diseñado para usarse en procesamiento paralelo con ray
    dictionary, num_hash, index = tupla
    iterador = iter(dictionary)
    FH = np.full((num_hash, len(dictionary)), 100, dtype=float)
    for i in range(len(dictionary)):
        indice = next(iterador)
        FH[:, i] = super_min_hash(dictionary[indice], num_hash)
    with open(f'fhs/file{index}.obj', 'wb') as filehandler:
        pickle.dump(FH, filehandler)
    
    
