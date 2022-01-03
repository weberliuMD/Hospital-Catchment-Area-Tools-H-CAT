import requests
import pandas as pd

def bing_geocode(Address, APIKEY):
    '''
    bing_geocode(Address) is a function developed to query the Bing Maps geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using Bing's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per Bing Maps console (a sign-up will be required).

    The gmaps REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - Geometry (Latitude and Longitude)
    - Confidence of thte address and geocoding system
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    bingREST = "http://dev.virtualearth.net/REST/v1/Locations?"
    webAddress = bingREST + "query=" + Address + "&key=" + APIKEY
    print("Request sent to "+ webAddress)
    r = requests.get(webAddress).json()
    authStatus = r['authenticationResultCode']
    if (authStatus != 'ValidCredentials'):
        print("Authentication is INVALID, make sure your API KEY is valid")
    statusCode = r['statusCode'] # Either 200 OR 401
    if (statusCode == 200):
        address = r['resourceSets'][0]['resources'][0]['address']
        confidence = r['resourceSets'][0]['resources'][0]['confidence']
        geocodes = r['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']
        df = pd.DataFrame([address])
        confidence = pd.DataFrame({'confidence':[confidence]})
        lat = pd.DataFrame({'lat':[geocodes[0]]})
        lng = pd.DataFrame({'lng':[geocodes[1]]})
        statusCode = pd.DataFrame({'statusCode':[statusCode]})
        df = pd.concat([df, confidence, lat, lng, statusCode], axis = 1)
        return df
    else:
        df = pd.DataFrame({'statusCode':[statusCode]})
        return df

