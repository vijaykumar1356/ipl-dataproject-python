from bs4 import BeautifulSoup as bs
import urllib.request
import csv

"""
this program is to scrape the data of details of all umpires
who umpired in IPL in all seasons. Then it creates a csv file of Umpires and
their nationality.
"""

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_umpires"
    sauce = urllib.request.urlopen(url).read()
    soup = bs(sauce, 'html.parser')
    table = soup.find("table", class_='wikitable plainrowheaders sortable')
    rows = table.find_all('tr')
    rows = iter(rows)
    next(rows)  # for skipping the headings of table i.e., 1st row
    with open('umpires_nation.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['umpire', 'nationality'])
        for row in rows:
            name = row.th.text.strip()
            nationality = row.td.text.strip()
            csv_writer.writerow([name, nationality])
