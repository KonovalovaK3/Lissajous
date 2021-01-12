import numpy as np
import matplotlib.pyplot as plt

h = 0.01
n = int(input('n = '))
x = np.arange(-1., 1.+h, h)
u = x.size
y = np.zeros(u)
y[-1] = 1
y[0] = (-1)**n
a = np.zeros(u)
b = np.zeros(u)
c = np.zeros(u)
alfa = np.zeros(u)
beta = np.zeros(u)


def coefa(h, x):
    a = (1-x**2)/(h**2) + x/(2*h)
    return a


def coefb(h, n, x):
    b = 2*(x**2 - 1)/(h**2) + n**2
    return b


def coefc(h, x):
    c = (1-x**2)/(h**2) - x/(2*h)
    return c


for i in range(1, u-1):
    a[i] = coefa(h, x[i])
    b[i] = coefb(h, n, x[i])
    c[i] = coefc(h, x[i])

alfa[2] = - c[1]/b[1]
beta[2] = -a[1]*y[0]/b[1]


for i in range(2, u-1):
    alfa[i+1] = -c[i]/(a[i]*alfa[i] + b[i])
    beta[i+1] = -a[i]*beta[i]/(a[i]*alfa[i] + b[i])

for i in range(u-2, 0, -1):
    y[i] = alfa[i+1]*y[i+1] + beta[i+1]


plt.title("Фигуры Лиссажу")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()