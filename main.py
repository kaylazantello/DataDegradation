# Project 4: Data Degradation
# Kayla Zantello and Lucio Infante

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import math

# define range of t values to evaluate and plot
t_range = np.linspace(-100, 100)

# solution 1
def sol1(t1):
    return math.exp(-t1/20)

# array for x(t) values for solution 1
xt1 = []

# use function defined above to populate x(t) array
for n in t_range:
    xt1.append(sol1(n))

# plot the results
plt.plot(t_range, xt1)
plt.title("Solution 1: x1(t) = e^(-t/20)")
plt.xlabel("t")
plt.ylabel("x1(t)")
plt.show()

# solution 2
def sol2(t2):
    return -math.exp(-t2/20)

# array for x(t) values for solution 2
xt2 = []

# use function defined above to populate x(t) array
for n in t_range:
    xt2.append(sol2(n))

# plot the results
plt.plot(t_range, xt2, 'orange')
plt.title("Solution 2: x2(t) = -e^(-t/20)")
plt.xlabel("t")
plt.ylabel("x2(t)")
plt.show()

# plot solution 1 and 2 together
plt.plot(t_range, xt1, label="Solution 1")
plt.plot(t_range, xt2, 'orange', label="Solution 2")
plt.title("x(t) = e^(At)*c")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.show()

# subplot of all three graphs
fig = plt.figure()
fig.suptitle("Subplots")
spec = fig.add_gridspec(2, 2)

# solution 1
ax00 = fig.add_subplot(spec[0, 0])
ax00.plot(t_range, xt1)
ax00.set(ylabel="x1(t)")

# solution 2
ax10 = fig.add_subplot(spec[1, 0])
ax10.plot(t_range, xt2, 'orange')
ax10.set(xlabel="t", ylabel="x2(t)")

# solutions 1 and 2 together
ax_1 = fig.add_subplot(spec[:, 1])
ax_1.plot(t_range, xt1, label="Solution 1")
ax_1.plot(t_range, xt2, 'orange', label="Solution 2")
ax_1.set(xlabel="t", ylabel="x(t)")
ax_1.legend()

plt.show()
