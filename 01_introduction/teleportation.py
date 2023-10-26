from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import UGate
import numpy as np

def generate_a_random_gate():
    return UGate(
        theta=np.random.random() * 2 * np.pi,
        phi=np.random.random() * 2 * np.pi,
        lam=np.random.random() * 2 * np.pi
    )


def simulate(circuit: QuantumCircuit):
    from qiskit_aer import AerSimulator
    from qiskit.result import marginal_distribution
    result = AerSimulator().run(circuit).result().get_counts()
    print(result)

    print("Filter by leftmost bit, which should be always 0.")
    print(marginal_distribution(result, [2]))



if __name__ == '__main__':
    print("This script simulates the teleportation of a quibit")

    in_qubit = QuantumRegister(1, "I")
    ebit0 = QuantumRegister(1, "A") # Alice ebit part
    ebit1 = QuantumRegister(1, "B") # Bob ebit part
    print(ebit0[0])

    # classical transportation channel
    a = ClassicalRegister(1, "a")
    b = ClassicalRegister(1, "b")

    protocol = QuantumCircuit(in_qubit, ebit0, ebit1, a, b)

    print("Create e-bit as phi+")
    protocol.h(ebit0)
    protocol.cx(ebit0, ebit1)
    protocol.barrier()

    print("Alice operates")
    protocol.cx(in_qubit, ebit0)
    protocol.h(in_qubit)
    protocol.barrier()

    print("Alice measures:")
    protocol.measure(ebit0, a)
    print(f"ebit[0] = a: {a}")
    protocol.measure(in_qubit, b)
    print(f"in_qubit = b: {b}")
    protocol.barrier()

    print("Bob receives a and b")
    print("Bob applies conditional X and Z gates")
    with protocol.if_test((a, 1)):
        protocol.x(ebit1)
    with protocol.if_test((b, 1)):
        protocol.z(ebit1)

    print(protocol)


    print("Now test this protocol..")
    test = QuantumCircuit(in_qubit, ebit0, ebit1, a, b)
    print("Apply random transformation on in_qubit")
    random_gate = generate_a_random_gate()
    test.append(random_gate, in_qubit)
    test.barrier()

    print("Perform protocol")
    test = test.compose(protocol)
    test.barrier()

    print("Revert random transformation")
    test.append(random_gate.inverse(), ebit1)
    
    result = ClassicalRegister(1, "Result")
    test.add_register(result)
    test.measure(ebit1, result)


    print("Simulate circuit..")
    simulate(test)

