# CO2 Assignment — Brute Force and Exhaustive Search

**Course:** CSA06 — Design and Analysis of Algorithms  
**Assignment:** Assignment 2 – CO2  
**Student:** [Your Name] · [Your Registration Number]  
**Institution:** [Your Institution]  
**Deadline:** Confirm the current LMS announcement (class announcement: 100 points, due Oct 29)

---

## Overview

This repository contains all seven questions of the CO2 assignment covering brute-force and exhaustive-search techniques studied in the Design and Analysis of Algorithms course.

| # | Question | Algorithm | Complexity |
|---|----------|-----------|------------|
| Q1 | Sorting Algorithms | Selection Sort, Bubble Sort, Insertion Sort | O(n²) |
| Q2 | Sequential Search | Linear scan with comparisons | O(n) |
| Q3 | Brute-Force String Matching | Slide-and-compare | O(n·m) |
| Q4 | Brute-Force Closest Pair | Enumerate all n(n−1)/2 pairs | O(n²) |
| Q5 | Brute-Force Convex Hull | Test all edges against all other points | O(n³) |
| Q6 | Exhaustive Search — 0-1 Knapsack | Enumerate all 2ⁿ subsets | O(2ⁿ) |
| Q7 | Design Challenge — Evidence-Based Redesign | Strip-sweep closest pair vs brute-force | O(n log n) avg |

---

## Directory Structure

```
CO2_Assignment/
├── Q1_Sorting_Algorithms/
│   ├── Pseudocode/sorting.txt
│   ├── Implementation_Code/sorting.py
│   └── Output_Screenshots/         ← capture genuine screenshots here
├── Q2_Sequential_Search/
│   ├── Pseudocode/sequential_search.txt
│   ├── Implementation_Code/sequential_search.py
│   └── Output_Screenshots/
├── Q3_Brute_Force_String_Matching/
│   ├── Pseudocode/string_matching.txt
│   ├── Implementation_Code/string_matching.py
│   └── Output_Screenshots/
├── Q4_Brute_Force_Closest_Pair/
│   ├── Pseudocode/closest_pair.txt
│   ├── Implementation_Code/closest_pair.py
│   └── Output_Screenshots/
├── Q5_Brute_Force_Convex_Hull/
│   ├── Pseudocode/convex_hull.txt
│   ├── Implementation_Code/convex_hull.py
│   └── Output_Screenshots/
├── Q6_Exhaustive_Search/
│   ├── Pseudocode/exhaustive_knapsack.txt
│   ├── Implementation_Code/exhaustive_knapsack.py
│   └── Output_Screenshots/
├── Q7_Day4_Design_Challenge/
│   ├── Pseudocode/redesign.txt
│   ├── Implementation_Code/redesign_closest_pair.py
│   └── Output_Screenshots/
├── Final_Report/
│   └── CO2_Assignment_Report.pdf
├── Supporting_Files/
│   ├── test_all.py
│   ├── run_experiments.py
│   ├── ASSIGNMENT_SOURCE_NOTE.md
│   ├── screenshots_README.txt
│   ├── datasets/sample_datasets.json
│   └── results/
│       ├── experiment_results.csv
│       ├── q7_comparison.csv
│       ├── experiment_run_log.txt
│       └── test_output.txt
└── README.md
```

---

## Python Requirements

- Python 3.8+ (tested with Python 3.11.9)
- Standard library only (`math`, `time`, `random`, `csv`, `pathlib`) — **no pip installs needed**

---

## Running Each Module

Run all commands from the `CO2_Assignment/` root directory.

```bash
# Q1 — Sorting Algorithms
python Q1_Sorting_Algorithms/Implementation_Code/sorting.py

# Q2 — Sequential Search
python Q2_Sequential_Search/Implementation_Code/sequential_search.py

# Q3 — Brute-Force String Matching
python Q3_Brute_Force_String_Matching/Implementation_Code/string_matching.py

# Q4 — Brute-Force Closest Pair
python Q4_Brute_Force_Closest_Pair/Implementation_Code/closest_pair.py

# Q5 — Brute-Force Convex Hull
python Q5_Brute_Force_Convex_Hull/Implementation_Code/convex_hull.py

# Q6 — Exhaustive Search (0-1 Knapsack)
python Q6_Exhaustive_Search/Implementation_Code/exhaustive_knapsack.py

# Q7 — Evidence-Based Redesign (strip-sweep vs brute-force)
python Q7_Day4_Design_Challenge/Implementation_Code/redesign_closest_pair.py
```

> On Windows, replace `python` with `py` if Python is installed via the Python Launcher.

---

## Running the Test Harness

```bash
python Supporting_Files/test_all.py
```

**Expected output (verified):**
```
PASS Q1 sorting algorithms
PASS Q2 sequential search
PASS Q3 brute-force string matching
PASS Q4 brute-force closest pair
PASS Q5 brute-force convex hull
PASS Q6 exhaustive knapsack
Q7 requires measured evidence and must be completed after Q1-Q6 experiments.
```

---

## Running the Experiment Script

```bash
python Supporting_Files/run_experiments.py
```

Results are written to `Supporting_Files/results/experiment_results.csv`.

**Actual measured results (Python 3.11.9, seed=42):**

| Algorithm | n | Seconds | Primary Operation Count |
|-----------|---|---------|------------------------|
| closest_pair | 100 | 0.001997 | 4,950 |
| closest_pair | 500 | 0.028294 | 124,750 |
| closest_pair | 1000 | 0.121213 | 499,500 |
| exhaustive_knapsack | 4 | 0.000047 | 16 |
| exhaustive_knapsack | 8 | 0.000522 | 256 |
| exhaustive_knapsack | 12 | 0.008674 | 4,096 |
| exhaustive_knapsack | 16 | 0.204904 | 65,536 |
| exhaustive_knapsack | 18 | 0.907941 | 262,144 |

---

## Time and Space Complexity Summary

| Question | Algorithm | Time Complexity | Space Complexity |
|----------|-----------|----------------|-----------------|
| Q1 | Selection Sort | O(n²) | O(1) |
| Q1 | Bubble Sort | O(n²) best O(n) | O(1) |
| Q1 | Insertion Sort | O(n²) best O(n) | O(1) |
| Q2 | Sequential Search | O(n) | O(1) |
| Q3 | Brute-Force String Match | O(n·m) | O(1) |
| Q4 | Brute-Force Closest Pair | O(n²) | O(1) |
| Q5 | Brute-Force Convex Hull | O(n³) | O(n) |
| Q6 | Exhaustive Knapsack | O(2ⁿ) | O(n) |
| Q7 (sweep) | Strip-Sweep Closest Pair | O(n log n) avg, O(n²) worst | O(n) |

---

## Experimental Methodology

- **Primary evidence:** operation counts (comparisons, pair evaluations, subsets examined) — deterministic and environment-independent.
- **Secondary evidence:** wall-clock timings via `time.perf_counter()` — hardware-dependent but indicative.
- **Reproducibility:** all random inputs use `random.Random(42)` fixed seed.
- **Equivalence:** Q7 baseline and redesign run on identical point sets.
- Results are stored in `Supporting_Files/results/` as CSV files.

---

## Q7 Redesign Explanation

### Bottleneck Identified
Q4 brute-force closest pair examines **n(n−1)/2** unique pairs → O(n²).  
At n=1000 this is **499,500** pair evaluations taking **0.121 s**.

### Growth Derivation
```
T(n) = n*(n-1)/2
n=100  →   4,950   (5× n increase → 25× work: confirmed)
n=500  → 124,750
n=1000 → 499,500   (2× n increase → 4× work: confirmed)
```

### Redesign Strategy — Strip-Sweep
1. Sort points by x-coordinate: O(n log n).
2. For each left pointer `i`, advance right pointer `j` only while `x[j] − x[i] < best_dist`.
3. Any pair with larger x-gap is pruned — it cannot be the closest pair.
4. Updating `best_dist` when a closer pair is found tightens the strip progressively.

### Measured Results (Q7 actual output, seed=42)

| n | BF Pairs | BF Sec | Sweep Pairs | Sweep Sec | Reduction |
|---|---------|--------|-------------|-----------|-----------|
| 50 | 1,225 | 0.000335 | 86 | 0.000070 | 93.0% |
| 100 | 4,950 | 0.001059 | 125 | 0.000075 | 97.5% |
| 500 | 124,750 | 0.030558 | 883 | 0.000490 | 99.3% |
| 1,000 | 499,500 | 0.124094 | 1,923 | 0.001336 | **99.6%** |
| 2,000 | 1,999,000 | 0.515156 | 3,822 | 0.002023 | 99.8% |

All distances verified correct (match brute-force to 1e-9 tolerance).

### Trade-offs
- **Advantage:** 97–99.8% fewer pair evaluations for random uniform data.
- **Overhead:** O(n log n) sort added; negligible vs savings for n ≥ 100.
- **Worst case:** degenerate inputs (all same x) remain O(n²).
- **Brute-force preferred when:** n < 50, adversarial input, or teaching simplicity.

---

## Screenshots

The `Output_Screenshots/` folder in each question directory is reserved for genuine screenshots.  
**No screenshots have been fabricated.** Capture real terminal output and save them there.  
See `Supporting_Files/screenshots_README.txt` for guidance.

---

## Known Limitations

1. `Output_Screenshots/` directories are empty — genuine screenshots must be captured manually.
2. Q7 worst-case remains O(n²) for degenerate x-aligned point sets.
3. Timings are environment-specific; the recorded values are from Python 3.11.9 on the development machine.
4. Q6 exhaustive knapsack becomes impractical beyond n ≈ 20 (2²⁰ = 1,048,576 subsets).
5. Student name and registration number are placeholders — fill before submission.

---

## Instructions for Capturing Screenshots

1. Open a terminal in the `CO2_Assignment/` directory.
2. Run each module script (commands listed above).
3. Use your OS screenshot tool (e.g., Win+Shift+S on Windows) to capture:
   - The source code in your editor.
   - The terminal output after running the script.
4. Save as PNG files in the corresponding `Output_Screenshots/` directory.
5. Name files descriptively, e.g., `q1_sorting_output.png`, `q1_source_code.png`.

---

## Evidence Policy

Operation counts are primary evidence; timings are additional and environment-specific.  
Q7 is based on measured evidence only — no improvements are claimed without experimental confirmation.  
Do not claim tests, screenshots, or measurements that were not produced.
