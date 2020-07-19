import requests
import shutil

def download_image(url, path_to_image):
    response = requests.get(str(url), stream=True)

    with open(path_to_image, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    return