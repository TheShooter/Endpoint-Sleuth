import re


def find_api_endpoints(path):
    root_class = None
    root_path = None
    root_nested = None
    endpoints = []
    with open(path, 'r') as file:
        lines = file.readlines()


    for line in lines:
        if '@Path' in line:

            if line.startswith(" "):
                endpoint_path = re.search(r'@Path\("(.*)"\)', line)
                if endpoint_path:
                  endpoint_path = endpoint_path.group(1)

                  if endpoint_path.startswith("/"):
                      endpoint_path = root_nested + endpoint_path
                  else:
                      endpoint_path = root_nested + "/" + endpoint_path
                  endpoints.append(endpoint_path)
                else:
                  endpoint_path = None
            else:
                endpoint_path = re.search(r'@Path\("(.*)"\)', line).group(1)
                if root_path:
                    endpoint_path = root_path + endpoint_path
                endpoints.append(endpoint_path)
                root_nested = endpoint_path
        elif '@WebMethod' in line:
            method_name = re.search(r'public (.*) ', line).group(1)
            endpoints[-1] = (endpoints[-1], method_name)
        elif 'class' in line and '{' in line:
            root_class = re.match(r'class (.*) ', line)
            if root_class:
              root_class.group(1)
            else:
              root_class = None
        elif root_class and '@Path' in line:
            root_path = re.search(r'@Path\("(.*)"\)', line).group(1)
        elif '@GET' in line or '@POST' in line or '@DELETE' in line or '@PUT' in line:
            method = re.search(r'@(.*)', line).group(1)
            endpoints[-1] = (endpoints[-1], method)

    return endpoints
