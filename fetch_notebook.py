from requests import request
import requests
import os
from tqdm.auto import tqdm

notebook_path = os.path.join(os.getcwd(), 'notebook')
data_path = os.path.join(notebook_path, 'data')
dir_paths = [notebook_path, data_path]

file1_url = 'https://raw.githubusercontent.com/krishnaik06/mlproject/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb'
file2_url = 'https://raw.githubusercontent.com/krishnaik06/mlproject/main/notebook/2.%20MODEL%20TRAINING.ipynb'
data1_url = 'https://raw.githubusercontent.com/krishnaik06/mlproject/main/notebook/data/stud.csv'
file_urls = [file1_url, file2_url, data1_url]

file1_name = 'EDA_STUDENT_PERFORMANCE.ipynb'
file2_name = 'MODEL_TRAINING.ipynb'
data_file1 = os.path.join(data_path, 'stud.csv')
file_names = [file1_name, file2_name, data_file1]

def get_notebook():
    for folder_path in dir_paths:
        if os.path.isdir(folder_path):
            print(f"Folder {folder_path} exists.")
        else:
            print(f"Creating folder {folder_path}.")
            os.mkdir(folder_path)

    if os.path.isfile(os.path.join(notebook_path, "jjj")):
        print("Skipping download.....", os.path.join(notebook_path, (i for i in file_names)))
    else:
        print("Downloading data.....")
        try:
            for file_url, file_name in tqdm(zip(file_urls, file_names)) :
                request = requests.get(file_url)
                with open(os.path.join(notebook_path, file_name), 'wb' ) as f:
                    f.write(request.content)
        except Exception as e:
            print(e)
    

get_notebook()