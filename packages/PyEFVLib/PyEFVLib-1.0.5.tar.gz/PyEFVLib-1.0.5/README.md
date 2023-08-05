# PyEFVLib

This package intends to support the solution of PDEs using the Element-based Finite Volume Method (EbFVM).

## Dependencies & Installation

- [Python 3](https://www.python.org/downloads/) (3.8.2);
- [meshio](https://pypi.org/project/meshio/) (4.0.15);
- [numpy](https://numpy.org/) (1.17.4);
- [pandas](https://pandas.pydata.org/)(1.1.3);
- [scipy](https://www.scipy.org/) (1.5.3);

## Usage

```python
from PyEFVLib import MSHReader, Grid, Point
import os, numpy as np

grid = PyEFVLib.read("meshes/mesh.msh")

totalVolume = 0.0
for element in grid.elements:
	for vertex in element:
		totalVolume += vertex.volume

print(totalVolume)
```