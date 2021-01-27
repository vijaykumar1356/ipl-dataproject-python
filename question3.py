import csv
from matplotlib import pyplot as plt
import numpy as np


def plot_country_umpires(countries, no_of_umpires):
    """
    This function takes array of countries and number of umpires from each
    country who participated in IPL in a descending order of count.
    """
    plt.style.use('fivethirtyeight')
    plt.barh(countries, no_of_umpires)
    plt.title("IPL Umpires vs Country of Origin ")
    plt.ylabel("Country of Origin")
    plt.xlabel("No of Umpires")
    plt.xticks(ticks=np.arange(9))
    plt.tight_layout()
    plt.show()


def solution():
    """
    this function fetches the umpires and their nationality from a csv file
    umpires_nation.csv and evaluates the number of foreign umpires
    participated in IPL country wise and sort the data descending order of
    number.
    """
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        match_umpires = []
        for line in csv_reader:
            umpires = [line['umpire1'], line['umpire2'], ]
            for umpire in umpires:
                if umpire != "" and umpire not in match_umpires:
                    match_umpires.append(umpire)

    with open('umpires_nation.csv', 'r') as csv_file:
        # this file has been generated with the help of scrape_umpires.py file,
        # where I used Beautiful Soup module to scrape the list of umpires and
        # their nationality.
        csv_reader = csv.DictReader(csv_file)
        name_nationality = {}
        for line in csv_reader:
            name_nationality[line['umpire']] = line['nationality']

    country_umpire = {}
    # country as key and no. of umpires belongs to that country as value
    for umpire in match_umpires:
        for person in name_nationality.keys():
            if umpire.split()[1] in person.split():
                if name_nationality[person] == 'India':
                    continue
                country_umpire.setdefault(name_nationality[person], 0)
                country_umpire[name_nationality[person]] += 1
                
    sorted_country_umpire = dict(sorted(
                                country_umpire.items(),
                                key=lambda x: x[1]
                                ),)
    plot_country_umpires(
                list(sorted_country_umpire.keys()),
                list(sorted_country_umpire.values()),
                )


if __name__ == '__main__':
    solution()
