import requests
from player import Player
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

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
    seasons = ["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25"]
    nationalities = ["USA","FIN","CAN","SWE","CZE","RUS","SLO","FRA","GBR","SVK",
                     "DEN","NED","AUT","BLR","GER","SUI","NOR","UZB", "LAT", "AUS"]
    season = Prompt.ask("Season", choices=seasons)
    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities)    
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Season {season} players from {nationality}")

        table.add_column("Player", justify="right", style="cyan", no_wrap=True)
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(
                str(player.name), str(player.team),
                  str(player.goals), str(player.assists), str(player.points))
        

        console = Console()
        console.print(table)
    

if __name__ == "__main__":
    main()
