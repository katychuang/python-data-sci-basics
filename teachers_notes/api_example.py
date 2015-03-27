# show how product information is collected from an API

import urllib2
import json

url = "http://api.shopstyle.com/api/v2/"
ties = "{}products?pid={}&cat=mens-ties&limit=100".format(url, mykeys.apiKey)
jsonResponse = urllib2.urlopen(ties)
data = json.load(jsonResponse)

total = data['metadata']['total'] 
limit = data['metadata']['limit'] 
offset = data['metadata']['offset'] 
pages = (total / limit)

print "{} total, {} per page. {} pages to process".format(total, limit, pages)

import pandas as pd 

tmp = pd.DataFrame(data['products'])
dfs = {}

for page in range(pages+1):
    allTies = "{}products?pid={}&cat=mens-ties&limit=100&offset={}&sort=popular".format(url, mykeys.apiKey, (page*50))
    jsonResponse = urllib2.urlopen(allTies)
    data = json.load(jsonResponse)
    dfs[page] = pd.DataFrame(data['products'])

dfs.keys()  
df = pd.concat(dfs, ignore_index=True)

# Cleaning records, removing duplicates
df = df.drop_duplicates('id')
df['priceLabel'] = df['priceLabel'].str.replace('$', '')
df['priceLabel'] = df['priceLabel'].astype(float)

#split brand into 2 columns

def breakId(x,y=0):
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


