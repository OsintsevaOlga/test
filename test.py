#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import math

'''
H0 = {gaussian(x, 0, 1)}
H1 = {gaussian(x, 2, 0.5)}
принимается H0 при попадании в интервал [-2, 2], в противном случае H1
'''

def gaussian(x, mu, sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2) / sigma / math.sqrt(2*math.pi)

xs = np.arange(-5, 5, 0.05)

plt.plot(xs, [gaussian(x, 0, 1) for x in xs], color = "red", label='$\sigma = 1$, $\mu = 0$')
plt.plot(xs, [gaussian(x, 2, 0.5) for x in xs], color = "black", label='$\sigma = 0.5$, $\mu = 2$')

plt.fill_between(xs, [gaussian(x, 0, 1)for x in xs], where=[(x < -2) for x in xs], color = "blue", label = 'ошибка I рода')
plt.fill_between(xs, [gaussian(x, 0, 1)for x in xs], where=[(x > 2) for x in xs], color = "blue")
plt.fill_between(xs, [gaussian(x, 2, 0.5)for x in xs], where =[((x >= -2) and (x <= 2)) for x in xs], color = "violet", label = 'ошибка II рода')

plt.legend()
plt.grid()

plt.show()
