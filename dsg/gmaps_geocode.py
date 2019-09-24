import urllib3
import json
import pandas as pd

def gmaps_geocode(Address, APIKEY):
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
        return "missing"
