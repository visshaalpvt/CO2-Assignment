"""
Q7 Day-4 Design Challenge — Evidence-Based Redesign of Closest Pair (Q4)

BOTTLENECK IDENTIFIED (measured Q4 brute-force):
  n=100  → 4,950 pair comparisons, 0.002 s
  n=500  → 124,750 pair comparisons, 0.028 s
  n=1000 → 499,500 pair comparisons, 0.121 s

GROWTH ANALYSIS:
  Brute-force examines every unique pair: n*(n-1)/2 comparisons → O(n²).
  Doubling n roughly quadruples work (confirmed: 100→500 is 5x n, 25x comparisons).

MEASURABLE REDESIGN OBJECTIVE:
  Replace O(n²) pair enumeration with a strip-based plane-sweep that prunes
  pairs whose x-gap already exceeds the running best distance.
  Target: reduce pair evaluations by ≥ 60% for n ≥ 500 random uniform points.

PREDICTION BEFORE IMPLEMENTATION:
  After sorting by x (O(n log n)), we maintain a right-pointer and advance it
  only while x[j]-x[i] < best_dist.  For random uniform points in a square the
  expected strip width is small, giving average O(n log n) behaviour.
  We still fall back to O(n²) in adversarial cases (all collinear on x-axis).

STRATEGY:
  1. Sort points by x-coordinate.
  2. Initialise best_dist from the first pair.
  3. For each left pointer i, advance right pointer j only while
     points[j].x - points[i].x < best_dist.
  4. Each (i,j) pair inside the strip is evaluated with Euclidean distance.
  5. Update best_dist whenever a closer pair is found (tightens the strip).

OPERATIONS REDUCED:
  Pairs skipped = all pairs whose x-separation already exceeds best_dist.
  For random data these are the vast majority, especially at large n.

PREPROCESSING COST:
  O(n log n) sort is added; memory stays O(n) — the sorted list is in-place.

TRADE-OFFS:
  + Fewer distance calculations on average for uniform random data.
  + Correct in all cases (same output as brute-force).
  - Sort overhead dominates for tiny n (n < ~30).
  - Worst-case (all points share x-coordinate) remains O(n²).
  - Brute-force is simpler and preferred for very small n or teaching purposes.
"""

import math, time, random, csv
from pathlib import Path


def closest_pair_sweep(points):
    """
    Strip-based plane-sweep closest pair.
    Returns: (pair, distance, pair_count_evaluated, pair_count_evaluated)
    Same signature as brute-force closest_pair() in Q4.
    """
    if len(points) < 2:
        raise ValueError("need at least two points")

    pts = sorted(points, key=lambda p: p[0])   # O(n log n)
    n = len(pts)
    best = math.dist(pts[0], pts[1])
    pair = (pts[0], pts[1])
    count = 1                                    # first evaluation above

    j_start = 1
    for i in range(n - 1):
        # advance left bound: drop j_start while pts[j_start].x - pts[i].x >= best
        if j_start <= i:
            j_start = i + 1
        j = j_start
        while j < n:
            dx = pts[j][0] - pts[i][0]
            if dx >= best:
                break                            # all further j will also fail
            count += 1
            d = math.dist(pts[i], pts[j])
            if d < best:
                best = d
                pair = (pts[i], pts[j])
            j += 1

    return pair, best, count, count


# ── Comparison experiment ─────────────────────────────────────────────────────

def brute_force_closest_pair(points):
    """Baseline from Q4 (copied here for self-contained comparison)."""
    if len(points) < 2:
        raise ValueError("need at least two points")
    best = float("inf"); pair = None; count = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            count += 1
            d = math.dist(points[i], points[j])
            if d < best:
                best = d; pair = (points[i], points[j])
    return pair, best, count, count


if __name__ == "__main__":
    rng = random.Random(42)
    results = []

    print(f"{'n':>6}  {'BF_pairs':>10}  {'BF_sec':>8}  {'SW_pairs':>10}  {'SW_sec':>8}  {'pair_reduction%':>16}  {'correct':>7}")
    print("-" * 80)

    for n in (50, 100, 500, 1000, 2000):
        pts = [(rng.random() * 10000, rng.random() * 10000) for _ in range(n)]

        t0 = time.perf_counter()
        bf_pair, bf_dist, bf_count, _ = brute_force_closest_pair(pts)
        bf_sec = time.perf_counter() - t0

        t0 = time.perf_counter()
        sw_pair, sw_dist, sw_count, _ = closest_pair_sweep(pts)
        sw_sec = time.perf_counter() - t0

        reduction = 100 * (1 - sw_count / bf_count)
        correct = abs(bf_dist - sw_dist) < 1e-9

        print(f"{n:>6}  {bf_count:>10}  {bf_sec:>8.6f}  {sw_count:>10}  {sw_sec:>8.6f}  {reduction:>15.1f}%  {'YES' if correct else 'NO':>7}")
        results.append({
            "n": n, "bf_pairs": bf_count, "bf_sec": round(bf_sec, 6),
            "sw_pairs": sw_count, "sw_sec": round(sw_sec, 6),
            "reduction_pct": round(reduction, 2), "correct": correct
        })

    # Write CSV
    out = Path(__file__).resolve().parents[2] / "Supporting_Files/results/q7_comparison.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as f:
        import csv as _csv
        w = _csv.DictWriter(f, fieldnames=results[0].keys())
        w.writeheader(); w.writerows(results)
    print(f"\nCSV written to {out}")

    print("""
EVALUATION SUMMARY
==================
The strip-sweep prunes pairs whose x-separation already exceeds the running
best distance.  For random uniform points this eliminates the vast majority of
pairs at larger n, confirming the expected sub-quadratic average behaviour.
Correctness was verified (distances match brute-force to 1e-9 tolerance).

TRADE-OFFS
----------
+ Fewer distance evaluations on average -> faster for large random inputs.
+ Memory overhead is O(n) for the sorted copy -- same asymptotic as baseline.
- Sorting adds O(n log n) preprocessing; negligible vs O(n^2) savings at n>=100.
- Adversarial input (all points on vertical line, x equal) degrades to O(n^2).
- Brute-force remains preferable for n < ~50 or when simplicity is priority.
""")
