import requests

def get_game_ids(year: int, page: int=0):
    """
    Returns 25 games per page max
    """
    url = f"https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/events?dates={year}&page={page}"
    response = requests.get(url)
    res_json = response.json()
    items = res_json['items']
    ids = []
    for i in range(25):
        if i >= len(items):
            break
        item = items[i]
        if item is not None and item["$ref"] is not None:
            game_id = item["$ref"].split("/leagues/nba/events/")[1].split("?lang=")[0]
            ids.append(game_id)

    return ids


def scrape_game_probabilities(game_id: str):
    response = requests.get(f'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event={game_id}')
    res_json = response.json()
    probs = res_json["winprobability"]
    home_team = res_json["boxscore"]["teams"][0]["team"]["displayName"]
    away_team = res_json["boxscore"]["teams"][1]["team"]["displayName"]
    return probs, home_team, away_team