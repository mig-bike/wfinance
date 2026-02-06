import numpy as np
import os

# Get all data from 'data'
data_files = os.listdir('data')

window_len = 10
volatility_threshold = 0.2

profit_threshold = 0.75 # Take profit
exit_threshold = 1.0 # Stop loss

num_plays = 200

games = []
trades = []

for file in data_files:
    data = np.load(f'data/{file}')

    entry_price = -1
    state = "neutral" # "neutral", "yes", "no"

    for i in range(len(data) - window_len):
        window = data[i:i+window_len]
        high = np.max(window)
        low = np.min(window)
        if abs(high - low) >= volatility_threshold and (window[-1] == low or window[-1] == high) and state == "neutral" and i < num_plays:
            if window[-1] == low:
                state = "yes"
            else:
                state = "no"
            entry_price = window[-1]
        elif state != "neutral":
            if state == "yes":
                if (window[-1] / entry_price) > (1 + profit_threshold):
                    trades.append((window[-1] / entry_price))
                    games.append(file)
                    state = "neutral"
                    entry_price = -1
                elif (window[-1] / entry_price) < (1 - exit_threshold):
                    trades.append((window[-1] / entry_price))
                    games.append(file)
                    state = "neutral"
                    entry_price = -1
            elif state == "no":
                if ((1-window[-1]) / (1 - entry_price)) > (1 + profit_threshold):
                    trades.append((1-window[-1]) / (1 - entry_price))
                    games.append(file)
                    state = "neutral"
                    entry_price = -1
                elif ((1-window[-1]) / (1 - entry_price)) < (1 - exit_threshold):
                    trades.append((1-window[-1]) / (1 - entry_price))
                    games.append(file)
                    state = "neutral"
                    entry_price = -1

    if state == "yes":
        trades.append((data[-1] / entry_price))
        games.append(file)
    elif state == "no":
        trades.append((1-data[-1]) / (1 - entry_price))
        games.append(file)

trades = np.array(trades)
mask = np.array(trades) > 1

print(trades)
# print(max(trades))
# print(min(trades))
# print(games)
print(np.sum(mask) / len(mask))
print(len(trades))
print(np.mean(trades))
# print(np.std(trades))
print(np.sum(trades))