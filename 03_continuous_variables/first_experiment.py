import strawberryfields as sf
from strawberryfields import ops

prog = sf.Program(1)

with prog.context as q:
    ops.Sgate(0.54) | q[0]
    ops.Sgate(0.54) | q[1]
    ops.Sgate(0.54) | q[2]
    ops.BSgate(0.43, 0.1) | (q[0], q[2])
    ops.BSgate(0.43, 0.1) | (q[1], q[2])
    ops.MeasureFock() | q


prog.print()
eng = sf.Engine('fock', backend_options={'cutoff_dim': 5})
result = eng.run(prog)


print(result)
state = result.state
print(state.trace())
print(state.dm().shape)
print(result.samples)

               

