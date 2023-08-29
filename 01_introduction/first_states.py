from numpy import sqrt
import numpy as np
from qiskit.quantum_info import Statevector, Operator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

if __name__ == '__main__':
    state_plus = Statevector([1 / sqrt(2), 1 / sqrt(2)])
    state_minus = Statevector([1 / sqrt(2), -1 / sqrt(2)])

    H = Operator(np.array([
        [1 / sqrt(2), 1 / sqrt(2)],
        [1 / sqrt(2), -1 / sqrt(2)]
    ]))

    print(f"Chi_plus {state_plus.draw('text')}")
    print(f"\t is valid: {state_plus.is_valid()}")
    print(f"\t measure (random): {state_plus.measure()[0]}")
    samples = state_plus.sample_counts(100000)
    print(f"\t sample (100000): {samples}")
    # plot_histogram(samples)
    # plt.show()


    print(f"Chi_minus {state_minus.draw('text')}")
    print(f"\t is valid: {state_minus.is_valid()}")
    print(f"\t measure (random): {state_minus.measure()[0]}")
    samples = state_minus.sample_counts(100000)
    print(f"\t sample (100000): {samples}")


    print(f"H(Chi_plus) = {state_plus.evolve(H).sample_counts(1000)}")
    print(f"H(Chi_minus) = {state_minus.evolve(H).sample_counts(1000)}")
