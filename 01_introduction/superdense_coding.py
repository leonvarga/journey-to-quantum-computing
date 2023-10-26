from qiskit import QuantumCircuit, QuantumRegister

from qiskit_aer.primitives import Sampler

if __name__ == '__main__':
    print("This script simulates superdense coding (sending two classical bits via a single ebit)")

    byte_to_sent = [0, 1, 0, 1, 0, 1, 0, 1]

    assert len(byte_to_sent) == 8
    
    ebit_a = QuantumRegister(len(byte_to_sent) // 2, "A") # Alice ebit part
    ebit_b = QuantumRegister(len(byte_to_sent) // 2, "B") # Bob ebit part

    protocol = QuantumCircuit(ebit_a, ebit_b)

    print("Create e-bits as phi+")
    for i in range(len(byte_to_sent) // 2):
        protocol.h(ebit_a[i])
        protocol.cx(ebit_a[i], ebit_b[i])
    protocol.barrier()


    print("Alice's operations")
    for i in range(len(byte_to_sent)):
     ebit_pos = i // 2
     if i % 2 == 0 and byte_to_sent[i] == 1:
         protocol.x(ebit_a[ebit_pos])
     if i % 2 == 1 and byte_to_sent[i] == 1:
         protocol.z(ebit_a[ebit_pos])
    protocol.barrier()

    print("Bob's operations")
    for i in range(len(byte_to_sent) // 2):
        protocol.cx(ebit_a[i], ebit_b[i])
        protocol.h(ebit_a[i])
    protocol.barrier()

    protocol.measure_all()
    print(protocol)
 
    
    result = Sampler().run(protocol).result()
    statistics = result.quasi_dists[0].binary_probabilities()
    for out, freq in statistics.items():
        # out = [out[i % len(out) if (i % 2 == 0) else (i + (len(out) // 2)) % len(out)] for i in range(len(out))]
        out = [out[i] for i in (3, 7, 2, 7, 1, 5, 0, 4)]
        print(f"{out} with probabilty {freq}")


