from secret_things import get_list_of_lists
from classes import Game

# season_games[0] = [home_team, away_team, home_score, away_score]
# season_games[0] = ['Columbus Blue Jackets', 'LA Kings', 10, 5]
season_games = get_list_of_lists()

games_as_classes = []

for game in season_games:
	class_game = Game(game[0], game[1], game[2], game[3])
	games_as_classes.append(class_game)

# {teamName: teamScore...} 
# {'Columbus Blue Jackets': 1, 'LA Kings': -1, ...} 
team_scores = {}

# fill in dict with team names and initialise to 0
for game in season_games:
	team_scores[game[0]] = 0 # home team
	team_scores[game[1]] = 0 # away team


for game in games_as_classes:
	if game.is_tie():
		team_scores[game.away_team] += 0.5
		team_scores[game.home_team] += 0.5

	else:
		team_scores[game.who_won()] += 1
		team_scores[game.who_lost()] -= 1

for k, v in team_scores.items():
	print(k, v)
