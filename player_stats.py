import requests

player_count = 50
base_url = 'https://www.shl.se/'
shl_player_stats_path = f'p/api/statistics/players_summary?ssgtUuid=qZl-8qb98ZuHk&count={player_count}'
#season_2022_2023 = f'/p/api/statistics/players_summary?ssgtUuid=qbN-6KVfJw7PO&count={player_count}'
all_players = requests.get(base_url + shl_player_stats_path).json()[0]['stats']

class Player:
    
    def get_stats_team(team_code):
        player_stats = []


        for player in all_players:
            if player['info']['teamCode'] in team_code:
                player_stats.append(player)


        return player_stats

    def get_stats_player(first_name=None, last_name=None):
        if not first_name or not last_name:
            return None

        
        for player in all_players:
            if player['info']['firstName'] == first_name and player['info']['lastName'] == last_name:
                return player

        return None