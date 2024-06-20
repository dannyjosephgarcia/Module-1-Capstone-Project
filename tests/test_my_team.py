import unittest
from my_team import MyTeam

COUNTRY = 'USA'
SPORT_NAME = 'Hockey'
TEAM_NAME = 'Blackhawks'
BEST_PLAYER = 'Connor Bedard'


class TestMyTeam(unittest.TestCase):
    def setUp(self):
        self.my_team = MyTeam(COUNTRY, SPORT_NAME, TEAM_NAME, BEST_PLAYER)

    def test_my_team_get_best_player(self):
        player_string = self.my_team.get_best_player()
        self.assertEqual("The best player on the Blackhawks is Connor Bedard", player_string)


if __name__ == "__main__":
    unittest.main()
