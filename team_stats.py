import requests

base_url = 'https://www.shl.se/'
shl_standing_path = 'p/api/statistics/standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'
rbk_path = 'p/api/statistics/games_games?ssgtUuid=qZl-8qb98ZuHk&teamUuid=ee93-ee93uy4oW&count=25'

teams = [
    {'TeamCode': 'RBK', 'TeamName': 'Rögle BK'},
    {'TeamCode': 'LHF', 'TeamName': 'Luleå Hockey'},
    {'TeamCode': 'SAIK', 'TeamName': 'Skellefteå AIK'},
    {'TeamCode': 'FHC', 'TeamName': 'Frölunda HC'},
    {'TeamCode': 'VLH', 'TeamName': 'Växjö Lakers'},
    {'TeamCode': 'FBK', 'TeamName': 'Färjestad BK'},
    {'TeamCode': 'OHK', 'TeamName': 'Örebro Hockey'},
    {'TeamCode': 'LIF', 'TeamName': 'Leksands IF'},
    {'TeamCode': 'IKO', 'TeamName': 'IK Oskarshamn'},
    {'TeamCode': 'BIF', 'TeamName': 'Brynäs IF'},
    {'TeamCode': 'LHC', 'TeamName': 'Linköping HC'},
    {'TeamCode': 'MIF', 'TeamName': 'Malmö Redhawks'},
    {'TeamCode': 'DIF', 'TeamName': 'Djurgården Hockey'},
    {'TeamCode': 'TIK', 'TeamName': 'Timrå IK'},
]

class Team:

    def get_all_team_stats():
        team_stats = []
        json = requests.get(base_url + shl_standing_path).json()[0]

        for stats in json['stats']:
            team_stats.append(stats)
        return team_stats

    def get_team_stats(team_code):
        for team in Team.get_all_team_stats():
            if team['TeamCode'] == team_code:
                return team
        return None

    def get_team_results():
        json = requests.get(base_url + rbk_path).json()
        for items in json:
            for x in items:
                print(x)
            print(items['stats'])
                