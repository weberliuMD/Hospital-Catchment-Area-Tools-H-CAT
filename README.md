# GeocodingTools
Python based scripts used to rapidly geocode hospital datasets.
**Developed by Weber Liu, 2019**
## INTRODUCTION
This set of scripts have been developed to use a variety of Geocoding APIs in order to convert hostpial patient data, in Address format, to a latitude/longitude format. Additional data returned from geocoding APIs will be retained in a separate file for any further analyses if necessary.
GeocodingTools is separated into two separate packages:
* DatasetPrep
* DatasetGeocode
* DatasetRecombine
The files do not have to be used together, however it is optimal if files ARE used in conjunction. Consult individual documentations to determine how the individual packages should be used.  

## DatasetPrep
DatasetPrep is a series of scripts, whose primary purpose is to prepare the original hospital file dataset for use with the DatasetGeocode package. It deals with data where:
* Patient data is NOT de-identified, and needs to be de-identified
* Patient address data is separated across multiple columns
* The database needs to be re-formatted into only PatientID and Address columns \(for use with DatasetGeocode\).

DatasetPrep is primarily based on the Python library **Pandas**

## DatasetGeocode
DatasetGeocode's primary purpose is to geocode 'prepared' datasets to be used with various geocoding APIs. API keys may need to be provided. All returned data from these APIs will be provided in a formatted manner and returned as a .csv file. The APIs currently supported in DatasetGeocode include:
* Google Maps Geocoding API

If you have requests to add more please contact me.

## DatasetRecombine
Following the Dataset separation by DatasetPrep, if necessary, this data will be recombined using the currently library.