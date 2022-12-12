import urllib.request

target_url = 'https://en.wikipedia.org/wiki/Main_Page'
with urllib.request.urlopen(target_url) as response:
   html = response.read()

if len(html) >= 3000: 
    print(html[:3000])

print("Number of characters in the document: ", len(html))