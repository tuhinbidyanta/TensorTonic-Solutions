import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x , dtype = float)
    var = np.sum((x-np.mean(x))**2)/(len(x)-1)
    return {"variance": var, "standard_deviation": np.sqrt(var)}
    