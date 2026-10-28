# Workshop Troubleshooting Guide: Python 3.14+ Environment & AI Setup

This document outlines quick fixes for instructors and workshop helpers when dealing with local operating system quirks, installation failures, or unexpected AI behaviors during the exercises.

---

## 1. Python Version & Dependency Issues

### Symptom: "Python 3.14 not found" or installation fails
* **Why it happens:** This training setup explicitly targets cutting-edge dependencies requiring Python 3.14. Some participants will have older versions (3.10, 3.11, 3.12) as their system default.
* **The Fix:** 
  1. Have them check their version using `python3 --version`.
  2. If they cannot install Python 3.14 on the spot, you can downgrade the `requirements.txt` file as an emergency fallback to match their environment:
     ```text
     matplotlib>=3.7.0
     numpy>=1.24.0,<2.0.0
     pandas>=2.0.0
     pytest>=7.3.0
     pytest-cov>=4.1.0
     scipy>=1.10.0
     ```
  3. Re-run `pip install -r requirements.txt`.

### Symptom: "pip: command not found" or Virtual Environment Activation Fails
* **Windows (PowerShell Execution Policy Restrictions):**
  * *Error:* `Script cannot be loaded because running scripts is disabled on this system.`
  * *The Fix:* Run PowerShell as an Administrator and execute: `Set-ExecutionPolicy RemoteSigned -Scope Process`, then try activating again using `.venv\Scripts\Activate.ps1`.
* **Linux / Ubuntu (Missing venv package):**
  * *Error:* `The virtual environment was not created successfully because ensurepip is not available.`
  * *The Fix:* Run `sudo apt-get install python3-venv` (or the specific versioned package like `python3.14-venv`).

---

## 2. Test Execution & Pathing Failures

### Symptom: `ModuleNotFoundError: No module named 'src'` when running pytest
* **Why it happens:** Python cannot find the root directory package alignment when running individual test files explicitly.
* **The Fix:** Instruct the participant to run `pytest` strictly from the repository's root folder using the explicit python invocation flags:
  ```bash
  python -m pytest
  ```
  This automatically appends the current working directory (`.`) to `sys.path`.

### Symptom: `FileNotFoundError: [Errno 2] No such file or directory: 'data/experimental_spectra.csv'`
* **Why it happens:** The participant either forgot to run the generator script or is execution-nested deep within the `src/` or `tests/` directories.
* **The Fix:** Ensure they step out to the repository root directory (`cd ..`) and run:
  ```bash
  python generate_data.py
  ```

---

## 3. AI Assistant Quirks & Divergence

### Symptom: The AI refuses to create a failing test and fixes the code instead
* **Why it happens:** Many commercial frontier models are over-optimized to "fix everything immediately" in a single response, disregarding the Red-Green-Refactor phase constraints.
* **The Fix:** Have the user re-prompt using a firm behavioral correction block:
  > "Stop. Do not write the implementation code yet. Review my AGENTS.md rules. Your current single task is to write ONLY the failing unit test. Do not touch src/analysis.py."

### Symptom: Local models run out of context and start hallucinating functions
* **Why it happens:** Participants are keeping their entire conversation timeline open inside one single chat window while performing multiple steps.
* **The Fix:** Enforce the "Fresh Session" rule. Have them open a completely new chat thread, paste the prompt template (`03_red_green_refactor.txt`), and pass a manual 2-line handoff note specifying exactly what just happened.

### Symptom: Curve Fitting Divergence / `OptimizeWarning: Covariance of the parameters could not be estimated`
* **Why it happens:** During Track B, if the AI shifts or randomizes the baseline guesses or constraints too much, `scipy.optimize.curve_fit` will throw a runtime warning or exception.
* **The Fix:** Remind the participant that the AI must stick to deterministic data-driven initial guesses derived directly from the loaded dataframe (e.g., setting the initial center guess `p0` to `wavelength[np.argmax(intensity)]` instead of `0.0`).

