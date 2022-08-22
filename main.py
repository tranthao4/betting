import requests
from player_stats import Player


base_url = 'https://www.shl.se/'
shl_standing_path = 'p/api/statistics/standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'

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


def get_shl_standings():
    return requests.get(base_url + shl_standing_path).json()[0]


def get_all_team_stats():
    team_stats = []
    json = requests.get(base_url + shl_standing_path).json()[0]

    for stats, team_name in zip(json['stats'], teams):
        #print(team_name['TeamName'])
        #print(stats)
        team_stats.append(stats)
    return team_stats


def get_team_stats(team_name):
    json = requests.get(base_url + shl_standing_path).json()[0]


if __name__ == '__main__':
    #get_all_team_stats()
    players = Player.get_stats_team('RBK')
    for x in players:
        print(x['info']['firstName'] + ' ' + x['info']['lastName'])

    player = Player.get_stats_player('Ryan', 'Lasch')
    print(player)