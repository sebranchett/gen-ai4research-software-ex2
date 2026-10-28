# AI Engineering Guidelines & Operational Manual

Welcome to the repository. This project serves as a pedagogical sandbox for university lecturers to learn how to guide AI models effectively through scientific software development tasks. 

Our context follows Phil, a postdoc managing an experimental pipeline. Your role is to co-pilot Phil's code updates using AI.

---

## 1. Core Philosophy

### Never Edit Tests to Make Them Pass
Tests represent your physical and mathematical invariants. If a test fails after a code modification, either:
1. The implementation code has a bug (most common).
2. The test was written with incorrect theoretical assumptions.
You must never relax, modify, or delete a test simply because an AI agent struggles to make the implementation code pass.

### Small Context, High Precision
Local and commercial AI models suffer from context drift and attention degradation. Keep your sessions modular. When passing tasks between tracks or features, use concise handoff notes rather than copying whole chat histories.

---

## 2. Coding Conventions

To maintain readability and structural integrity across automated edits, all code in this repository must strictly adhere to the following rules:

* **Type Hinting:** All function signatures must include explicit type hints for arguments and return values (e.g., `def fit_data(x: np.ndarray) -> GeometricResults:`).
* **Docstrings:** Use NumPy-style docstrings detailing Parameters, Returns, and explicitly stated mathematical assumptions.
* **Deterministic Seeding:** Any function utilizing stochastic elements or optimization initialization guesses (e.g., `scipy.optimize`) must accept a seed or handle bounds deterministically.
* **Dependency Isolation:** Keep data input/output (I/O) completely separate from numerical transformation and fitting pipelines.

---

## 3. How to Run the Environment

### Setup the Environment
Ensure you have Python 3.10+ installed. Populate your virtual environment and dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Test Suite
We use `pytest` for validation. Run the following commands from the root directory:

* Run all tests:
  ```bash
  pytest
  ```
* Run with print statements enabled (verbose):
  ```bash
  pytest -v -s
  ```
* Check code coverage to identify untested branches:
  ```bash
  pytest --cov=src tests/
  ```
