# utils.py

import os
import requests
from django.conf import settings
from urllib.parse import urlparse, quote

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the file name from the URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            # Encode the filename to handle special characters
            encoded_filename = quote(filename)
            # Construct the save path
            save_path = os.path.join(settings.MEDIA_ROOT, encoded_filename)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            # Return the relative path of the saved image
            return os.path.relpath(save_path, settings.MEDIA_ROOT)
        else:
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None
