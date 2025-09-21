from tkinter import filedialog
import os

ct_title = "Select a calibration table."
mdb_title = "Select a source database."
txt_type = [("Text Files", "*.txt")]
mdb_type = [("Microsoft Access Database", "*.mdb")]

# Variable declaration
errorType = 0
tNumber = 0
tSize = ""
tProduct = ""
tHeightVolume = [0]
catchData = False

# Open dialog for file selection
def selectFile(dialogTitle, fileType):
    _path = filedialog.askopenfilename(title=dialogTitle, filetypes=fileType)
    return _path

# Find string in other string
def findString(source_string, search_string):
    return search_string in source_string

# Return substring from between 2 chars
def findSubstring(s, start_char, end_char):
    global errorType
    start_index = s.find(start_char)
    if start_index == -1:
        errorType = 1
        return 0
    end_index = s.find(end_char, start_index + 1)
    if end_index == -1:
        errorType = 1
        return 0
    return s[start_index + 1:end_index]

# Return char after '.'
def findTankNum(s):
    global errorType
    _i = s.find('.')
    if _i != -1 and _i + 1 < len(s):
        return int(s[_i + 1])
    else:
        errorType = 1

# Read calibration table and catch important data
def handleCalibrationTable(tabCalibration_path):
    global errorType, tNumber, tSize, tProduct, catchData, tHeightVolume
    if tabCalibration_path:
        print("Calibration table path: ", tabCalibration_path)
        tHeightVolume = [0]
        catchData = False
        with open(tabCalibration_path, 'r') as file:
            print("Scanning calibration table for required data.")
            for line in file:
                line = line.strip()
# CATCHING HEIGHT-VOLUME DATA
                if catchData and line != "":
                    _tmp = line.split()
                    tHeightVolume.append(float(_tmp[1]))
# CATCHING TANK NUMBER, SIZE AND PRODUCT TYPE
                elif findString(line, "Název"):
                    tNumber = findTankNum(line)
                    print("Found tank number: ", tNumber)
                    _tmp = findSubstring(line, '(', ')')
                    tSize, tProduct = _tmp.split("; ", 1)
                    print("Found tank product: ", tProduct)
                    print("Found tank volume: ", tSize)
# CATCH INACTIVE ZONE DATA
                elif findString(line, "Neaktivní"):
                    _tmp = line.split(" ")
                    tHeightVolume[0] = float(_tmp[2])
                    print("Found inactive zone: ", tHeightVolume[0])
# FIND BEGINING OF HEIGHT-VOLUME DATA
                elif findString(line, "[cm]"):
                    catchData = True
            catchData = False
            print("Finished reading calibration table. Collected data:")
            print("tNumber:  ", tNumber)
            print("tSize:    ", tSize)
            print("tProduct: ", tProduct)
            print("\nheight indexes: ", len(tHeightVolume))
    else:
        errorType = 2

# Temp function to test handling calibration tables
def tmpFileDump():
    with open("betaDumpFile.txt", "w") as file:
        print("Writing to Dump file.")
        file.write("Tank n.:   " + str(tNumber) + "\n")
        file.write("Tank size: " + str(tSize) + "\n")
        file.write("Product:   " + str(tProduct) + "\n\n")
        for i in range(len(tHeightVolume)):
            file.write(str(i) + "\t\t")
            file.write(f"{tHeightVolume[i]:.3f}" + "\n") 
        print("finished writing Dump file.")

