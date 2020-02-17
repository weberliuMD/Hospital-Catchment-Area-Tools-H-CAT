import sys
sys.path.append('../..')
import datasetgeocode as dsg
dsg.bing_batch_geocode("../../PNT_Formatted_Address/PNT_here.csv")