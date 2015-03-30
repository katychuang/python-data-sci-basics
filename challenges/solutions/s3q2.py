from s3q1 import *

solid_ties = filter_col_by_string(data_from_csv, "print", "_solid")

def filter_col_by_float(data_sample, field, direction, filter_condition):
  filtered_rows = []
  
  col = int(data_sample[0].index(field))
  cond = float(filter_condition)
  
  for row in data_sample[1:]:
    element = float(row[col])
    
    if direction == "<":
      if element < cond:
        filtered_rows.append(row)
    elif direction == "<=":
      if element <= cond:
        filtered_rows.append(row)
    elif direction == ">":
      if element > cond:
        filtered_rows.append(row)
    elif direction == ">=":
      if element >= cond:
        filtered_rows.append(row)
    elif direction == "==":
      if element == cond:
        filtered_rows.append(row)  
    else:
      pass
  return filtered_rows

# code above this line is included to make this file compile on its own.
# -------------------------------------------------------------------------

# here is the answer:
 
solid35 = filter_col_by_float(solid_ties, "priceLabel", "<", 35)
solid45 = filter_col_by_float(solid_ties, "priceLabel", ">", 45)
