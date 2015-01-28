# coding: utf-8

# numpy_utils for Intro to Data Science with Python
# Author: Kat Chuang
# Created: Nov 2014

# --------------------------------------

import numpy


## Stage 2 begin

fieldNames = ['', 'id', 'priceLabel', 'name','brandId', 'brandName', 'imageLink',
              'desc', 'vendor', 'patterned', 'material']

dataTypes = [('myint', 'i'), ('myid', 'i'), ('price', 'f8'), ('name', 'a200'),
             ('brandId', '<i8'), ('brandName', 'a200'), ('imageUrl', '|S500'), 
             ('description', '|S900'),  ('vendor', '|S100'),  ('pattern', '|S50'),  ('material', '|S50'), ]

def load_data(filename):
	my_csv = numpy.genfromtxt(filename, delimiter='\t', skip_header=1,
                            names=fieldNames, invalid_raise=False, 
                            dtype=dataTypes)
	return my_csv

#2.a count
def size(my_csv):
	print("Length (numpy): {}".format(my_csv.size))

#2.b sum
def calculate_numpy_sum(my_field):
    field_in_float = [float(item) for item in my_field] 
    total = numpy.sum(field_in_float)
    return total

#2.c mean
def find_numpy_average(my_field):
    field_in_float = [float(item) for item in my_field] 
    total = calculate_numpy_sum(field_in_float)
    size = len(my_field)
    average = total / size
    return average

#2.d max, min
def numpy_max(my_field_in_float):
    return numpy.amax(my_field_in_float)
 
def numpy_min(my_field_in_float):
    return numpy.amin(my_field_in_float)



## Stage 2 end

# --------------------------------------

## Stage 3 begin

from my_utils import filter_col_by_string, filter_col_by_float

## Stage 3 end

# --------------------------------------

## Stage 4 begin

from my_utils import write_to_file, write_brand_and_price_to_file

## Stage 4 end

# --------------------------------------

## Stage 5 begin

import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_all_bars(prices_in_float, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    prices = list(map(int, prices_in_float))
    X = numpy.arange(len(prices))
    width = 0.25
    ax.bar(X+width, prices, width) 
    ax.set_xlim([0, 5055])
    fig.savefig(exported_figure_filename)

def create_chart_for_embed(sample, title):
    prices = sorted(map(int, sample))
    x_axis_ticks = list( range(len(sample)) )
    plt.plot(x_axis_ticks, prices, 'g', label='price points', linewidth=2)

def export_chart(sample, title):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    prices = sorted(map(int, sample))
    x_axis_ticks = list( range(len(sample)) )
    ax.plot(x_axis_ticks, prices, 'g', label='price points', linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(title)
    ax.set_ylabel('Number of Ties')
    if len(prices) > 20:
        ax.set_xlim([0, round(len(prices), -1)])
    else:
        ax.set_xlim([0, len(prices)])
    fig.savefig('_charts/' + title + '.png')

def prices_of_list(sampleData):
    temp_list = []
    for row in sampleData[1:]:
        priceCol = float(row[2])
        temp_list.append(priceCol)
    return temp_list

## Stage 5 end

# --------------------------------------

## Stage 6 begin

## Stage 6 end

# --------------------------------------
