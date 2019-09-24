# datasetprep (dsp)
Python scripts used to prepare datasets for geocoding
**Developed by Weber Liu, 2019**

## datasetgeocode (dsg)
DatasetGeocode's primary purpose is to geocode 'prepared' datasets to be used with various geocoding APIs. API keys may need to be provided. All returned data from these APIs will be provided in a formatted manner and returned as a .csv file. The APIs currently supported in DatasetGeocode include:
- [ ] Google Maps Geocoding API (https://developers.google.com/maps/documentation/geocoding)
- [ ] Bing Maps REST Services (https://docs.microsoft.com/en-us/bingmaps/rest-services)
- [ ] MAPQUEST developers Open Geocoding API (https://developer.mapquest.com/documentation/open/geocoding-api/)
- [ ] OpenStreetMaps(OSM) Nominatim Geocoder (https://nominatim.openstreetmap.org)
    - [ ] NetToolkit Geocoding via OSM (https://www.nettoolkit.com)
    - [ ] LocationIQ Geocoding via OSM (https://locationiq.com/)
    - [ ] OpenCageData Geocoding via OSM (https://opencagedata.com/)
- [ ] HERE Geocoding API (https://developer.here.com/documentation/geocoder/topics/what-is.html)
- [ ] ARCGIS REST API (https://developers.arcgis.com/rest/geocode/api-reference/geocoding-geocode-addresses.htm)
- [ ] TOMTOM Geocoding API (https://developer.tomtom.com/search-api/search-api-documentation-geocoding/geocode)
- [ ] Yahoo! Maps Web Services Geocoding API (https://developer.yahoo.com/maps/rest/V1/geocode.html)
 Melissa Geocoding (https://www.melissa.com/geocoding)

*Non-Vietnam Geocoding systems
- [ ] Texas A&M (USA) Geoservices (http://geoservices.tamu.edu/Services/Geocode/WebService/)
- [ ] TIGER USA Geocoding (http://www.tigergeocoder.com/)

## API KEYS
To use the dsg tools, it is important to have the relevant API keys. API keys can be stored in the root folder, and will be imported automatically when using the datasetprep module. Each geocoding source will have its own necessary API Keys. Detail will be as follows.
### GMAPS API Key
The GMAPS API Key can be obtained from https://console.cloud.google.com - it is necessary to sign up with a billing account. First time users will be provided with promotional credits, as well as monthly credits for use with the Google Maps platform (Further research may be necessary with regards to this). When signing up, it will query which APIs you wish to activate. The Geocoding APIs from Google are hidden within the **Places API**. Make sure this is selected.
GMAPS will deliver the API Key and you can add this to the keys.py script in the root directory. 