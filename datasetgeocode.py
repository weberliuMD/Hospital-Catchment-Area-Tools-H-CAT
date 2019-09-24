#Import Geocoding API scripts
# from dsg import ArcGIS_geocode as arcgis
# from dsg import bingmaps_geocode as bing
from dsg import gmaps_geocode as gmaps
# from dsg import here_geocode as here
# from dsg import mapquest_geocode as mapquest
# from dsg import OSM_geocode as osm
# from dsg import tomtom_geocode as tomtom
# from dsg import yahoo_geocode as yahoo

#Import API Keys
import keys

#Imports for file loading
import pandas as pd


def load_data (fileDir):
    '''
    load_data(fileDir) is a simpler alterative in the dsg module, compared to the dsp module. This allows 
    simple file loading, given the location of the .csv file. 
    This function within the module expects data to be in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    With this two-column data, the data will be returned as a dataFrame
    
    Author: Weber Liu
    Date created: 25/09/2019
    '''
    data = pd.read_csv(fileDir)
    print(data.head())
    return data

def gmaps_geocode(Address, APIKEY=keys.GMAPS_APIKEY,):
    '''
    gmaps_geocode(Address, APIKEY) is a function developed to query the google Maps geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using Google's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per google cloud console (a sign-up will be required).

    The gmaps REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - individual address data
    - Geometry (Latitude and Longitude)
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return gmaps.gmaps_geocode(Address, APIKEY)

def gmaps_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None):
    data = load_data(fileLocation)
    height = data.shape[0]
    geocodedOutput = pd.DataFrame()
    print(height)
    for i in range(height):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APIKEY==None:
                geocodedData = gmaps_geocode(data.iloc[i][1])
            else:
                geocodedData = gmaps_geocode(Address=data.iloc[i][1], APIKEY = APIKEY)
            combinedData = pd.concat([od, geocodedData], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_gmaps.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_gmaps_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            print("Something went wrong, error was caught, moving on...")
