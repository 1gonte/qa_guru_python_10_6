import os
import pytest
import shutil


from script_zip import archive_data_to_zip, extract_data_from_zip


PROJECT_RESOURCES_PATH = os.path.join(os.path.dirname(os.getcwd()), 'resources')
PROJECT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), 'files')
ZIP_FILE_NAME = 'files.zip'


@pytest.fixture(autouse=True)
def data_manager():
    if not os.path.exists(PROJECT_RESOURCES_PATH):
        os.mkdir(PROJECT_RESOURCES_PATH)
    archive_data_to_zip(PROJECT_DATA_PATH, PROJECT_RESOURCES_PATH, ZIP_FILE_NAME)
    extract_data_from_zip(PROJECT_RESOURCES_PATH+'/'+ZIP_FILE_NAME)

    yield

    shutil.rmtree(PROJECT_RESOURCES_PATH)