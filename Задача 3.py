import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from openpyxl.compat.numbers import NUMPY
from pandas.compat.numpy import np_long
import numpy as np
x = np.linspace(-np.pi, np.pi, 50)
y = x
z = np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')