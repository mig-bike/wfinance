import numpy as np 
import matplotlib.pyplot as plt

drift = 0.2
increment = 1000 #how much total numbers
yrs = 1
S0 = 100
volatility = 0.5

dt = yrs/increment
x = np.linspace(0, yrs, increment)
brownian_increments = np.random.normal(0, np.sqrt(dt), increment)
Wt = np.cumsum(brownian_increments)
Wt[0] = 0
thing_in_exponent = (drift - volatility ** 2 / 2) * x + volatility * Wt
St = S0 * np.exp(thing_in_exponent)

m = np.max(St)

plt.plot(x, St)
plt.xlabel('Time (years)')
plt.ylabel('Stock Price')
plt.title('Stock Price Simulation')
plt.ylim(0,max(200, m + 25))
plt.show()
