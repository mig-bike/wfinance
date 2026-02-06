import numpy as np
from scrape import get_game_ids, scrape_game_probabilities
import pandas as pd
import matplotlib.pyplot as plt

# def get_price_history(market_id: int, start_ts: int, end_ts: int):
#     response = requests.get(f'https://clob.polymarket.com/prices-history?market={market_id}&fidelity=1&startTs={start_ts}&endTs={end_ts}')
#     return response.json()['history']

# def extract_price(price_history: list[dict]):
#     return [price['p'] for price in price_history]

# price = np.array(extract_price(get_price_history(87413541522011440617239482051839620325250854997635173812757786298094460315826, 1770249600, 1770261300)))
# price = price

# # Compute percent moves
# percent_moves = np.diff(price) / price[:-1]

# # Compute average percent move
# average_percent_move = np.mean(percent_moves)

# # Compute standard deviation of percent moves
# standard_deviation = np.std(percent_moves)

# print(average_percent_move, standard_deviation)

probs = np.load('data/401705189.npy')

# # Compute z-score
plt.plot(probs)
plt.ylim(0, 1)
plt.xlabel('Time')
plt.ylabel('Probability')
plt.title('Probability History')
plt.show()

# n_pages = 57

# if __name__ == "__main__":
#      for i in range(1, n_pages + 1):
#          game_ids = get_game_ids(2025, i)
#          for game_id in game_ids:
#              probs, home_team, away_team = scrape_game_probabilities(game_id)
#              probs = pd.DataFrame(probs)
#              if "homeWinPercentage" in probs.columns:
#                  home_win_percentage = probs["homeWinPercentage"]
#                  for i in range(len(home_win_percentage)):
#                     if i != 0 and i < len(home_win_percentage) - 3:
#                         if (home_win_percentage[i]/home_win_percentage[i-1] > 1.25 or home_win_percentage[i]/home_win_percentage[i+1] > 1.25) or (home_win_percentage[i]/home_win_percentage[i-1] < 0.75 or home_win_percentage[i]/home_win_percentage[i+1] < 0.75):
#                             home_win_percentage[i] = home_win_percentage[i-1]
#                  np.save(f'data/{game_id}.npy', home_win_percentage)
#              else:
#                  print(game_id)