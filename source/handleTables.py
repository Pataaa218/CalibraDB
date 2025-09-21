from tkinter import filedialog
import os
from time import sleep

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
def handleCalibrationTable(tabCalibration_path, feedback, GUI):
    global errorType, tNumber, tSize, tProduct, catchData, tHeightVolume
    if tabCalibration_path:
        tHeightVolume = [0]
        catchData = False
        with open(tabCalibration_path, 'r') as file:
            for line in file:
                line = line.strip()
                feedback.set(f'Scanning file:\nTank n.{tNumber}\nTank size: {tSize}\nProduct: {tProduct}\nInactive zone: {tHeightVolume[0]}\nIndexed: {len(tHeightVolume)}')
                GUI.update_idletasks()
                sleep(0.01)
# CATCHING HEIGHT-VOLUME DATA
                if catchData and line != "":
                    _tmp = line.split()
                    tHeightVolume.append(1000*float(_tmp[1]))
# CATCHING TANK NUMBER, SIZE AND PRODUCT TYPE
                elif findString(line, "Název"):
                    tNumber = findTankNum(line)
                    _tmp = findSubstring(line, '(', ')')
                    tSize, tProduct = _tmp.split("; ", 1)
# CATCH INACTIVE ZONE DATA
                elif findString(line, "Neaktivní"):
                    _tmp = line.split(" ")
                    tHeightVolume[0] = 1000*float(_tmp[2])
# FIND BEGINING OF HEIGHT-VOLUME DATA
                elif findString(line, "[cm]"):
                    catchData = True
            catchData = False
            feedback.set(f'Exctreacted data:\nTank n.{tNumber}\nTank size: {tSize}\nProduct: {tProduct}\nInactive zone: {tHeightVolume[0]}\nIndexed: {len(tHeightVolume)}\n\nPress CONFIRM to write, or\nselect a new file.')
            GUI.update_idletasks()
    else:
        errorType = 2

# Temp function to test handling calibration tables
def tmpFileDump():
    with open("betaDumpFile.txt", "w") as file:
        print("Writing to Dump file.")
        file.write("tNumber:   " + str(tNumber) + "\n")
        file.write("tSize: " + str(tSize) + "\n")
        file.write("tProduct:   " + str(tProduct) + "\n\n")
        for i in range(len(tHeightVolume)):
            file.write(str(i) + "\t\t")
            file.write(str(tHeightVolume[i]), "\n") 
        print("finished writing Dump file.")

