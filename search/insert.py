import openpyxl

def insert_data(data, filename):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    worksheet.append(["Endpoint", "Request method"])

    for item in data:

        if isinstance(item, tuple):
            endpoint, method = item
            worksheet.append([str(endpoint), method])
        else:
           worksheet.append([str(item), "GET"])

    workbook.save(f"{filename}.xlsx")
    print("Results saved")

