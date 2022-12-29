import argparse
from apis.find import find_api_endpoints
from apis.test import test_api_endpoint
from decompiling.decompiler import decompile_jar
from decompiling.extract import extract_file
from search.search_file import search_files
from search.insert import insert_data



def main():
    parser = argparse.ArgumentParser(description="Endpoint Sleuth is an open source tool that helps developers and security professionals extract undocumented API endpoints from WAR, JAR or EAR packages")
    parser.add_argument("--path", required=True, help="The path to the decompiled EAR, JAR or WAR")
    parser.add_argument("--filename", type=str, help="the filename to save the output",default="output")
    args = parser.parse_args()
    print("""
 _____             _                _         _     ____   _               _    _     
| ____| _ __    __| | _ __    ___  (_) _ __  | |_  / ___| | |  ___  _   _ | |_ | |__  
|  _|  | '_ \  / _` || '_ \  / _ \ | || '_ \ | __| \___ \ | | / _ \| | | || __|| '_ \ 
| |___ | | | || (_| || |_) || (_) || || | | || |_   ___) || ||  __/| |_| || |_ | | | |
|_____||_| |_| \__,_|| .__/  \___/ |_||_| |_| \__| |____/ |_| \___| \__,_| \__||_| |_|
              |_|                                                              

        """)
    file_paths = search_files(args.path, '.java')

    api_endpoints = []
    for file_path in file_paths:
        api_endpoints += find_api_endpoints(file_path)
    print(f"API Endpoints found:\n{api_endpoints}")
    insert_data(api_endpoints, args.filename)


if __name__ == '__main__':
    main()
