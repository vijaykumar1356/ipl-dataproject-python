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


def plot_stackchart(teams_list, sorted_data):
    """
    this function takes array of sorted IPL teams and corresponding sublist
    indexed in the parent list where each sublist consist of number of matches
    played by particular team in each season from 2008-2017.
    ex: CSK --> [14,15,13,17,18,14,13,18,16,15]
    """
    ind = np.arange(len(teams_list))
    np_sd = np.array(sorted_data)   # converting the nested list as numpy array
    plt.bar(
        ind,
        np_sd[9],
        bottom=np_sd[8]+np_sd[7]+np_sd[6]+np_sd[5]+np_sd[4] +
        np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2017
        )
    plt.bar(
        ind,
        np_sd[8],
        bottom=np_sd[7]+np_sd[6]+np_sd[5]+np_sd[4] +
        np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2016
        )
    plt.bar(
        ind,
        np_sd[7],
        bottom=np_sd[6]+np_sd[5]+np_sd[4]+np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2015)
    plt.bar(
        ind,
        np_sd[6],
        bottom=np_sd[5]+np_sd[4]+np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2014
        )
    plt.bar(
        ind,
        np_sd[5],
        bottom=np_sd[4]+np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2013
        )
    plt.bar(
        ind,
        np_sd[4],
        bottom=np_sd[3]+np_sd[2]+np_sd[1]+np_sd[0],
        label=2012
        )
    plt.bar(ind, np_sd[3], bottom=np_sd[2]+np_sd[1]+np_sd[0], label=2011)
    plt.bar(ind, np_sd[2], bottom=np_sd[1]+np_sd[0], label=2010)
    plt.bar(ind, np_sd[1], bottom=np_sd[0], label=2009)
    plt.bar(ind, np_sd[0], label=2008)
    plt.xticks(ticks=ind, labels=teams_list, fontsize='small')
    plt.ylabel("Seasons")
    plt.xlabel("Teams")
    plt.title('Matches played by Team by Season')
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1), edgecolor='orange')
    plt.tight_layout()
    plt.show()


def solution():
    """
    this function creates IPL's season wise matches played by each team in
    dictionary format, and total number of unique teams participated sorted in
    alphabetical manner and process the season wise data and create a new list
    of matches played by each team per season as a sublist in a parent list
    sorted according to team names sorted alphabetically.
    """
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        season_wise = {}
        # creates a season as key and
        # a dictionary of matches played by each team in a season as value
        unique_teams = {}   # creates set of unique teams for all seasons
        # with value as empty list
        for line in csv_reader:
            season_wise.setdefault(line['season'], {})
            teams = [line['team1'], line['team2']]
            for team in teams:
                season_wise[line['season']].setdefault(team, 0)
                season_wise[line['season']][team] += 1
                if team not in unique_teams:
                    unique_teams.setdefault(team, [])

    sort_season = dict(sorted(season_wise.items(), key=lambda x: x[0]))
    sort_unq_teams = dict(sorted(unique_teams.items(), key=lambda x: x[0]))

    for key in sort_season:
        sort_season[key] = dict(sorted(
                                    sort_season[key].items(),
                                    key=lambda x: x[0],
                                    ))
        for team in sort_unq_teams:
            if team in sort_season[key].keys():
                sort_unq_teams[team] += [sort_season[key][team]]
            else:
                sort_unq_teams[team] += [0]
    try:
        l1 = sort_unq_teams['Rising Pune Supergiant']
        l2 = sort_unq_teams['Rising Pune Supergiants']
        del sort_unq_teams['Rising Pune Supergiant']
        final = [sum(i) for i in zip(l1, l2)]
        sort_unq_teams['Rising Pune Supergiants'] = final
    except Exception as e:
        print(e)
    season_data = []
    for i in range(len(sort_unq_teams['Rising Pune Supergiants'])):
        sub_list = []
        for key in sort_unq_teams.keys():
            sub_list.append(sort_unq_teams[key][i])
        season_data.append(sub_list)
    teams_list = make_acronyms(list(sort_unq_teams.keys()))
    plot_stackchart(teams_list, season_data)


if __name__ == '__main__':
    solution()
