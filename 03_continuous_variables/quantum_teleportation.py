import strawberryfields as sf
from strawberryfields import ops

import numpy as np
from matplotlib import pyplot as plt


np.random.seed(42)

prog = sf.Program(3)


alpha = 1+0.5j
r = np.abs(alpha)
phi = np.angle(alpha)

with prog.context as q:
    # prepare init state
    ops.Coherent(r, phi) | q[0]
    ops.Squeezed(-2) | q[1]
    ops.Squeezed(2) | q[2]

    # apply gates
    BS = ops.BSgate(np.pi / 4, np.pi)
    BS | (q[1], q[2])
    BS | (q[0], q[1])

    # perform homodyne measurements
    ops.MeasureX | q[0]
    ops.MeasureP | q[1]

    # displacement gate conditioned on 
    # the transported information
    ops.Xgate(np.sqrt(2) * q[0].par) | q[2]
    ops.Zgate(-np.sqrt(2) * q[1].par) | q[2]

eng = sf.Engine('fock', backend_options={
    'cutoff_dim': 15
})

result = eng.run(prog, shots=1, modes=None, compile_options={})
print(result.state)
print(result.samples)

# rho2 = np.einsum('kkllij->ij', result.state.dm())
# probs = np.real_if_close(np.diagonal(rho2))
# print(probs)

fock_probs = result.state.all_fock_probs()
plt.bar(range(7), np.sum(fock_probs, axis=(0, 1))[:7])
plt.xlabel('Fock state')
plt.ylabel('Marginal probability')
plt.title('Mode 2')
plt.show()

