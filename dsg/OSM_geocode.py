import requests
import pandas as pd

def OSM_geocode(Address):
    '''
    gmaps_geocode(Address) is a function developed to query the google Maps geocoding API.
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
    osmREST = "https://nominatim.openstreetmap.org/search?q="
    webAddress = osmREST + Address + "&format=json"
    print("Request sent to "+ webAddress)
    headers = {
        'User-Agent': 'Hospital_PatientAddress_Geocode',
        'From': 'weber.liu@sydney.edu.au'  # This is another valid field
    }
    r = requests.get(webAddress, headers=headers).json()
    # print(respData)
    if len(r) != 0:
        df = pd.DataFrame(r)
        while (df.shape[0] > 1):
            removeLine = df.shape[0]-1
            dConcat = pd.DataFrame(df.iloc[removeLine]).T
            dConcat = dConcat.reset_index()
            dConcat = dConcat.drop(['index'], axis = 1)
            dConcat = dConcat.add_suffix("_lvl"+str(removeLine))
            dConcat = dConcat.dropna(axis='columns')
            df = df.drop([removeLine])
            df = df.join(dConcat, lsuffix="_lvl"+str(removeLine-1), rsuffix="_lvl"+str(removeLine))
            # df = pd.concat([df, dConcat], axis = 1)
        df = df.assign(status = ["200"])
        return df
    else:
        df = pd.DataFrame()
        df = df.assign(status = ["Address not found"])
        return df