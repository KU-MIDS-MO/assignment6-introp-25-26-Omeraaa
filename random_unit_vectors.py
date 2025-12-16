import numpy as np
from numpy.linalg import norm

def random_unit_vectors(num_vectors, dim):
    matrix = np.random.randn(num_vectors, dim)

    result_list = []
    for vector in matrix:
        vec_len = norm(vector)
        
        unit_vec = vector / vec_len
        
        result_list.append(unit_vec)

    return np.array(result_list)