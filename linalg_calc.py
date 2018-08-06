import numpy as np
from typing import List

def V(vec: List[int]):
    return np.array(vec)

def args_to_numpy(func):
    '''Decorator to convert lists into numpy arrays'''
    def vec(*args):
        return func(*[np.array(x) for x in args])
    return vec

@args_to_numpy
def comp_a(a, b):
    '''Find component of vec b along vec a'''
    return ((a @ b) / (b @ b))

@args_to_numpy
def proj_ab(a, b):
    '''vector projection of vec b along vec a'''
    a = V(a); b = V(b)
    return ((a @ b) / (a @ a)) * a

# Either use breakpoint or use "python -i linalg_calc.py"
# import pdb;pdb.set_trace()