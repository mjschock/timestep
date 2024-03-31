# contents of refraction.py
from __future__ import annotations

import numpy as np


def snell(theta_inc: float, n1: float, n2: float) -> np.ndarray:
    """
    Compute the refraction angle using Snell's Law.

    See https://en.wikipedia.org/wiki/Snell%27s_law

    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1, n2 : float
        The refractive index of medium of origin and destination medium.

    Returns
    -------
    theta : float
        refraction angle

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.

    >>> snell(np.pi/4, 1.00, 1.33)
    0.5605584137424605
    """
    angle: np.float64 = np.arcsin(n1 / n2 * np.sin(theta_inc))

    assert isinstance(angle, np.float64), f"{isinstance(angle, np.float64)} != True"

    return angle
