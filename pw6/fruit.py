import urllib.request, urllib.parse, urllib.error
import json
import ssl

# https://www.fruityvice.com
# Fruityvice API 
serviceurl = 'https://www.fruityvice.com/api/fruit/'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    fruit = input('Enter a fruit name: ')
    if len(fruit) < 1: break

    url = serviceurl + urllib.parse.quote(fruit.lower()) 

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    
    if not js or 'name' not in js or 'nutritions' not in js:
        print('==== Invalid response or fruit not found ====')
        continue

    print('\nFRUIT INFORMATION:')
    print('Name:', js['name'])
    print('Family:', js['family'])
    print('Calories:', js['nutritions']['calories'])
    print('Sugar:', js['nutritions']['sugar'])
    print('Carbohydrates:', js['nutritions']['carbohydrates'])
