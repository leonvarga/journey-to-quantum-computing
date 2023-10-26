import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler

SIMULATION_RUNS = 10000

def play_chsh_game(strategy):
    x, y = np.random.randint(2), np.random.randint(2)

    # apply strategy
    a, b = strategy(x, y)

    # apply ruleset
    if x & y == 1:
        return a != b
    else:
        return a == b

def classical_strategy(x, y):
    # Alice's answer
    if x == 0:
        a = 0
    elif x == 1:
        a = 1

    # Bob's answer
    if y == 0:
        b = 1
    elif y == 1:
        b = 0

    return a, b


def chsh_circuit(x, y):
    ebit0 = QuantumRegister(1, "A") # Alice ebit part
    ebit1 = QuantumRegister(1, "B") # Bob ebit part

    a = ClassicalRegister(1, "a")
    b = ClassicalRegister(1, "b")

    protocol = QuantumCircuit(ebit0, ebit1, a, b)

    # Create e-bit as phi+
    protocol.h(ebit0)
    protocol.cx(ebit0, ebit1)
    protocol.barrier()

    # Alice's operations
    if x:
        # protocol.ry(-np.pi / 2, ebit0)
        protocol.ry(-np.pi / 2, ebit0)

    # Bob's operations
    if y:
        protocol.ry(np.pi / 4, ebit1)
    else:
        protocol.ry(- np.pi / 4, ebit1)


    protocol.measure(ebit0, a)
    protocol.measure(ebit1, b)

    return protocol



sampler = Sampler()

def quantum_strategy(x, y):
    result = sampler.run(chsh_circuit(x, y), shots=1).result()
    statistics = result.quasi_dists[0].binary_probabilities()
    bits = list(statistics.keys())[0]
    a, b = bits[0], bits[1]
    return a, b

if __name__ == '__main__':
    scores = []
    for i in range(SIMULATION_RUNS):
        scores.append(play_chsh_game(classical_strategy))

    print(f"Win probability for classical approach: {np.mean(scores)}")

    scores = []
    for i in range(SIMULATION_RUNS):
        scores.append(play_chsh_game(quantum_strategy))

    print(f"Win probability for quantum approach: {np.mean(scores)}")





