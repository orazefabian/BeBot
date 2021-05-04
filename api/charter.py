import matplotlib.pyplot as plt
import numpy as np
import json
from types import SimpleNamespace


def convert_json_to_object(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def get_goals_team(team, stats_object):
    arr = []
    for game in stats_object.data.encounters:
        result = game.fulltime_result.split(" - ")
        if game.home_team == team:
            arr.append(int(result[0]))
        else:
            arr.append(int(result[1]))
    return arr[::-1]


def get_game_dates(stats_object):
    arr = []
    for game in stats_object.data.encounters:
        arr.append(game.start_date)
    return arr[::-1]


def plot_head_to_head_stats(json_data):
    stats_object = convert_json_to_object(json_data)
    home = stats_object.data.stats.home_team.team_name
    away = stats_object.data.stats.away_team.team_name

    home_goals = get_goals_team(home, stats_object)
    away_goals = get_goals_team(away, stats_object)
    game_dates = get_game_dates(stats_object)

    plt.title("Head to head goal comparison")
    plt.plot(game_dates, home_goals, linewidth=3.0)
    plt.plot(game_dates, away_goals, linewidth=3.0)
    plt.ylabel("Goals scored")
    plt.xlabel("Game dates")
    plt.legend([home, away])
    plt.grid(True)
    plt.show()
