import strawberryfields as sf
from strawberryfields import ops

import numpy as np

np.random.seed(50)


boson_sampling = sf.Program(4)

with boson_sampling.context as q:
    # prepare input
    ops.Fock(1) | q[0]
    ops.Fock(1) | q[1]
    ops.Vac | q[2]
    ops.Fock(1) | q[3]

    # rotation gate
    ops.Rgate(0.5719) | q[0]
    ops.Rgate(-1.9782) | q[1]
    ops.Rgate(2.0603) | q[2]
    ops.Rgate(0.0644) | q[3]

    # beamsplitter array
    ops.BSgate(0.7804, 0.8578)  | (q[0], q[1])
    ops.BSgate(0.06406, 0.5165) | (q[2], q[3])
    ops.BSgate(0.473, 0.1176)   | (q[1], q[2])
    ops.BSgate(0.563, 0.1517)   | (q[0], q[1])
    ops.BSgate(0.1323, 0.9946)  | (q[2], q[3])
    ops.BSgate(0.311, 0.3231)   | (q[1], q[2])
    ops.BSgate(0.4348, 0.0798)  | (q[0], q[1])
    ops.BSgate(0.4368, 0.6157)  | (q[2], q[3])


eng = sf.Engine(backend='gaussian')
# eng = sf.Engine(backend='fock', backend_options={'cutoff_dim': 7})
result = eng.run(boson_sampling)

probs = result.state.all_fock_probs()

print(probs[1, 1, 0, 1])
