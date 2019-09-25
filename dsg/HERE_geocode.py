import requests
import pandas as pd

def here_geocode(Address, APP_ID, APP_CODE):
    '''
    here_geocode(Address) is a function developed to query the HERE geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using HERE's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per google cloud console (a sign-up will be required).

    The HERE REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - individual address data
    - Geometry (Latitude and Longitude)
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    Updated: 26/09/2019
    '''

    HEREREST = "https://geocoder.api.here.com/6.2/geocode.json?app_id="
    webAddress = HEREREST + APP_ID + "&app_code=" + APP_CODE + "&searchtext=" + Address

    print("Request sent to "+ webAddress)
    r = requests.get(webAddress).json()
    r = r['Response']['View']
    if (len(r) > 0):
        numResults = len(r[0]['Result'])
        df = pd.DataFrame()
        for i in range(numResults):
            rr = r[0]['Result'][i]['Location']
            locationId = pd.DataFrame({'locationId':[rr['LocationId']]}).add_suffix("_"+str(i))
            lat = pd.DataFrame({'lat':[rr['NavigationPosition'][0]['Latitude']]}).add_suffix("_"+str(i))
            lng = pd.DataFrame({'lng':[rr['NavigationPosition'][0]['Longitude']]}).add_suffix("_"+str(i))
            Address = pd.DataFrame([rr['Address']]).drop(['AdditionalData'], axis = 1).add_suffix("_"+str(i))
            df = pd.concat([df, Address, locationId, lat, lng], axis = 1)
        statusCode = pd.DataFrame({'statusCode':['200']})
        df = pd.concat([df, statusCode], axis = 1)
        return df
    else:
        df = pd.DataFrame({'statusCode':['No data']})
        return df