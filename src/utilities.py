
"""
General-purpose utilities for quantum computing experiments.
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit


def create_bell_circuit(measure=True):
    """
    Create a two-qubit Bell state circuit.

    Args:
        measure (bool): Whether to include measurements.

    Returns:
        QuantumCircuit: Bell state circuit.
    """

    qc = QuantumCircuit(2, 2 if measure else 0)

    qc.h(0)
    qc.cx(0, 1)

    if measure:
        qc.measure([0, 1], [0, 1])

    return qc


def calculate_probability(counts):
    """
    Convert measurement counts into probabilities.

    Args:
        counts (dict): Measurement counts from Qiskit.

    Returns:
        dict: Measurement probabilities.
    """

    total_shots = sum(counts.values())

    if total_shots == 0:
        raise ValueError("Measurement counts cannot be empty.")

    return {
        state: count / total_shots
        for state, count in counts.items()
    }


def plot_measurement_counts(counts, title="Quantum Measurement Results"):
    """
    Plot quantum measurement counts.

    Args:
        counts (dict): Measurement counts from Qiskit.
        title (str): Plot title.
    """

    states = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(8, 5))
    plt.bar(states, values)

    plt.xlabel("Measured Quantum State")
    plt.ylabel("Number of Measurements")
    plt.title(title)

    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
