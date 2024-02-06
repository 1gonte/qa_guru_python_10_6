import os
import zipfile
from zipfile import ZipFile
import glob


def archive_data_to_zip(data_path, zip_path, zip_name='files.zip'):
    with zipfile.ZipFile(os.path.join(zip_path, zip_name), 'w') as writer:
        for file in glob.glob(os.path.join(data_path, '*')):
            writer.write(file, os.path.basename(file))


def extract_data_from_zip(zip_patch):
    with ZipFile(zip_patch, 'r') as reader:
        reader.extractall(os.path.join(os.path.dirname(os.getcwd()), 'resources'))
