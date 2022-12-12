import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
c = int(input('Enter count: '))
line = int(input('Enter position: '))

print('Recieving: %s' % url)
for i in range(0, c):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cnt = 0
    pos = 0
    for tag in tags:
        pos += 1
        if pos == line:
            print('Recieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            pos = 0
            break
    url = link
    
