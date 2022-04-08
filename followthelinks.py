import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
    # print(tag.get('href', None))

for i in range (0, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = (tags[position-1].get('href'))
    url = link
print('Retrieving:',url)
print('Name:',url[39:45])