import numpy as np
import matplotlib.pyplot as plt

dt = 1 #time step
T = 2880 #big time
S0 = 0.5 #assumes that the two teams have no favorite (use real thing)
vol = 0.5 #volatility

x = np.linspace(0, T, T) #per minute
t = np.arange(T)
vars = t/(T * (T - t))
stddevs = np.sqrt(vars)
volatility_increments = np.random.normal(0, stddevs)

S = np.zeros(T)
S[0] = S0

# iterate the process
for n in range(1, T):
    S[n] = S[n-1] + S[n-1] * (1 - S[n-1]) * volatility_increments[n-1] * vol

# optional: plot
plt.plot(S)
plt.xlabel("Time")
plt.ylabel("S_t")
plt.show()