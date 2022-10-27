from zipfile import ZipFile

with ZipFile('reaal.zip', 'r') as zip_object:
    zip_object.extractall()

# list of files that are archived in the ZIP file

print(zip_object.namelist())

