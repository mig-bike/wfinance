import requests
import matplotlib.pyplot as plt

def get_price_history(market_id: str, start_ts: int, end_ts: int):
    response = requests.get(f'https://clob.polymarket.com/prices-history?market={market_id}&fidelity=1&startTs={start_ts}&endTs={end_ts}')
    return response.json()

def extract_price(price_history: list[dict]):
    return [price['p'] for price in price_history]

price = extract_price(get_price_history('12174907552380481449558625286581790517252890375007137204936009091630461152066', 1761174000, 1761184800)['history'])

plt.plot(price)
plt.ylim(0, 1)
plt.xlabel('Time')
plt.ylabel('Price (normalized)')
plt.title('Price History')
plt.show()