# GeocodingTools
Python based scripts used to rapidly geocode hospital datasets.
**Developed by Weber Liu, 2019**
## INTRODUCTION
This set of scripts have been developed to use a variety of Geocoding APIs in order to convert hostpial patient data, in Address format, to a latitude/longitude format. Additional data returned from geocoding APIs will be retained in a separate file for any further analyses if necessary.
GeocodingTools is separated into two separate packages:
* datasetprep (dsp)
* DatasetGeocode
* DatasetRecombine
The files do not have to be used together, however it is optimal if files ARE used in conjunction. Consult individual documentations to determine how the individual packages should be used.  

## datasetprep (dsp)
datasetprep is a series of scripts, whose primary purpose is to prepare the original hospital file dataset for use with the DatasetGeocode package. It deals with data where:
* Patient data is NOT de-identified, and needs to be de-identified
* Patient address data is separated across multiple columns
* The database needs to be re-formatted into only PatientID and Address columns \(for use with DatasetGeocode\).

DatasetPrep is primarily based on the Python library **Pandas**
Functions available in datasetprep includes *load_data(fileName)*

## datasetgeocode (dsg)
DatasetGeocode's primary purpose is to geocode 'prepared' datasets to be used with various geocoding APIs. API keys may need to be provided. All returned data from these APIs will be provided in a formatted manner and returned as a .csv file. The APIs currently supported in DatasetGeocode include:
- [ ] Google Maps Geocoding API (https://developers.google.com/maps/documentation/geocoding)
- [ ] Bing Maps REST Services (https://docs.microsoft.com/en-us/bingmaps/rest-services)
- [ ] MAPQUEST developers Open Geocoding API (https://developer.mapquest.com/documentation/open/geocoding-api/)
- [ ] OpenStreetMaps(OSM) Nomatim Geocoder (https://nominatim.openstreetmap.org)
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

## datasetrecombine (dsr)
Following the Dataset separation by DatasetPrep, if necessary, this data will be recombined using the currently library.

## datasetnetworkanalysis(dsna)