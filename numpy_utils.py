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

def size(my_csv):
	print("Shape (rows, col): {}".format(my_csv.shape))

def number_of_records(my_csv):
	print("Length: {}".format(my_csv.size))

## Stage 2 end

# --------------------------------------

## Stage 3 begin

def filter_col_by_string(theData, field, filterCondition):
    filteredRows = []
    
    #find index of field in first row
    col = int(theData[0].index(field))
    
    for row in theData[1:]:
        if row[col] == filterCondition:
            filteredRows.append(row)
    return filteredRows

def filter_col_by_float(theData, field, direction, filterCondition):
    filteredRows = []
    
    #find index of field in first row
    col = int(theData[0].index(field))
    cond = float(filterCondition)
    
    for row in theData[1:]:
        element = float(row[col])
        
        if direction == "<":
            if element < cond:
                filteredRows.append(row)
                
        elif direction == "<=":
            if element <= cond:
                filteredRows.append(row)

        elif direction == ">":
            if element > cond:
                filteredRows.append(row)

        elif  direction == ">=":
            if element >= cond:
                filteredRows.append(row)
                
        elif  direction == "==":
            if element == cond:
                filteredRows.append(row)
        else:
            pass
        
    return filteredRows

def calculateNumpySum(theData):
    tSum = 0
    for row in theData:
        price = float(row[2])
        tSum += price
    return tSum

## Stage 3 end

# --------------------------------------

## Stage 4 begin

def write_brand_and_price_to_file(filename, dataSample):

    # confirm that the columns only have two columns, otherwise take the two fields
    numFields = len(dataSample[0])
    
    brandFieldIndex = 5 #int(dataSample[0].index("brand"))
    priceFieldIndex = 2 #int(dataSample[0].index("priceLabel"))
    
    #if numFields > 2:
    newArray = []
    for record in dataSample:
        newRecord = [None] * 2
        newRecord[0] = record[brandFieldIndex]
        newRecord[1] = record[priceFieldIndex]
        newArray.append(newRecord)

    # write the file
    writeToFile2(filename, newArray)  

## Stage 4 end

# --------------------------------------

## Stage 5 begin

import matplotlib.pyplot as plt
plt.style.use('ggplot')

def create_chart_for_embed(plot, sample, title):
    prices = sorted(map(int, sample))
    xAxisTicks = list( range(len(prices)) )
    width=0.25
    plot.plot(xAxisTicks, prices, 'g', label='price points',linewidth=2)

def export_chart(sample, title):
    prices = sorted(map(int, sample))
    xAxisTicks = list( range(len(prices)) )
    width=0.25
    tempChartVar = pylab.plot(xAxisTicks, prices, 'g', label='price points',linewidth=2)
    plt.title(title)
    plt.xlabel(title)
    plt.ylabel('Number of Ties')
    if len(prices) > 20:
        plt.xlim([0, round(len(prices), -1)])
    else:
        plt.xlim([0, len(prices)])
    plt.show()
    plt.savefig('_charts/' + title + '.png')

def prices_of_list(sampleData):
    tempList = []
    for row in sampleData[1:]:
        priceCol = float(row[2])
        tempList.append(priceCol)
    return tempList

## Stage 5 end

# --------------------------------------

## Stage 6 begin

## Stage 6 end

# --------------------------------------
