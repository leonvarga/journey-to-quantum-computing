import strawberryfields as sf
from strawberryfields import ops
import numpy as np


from visualization import visualize_state

if __name__ == '__main__':
    prog = sf.Program(2)

    with prog.context as q:
        ops.Vac | q[0]
        ops.Vac | q[1]

        # ops.Sgate(1) | q[0]
        # ops.Sgate(-1) | q[1]
        ops.Dgate(0.55) | q[0]
        ops.Dgate(-0.55) | q[1]

        ops.Rgate(np.pi/4) | q[0]

        ops.BSgate() | (q[0], q[1])

    eng = sf.Engine('fock', backend_options={'cutoff_dim': 20})
    state = eng.run(prog).state
    print(state)

    visualize_state(state, limit=5, mode=1)

