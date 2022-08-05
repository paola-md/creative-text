import gdown
import zipfile

def get_models():
    output = "test.zip"
    url='https://drive.google.com/file/d/1kwJa35GNANQRzEcbp-RwPst01sNwkv9X/view?usp=sharing'
    gdown.download(url=url, output=output, quiet=False, fuzzy=True)

    directory_to_extract_to = "./models"
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)