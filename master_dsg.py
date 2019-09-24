import datasetgeocode as dsg
import pandas as pd

data = dsg.load_data("./Admissions_data/HTD_Trim.csv")

height = data.shape[0]
print(height)
for i in range(height):
    originalData = data.iloc[1]
    od = pd.DataFrame(originalData).T
    od = od.reset_index()
    od = od.drop(['index'], axis=1)
    geocodedData = dsg.gmaps_geocode(data.iloc[1][1])
    combinedData = pd.concat([od, geocodedData], axis=1)
    print(combinedData)

