import numpy as np

def estimate_pi(num_samples):
    points = np.random.rand(num_samples, 2)
    
    distances = np.sum(points**2, axis=1)
    
    is_inside = distances <= 1
    
    count = np.sum(is_inside)
    
    pi_estimate = 4 * count / num_samples
    
    return pi_estimate