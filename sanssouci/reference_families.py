import numpy as np


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# REFERENCE FAMILIES
# R source code: https://github.com/pneuvial/sanssouci/
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def t_inv_linear(p0):
    """


    Parameters
    ----------

    p0 : array-like of shape (B, p)
        A numpy array of size [B,p] of null p-values obtained from
        B permutations for p hypotheses.

    Returns
    -------

    array-like of shape (B, p) :
        numpy array with the same size of p0

    Notes
    -----

    Warning: In case the last command does not work, you can use alternatively:

    out=pval0_sorted_all*1.
    for i in range(pval0_sorted_all.shape[0]):
      out[i,:]=pval0_sorted_all[i,:]/normalized_ranks[:]
    return out
    """

    p = p0.shape[1]

    normalized_ranks = (np.arange(p) + 1) / float(p)

    return p0 / normalized_ranks


def t_linear(alpha, k, m):
    """

    Parameters
    ----------

    alpha : int
    k : int
    m : int

    Returns
    -------

    int

    """
    return alpha * k / (m * 1.0)
