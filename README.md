# Workshop Manual: Effective AI Collaboration for Scientific Software

This repository is a pedagogical aid, designed for university researchers. Through this hands-on workshop, you will learn how to shift from using AI as a simple autocomplete tool to treating it as a structured, deterministic engineering co-pilot.

---

## The Scenario

**Meet Phil.** Phil is a postdoc managing a complex, shared experimental spectroscopy setup. His experiment outputs massive quantities of data. Phil needs to clean this data, isolate physical signal peaks from shifting background noise, fit the cleaned data to mathematical models, and plot the final curves in a format clean enough for publication. 

Phil’s pipeline works fine under pristine laboratory conditions, but it is fragile, lacks deep testing, and breaks when confronted with real-world experimental noise or data anomalies.

Your mission is to help Phil refactor, stabilize, and extend this codebase using AI assistants, without violating core physical constraints or breaking existing features.

---

## Prerequisites & Installation

Before running the exercises, ensure your local environment is configured:

1. Clone or extract this repository to your local machine.
2. Initialize your virtual environment and install dependencies:
   ```bash
   python --version  # This workshop has been tested with Python 3.12 and 3.14
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```
3. Verify the baseline test suite passes:
   ```bash
   python -m pytest
   ```

The dataset `data/experimental_spectra.csv` has already been generated for you using the script in `workshop_preparation`.

---

## Workshop Warm-Up (Both Tracks)
**Goal:** Build a mental model of the codebase before writing a single line of code.

1. Open your AI Assistant interface.
2. Ask your AI Assistant to analyse `src/analysis.py` and provide a structured overview.
3. Check the AI's explanation against the source files. Did it correctly identify how data flows from file storage to the plotting module? Did it notice any architectural flaws?
4. Now read, copy and paste the text from `prompts/01_zoom_out.txt` into the prompt window. What do you observe?

---

## Track A: Intermediate Track (Testing & Bug Remediation)
**Goal:** Use AI to uncover structural edge cases, write automated regression tests, and fix silent data-corruption bugs.

### Step 1: Discover Missing Tests
* Open `src/analysis.py` and inspect `load_and_clean_data`. Notice that it naively assumes all rows are clean numbers.
* Open `prompts/04_diagnose.txt`. Copy its structure to ask the assistant to evaluate why passing the real `data/experimental_spectra.csv` into `load_and_clean_data` causes a downstream crash.

### Step 2: Write the Regression Test
* Instruct the assistant to generate a new test function named `test_load_and_clean_with_real_anomalies` inside `tests/test_analysis.py`.
* **Constraint:** Remember the core philosophy in `AGENTS.md`: *Never edit tests to make them pass.* The test must reflect proper data integrity expectations (i.e., data columns must end up purely numeric, and corrupted text rows must be stripped out).
* Run `pytest`. You should see your new test **Fail** (Red phase).

### Step 3: Repair the Logic
* Feed the traceback error and the code back to the AI using the `04_diagnose.txt` template format.
* Apply the AI’s suggested fix to `src/analysis.py` (e.g., using `pd.to_numeric(..., errors='coerce')`).
* Run `pytest` again. Verify everything turns **Green**.

---

## Track B: Advanced Track (Test-Driven Feature Extension)
**Goal:** Implement a brand-new analysis option using a strict Red-Green-Refactor loop. You will practice managing the AI's context budget by starting fresh sessions and passing brief handoff notes.

### Step 1: Let the Agent Grill You
* You want to add a feature: **Clipping negative intensity values to 0.0 inside `baseline_subtraction`**, because negative light intensity is physically impossible.
* Copy the text from `prompts/02_grill_me.txt` into a **fresh** AI session.
* Answer the AI’s 3 to 5 questions regarding your design criteria (e.g., how to handle float accuracies, whether to log clipped values, etc.).
* Have the AI output a precise **3-to-5 line specification** for this physical constraint feature.

### Step 2: The Red Phase
* Start a **fresh** AI session. Copy the text from `prompts/03_red_green_refactor.txt`.
* Set your Phase to **RED** and paste your new specification in the handoff block.
* The AI will generate a test asserting that input values dropping below the background reference are clipped cleanly to `0.0`.
* Add this code to `tests/test_analysis.py` and run `pytest`. Ensure it fails.

### Step 3: The Green Phase
* Start a **fresh** AI session. Use the `03_red_green_refactor.txt` prompt format.
* Set your Phase to **GREEN** and paste a handoff note showing the failing test output.
* Have the AI modify `baseline_subtraction` in `src/analysis.py` to make the test pass.
* Run `pytest` to confirm the entire suite is green.

### Step 4: The Refactor Phase
* Use the final phase of the template to clean up the code. Have the AI verify that the implementation adheres to the styling, type hints, and documentation criteria outlined in `AGENTS.md`.

---

## Key Takeaways for Participants
* **AI as an Executant, You as the Architect:** The AI writes clean loops and test wrappers, but you must define the mathematical boundaries and physical invariants.
* **Context Budgeting:** Large chat histories make AI models lazy and inaccurate. Breaking tasks into small, structured handoff intervals keeps local and open models highly sharp and predictable.

