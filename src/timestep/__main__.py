from __future__ import annotations

import numpy as np

from timestep.refraction import snell


def main() -> None:
    assert (
        snell(np.pi / 4, 1.00, 1.33) == 0.5605584137424605
    ), f"{snell(np.pi / 4, 1.00, 1.33)} != 0.5605584137424605"


if __name__ == "__main__":
    main()
