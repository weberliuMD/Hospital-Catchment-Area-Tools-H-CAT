# datasetprep (dsp)
Python scripts used to prepare datasets for geocoding
**Developed by Weber Liu, 2019**

## datasetprep (dsp)
datasetprep is a series of scripts, whose primary purpose is to prepare the original hospital file dataset for use with the DatasetGeocode package. It deals with data where:
* Patient data is NOT de-identified, and needs to be de-identified
* Patient address data is separated across multiple columns
* The database needs to be re-formatted into only PatientID and Address columns \(for use with DatasetGeocode\).

DatasetPrep is primarily based on the Python library **Pandas**
Functions available in datasetprep includes *load_data(fileName)*