

def cattos(update, context):
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    update.message.reply_photo(photo=url)