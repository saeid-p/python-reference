#### Write a File ####
with open('somefile.txt', 'w') as file:
    file.write('tomato\npasta\ngarlic')

#### Read a File ####
with open('somefile.txt', 'r') as file:
    # Read the whole content into one string.
    content = file.read()
    # Make a list where each line of the file is an element in the list.
    print(file.readlines())
    
try:
    with open("fileName.dat", "r") as file:
        print(file.read())
except FileExistsError:
    print('File not found.')

#### Read File Line-By-Line ####    
with open('myFile.txt', 'r') as file:
    for line in file:
        print(line)

#### File System ####
import os

rootDirectory = 'C:/'
for root, folders, files in os.walk(rootDirectory):
    for filename in files:
        print(root, filename)

path = '/path/to/some/file.txt'
if os.path.isfile(path):
    print('It is a file!')

if os.path.exists(path):
    print('Exists!')
    
#### Text Processing ####

with open(filePath, 'r') as file:
    for line in file:
        segments = line.split('|')
        for segment in segments:
            print(segment)
            
#### JSON Processing ####
import json

with open(filePath, 'r') as file:
    for line in file:        
        payload = json.loads(line)
        print(payload["00020001"])

#### CSV File Processing ####
import csv

with open(filePath) as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        print(row[0])
