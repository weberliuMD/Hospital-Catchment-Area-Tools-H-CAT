import datasetgeocode as dsg
import pandas as pd

data = dsg.load_data("./Admissions_data/HTD_Trim.csv")

print(dsg.gmaps_geocode(data.iloc[1][1]))
