import json
import os
import re


def extract_numeric_value(path):
    """
    Extracts the file name as a numerical value
    :param path:
    :return:
    """
    match = re.search(r'/(\d+)\.json$', path)
    return int(match.group(1)) if match else 0


if __name__ == '__main__':
    """
    This script reads all the API response files from the YouTube API and puts it all in a single file.
    This makes the importing of this data in Open Search easy.
    """

    json_files_location = "json"
    directory = os.path.abspath(json_files_location)

    paths = [f"{directory}/{file}" for file in os.listdir(json_files_location)]
    sorted_paths = sorted(paths, key=extract_numeric_value)

    master_list = []

    for path in sorted_paths:
        with open(path, "r") as file:
            file_data = json.load(file)["items"]
            master_list.extend(file_data)

    with open("bible-in-a-year.json", "w") as json_file:
        json.dump(master_list, json_file, indent=2)
