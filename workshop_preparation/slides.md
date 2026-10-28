---
marp: true
theme: default

_class: lead
paginate: true
---

# Slide 1: Title Slide
## Teaching AI Literacy for Scientific Software
### Empowering Researchers with Structured AI Engineering Workflows
**Presenters:** Luis Laguarda Sanchez and Susan Branchett, TU Delft 
**Target Audience:** University Researchers

---

# Slide 2: The Core Problem
## Moving Beyond the "Autocomplete" Trap
* **The Reality:** Most researchers use AI as an isolated, ad-hoc chat box to fix single broken lines of code.
* **The Risk:** This leads to silent data corruption, unmaintainable technical debt, and hallucinated mathematical logic.
* **The Solution:** Treat the AI as an eager, highly competent, but completely literal junior engineer who requires deterministic guardrails.

---

# Slide 3: Meeting Our Scenario
## Case Study: Phil the Postdoc
* **The Scientist:** Phil works with a complex, shared experimental spectroscopy rig.
* **The Pipeline:** His script processes raw data, subtracts instrument background noise, fits data to a Gaussian profile, and saves plots.
* **The Fragility:** It works on perfectly simulated clean files, but crashes or physically violates constraints on real experimental datasets.
* **Your Role:** Co-pilot Phil’s pipeline changes using systematic AI interactions.

---

# Slide 4: Repository Rule Book (AGENTS.md)
## Our Operational Constraints
1. **Never edit tests to make them pass:** Tests represent your physical invariants and mathematical bedrock. If an AI can't pass a test, the implementation logic is flawed, not the test.
2. **Type hints & Docstrings:** All function updates must explicitly enforce data formats.
3. **Deterministic Seeding:** No unguided fitting steps.
4. **Context Budget Management:** AI models degrade as chat history lengthens. We will use short, structured session handoffs.

---

# Slide 5: Warm-Up Activity
## Task: The "Zoom Out" Prompt
* **Objective:** Build an architectural mental model before modifying code.
* **Action:** 
  1. Open a fresh AI session.
  2. Copy the template inside `prompts/01_zoom_out.txt`.
  3. Review the AI's explanation of `src/analysis.py`.
* **Question for the Room:** Did the AI correctly track how data flows? Did it highlight any hidden architectural vulnerabilities or missing folders?

---

# Slide 6: Track A: Basic Track
## Objective: Regression Testing & Error Remediation
* **The Catch:** Run `generate_data.py` to create the real public dataset. It contains a random text entry: `"CORRUPTED_SIGNAL"`.
* **The Workflow:**
  1. Use `prompts/04_diagnose.txt` to figure out why the naive dataset loader crashes.
  2. Force the AI to write a strict, failing regression test capturing this real-world anomaly.
  3. Use the diagnostic prompt to patch `analysis.py` safely using `pd.to_numeric()`.
* **Outcome:** The codebase is now resilient against dirty experimental data.

---

# Slide 7: Track B: Advanced Track
## Objective: Test-Driven Feature Extension
* **The Feature:** We need to clip negative intensity values to `0.0` inside `baseline_subtraction()` because negative light intensity is physically impossible.
* **The Workflow (Red-Green-Refactor Loop):**
  1. **Grill Me:** Run `02_grill_me.txt` in a *fresh* session to extract physical constraints and mathematical boundaries.
  2. **Red Phase:** Let the AI draft an isolated failing test matching your specification.
  3. **Green Phase:** In a *fresh* session, pass a short handoff note to make the AI implement the minimal code to pass.
  4. **Refactor Phase:** Ensure strict `AGENTS.md` structural compliance.

---

# Slide 8: Key Takeaways
## Best Practices for Research Groups
* **Isolate Content Windows:** Do not let a single chat thread run for hours. Reset the session and pass crisp, 2-line handoff summaries to keep the model sharp.
* **Specify Before Coding:** Never let the AI write features until it has "grilled" you on edge cases and produced a short, written specification.
* **Automate Verification:** Use `pytest` to act as an objective, automated grader for the AI's outputs.

