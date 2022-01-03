import pandas as pd
import math

def load_data (fileDir):
    """
    load_data(fileDir) takes in the location of the .csv file, and parses it into a dataframe object 
    under the pandas library. It will then prompt an input for the proportion of lines to threshold before
    removing a column.
    This function will return a dataframe containing the thresholded dataset from a .csv file

    Author: Weber Liu
    Date first written: 23/09/2019
    Date last updated: 23/09/2019
    """

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