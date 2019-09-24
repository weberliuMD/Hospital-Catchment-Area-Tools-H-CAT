import urllib3
import json
import pandas as pd

def gmaps_geocode(Address, APIKEY):
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
    gmapsREST = "https://maps.googleapis.com/maps/api/geocode/json?address="
    webAddress = gmapsREST + Address + "&key=" + APIKEY
    print("Request sent to "+ webAddress)
    http = urllib3.PoolManager()
    r = http.request('GET', webAddress)
    r = json.loads(r.data.decode('utf-8'))
    # print(respData)
    if r['status'] == 'OK':
        formattedAddress = r['results'][0]['formatted_address'] #formattedAddress is a str
        address = r['results'][0]['address_components'] #address is a list of dicts
        geometry = r['results'][0]['geometry']['location'] #geometry is a duct with only lat and long     
        df = pd.DataFrame(address)
        numElements = df.shape[0]
        df = df.drop(['short_name'], axis = 1)
        for i in range(numElements):
            df['types'][i]= ''.join(df['types'][i])
        df = df.T
        df.columns = df.iloc[1]
        df = df.drop(['types'], axis = 0)
        df = df.assign(formatted_address = [formattedAddress])
        df = df.assign(latitude = [geometry['lat']])
        df = df.assign(longitude = [geometry['lng']])
        df = df.reset_index()
        df = df.drop(['index'], axis=1)
        return df
    else:
        return r['status']
