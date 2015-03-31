from s3q1 import *

# code above this line is included to make this file compile on its own.
# -------------------------------------------------------------------------

# here is the answer:

cotton_ties = filter_col_by_string(data_from_csv, "material", "_cotton")
cotton_and_striped = filter_col_by_string(cotton_ties, "print", "_striped")

