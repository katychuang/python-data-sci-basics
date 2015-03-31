from s3q1 import *

def number_of_records(data_sample):
    return len(data_sample)

def calculate_sum(data_sample):
    total = 0
    for row in data_sample[1:]:
        price = float(row[2])
        total += price
    return total

def find_average(data_sample, headers=False):
    total = calculate_sum(data_sample)
    size = number_of_records(data_sample)
    if headers:
        total -= 1

    average = total / size
    
    # return average   
    
    return '{:03.2f}'.format(average)

gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")

avg_gucci = find_average(gucci_ties, True)
avg_jcrew = find_average(jcrew_ties, True)


# code above this line is included to make this file compile on its own.
# -------------------------------------------------------------------------

# here is the answer:


def comparison(brand_a, brand_a_avg, brand_b, brand_b_avg):
    brand_name = ""
    if float(brand_a_avg) > float(brand_b_avg):
        brand_name = brand_a
    elif float(brand_a_avg) < float(brand_b_avg):
        brand_name = brand_b
    else:
        brand_name = "neither"
    return "The brand that is more likely to have a higher price tag is: {}".format(brand_name)

sentence = comparison("Gucci", avg_gucci, "J. Crew",  avg_jcrew)

