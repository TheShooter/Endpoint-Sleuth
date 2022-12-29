import os


def search_files(dir, file_extension):
    file_paths = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))

    return file_paths
