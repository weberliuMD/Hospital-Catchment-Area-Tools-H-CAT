import datasetPrep as dsp

#Start the master function
print("Where is the Original data file?")
print("Ensure that you do not enter the location with quotation marks")
print("Ensure also that there is only one header line")
fileLocation = "./Admissions_data/HTD_Original.csv"                 #input()

#load the file
data = dsp.dataLoader(fileLocation)

print("What is the column name for the patient ID?")
IDCol = "ID"                                                        #input()
print("What is the column name for the patient address?")
addressCol = "Address"                                              #input()

