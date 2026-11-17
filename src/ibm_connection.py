import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService

# Load credentials from project .env
load_dotenv()

# Retrieve API key
token = os.getenv("IBM_QUANTUM_TOKEN")

if not token:
    raise ValueError("IBM Quantum API key not found. Check your .env file.")

# Initialize IBM Quantum service
service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=token
)

print("Successfully connected to IBM Quantum!")

# List available quantum computers
backends = service.backends()

for backend in backends:
    print(backend.name)
