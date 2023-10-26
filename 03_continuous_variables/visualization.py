import strawberryfields as sf
from strawberryfields import ops

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def visualize_state(state, limit=5, mode=0):
    fig = plt.figure()
    X = np.linspace(-limit, limit, 100)
    P = np.linspace(-limit, limit, 100)

    Z = state.wigner(mode, X, P)

    X, P = np.meshgrid(X, P)

    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, P, Z, lw=0.5, rstride=1, cstride=1, cmap='RdYlGn')
    ax.set_xlabel('Position')
    ax.set_ylabel('Momentum')
    #fig.set_size_inches(4.8, 5)
    # ax.set_axis_off()
    plt.show()
    return fig


if __name__ == '__main__':
    prog = sf.Program(1)

    with prog.context as q:
        ops.Vac | q[0]
        ops.Sgate(-1) | q[0]
        ops.Rgate(np.pi/4) | q[0]
        ops.Dgate(0.55) | q[0]
        # ops.Coherent() | q[0]
        #         

    eng = sf.Engine('gaussian')
    eng = sf.Engine('fock', backend_options={'cutoff_dim': 20})
    state = eng.run(prog).state

    visualize_state(state, limit=5)

