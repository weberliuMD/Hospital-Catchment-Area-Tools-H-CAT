import pandas as pd
import math

def dataLoader (fileDir):
    data = pd.read_csv(fileDir)
    print(data.head())
    heightOfData = data.shape[0]
    numberOfColumns = data.shape[1]
    print("The height of the dataset is", heightOfData)
    print("The number of columns are", numberOfColumns, "before removing empty columns")
    
    print("What proportion of a column do you need empty in order for you to drop that columns? - answer in a decimal")
    dropProp = input()
    dropThresh = int(math.ceil(heightOfData*float(dropProp)))
    print("The threshold number of empty columns is", dropThresh, "which represents", dropProp,"amount of your data")
    data = data.dropna(axis=1, how='any', thresh=dropThresh)
    numberOfColumns = data.shape[1]
    print("the number of columns are", numberOfColumns, "after removing empty columns at a", dropProp,"threshold")
    print(data.head())
    return data

