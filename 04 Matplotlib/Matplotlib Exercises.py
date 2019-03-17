import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()

# Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title')
plt.show()

# Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x, z)
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_xlim(20, 22)
ax2.set_ylabel('y')
ax2.set_ylim(30, 50)
ax2.set_title('zoom')
plt.show()

# Use plt.subplots(nrows=1, ncols=2) to create the plot below.
# plt.subplots(nrows=1, ncols=2)
# plt.subplot(121)
# plt.plot(x, y)
# plt.subplot(122)
# plt.plot(x, z)
# plt.show()

# OU

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color="blue", lw=3, ls='--')
axes[1].plot(x, z, color="red", lw=3, ls='-')
plt.show()

# resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
axes[0].plot(x, y, color="blue", lw=3, ls='--')
axes[1].plot(x, z, color="red", lw=3, ls='-')
plt.show()

