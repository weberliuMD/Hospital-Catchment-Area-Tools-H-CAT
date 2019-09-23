import pandas as pd

def dataLoader (fileDir):
    data = pd.read_csv(fileDir)
    print(data.head())
    return data

