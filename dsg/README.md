# datasetprep (dsp)
Python scripts used for geocoding

**Developed by Weber Liu, 2019**

## API KEYS
To use the dsg tools, it is important to have the relevant API keys. API keys can be stored in the root folder, and will be imported automatically when using the datasetprep module. Each geocoding source will have its own necessary API Keys. Detail will be as follows.
### GMAPS API Key
The GMAPS API Key can be obtained from https://console.cloud.google.com - it is necessary to sign up with a billing account. First time users will be provided with promotional credits, as well as monthly credits for use with the Google Maps platform (Further research may be necessary with regards to this). When signing up, it will query which APIs you wish to activate. The Geocoding APIs from Google are hidden within the **Places API**. Make sure this is selected.
GMAPS will deliver the API Key and you can add this to the keys.py script in the root directory. 