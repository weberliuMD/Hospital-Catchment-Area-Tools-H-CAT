import datasetgeocode as dsg
# dsg.gmaps_batch_geocode("Admissions_data/HTD_Trim.csv")
# dsg.OSM_batch_geocode("Admissions_data/HTD_Trim.csv")
dsg.mapquest_batch_geocode("Admissions_data/HTD_Trim.csv")
# dsg.bing_batch_geocode("Admissions_data/HTD_Trim.csv", startPos = 4121)
dsg.here_batch_geocode("Admissions_data/HTD_Trim.csv")
# dsg.tomtom_batch_geocode("Admissions_data/HTD_Trim.csv", startPos=38432)
dsg.tomtom_batch_fuzzysearch("Admissions_data/HTD_Trim.csv")