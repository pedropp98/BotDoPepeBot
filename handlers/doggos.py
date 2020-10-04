import requests
import re

def image():
    allowedExtension = ['jpg', 'jpeg', 'png']
    while True:
        url = requests.get('https://random.dog/woof.json').json()['url']
        fileExtension = re.search("([^.]*)$", url).group(1).lower()
        if fileExtension in allowedExtension:
            break
    return url

def doggos(update, context):
    update.message.reply_photo(photo = image())