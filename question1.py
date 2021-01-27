import csv
from matplotlib import pyplot as plt
import numpy as np


def make_acronyms(dt_set):
    """
    this function takes a list of strings as argument and process them each
    and converts them to acronyms with first character of each substring split
    at 'space' in the original string from the list.
    ex: Chennai Super Kings --> CSK
    """
    new_dt_set = []
    for item in dt_set:
        new_dt_set.append("".join(e[0] for e in item.split()))
    return new_dt_set


def plot_teams_runs(teams, total_runs):
    """ plotting a bar chart for all IPL teams vs total runs scored from all
    seasons"""
    plt.style.use('bmh')
    plt.bar(teams, total_runs,)
    plt.title("Total Runs scored from 2008-2016")
    plt.xlabel("IPL Teams")
    plt.ylabel("Total Score")
    plt.yticks(ticks=np.arange(0, 25001, 2500))
    plt.tight_layout()
    plt.show()


def solution():
    """
    this function creates a dictionary of all the teams and their total runs
    over the history of IPL(2008-2017) and sort the data in descending order
    of runs scored and send the data as arguments to plot a bar graph.
    """
    with open("deliveries_new.csv", 'r') as csv_file:
        teams_runs = {}
        file_reader = csv.DictReader(csv_file)
        for row in file_reader:
            teams_runs.setdefault(row['batting_team'], 0)
            teams_runs[row['batting_team']] += int(row['total_runs'])

    sort_teams = dict(
                    sorted(
                        teams_runs.items(),
                        key=lambda x: x[1],
                        reverse=True))

    teams = list(sort_teams.keys())
    total_runs = list(sort_teams.values())
    plot_teams_runs(make_acronyms(teams), total_runs)


if __name__ == '__main__':
    solution()
