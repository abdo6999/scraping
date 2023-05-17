import os
import shutil
import glob

source_dir = "./output"

files = os.listdir(source_dir)
for file in files:
    destination_dir = f"./all-dictionary-imgs(preview+inner)/{file}"
    jsonFiles = os.listdir(f"./output/{file}")
    checks = os.listdir(destination_dir)
    for check in checks:
        destination_dir = f"./all-dictionary-imgs(preview+inner)/{file}/{check}"
        jsonFiles = glob.glob(f"./output/{file}/*.json")

    for jsonFile in jsonFiles:
        # Extract the uppercase substring from the JSON file name
        file_path = f"./output/{file}/{jsonFile}"
        name = os.path.splitext(jsonFile)[0]  # Remove the file extension
        name_parts = name.split("_")
        if len(name_parts) >= 2:
            uppercase_name = "_".join(name_parts[1:]).upper()
            uppercase_name = uppercase_name.replace(" ", "_").replace("’", "_")

            destination_dir = f"./all-dictionary-imgs(preview+inner)/{file}/{uppercase_name}"
            shutil.move(file_path, destination_dir)
            print(f"Moved {jsonFile} successfully.")

















# for file in files:
#     destination_dir = f"./all-dictionary-imgs(preview+inner)/{file}"
#     jsonFiles = os.listdir(f"./output/{file}")
#     checks = os.listdir(destination_dir)
#     for check in checks:
#         destination_dir = f"./all-dictionary-imgs(preview+inner)/{file}/{check}/*.json"
#         jsonFiles = glob.glob(destination_dir)
#         if jsonFiles:
#             continue
#         else:
#             print(f'{check}')