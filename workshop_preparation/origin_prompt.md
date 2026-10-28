This repository was generated with the help of AI.
## Planning
Gemini was used to create the plan and first versions of the files.
The original prompt was:
```
I need to create a small example python repository to teach university lecturers to use AI effectively for scientific software. It should contain realistic but slightly buggy research code, a partial test suite, and a public dataset. It should also contain a short AGENTS.md (how to run the tests, “never edit tests to make them pass”, coding conventions) and a few reusable prompt templates (grill me, red-green-refactor, zoom out, diagnose), so participants leave with a toolkit they can reuse. The scenario is: “Phil is a postdoc who works with a complex and shared experimental setup. The experiment produces huge quantities of data that Phil need to analyse, fit to theoretical models and plot in a format suitable for publication.”
The tasks the lecturers will perform are:
•	Warm-up (both tracks): ask the assistant to “zoom out” and explain the structure of the codebase before touching anything; check its explanation against the code.
•	Basic track: ask the assistant to write missing tests for one function, run them, then fix the bug the tests expose, keeping the new test as a regression test.
•	Advanced track: add a small feature (e.g. a new analysis option) using the full loop: let the agent grill you, have it write a three-to-five line spec, then implement it red, green, refactor, one behaviour per step. Start a fresh session for each step, passing on a short handoff note, so the local model stays within its context budget. The provided tests must still pass.
What are the steps I need to take to create such a repository?
```

## Refining
GitHub Copilot was then used to remove formatting errors and further refine the exercise.