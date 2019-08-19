import csv
def datasetLoadPrint(openFile):
    with open (openFile) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")

        