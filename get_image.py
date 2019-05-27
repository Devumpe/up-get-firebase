from google.cloud import storage
import pyrebase
import os
import urllib.request 
import requests

  # โหลดรูป
    #blob.public_url คือurlรูปบนfirebase
    image_storage = requests.get(blob.public_url)
    #ชื่อpath folderที่จะเซฟรูป
    with open('img_for_ocr/'+image, 'wb') as f:
        f.write(image_storage.content)