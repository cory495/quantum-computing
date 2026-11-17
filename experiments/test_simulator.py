
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a Bell state
qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

# Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=1024)
result = job.result()

print("Measurement results:")
print(result.get_counts())
