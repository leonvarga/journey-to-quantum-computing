import numpy as np
import strawberryfields as sf
from strawberryfields import ops

overall_samples = []

for i in range(100):
    prog = sf.Program(1)

    with prog.context as q:
        ops.Vacuum() | q
        ops.Squeezed(2) | q

        ops.MeasureFock() | q


    eng = sf.Engine('fock', backend_options={'cutoff_dim': 6})
    result = eng.run(prog)

    overall_samples.append(result.samples[0][0])

print(np.array(overall_samples))
print(np.array(overall_samples).mean())
