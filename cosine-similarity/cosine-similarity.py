import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a , dtype= float)
    b = np.asarray(b,dtype=float)
    c= np.linalg.norm(a) if np.linalg.norm(a) != 0 else 1.0
    d = np.linalg.norm(b) if np.linalg.norm(b) != 0 else 1.0
    return float(np.dot(a,b)/(c*d))
    
    # pass