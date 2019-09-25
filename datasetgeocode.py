#Import Geocoding API scripts
# from dsg import ArcGIS_geocode as arcgis
from dsg import bingmaps_geocode as bing
from dsg import gmaps_geocode as gmaps
from dsg import HERE_geocode as here
from dsg import mapquest_geocode as mq
from dsg import OSM_geocode as osm
from dsg import tomtom_geocode as tomtom
# from dsg import yahoo_geocode as yahoo

#Import API Keys
import keys

#Imports for file loading
import pandas as pd

#import time to ensure no server overload
import time

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

def gmaps_geocode(Address, APIKEY=keys.GMAPS_APIKEY):
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

def gmaps_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None, startPos = 0, endPos = None):
    ''''
    gmaps_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the google Maps geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APIKEY - if an APIKEY is provided, it will be used. Otherwise, the APIKEY in keys.py will be used.

    This batch geocoder has the dependency of the gmaps_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_gmaps.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
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
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")

def OSM_geocode(Address):
    '''
    OSM_geocode(Address, APIKEY) is a function developed to query the Nominatim (OSM) geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using OSM's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.

    The OSM REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - Geometry (Latitude and Longitude)
    - Place_id and OSM_id identifiers 
    - A status of whether or not retrieval was complete (200 == GOOD)
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return osm.OSM_geocode(Address)

def OSM_batch_geocode(fileLocation, saveProgress = 200, startPos = 0, endPos = None):
    ''''
    OSM_batch_geocode(fileLocation, saveProgress = 200) is a function developed to query the Nominatim geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    as OSM and Nominatim are open-sourced, there is no need for an API key

    This batch geocoder has the dependency of the OSM_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_OSM.csv")
    
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = OSM_geocode(Address=data.iloc[i][1])
            combinedData = pd.concat([od, geocodedData], axis=1)
            # combinedData = od.join(geocodedData)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_OSM.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_OSM_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")
        time.sleep(1)

def mapquest_geocode(Address, APIKEY=keys.MAPQUEST_APIKEY):
    '''
    mapquest_geocode(Address, APIKEY) is a function developed to query the mapquest (by Verizon) geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using mapquest's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.

    The mapquest REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address with various degrees of administrative areas, along with postal codes
    - Geometry (latitude and longitude)
    - mapUrl - map image of the location
    - MapQuest linkID, geocodeQuality and geocodeQualityCode
    - A status of whether or not retrieval was complete (response will be 0, regardless of whether or not it was properly geocoded)
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return mq.mapquest_geocode(Address, APIKEY)

def mapquest_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None, startPos = 0, endPos = None):
    ''''
    mapquest_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the mapquest geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APIKEY - if an APIKEY is provided, it will be used. Otherwise, the APIKEY in keys.py will be used.

    This batch geocoder has the dependency of the mapquest_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_mapquest.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APIKEY==None:
                geocodedData = mapquest_geocode(data.iloc[i][1])
            else:
                geocodedData = mapquest_geocode(Address=data.iloc[i][1], APIKEY = APIKEY)
            combinedData = pd.concat([od, geocodedData], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_mapquest.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_mapquest_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")

def mapquest_open_geocode(Address, APIKEY=keys.MAPQUEST_APIKEY):
    '''
    mapquest_open_geocode(Address, APIKEY) is a function developed to query the mapquest (OSM) geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using mapquest's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.

    The mapquest REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address with various degrees of administrative areas, along with postal codes
    - Geometry (latitude and longitude)
    - mapUrl - map image of the location
    - MapQuest linkID, geocodeQuality and geocodeQualityCode
    - A status of whether or not retrieval was complete (response will be 0, regardless of whether or not it was properly geocoded)
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return mq.mapquest_open_geocode(Address, APIKEY)

def mapquest_open_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None, startPos = 0, endPos = None):
    ''''
    mapquest_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the mapquest geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APIKEY - if an APIKEY is provided, it will be used. Otherwise, the APIKEY in keys.py will be used.

    This batch geocoder has the dependency of the mapquest_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_mapquest.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APIKEY==None:
                geocodedData = mapquest_open_geocode(data.iloc[i][1])
            else:
                geocodedData = mapquest_open_geocode(Address=data.iloc[i][1], APIKEY = APIKEY)
            combinedData = pd.concat([od, geocodedData], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_mapquest.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_mapquest_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")

def bing_geocode(Address, APIKEY=keys.BING_APIKEY):
    '''
    bing_geocode(Address) is a function developed to query the Bing Maps geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using Bing's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per Bing Maps console (a sign-up will be required).

    The BING REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - Geometry (Latitude and Longitude)
    - Confidence of thte address and geocoding system
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return bing.bing_geocode(Address, APIKEY)

def bing_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None, startPos = 0, endPos = None):
    ''''
    bing_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the bing maps geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APIKEY - if an APIKEY is provided, it will be used. Otherwise, the APIKEY in keys.py will be used.

    This batch geocoder has the dependency of the bing_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_bing.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APIKEY==None:
                geocodedData = bing_geocode(data.iloc[i][1])
            else:
                geocodedData = bing_geocode(Address=data.iloc[i][1], APIKEY = APIKEY)
            combinedData = pd.concat([od, geocodedData], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_bing.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_bing_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")

def here_geocode(Address, APP_ID = keys.HERE_APPID, APP_CODE = keys.HERE_APPCODE):
    '''
    here_geocode(Address) is a function developed to query the HERE geocoding API.
    This function takes in the argument of:
    Address: The address of the patient, spaces allowed - fuzzy matching using HERE's Algorithm
    will clarify any issues. Provide as much detail as possible in the address.
    APIKEY: The APIKEY as per HERE console (a sign-up will be required).

    The HERE REST-API will return a JSON dataset, and from that, this application will determine if the address
    were entered correctly (i.e. status 200 OK), and then interpret the data into:
    - Formatted Address (can be used for further geocoding with alternative systems)
    - Geometry (Latitude and Longitude)
    - Confidence of thte address and geocoding system
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    return here.here_geocode(Address, APP_ID, APP_CODE)

def here_batch_geocode(fileLocation, saveProgress = 200, APP_ID = None, APP_CODE = None, startPos = 0, endPos = None):
    ''''
    here_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the HERE maps geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APP_ID - the APP_ID returned upon signing up for HERE
    APP_CODE - the APP_CODE returned upon singing up for HERE

    This batch geocoder has the dependency of the here_geocode() function within this module.

    Author: Weber Liu
    Date Created: 25/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_here.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APP_ID==None and APP_CODE == None:
                geocodedData = here_geocode(data.iloc[i][1])
            else:
                geocodedData = here_geocode(Address=data.iloc[i][1], APP_ID = APP_ID, APP_CODE = APP_CODE)
            combinedData = pd.concat([od, geocodedData], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_here.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_here_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")


def tomtom_geocode(Address, APIKEY = keys.TOMTOM_APIKEY):
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
    - TOMTOM api identifier ID
    This data is then returned as a DataFrame to the user.

    Author: Weber Liu
    Date Created: 26/09/2019
    '''
    return tomtom.tomtom_geocode(Address, APIKEY)

def tomtom_batch_geocode(fileLocation, saveProgress = 200, APIKEY = None, startPos = 0, endPos = None):
    ''''
    tomtom_batch_geocode(fileLocation, saveProgress = 200, APIKEY=None) is a function developed to query the TomTom maps geocoding API.
    This function takes in the argument of:
    fileLocation - the location of the .csv file in the following format:
    ------------------------------------------
    |Patient identifier | Patient address    |
    ------------------------------------------
    |ID_001             | 123 Address st, ...|
    (etc...)
    ------------------------------------------
    saveProgress - the number of geocodes conducted before a progress file is saved - this will occur alongside the live-save files
    APIKEY - the API Key for the application you obtain from the TomTom website

    This batch geocoder has the dependency of the tomtom_geocode() function within this module.

    Author: Weber Liu
    Date Created: 26/09/2019
    '''
    data = load_data(fileLocation)
    height = data.shape[0]
    if (startPos == 0):
        geocodedOutput = pd.DataFrame()
    else:
        geocodedOutput = pd.read_csv("./Geocoded_output_tomtom.csv")
    if (endPos == None):
        endPos = height
        print("end position is", height)
    for i in range(startPos, endPos):
        originalData = data.iloc[i]
        od = pd.DataFrame(originalData).T
        od = od.reset_index()
        od = od.drop(['index'], axis=1)
        try:
            geocodedData = None
            if APIKEY == None:
                geocodedData = tomtom_geocode(data.iloc[i][1])
            else:
                geocodedData = tomtom_geocode(Address=data.iloc[i][1], APIKEY = APIKEY)
            print("combining data")
            combinedData = pd.concat([od, geocodedData], axis=1)
            print("appending data to list")
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            print("Completed row", i)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
        except:
            df = pd.DataFrame({'statusCode':['Error!']})
            combinedData = pd.concat([od, df], axis=1)
            geocodedOutput = geocodedOutput.append(combinedData, ignore_index = True, sort=False)
            export_csv = geocodedOutput.to_csv('./Geocoded_output_tomtom.csv', index = False, header=True, encoding='utf_8_sig')
            if (i % saveProgress == 0):
                fileName = "./Geocoded_output_tomtom_" + str(i) + "_PROGRESS.csv"
                export_csv = geocodedOutput.to_csv(fileName, index = False, header=True, encoding='utf_8_sig')
            print("Something went wrong, error was caught, moving on...")