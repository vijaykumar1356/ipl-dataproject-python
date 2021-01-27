import csv
"""
this program processes deliveries.csv file and reproduces the same data
whie fixing a minor bug in the file.
Bug Details: Team name 'Rising Pune Supergiants' is misspelt as
'Rising Pune Supergiant' in one whole season. due to that data is
separated into two containers while creating a dictionary object.
"""
if __name__ == '__main__':
    with open("deliveries.csv", 'r') as cs_file:
        cs_read = csv.DictReader(cs_file)
        with open('deliveries_new.csv', 'w') as csv_file:
            fieldnames = cs_read.fieldnames
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
                delimiter=',',)
            csv_writer.writeheader()

            for line in cs_read:
                if line['batting_team'] == 'Rising Pune Supergiant':
                    line['batting_team'] = 'Rising Pune Supergiants'
                csv_writer.writerow(line)
