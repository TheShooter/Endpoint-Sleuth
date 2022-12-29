import zipfile

    #Open the EAR file
def extract_file(ear_path):
    with zipfile.ZipFile(ear_path, 'r') as ear_file:
    #Extract the contents of the EAR file to a temporary directory
     ear_file.extractall('./temp')