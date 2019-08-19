# GeocodingTools
Python based scripts used to rapidly geocode hospital datasets
**Developed by Weber Liu, 2019**
## INTRODUCTION
This set of scripts have been developed to use a variety of Geocoding APIs in order to convert hostpial patient data, in Address format, to a latitude/longitude format. Additional data returned from geocoding APIs will be retained in a separate file for any further analyses if necessary.
GeocodingTools is separated into two separate packages:
* DatasetPrep
* DatasetGeocode
The files do not have to be used together, however it is optimal if files ARE used in conjunction. Consult individual documentations to determine how the individual packages should be used.  

## DatasetPrep
DatasetPrep is a series of scripts, whose primary purpose is to prepare the original hospital file dataset for use with the DatasetGeocode package. 