import requests

base_url = 'https://www.shl.se/'
shl_standing_path = 'p/api/statistics/standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'
games_path = 'p/api/statistics/games_games?ssgtUuid=qZl-8qb98ZuHk&teamUuid='

teams = [
    {'TeamCode': 'RBK', 'TeamName': 'Rögle BK', 'uuid': 'ee93-ee93uy4oW'},
    {'TeamCode': 'LHF', 'TeamName': 'Luleå Hockey', 'uuid': '1a71-1a71gTHKh'},
    {'TeamCode': 'SAIK', 'TeamName': 'Skellefteå AIK', 'uuid': '50e6-50e6DYeWM'},
    {'TeamCode': 'FHC', 'TeamName': 'Frölunda HC', 'uuid': '087a-087aTQv9u'},
    {'TeamCode': 'VLH', 'TeamName': 'Växjö Lakers', 'uuid': 'fe02-fe02mf1FN'},
    {'TeamCode': 'FBK', 'TeamName': 'Färjestad BK', 'uuid': '752c-752c12zB7Z'},
    {'TeamCode': 'OHK', 'TeamName': 'Örebro Hockey', 'uuid': '82eb-82ebmgaJ8'},
    {'TeamCode': 'LIF', 'TeamName': 'Leksands IF', 'uuid': '9541-95418PpkP'},
    {'TeamCode': 'IKO', 'TeamName': 'IK Oskarshamn', 'uuid': '259b-259bYGVIp'},
    {'TeamCode': 'BIF', 'TeamName': 'Brynäs IF', 'uuid': '1ab8-1ab8bfj7N'},
    {'TeamCode': 'LHC', 'TeamName': 'Linköping HC', 'uuid': '41c4-41c4BiYZU'},
    {'TeamCode': 'MIF', 'TeamName': 'Malmö Redhawks', 'uuid': '8e6f-8e6fUXJvi'},
    {'TeamCode': 'DIF', 'TeamName': 'Djurgården Hockey', 'uuid': '2459-2459QTs1f'},
    {'TeamCode': 'TIK', 'TeamName': 'Timrå IK', 'uuid': '31d1-31d1NbSlR'},
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

    def get_team_results(team_code):
        json = requests.get(f'{base_url}{games_path}{Team._get_team_uuid(team_code)}&count=52').json()[0]
        all_games = json['games']
        for game_id in all_games:
            print(all_games[game_id]['homeTeamName'])
            print(all_games[game_id]['homeTeamResult'])
            print(all_games[game_id]['awayTeamName'])
            print(all_games[game_id]['awayTeamResult'])
            print(all_games[game_id]['periodResults'])
            print(all_games[game_id]['overtime'])
            break
                
    def _get_team_uuid(team_code):
        for team in teams:
            if team_code == team['TeamCode']:
                return team['uuid']