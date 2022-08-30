import requests
from player_stats import Player
from team_stats import Team


base_url = 'https://www.shl.se/'
shl_standing_path = 'p/api/statistics/standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'


def get_shl_standings():
    return requests.get(base_url + shl_standing_path).json()[0]


if __name__ == '__main__':
    #get_all_team_stats()
    #players = Player.get_stats_team('RBK')
    #for x in players:
    #    print(x['info']['firstName'] + ' ' + x['info']['lastName'])

    #player = Player.get_stats_player('Ryan', 'Lasch')
    #print(player)

    #print(Team.get_team_stats(team_code='RBK'))

    Team.get_team_results('RBK')