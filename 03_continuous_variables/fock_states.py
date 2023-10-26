import numpy as np
import strawberryfields as sf
from strawberryfields import ops

overall_samples = []

for i in range(10000):
    prog = sf.Program(2)

    with prog.context as q:
        ops.Fock(1) | q[0]
        ops.Vacuum() | q[1]

        ops.S2gate(0) | (q[0], q[1])

        # ops.BSgate(np.pi / 4) | (q[0], q[1])

        ops.MeasureFock() | q[0]
        ops.MeasureFock() | q[1]

    eng = sf.Engine('fock', backend_options={'cutoff_dim': 6})
    result = eng.run(prog)

    overall_samples.append(result.samples)
    if abs(result.state.trace() - 1.0) > 0.1:
        print("Trace critical")

overall_samples = np.stack(overall_samples)

print(np.mean(overall_samples, axis=0))

overall_samples = []

for i in range(100):
    prog = sf.Program(1)

    with prog.context as q:
        ops.Vacuum() | q[0]

        ops.MeasureX | q[0]

    eng = sf.Engine('fock', backend_options={'cutoff_dim': 6})
    result = eng.run(prog)

    overall_samples.append(result.samples)
    if abs(result.state.trace() - 1.0) > 0.1:
        print("Trace critical")

overall_samples = np.stack(overall_samples)

print(overall_samples)
print(np.mean(overall_samples, axis=0))

