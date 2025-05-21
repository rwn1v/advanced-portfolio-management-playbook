import numpy as np

def compute_signal_to_risk_weights(alpha, vol):
    return alpha / vol

def normalize(weights):
    return weights / np.sum(np.abs(weights))
