import os
import shutil

path = "C:/file_sorter/sample"
file_names = os.listdir(path)
print(file_names)

folder_names = ['CSV files', 'TXT files', 'IMG files']

for folder_name in folder_names:
    if not os.path.exists(path + '/' + folder_name):
        os.makedirs(path + '/' + folder_name)

for file_name in file_names:
    if ".csv" in file_name and not os.path.exists(path + "/CSV files/" + file_name):
        shutil.move(path + '/' + file_name, path + "/CSV files/" + file_name)
    elif ".png" in file_name and not os.path.exists(path + "/IMG files/" + file_name):
        shutil.move(path + '/' + file_name, path + "/IMG files/" + file_name)
    elif ".txt" in file_name and not os.path.exists(path + "/TXT files/" + file_name):
        shutil.move(path + '/' + file_name, path + "/TXT files/" + file_name)
   