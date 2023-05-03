import requests
from tqdm import tqdm
import os
import zipfile

def is_zip_file(file_path):
    return zipfile.is_zipfile(file_path)

def delete_all_zip_files_except(directory, exclude_file, file_end):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if file.endswith(file_end) and file != exclude_file:
            os.remove(file_path)

def combine_zip_files(directory, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as output_zip:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if is_zip_file(file_path):
                    with zipfile.ZipFile(file_path, 'r') as input_zip:
                        for file_info in input_zip.infolist():
                            if os.path.normpath(file_info.filename) not in [os.path.normpath(existing_file) for existing_file in output_zip.namelist()]:
                                output_zip.writestr(file_info, input_zip.read(file_info))


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(output_path, 'wb') as file, tqdm.wrapattr(file, "write", total=total_size) as progress_file:
        for data in response.iter_content(chunk_size=4096):
            progress_file.write(data)

    return response.status_code
