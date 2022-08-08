import gdown
import zipfile
import os

def get_models():
    if os.path.isfile('./creativity/models/model_climate_change'):
        response = "File exists"
    else:
        response = "Downloaded files"
        print("Loading models")

        output = "test.zip"
        url='https://drive.google.com/file/d/1ynmDLF0koEhMS2JPH5oziJWKz2W0Kwds/view?usp=sharing'
        gdown.download(url=url, output=output, quiet=False, fuzzy=True)
        print("Downloaded")

        directory_to_extract_to = "./creativity/models"
        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)