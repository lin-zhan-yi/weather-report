import requests
from io import BytesIO #解析照片
from PIL import Image #編輯照片
from os import getenv
from dotenv import load_dotenv

load_dotenv()

RANDON_PHOTO_URL='https://api.unsplash.com/photos/random'
api_key=getenv("UNSPLASH_API_KEY")
def listImageURL(raw_data):
    links=[photo["urls"]["full"]for photo in raw_data]
    return links

def downloadImage(links):

    image_list=[]

    for link in links:
        download=requests.get(link)
        if download.status_code==200:
            image =Image.open(BytesIO(download.content))
            image_list.append(image)

    return image_list

def getBackground(weather,count):
    global RANDON_PHOTO_URL

    url=RANDON_PHOTO_URL + f'?query={weather}&count={count}'

    get_background_request=requests.get(url,headers={
        "Authorization": f'Client-ID {api_key}'
    })

    if get_background_request.status_code==200:
        url_list=listImageURL(get_background_request.json())
        image_list=downloadImage(url_list)

        return image_list
    return None
