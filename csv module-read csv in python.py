import csv
def parse_csv(filename):
    data = []
    with open(filename, 'rb') as f:
        entry = csv.DictReader(f)
        for line in entry:
            data.append(line)
    return data
