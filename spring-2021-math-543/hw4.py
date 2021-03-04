import numpy as np
import matplotlib.pyplot as plt

def QR_MGS(A):
    m, n = A.shape
    V = np.matrix.copy(A)
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for ii in range(n):
        R[ii ,ii] = np.linalg.norm(V[:, ii])
        Q[:, ii] = V[:, ii] / R[ii, ii]
        for jj in range(ii + 1, n):
            R[ii, jj] = np.dot(Q[:, ii].T, V[:, jj])
            V[:, jj] -= R[ii, jj]*Q[:, ii]

    return Q, R

x = np.linspace(-128, 128, 257)/128
A = np.ones((257, 4))
for ii in range(1, 4):
    A[:, ii] = x**ii

Q, R = QR_MGS(A)

lgnd = ["$x^{}$".format(ii) for ii in range(4)]
plt_type = ["ro-", "b*-", "g-", "yx"]
fig = plt.figure(figsize=(11, 7))
ax = plt.gca()

for ii in range(4):
    ax.plot(Q[:, ii], label=lgnd[ii])
ax.grid()
ax.legend()
plt.show()