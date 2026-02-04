import numpy as np
import matplotlib.pyplot as plt

dt = 1
T = 2880
S0 = 0.5
vol = 3

K = 100
t_decide = 2780

t = np.arange(T)
vars = t / (T * (T - t))
vars[0] = 0
stddevs = np.sqrt(vars)
volatility_increments = np.random.normal(0, stddevs)

S = np.zeros(T)
S[0] = S0

X_T = None  # end zero or one?

for n in range(1, T):
    noise = S[n-1] * (1 - S[n-1]) * volatility_increments[n-1] * vol

    # decide terminal state at t = 2780
    if n == t_decide:
        X_T = 1.0 if np.random.rand() < S[n-1] else 0.0

    # pinning drift after decision
    if X_T is not None and n >= T - K:
        drift = (X_T - S[n-1]) / (T - n)
    else:
        drift = 0.0

    S[n] = S[n-1] + noise + drift
    S[n] = np.clip(S[n], 0, 1)

plt.plot(S)
plt.xlabel("Time")
plt.ylabel("S_t")
plt.show()
