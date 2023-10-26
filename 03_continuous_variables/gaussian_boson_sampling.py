import strawberryfields as sf
from strawberryfields import ops
from thewalrus import hafnian as haf

import numpy as np

np.random.seed(50)


boson_sampling = sf.Program(4)

U = np.array([
    [ 0.219546940711-0.256534554457j, 0.611076853957+0.524178937791j,
     -0.102700187435+0.474478834685j,-0.027250232925+0.03729094623j],
    [ 0.451281863394+0.602582912475j, 0.456952590016+0.01230749109j,
     0.131625867435-0.450417744715j, 0.035283194078-0.053244267184j],
    [ 0.038710094355+0.492715562066j,-0.019212744068-0.321842852355j,
     -0.240776471286+0.524432833034j,-0.458388143039+0.329633367819j],
    [-0.156619083736+0.224568570065j, 0.109992223305-0.163750223027j,
     -0.421179844245+0.183644837982j, 0.818769184612+0.068015658737j]
])
r = 1


with boson_sampling.context as q:
    # prepare input
    ops.Squeezed(r) | q[0]
    ops.Squeezed(r) | q[1]
    ops.Squeezed(r) | q[2]
    ops.Squeezed(r) | q[3]

    ops.Interferometer(U) | q



eng = sf.Engine(backend='gaussian')
# eng = sf.Engine(backend='fock', backend_options={'cutoff_dim': 7})
result = eng.run(boson_sampling)
eng.print_applied()


measure_states = [[0,0,0,0], [1,1,0,0], [0,1,0,1], [1,1,1,1], [2,0,0,0]]
for i in measure_states:
    probs = result.state.fock_prob(i)
    print(f"|{''.join([str(j) for j in i])}>: {round(probs, 5)}")


B = (np.dot(U, U.T) * np.tanh(r))


def calc_prob(submatrix, n=1):
    return np.abs(haf(submatrix))**2 / (n*np.cosh(r)**4)

print(calc_prob(B))#[:, [0, 0]][[0, 0]], n=1))
