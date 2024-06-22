from sports_team import SportsTeam


class MyTeam(SportsTeam):
    def __init__(self, country, sport_name, team_name, best_player, anthem_words):
        super().__init__(country, sport_name)
        self.team_name = team_name
        self.best_player = best_player
        self.anthem_words = anthem_words

    def get_best_player(self):
        player = self.best_player
        return f"The best player on the {self.team_name} is {player}"

    def get_anthem_words(self):
        return self.anthem_words


if __name__ == "__main__":
    blackhawks = MyTeam('USA', 'hockey', 'Blackhawks', 'Connor Bedard',
                        'O say can you see')
    print(blackhawks.get_best_player())
