import pandas as pd

def dataLoader (fileDir):
    data = pd.read_csv(fileDir)
    data.head()
    return data
