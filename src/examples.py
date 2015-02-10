# coding: utf-8

#
# Intro to Data Science with Python
# Author: Kat Chuang
# Created: Nov 2014

# --------------------------------------

from my_utils import *
from numpy_utils import *

# --------------------------------------

print("\n>>> SHOWING STAGE 2 EXAMPLES")

"""
Stage 2: Describing Data

This section the students can learn to use Numpy library or basic Python data structures, such as nested lists or dictionaries.

A. Loading raw data into data structure(s)
B. Calculate descriptive Stats
	- Max, Min, Median, Mean
	- Sums and Totals

"""

### Loading data into a data structure (list of lists)
print("Part 1- Loading data into data structures")


# we're using these functions
from my_utils import open_with_csv
from numpy_utils import load_data

# sample filename
sample_file = 'data.csv' 

## 1. read in the data captured using the python CSV module
data_from_csv = open_with_csv(sample_file)
print("The header contains these fields: \n", data_from_csv[0])

## 2. read in the data captured using numpy
my_csv = load_data(sample_file)


print("\nPart 2 - describe data")
print("2.a. Show size of dataset")
# Calculating descriptive stats by showing the length of a list
# How many rows are there? 
from my_utils import number_of_records
print("Length: ", number_of_records(data_from_csv), "rows in", sample_file, "including header")

# show length using numpy array
from numpy_utils import size
size(my_csv)

# How many brands? How many colors are represented?
# What price range is represented?


print("\n2.b. Calculating Sum")
## 3. Let's dig further into the prices, by calculating the average and median.

# Sums of all the prices
from my_utils import calculate_sum
the_sum = calculate_sum(data_from_csv)
print("The Sum: $", the_sum)

# Format the output to show up to two decimal points
from numpy_utils import calculate_numpy_sum
price = my_csv['priceLabel']
my_sum = calculate_numpy_sum(price)
print("The Sum (numpy): $", my_sum)


print("\n2.c. Average")
from my_utils import find_average
print("Average:", find_average(data_from_csv, True))

midpoint = round(len(data_from_csv)/2)
print("Average of first half", find_average(data_from_csv[:midpoint], True))
print("Average of last half", find_average(data_from_csv[midpoint:], False))


price_in_float = [float(item) for item in price]
print("Average (numpy):", find_numpy_average(price_in_float))

print("\n2.d. Max, Min")
from my_utils import find_max, find_min, find_max_min
print("Highest Priced Tie: $", find_max(data_from_csv[1:], 2), "// Lowest Priced Tie: $", find_min(data_from_csv[1:], 2) )
#print(find_max_min(data_from_csv[1:], 2))

from numpy_utils import numpy_max, numpy_min
print("(Numpy) Highest Priced Tie: $", numpy_max(price_in_float), "// Lowest Priced Tie: $", numpy_min(price_in_float) )


print("\n>>> SHOWING STAGE 3 EXAMPLES")

"""
Stage 3: Cleaning data

Cleaning Data
Filtering Rows (Motion graphics?)
Grouping columns
Quiz -
"""

### Cleaning data
print("3.a Cleaning data")

# find cashmere ties
my_improved_csv = create_bool_field_from_search_term(data_from_csv, "cashmere")
print(number_of_records(my_improved_csv), "ties made with cashmere")


print("Filtering for correct count...")
number_cashmere_ties = filter_col_by_bool(my_improved_csv, 11)
# add boolean fields

print("3.b Filtering rows")
from my_utils import filter_col_by_string, filter_col_by_float


### Filtering Ties by string

# Look at ties of brand Hermes vs JCrew
hermes_ties = filter_col_by_string(data_from_csv, "brandName", "Hermes")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")
print("Found ", len(hermes_ties), "Hermes Ties")
print("Found ", len(jcrew_ties), "J.Crew Ties")

# Only look at rows of "silk" ties or only "wool"
silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
wool_ties = filter_col_by_string(data_from_csv, "material", "_wool")
print("Found ", len(silk_ties), "Silk Ties")
print("Found ", len(wool_ties), "Wool Ties")

# Look at ties < $20 vs ties over $100
under_20_dollars = filter_col_by_float(data_from_csv, "priceLabel", "<=", 20)
over_100_dollars = filter_col_by_float(data_from_csv, "priceLabel", ">=", 100)
print("Found ", len(under_20_dollars), " ties < $20")
print("Found ", len(over_100_dollars), " ties < $100")

print("3.c Grouping rows")
# Compare Maximum Prices
max_hermes_tie_price = find_max(hermes_ties[1:], 2)
max_jcrew_tie_price = find_max(jcrew_ties[1:], 2)
print("Maximum Hermes Tie Price is: ", '{:03.2f}'.format(max_hermes_tie_price))
print("Maximum J.Crew Tie Price is: ", '{:03.2f}'.format(max_jcrew_tie_price))

# Printed vs Solid. Are the printed ties cheaper? 
avg_print_ties = find_average(filter_col_by_string(data_from_csv, "print", "_print"))
avg_paisley_ties = find_average(filter_col_by_string(data_from_csv, "print", "_paisley"))
avg_striped_ties = find_average(filter_col_by_string(data_from_csv, "print", "_striped"))
avg_solid_ties = find_average(filter_col_by_string(data_from_csv, "print", "_solid"))
print("Avg Print $", avg_print_ties)
print("Avg Paisley $", avg_paisley_ties)
print("Avg Stripes $", avg_striped_ties)
print("Avg Solid $", avg_solid_ties)

print("\n>>> SHOWING STAGE 4 EXAMPLES")

"""
Stage 4: Exporting

CSV or TSV
Excel
Code challenge - export data
"""

# Exporting CSV Files
print("4.a Exporting CSV Files")
from my_utils import write_to_file
## Export Hermes Ties
write_to_file("_data/hermes.csv", hermes_ties)

## Export JCrew Ties
write_to_file("_data/jcrew.csv", jcrew_ties)

## numpy version
print("ERROR line 173")
#numpy.savetxt("numpy_woolTies.csv", wool_ties, delimiter=",", fmt="%s")

# further filter and combine with savetxt
solid_silk_ties = filter_col_by_string(data_from_csv, "print", "_solid")
print("ERROR line 178")
#numpy.savetxt("numpy_solidSilkTies.csv", solid_silk_ties, delimiter=",", fmt="%s")

## Writing more functions to export csv files
print("4.b More functions")
#i.e. save two columns
from my_utils import write_brand_and_price_to_file
write_brand_and_price_to_file('_data/test.csv', hermes_ties)

from my_utils import write_min_max_csv, write_two_cols, write_append_file
write_min_max_csv('_data/write_min_max.csv', hermes_ties[1:])

write_two_cols('_data/write_two_cols.csv', hermes_ties[1:], 3, 7)

write_append_file('_data/write_min_max.csv', jcrew_ties[1:])

from my_utils import write_sorted_prices, write_sorted_string
write_sorted_prices('_data/write_sorted_price.csv', jcrew_ties[1:], "ascending")

# Exporting to Excel
print("4.c Exporting to Excel")

# reusing a function before to grab a new data sample
kiton_ties = filter_col_by_string(data_from_csv, "brandName", "Kiton")

from my_utils import save_spreadsheet
save_spreadsheet('kiton.xlsx', kiton_ties)

print("\n>>> SHOWING STAGE 5 EXAMPLES")

"""
Stage 5: Charts and Tables

This section may cover matplotlib with ggplot stylesheet for creating views of charts and tables.

Bar Charts
Line Charts
Tables
Code Challenge - create a chart
"""

# Line charts
print("5.a Line Charts")

from my_utils import create_line_chart
create_line_chart(prices_of(hermes_ties), "Distribution of Prices for Hermes Ties", "_charts/line_hermes.png")
create_line_chart(prices_of(jcrew_ties), "Distribution of Prices for J.Crew Ties", "_charts/line_jcrew.png")
create_line_chart(prices_of(kiton_ties), "Distribution of Prices for Kiton Ties", "_charts/line_kiton.png")


# Bar charts
print("5.b Bar Charts")
from numpy_utils import plot_all_bars
plot_all_bars(price_in_float,  "_charts/all_prices.png")
print("_charts/created all_prices.png")

from my_utils import create_bar_chart, group_prices_by_range
price_groups = group_prices_by_range(price_in_float)
create_bar_chart(price_groups, "_charts/price_in_groups.png") 
print("created _charts/price_in_groups.png")


print("5.c Tables")
from my_utils import create_table
brands = my_csv['brandName']
columns = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
write_brand_and_price_to_file("_data/tempTableFile.csv", data_from_csv)
brand_and_price_data = open_with_csv("_data/tempTableFile.csv", d=',')
create_table(brand_and_price_data, price_groups, brands, columns, "_charts/prices_in_table.png") 
print("created _charts/prices_in_table.png")

print("5.d quickly check to see if there might be discounted items for these brands...")
my_list = ["Burberry", "Dolce & Gabbana", "Gucci", "Yves Saint Laurent"]
for x in my_list:
    print_brand_avg_min(x, data_from_csv)

print("\n>>> SHOWING STAGE 6 EXAMPLES")

"""
Stage 6: Creating Reports

Export a chart as image
Edit title and axes labels
Code Challenge - save chart image with certain resolution and labels
"""

labels = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"] 
plot1 = plot_minimal_graph(price_in_groups, labels)
table_text = build_table_text(data_sample, brand_names)
table_text = build_table_text(brand_and_price_data, brands)
plot2 = plot_graph_with_table(table_text[0], table_text[1], labels)


pp = PdfPages('foo.pdf')
pp.savefig(plot1, bbox_inches='tight')
pp.savefig(plot2, bbox_inches='tight')
pp.close()

