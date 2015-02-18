# coding: utf-8

#
# Intro to Data Science with Python
# Robot demo
# Author: Kat Chuang
# Created: Nov 2014

# --------------------------------------

from my_utils import *

data_from_csv = open_with_csv('data.csv')

def plot_bar_graphs(mypdf, data_sample, brand, conditions):
  for cond in conditions: 
    item_sample = filter_col_by_string(data_sample, brand, cond)
    y = [float(x[2]) for x in item_sample[1:]]
    price_groups = group_prices_by_range(y) 
    item_chart = plot_minimal_graph(price_groups, [], cond)
    mypdf.savefig(item_chart, bbox_inches='tight')

mypdf = PdfPages('reports.pdf')
plot_bar_graphs(mypdf, data_from_csv, "brandName", ["DKNY", "Gucci", "Kiton"])
mypdf.close()
