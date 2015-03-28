# show how product information is collected from an API

# first import packages
import urllib2
import json
import pandas as pd

# this is your api information 
my_api_key = "XXXXXXXXXXX"

# build the api url, passing in your api key
url = "http://api.shopstyle.com/api/v2/"
ties = "{}products?pid={}&cat=mens-ties&limit=100".format(url, my_api_key)

# open the connection to the api endpoint
jsonResponse = urllib2.urlopen(ties)
data = json.load(jsonResponse)

# parse the response to find out how many pages of results there are
total = data['metadata']['total'] 
limit = data['metadata']['limit'] 
offset = data['metadata']['offset'] 
pages = (total / limit)

print "{} total, {} per page. {} pages to process".format(total, limit, pages)

# tmp = pd.DataFrame(data['products'])

# set up an empty dictionary
dfs = {}

# connect with api again, page by page and save the results to the dictionary 
for page in range(pages+1):
    allTies = "{}products?pid={}&cat=mens-ties&limit=100&offset={}&sort=popular".format(url, mykeys.apiKey, (page*50))
    jsonResponse = urllib2.urlopen(allTies)
    data = json.load(jsonResponse)
    dfs[page] = pd.DataFrame(data['products'])

# convert the dictionary to a pandas data frame object
df = pd.concat(dfs, ignore_index=True)

# Cleaning records, removing duplicates
df = df.drop_duplicates('id')
df['priceLabel'] = df['priceLabel'].str.replace('$', '')
df['priceLabel'] = df['priceLabel'].astype(float)

# continue cleaning up the data, split data into columns as necesary
def breakId(x, y = 0):
    try:
        y = x["id"]
    except:
        pass
    return y

def breakName(x, y=""):
    try:
        y = x["name"]
    except:
        pass
    return y

df['brandId'] = df['brand'].map(breakId);
df['brandName'] = df['brand'].map(breakName);

def breakCanC(x,y=""):
    try:
        y = x[0]["canonicalColors"][0]["name"]
    except:
        pass
    return y

def breakColorName(x, y=""):
    try:
        y = x[0]["name"]
    except:
        pass
    return y

def breakColorId(x, y=""):
    try:
        y = x[0]["canonicalColors"][0]["id"]
    except:
        pass
    return y

df['colorId'] = df['colors'].map(breakColorId);
df['colorFamily'] = df['colors'].map(breakCanC);
df['colorNamed'] = df['colors'].map(breakColorName);

# export to data.csv
df.to_csv("data.csv", sep='\t', encoding='utf-8', 
          columns=['id', 'priceLabel', 'name','brandId', 'brandName', 'colorId', 'colorFamily', 'colorNamed'])


