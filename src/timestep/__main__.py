import numpy as np

from timestep.refraction import snell


def main():
    print(snell(np.pi/4, 1.00, 1.33))

if __name__ == "__main__":
    main()
