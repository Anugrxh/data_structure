import matplotlib.pyplot as plt
import numpy as np

# Full CPU model names for each test
cpu_labels = [
    "i5-4460S (1)", "i5-4460S (2)", "i5-4460S (3)", "i5-4460S (4)", "i5-4460S (5)",
    "i5-4460S (6)", "i5-4460S (7)", "i5-4460S (8)", "i5-4460S (9)", "i5-4460S (10)",
    "i5-4460S (11)", "i3-9100 (12)", "i3-2120 (13)", "i3-2120 (14)", "i3-2120 (15)"
]

# O(n) and O(n^2) execution times
o_n_times = [
    0.000989, 0.000959, 0.000865, 0.000249, 0.000328,
    0.000320, 0.000894, 0.000775, 0.000908, 0.000881,
    0.000354, 0.000177, 0.000244, 0.000243, 0.000322
]

o_n2_times = [
    21.552000, 20.889201, 22.387099, 24.798328, 21.399481,
    21.599269, 21.408919, 20.887022, 20.849592, 21.301035,
    21.548860, 19.329474, 21.442800, 21.472854, 21.519772
]

# X-axis positions
x = np.arange(len(cpu_labels))

# Plot
plt.figure(figsize=(12, 6))
plt.plot(x, o_n_times, marker="o", linestyle="-", color="blue", label="O(n) Time (log scale)")
plt.plot(x, o_n2_times, marker="o", linestyle="-", color="red", label="O(n^2) Time")

# Log scale for better visibility of O(n)
plt.yscale("log")

plt.xticks(x, cpu_labels, rotation=45, ha="right")
plt.xlabel("CPU Model (Test Number)")
plt.ylabel("Execution Time (s)")
plt.title("O(n) vs O(n^2) Execution Time Across Different CPUs")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Save and show the plot
plt.savefig("cpu_performance_plot.png", dpi=300, bbox_inches="tight")
plt.show()
