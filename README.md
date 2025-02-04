DSA Graph Analysis


Overview

This project analyzes the execution time of O(n) and O(n²) complexities on different system specifications. It includes data collection, visualization using Tkinter, and a Python script to generate the graph.




Files Included

ds.txt: Contains detailed information about system specifications and execution times for O(n) and O(n²). Currently, it includes data for 15 different test cases.

DSA_GRAPH.png: The actual graph generated using Python Tkinter, visualizing the performance of O(n) and O(n²) across different systems.

DSA_GRAPH_CODE.py: The Python script responsible for generating the graph based on the data in ds.txt.



Requirements

Python 3.x

Tkinter (included with standard Python installation)

Matplotlib (if additional plotting is needed)



Usage

Ensure Python is installed on your system.

Run the Python script to generate the graph:

python DSA_GRAPH_CODE.py

The graph will be displayed using Tkinter and saved as DSA_GRAPH.png.



Interpretation

The graph visualizes how execution time varies for O(n) and O(n²) across different CPUs.

ds.txt provides raw benchmark data, useful for deeper analysis.

The visualization helps understand the impact of increasing computational complexity on different hardware.



Future Improvements

Automate data collection for additional CPUs.

Compare different algorithmic complexities beyond O(n) and O(n²).

Enhance UI/UX of the Tkinter visualization.



