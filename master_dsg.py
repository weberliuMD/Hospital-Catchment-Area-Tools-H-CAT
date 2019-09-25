import datasetgeocode as dsg
# dsg.gmaps_batch_geocode("Admissions_data/HTD_Trim.csv", endPos = 1800)
# dsg.OSM_batch_geocode("Admissions_data/HTD_Trim.csv", endPos = 1000)
#dsg.mapquest_batch_geocode("Admissions_data/HTD_Trim.csv", endPos = 1000)
dsg.bing_batch_geocode("Admissions_data/HTD_Trim.csv", endPos = 1000)