import numpy as np

def get_random_subset_of_naturals_simple():
    all_numbers = np.arange(1, 21)

    decisions = np.random.rand(20) < 0.5 

    final = all_numbers[decisions]

    return final