import csv
from matplotlib import pyplot as plt
import numpy as np


def plot_rcb_topbatsmen(batsmen, total_score):
    """
    this function takes RCB Batsmen data and their scores in a descending order
    and plots the top batsmen from RCB who scored runs exclusively for RCB.
    """
    plt.style.use('ggplot')
    plt.barh(batsmen, total_score,)
    plt.title("Top 15 Batsmen for RCB (2008-17)")
    plt.ylabel("Batsman")
    plt.xlabel("Runs Scored")
    plt.xticks(ticks=np.arange(0, 5000, 500))
    plt.tight_layout()
    plt.show()


def solution():
    """
    this function creates a dictionary of rcb_batsmen names and runs scored
    from all seasons and sort them in ascending order of scores and send the
    data to plot a bar chart of TOP batsmen of RCB with runs.
    """
    with open("deliveries_new.csv", 'r') as csv_file:
        rcb_batsmen_scores = {}
        file_reader = csv.DictReader(csv_file)
        for row in file_reader:
            if row['batting_team'] == 'Royal Challengers Bangalore':
                rcb_batsmen_scores.setdefault(row['batsman'], 0)
                rcb_batsmen_scores[row['batsman']] += int(row['batsman_runs'])

    sort_batsmen_scores = dict(sorted(
                                rcb_batsmen_scores.items(),
                                key=lambda x: x[1],
                                reverse=True))
    batsmen = list(sort_batsmen_scores.keys())
    total_score = list(sort_batsmen_scores.values())
    plot_rcb_topbatsmen(batsmen[:15][::-1], total_score[:15][::-1])
    # sending the lists sliced up to 15 items and then reversed


if __name__ == '__main__':
    solution()
