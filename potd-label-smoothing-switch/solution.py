import numpy as np
from scipy.special import log_softmax

def label_smoothing(logits: np.ndarray, y: int, eps: float) -> tuple[np.ndarray, float]:
    """
    Build the label-smoothed target distribution over C = len(logits)
    classes and compute its cross-entropy loss against logits.

    q[c] = 1 - eps + eps/C for c == y, else eps/C.
    loss = -sum(q * log_softmax(logits)).

    Return (q, loss).
    """
    # TODO: smooth EVERY class by eps/C first, then add the remaining
    # mass (1 - eps) onto the true class y.
    C = len(logits)
    q = np.ones(C)
    
    for c in range(C):
        q[c] = eps/C
        if c == y:
            q[c] += 1 - eps
        
    loss = -sum(q * log_softmax(logits))
    return (q, loss)
