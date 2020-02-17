import datasetgeocode as dsg
# dsg.gmaps_batch_geocode("./PNT_Formatted_Address/PNT_bing.csv")
# dsg.OSM_batch_geocode("./HTD_Formatted_Address/HTD_bing.csv")
dsg.mapquest_batch_geocode("Admissions_data/HTD_Trim.csv", startPos = 12401, endPos = 12803)
# dsg.bing_batch_geocode("./PNT_Formatted_Address/PNT_gmaps.csv")
# dsg.here_batch_geocode("./PNT_Formatted_Address/PNT_gmaps.csv")
# dsg.tomtom_batch_geocode("Admissions_data/HTD_Trim.csv")
# dsg.tomtom_batch_fuzzysearch("Admissions_data/HTD_Trim.csv", startPos=1813)