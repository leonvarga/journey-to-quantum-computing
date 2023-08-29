import numpy as np

sqrt_2 = np.sqrt(2)

def to_prob(v: np.ndarray):
    f = lambda x: x ** 2
    return np.array(list(map(f, v)))

if __name__ == '__main__':
    ket_0 = np.array([1,0])
    ket_1 = np.array([0,1])

    H = np.array(
        [
            [1/sqrt_2, 1/sqrt_2],
            [1/sqrt_2, -1/sqrt_2]
        ])

    print(ket_0 / 2 + ket_1 / 2)

    chi_0 = np.matmul(H, ket_0)
    chi_1 = np.matmul(H, ket_0)

    print((to_prob(chi_0) == to_prob(chi_1)).all())

