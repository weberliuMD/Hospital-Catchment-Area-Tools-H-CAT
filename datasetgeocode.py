#Import Geocoding API scripts
# from dsg import ArcGIS_geocode as arcgis
# from dsg import bingmaps_geocode as bing
from dsg import gmaps_geocode as gmaps
# from dsg import here_geocode as here
# from dsg import mapquest_geocode as mapquest
# from dsg import OSM_geocode as osm
# from dsg import tomtom_geocode as tomtom
# from dsg import yahoo_geocode as yahoo

#Import API Keys
import keys

def gmaps_geocode(Address, APIKEY=keys.GMAPS_APIKEY,):
    return gmaps.gmaps_geocode(Address, APIKEY)
