import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
    
    def test_player_not_in_players(self):
        self.assertEqual(self.stats.search("Selänne"), None)
    
    def test_team_players_count(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("PIT")), 1)

    def test_top_players_by_points_search_correct(self):
        best = self.stats.top(1)

        self. assertEqual(best[0].name, "Gretzky")
        self.assertEqual(best[0].points, 124)
    
    def test_top_player_by_goals(self):
        best = self.stats.top(1, SortBy.GOALS)

        self.assertEqual(best[0].name, "Lemieux")
    
    def test_top_player_by_assists(self):
        best = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(best[0].name, "Gretzky")
