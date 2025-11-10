import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    
    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        
        return players
        


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
        self.players_sorted = sorted(
            self.players, key=lambda player:player.points, reverse=True)

    def top_scorers_by_nationality(self, nationality):
        result = []
        for player in self.players_sorted:
            if player.nationality == nationality:

                result.append(player)
        
        return result

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    
    for player in players:
        print(player)
    
    

if __name__ == "__main__":
    main()
