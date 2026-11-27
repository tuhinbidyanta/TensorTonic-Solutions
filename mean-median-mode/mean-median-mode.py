from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    mean = np.mean(x)
    median = np.nanmedian(x)
    d = Counter(x)
    mode = max(d,key=d.get)

    # modes = values[counts == counts.max()]
    return {"mean":float(mean) , "median":float(median) , "mode":mode}
    # pass