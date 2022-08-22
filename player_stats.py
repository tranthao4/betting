import requests
from main import base_url

player_count = 50
shl_player_stats_path = f'p/api/statistics/players_summary?ssgtUuid=qZl-8qb98ZuHk&count={player_count}'
season_2022_2023 = f'/p/api/statistics/players_summary?ssgtUuid=qbN-6KVfJw7PO&count={player_count}'

def get_player_stats():
    player_stats = []

    data = requests.get(base_url + shl_player_stats_path).json()
    top_chart = data[0]['stats']
    for player in top_chart:
        player_stats.append(player)

    for p in player_stats:
        print(p)

get_player_stats()