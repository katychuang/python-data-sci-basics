data_from_csv = [[]]

try:
    output=filter_by_string(data_from_csv, "brandName", "Dolce & Gabbana")
    assert output == filter_col_by_string(data_from_csv, "brandName", "Dolce & Gabbana")
except NameError:
    failure("Where's `filter_by_string()`?")
except AssertionError:
    failure()
else:
    success()
