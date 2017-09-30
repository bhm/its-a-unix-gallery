import requests
from io import BytesIO
from PIL import Image


class RemoteImage(object):
    def __init__(self, url):
        with requests.get(url) as response:
            self.__image_content = BytesIO(response.content)

    def open(self, **options):
        return Image.open(self.__image_content).show(title="Image", **options)
