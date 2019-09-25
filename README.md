# Hospital Catchment Area Tools (H-CAT)
Python based scripts used to rapidly process hospital admissions data, geocode hospital datasets, and calculate hospital catchment areas.

**Developed by Weber Liu, 2019**
## INTRODUCTION
This set of scripts have been developed to use a variety of Geocoding APIs in order to convert hostpial patient data, in Address format, to a latitude/longitude format. Additional data returned from geocoding APIs will be retained in a separate file for any further analyses if necessary.
H-CAT is separated into two separate packages:
* datasetprep (dsp)
* datasetgeocode (dsg)
* datasetrecombine (dsr)
* datasetnetworkanalysis (dsna)
The files do not have to be used together, however it is optimal if files ARE used in conjunction. Consult individual documentations to determine how the individual packages should be used.  

## DEPENDENCIES
Before using any of the scripts, ensure you have installed (pip install)
* requests
* pandas

## datasetprep (dsp)
datasetprep is a series of scripts, whose primary purpose is to prepare the original hospital file dataset for use with the datasetgeocode (dsg) package. It deals with data where:
* Patient data is NOT de-identified, and needs to be de-identified
* Patient address data is separated across multiple columns
* The database needs to be re-formatted into only PatientID and Address columns \(for use with DatasetGeocode\).

DatasetPrep is primarily based on the Python library **Pandas**
Functions available in datasetprep includes *load_data(fileName)*

## datasetgeocode (dsg)
DatasetGeocode's primary purpose is to geocode 'prepared' datasets to be used with various geocoding APIs. API keys may need to be provided. All returned data from these APIs will be provided in a formatted manner and returned as a .csv file. The APIs currently supported in DatasetGeocode include:
- ✔ Google Maps Geocoding API (https://developers.google.com/maps/documentation/geocoding)
- ✔ Bing Maps REST Services (https://docs.microsoft.com/en-us/bingmaps/rest-services)
- ✔ Mapquest (Verizon) developers Geocoding API (https://developer.mapquest.com/documentation/geocoding-api/)
- ✔ OpenStreetMaps(OSM) 
    - ✔ Nominatim Geocoder (https://nominatim.openstreetmap.org)
    - :o: NetToolkit Geocoding via OSM (https://www.nettoolkit.com)
    - :o: LocationIQ Geocoding via OSM (https://locationiq.com/)
    - :o: OpenCageData Geocoding via OSM (https://opencagedata.com/)
    - ✔ Mapquest developers OPEN Geocoding API (https://developer.mapquest.com/documentation/open/geocoding-api/)
- ✔ HERE Geocoding API (https://developer.here.com/documentation/geocoder/topics/what-is.html)
- ❌ ARCGIS REST API (https://developers.arcgis.com/rest/geocode/api-reference/geocoding-geocode-addresses.htm) - **PAID SERVICE**
- ✔ TOMTOM Geocoding API (https://developer.tomtom.com/search-api/search-api-documentation-geocoding/geocode)
- ❌ Yahoo! Maps Web Services Geocoding API (https://developer.yahoo.com/maps/rest/V1/geocode.html) - **DEPRECATED**
- ❌ Melissa Geocoding (https://www.melissa.com/geocoding) - **PAID SERVICE**

***USA-only Geocoding systems**
- :o: Texas A&M (USA) Geoservices (http://geoservices.tamu.edu/Services/Geocode/WebService/)
- :o: TIGER USA Geocoding (http://www.tigergeocoder.com/)

**This step requires the creation of a keys.py file in the root directory (here) to contain the API keys. It is important to keep your API keys either restricted or hidden**
**N.B. As geocoding tools are coded, they will be crossed off from above**

The datasetgeocode (dsg) toolkit will provide individual modules for **singular address geocodes**, as well as for **batch geocoding**. 

## datasetrecombine (dsr)
Following the Dataset separation by DatasetPrep, if necessary, this data will be recombined using the current library.

## datasetnetworkanalysis (dsna)
Network analysis is necessary to determine the travel-time from an address to a certain location (in this case, the travel time from the patient's residence or ward centroid to the hospital).
Using ward centroids, we enhance the de-identification process and can use a Boolean to determine if an address lies within a pre-defined 30-minutes catchment area from the hospital, based on various APIs.
Using addresses, we can enhance the precision on top of a boolean, and implement K-means clustering to more accurately determine a 2km radiusfrom the hospital. This will be implemented alongside the **catchmentareatools(catch)** module.
The currently identified network analysis APIs which will be implemented include:
- [ ] ESRI Network Analyst
- [ ] Google Distance Matrix
- [ ] Bing maps distance matrix (https://docs.microsoft.com/en-us/bingmaps/rest-services/routes/calculate-a-distance-matrix)
- [ ] MapQuest RouteMatrix
- [ ] OpenStreetMaps (OSM) 
    - [ ] openrouteservice (https://openrouteservice.org/)
    - [ ] open source routing machine (http://project-osrm.org/)
    - [ ] BRouter (http://brouter.de/brouter/)
    - [ ] YOUR NAvication (http://yournavigation.org/)
    - [ ] Graphhopper(https://graphhopper.com/)
- [ ] Tomtom Routing API
- [ ] Melissa street route API


## catchmentareatools (catch)
There are multiple ways of determining a catchment area of a hospital. 
As I am not a statistician, the following list does not currently make sense to me, and things may be in the wrong position. More research into each catchment area system will be done soon, after completion of all tools listed above, in an orderly fashion.
The following list is not complete, however attempts will be made to perform all following catchment area calculations:
1. Distance-based catchment area
    - 2SFCA
    - E2SFCA
    - 3SFCA
2. Travel-time based
    - Lancet 30-minute rule (requires dsna module)
3. Patient-presentation based
    - KNN (K Nearest-Neighbours)
    - Kernel Density estimation
    - Monte Carlo simulation
    - SATScan
    - Moran's coefficient
    - FleXScan
    - EpiScan
    - MEET maximized excess event test
    - Empirical Bayes smoothing
    - Knox test
