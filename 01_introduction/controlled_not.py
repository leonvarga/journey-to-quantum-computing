from qiskit.quantum_info import Statevector, Operator
import numpy as np
from numpy import sqrt

if __name__ == '__main__':
    op_not = Operator(
        np.array([
            [0, 1],
            [1, 0]
        ]))

    op_cx = Operator(
        np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]))
    
    state_1 = Statevector.from_label('1')
    print(state_1)
    print(state_1.evolve(op_not))

    state_alpha = state_1 ^ Statevector([1, 1] / sqrt(2))    
    print(f"Magic measured: {state_alpha.measure()[0]}")
    measured = state_alpha.measure()

    print(f"Real measured (state collapsed): {measured[0]}")
    state_alpha = measured[1]
    print(f"CNOT: {state_alpha.evolve(op_cx).measure()[0]}")

    print("== Reinit ==")

    state_alpha = state_1 ^ Statevector([1, 1] / sqrt(2))    
    print(f"Magic measured: {state_alpha.measure()[0]}")
    measured = state_alpha.measure([1])
    print(f"Real measured only rightmost qubit: {measured[0]}")
    state_alpha = measured[1]
    print(f"CNOT: {state_alpha.evolve(op_cx).measure()[0]}")

    print("== Partial measurement of W ==")
    w = Statevector([0, 1, 1, 0, 1, 0, 0, 0] / sqrt(3))
    print(f"Probabilies pre measurement : {w.probabilities()}")
    measured, w = w.measure([2]) 
    print(f"w[2] = {measured}")
    print(f"Probabilies pre measurement : {w.probabilities()}")
