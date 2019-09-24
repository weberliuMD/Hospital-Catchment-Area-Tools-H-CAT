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