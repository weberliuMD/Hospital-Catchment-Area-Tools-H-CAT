import requests
import pandas as pd

def tomtom_geocode(Address, APIKEY):
    '''
    tomtom_geocode(Address) is a function developed to query the TomTom Search geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using TomTom's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per TomTom developer (a sign-up will be required).

    The gmaps REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - Geometry (Latitude and Longitude)
    - Confidence of thte address and geocoding system
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    #Build query address
    TomTomREST_1 = "https://api.tomtom.com/search/2/geocode/"
    TomTomREST_2 = ".JSON?key="
    webAddress = TomTomREST_1 + Address + TomTomREST_2 + APIKEY

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

