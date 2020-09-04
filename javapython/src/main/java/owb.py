import sys
import ast
import json
from json import loads

f = open("myfile.txt", "w")
import json
def printSupplierCoverage(x):
    file = open(x)


    file = file.read()
    bidsDictionary = json.loads(file)
    bidsDictionary
    itemTermValues = bidsDictionary['itemTermValues']
    itemTermValues
    import pandas as pd
    df = pd.DataFrame(itemTermValues)
    df

    #itemCoverage
    itemDf = list()
    for itemValue in df['itemValues']:
        itemDf = itemDf+(itemValue)
    pd.DataFrame(itemDf)

    itemCoverage = dict()
    for item in itemDf:
        key = item['itemId']
        if(key in itemCoverage.keys()):
            itemCoverage[key]=itemCoverage[key]+1
        else:
            itemCoverage[key]=1

    print(itemCoverage)


    #supplierCoverage
    supplierCoverage = dict()
    for supplier in df.submitFor:
        if(supplier in supplierCoverage.keys()):
            supplierCoverage[supplier]=supplierCoverage[key]+1
        else:
            supplierCoverage[supplier]=1

    print(supplierCoverage)

    for x in supplierCoverage.keys():
        f.write(x +":")
        f.write(str(supplierCoverage[x]))

    f.close()

print ("Supplier Coverage::::::::")
printSupplierCoverage('/Users/i506644/workbench/workbench/javapython/src/main/java/bids.json')
