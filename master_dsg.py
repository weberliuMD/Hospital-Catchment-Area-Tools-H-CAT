import datasetgeocode as dsg
import pandas as pd

data = dsg.load_data("./Admissions_data/HTD_Trim.csv")

height = data.shape[0]

geocodedOutput = pd.DataFrame()

print(height)
for i in range(height):
    originalData = data.iloc[i]
    od = pd.DataFrame(originalData).T
    od = od.reset_index()
    od = od.drop(['index'], axis=1)
    geocodedData = dsg.gmaps_geocode(data.iloc[i][1])
    combinedData = pd.concat([od, geocodedData], axis=1)
    geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True)
    print("Completed row", i)
    export_csv = geocodedOutput.to_csv(r'./Geocoded_output_gmaps.csv', index = False, header=True, encoding='utf_8_sig')
    if (i % 200 == 0):
        fileName = "./Geocoded_output_gmaps_" + str(i) + "_PROGRESS.csv"
        export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')


