import csv  # this was the solution from Question1

def open_with_csv(filename, d='\t'):
    data = []
    with open(filename, encoding='utf-8') as tsvin:
        tsvin = csv.reader(tsvin, delimiter=d)
        for row in tsvin:
            data.append(row)
    return data
