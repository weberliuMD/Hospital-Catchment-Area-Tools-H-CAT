import urllib3
import json

def gmaps_geocode(Address, APIKEY):
    gmapsREST = "https://maps.googleapis.com/maps/api/geocode/json?address="
    webAddress = gmapsREST + Address + "&key=" + APIKEY
    print("Request sent to "+ webAddress)
    http = urllib3.PoolManager()
    r = http.request('GET', webAddress)
    response = json.loads(r.data.decode('utf-8'))
    # print(respData)
    if response['status'] == 'OK':
        
        
        return response
    else:
        return
