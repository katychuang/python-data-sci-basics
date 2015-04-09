import csv #from s2q1.py

# function from s2q2.py
def open_with_csv(filename, d='\t'):
  data = []
  with open(filename, encoding='utf-8') as tsvin:
    tie_reader = csv.reader(tsvin, delimiter=d)
    for row in tie_reader:
      data.append(row)
  return data

def filter_col_by_string(the_data, field, filter_condition):
    filtered_rows = []
    
    #find index of field in first row
    col = int(the_data[0].index(field))
    filtered_rows.append(the_data[0])

    for row in the_data[1:]:
        if row[col] == filter_condition:
            filtered_rows.append([x for x in row])
            
    return filtered_rows

data_from_csv = open_with_csv('data.csv')

# code above this line is included to make this file compile on its own.
# -------------------------------------------------------------------------

# here is the answer:
dkny_ties = filter_col_by_string(data_from_csv, "brandName", "DKNY")


# --------------------------------------------------------------------------
# for testing:
# print(dkny_ties)

