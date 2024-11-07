import os
import zipfile

import pytest

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
path_to_directory_files = os.path.join(current_dir, "files")
path_to_directory_archive = os.path.join(current_dir, "arhives")


@pytest.fixture(scope="session", autouse=False)
def add_files_to_zip():
    if not os.path.exists(path_to_directory_archive):
        os.mkdir(path_to_directory_archive)
    elif not os.path.exists(os.path.join(path_to_directory_archive, "test.zip")):
        file_dir = os.listdir(path_to_directory_files)
        with zipfile.ZipFile(os.path.join(path_to_directory_archive, "test.zip"), mode="w") as zf:
            for file in file_dir:
                add_file = os.path.join(path_to_directory_files, file)
                zf.write(add_file, os.path.basename(add_file))

    yield

    os.remove(path_to_directory_archive + "/test.zip")
