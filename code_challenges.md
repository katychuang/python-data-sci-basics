# List of Code Challenges

## Stage 2

1. Try to import the csv module

`import csv`

2. Write a function `open_with_csv` that takes one argument parameter. This function will return an empty list `data`.

```
def open_with_csv(filename):
    data = []
    return data
```

## Stage 3

1. Filter all the DKNY branded ties from my_csv into dknyTies using the function filter_col_by_string()

`filter_col_by_string(data_from_csv, "brandName", "Dolce & Gabbana")`

2. Filter all the solid color ties under $35 to solid35 and over $45 to solid45 using the function filter_col_by_float()

```
solid35 = filter_col_by_float(solid_ties, "priceLabel", "<", 35)
solid45 = filter_col_by_float(solid_ties, "priceLabel", ">", 45)
```

3. Is the average Gucci tie price higher than the average J. Crew tie price? Write a function comparison() that compares Gucci tie price and J.Crew Tie price, and prints out the one sentence "The brand that is more likely to have a higher price tag is: brandName" where brandName is the brand  with a higher price.

```
def comparison(brand_a, brand_b):
    brand_name = ""
    if brand_a > brand_b:
        brand_name = brand_a
    elif brand_b > brand_a:
        brand_name = brand_b
    else:
        brand_name = "neither"
    return "The brand that is more likely to have a higher price tag is:{}".format(brand_name)

comparison(gucci_ties, jcrew_ties)
```

4. *bonus* Write a function filter_by_brand_and_price(data, brand, price) that lets you filter a dataset with two conditions

```
def filter_by_brand_and_price(data, brand, price):
    new_data = []
    #filter by brand
    #filter by price
    return new_data
```

## Stage 4

1. Using the function, filter_col_by_string(), how would you call it so that it exports 'Dolce & Gabbana' brand ties?

2. Define a function that would allow you to filter ties made of 'cotton' material and a pattern matching the string "_striped" under the striped field. This would be a function that accepts two arguments and returns a list.

3. Define a function with two input arguments: (1) filename, and (2) a list of columns to be exported using integer values.

4. Export a CSV file with each sample having only three fields: brand name, price, and material. How would you call the function from task 3 that takes in two arguments?


