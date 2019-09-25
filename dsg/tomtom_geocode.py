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
    Date Created: 26/09/2019
    '''
    #Build query address
    TomTomREST_1 = "https://api.tomtom.com/search/2/geocode/"
    TomTomREST_2 = ".JSON?key="
    webAddress = TomTomREST_1 + Address + TomTomREST_2 + APIKEY

    print("Request sent to "+ webAddress)
    r = requests.get(webAddress).json()
    try:
        if (r['httpStatusCode'] == 404):
            df = pd.DataFrame({'statusCode':[404]})
            return df
    except:
        numResults = r['summary']['numResults']
        r = r['results']
        if (numResults > 0):
            df = pd.DataFrame()
            for i in range(numResults):
                rr = r[i]
                locationId = pd.DataFrame({'locationId':[rr['id']]}).add_suffix("_"+str(i))
                Address = pd.DataFrame([rr['address']]).add_suffix("_"+str(i))
                lat = pd.DataFrame({'lat':[rr['position']['lat']]}).add_suffix("_"+str(i))
                lng = pd.DataFrame({'lng':[rr['position']['lon']]}).add_suffix("_"+str(i))
                df = pd.concat([df, locationId, Address, lat, lng], axis = 1)
            statusCode = pd.DataFrame({'statusCode':['200']})
            df = pd.concat([df, statusCode], axis = 1)
            return df
        else:
            df = pd.DataFrame({'statusCode':['No data']})
            return df

