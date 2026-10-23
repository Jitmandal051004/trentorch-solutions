import numpy as np


def mse_loss(input: np.ndarray, target: np.ndarray, reduction: str = "mean") -> float | np.ndarray:
    """
    input:     shape matching target, any shape
    target:    shape matching input, any shape
    reduction: 'mean' | 'sum' | 'none'

    Returns:
        a Python float when reduction is 'mean' or 'sum';
        an array shaped like input when reduction is 'none'
    """
    # TODO: Implement mean squared error from Theory.
    # Branch on `reduction` explicitly. Raise ValueError for anything else.
    er = target - input
    sq_er = er**2
    res = 0
    if reduction == "mean":
        res = float(np.mean(sq_er))
    elif reduction == "sum":
        res = float(np.sum(sq_er))
    elif reduction == "none":
        res = sq_er
    else:
        raise ValueError(
            "reduction must be 'mean', 'sum', or 'none'"
        )

    return res
    pass
