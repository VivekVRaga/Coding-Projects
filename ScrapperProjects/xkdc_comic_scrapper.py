import requests, os
from bs4 import BeautifulSoup
#Download the desctription and image of XKDCs latest comic

r = requests.get("https://xkcd.com/")

soup = BeautifulSoup(r.content, "html.parser")

g_da = soup.find_all("img")

#get the title of the comic
imgTitle =g_da[2].get('title')
print(imgTitle)

#get the image name and extension
imgURL = g_da[2].get('src')

#make it an absolute dir
r = requests.get('https:'+imgURL)

# make and save directory
os.makedirs('xkcd', exist_ok=True)
imageFile = open(os.path.join('xkcd', os.path.basename(imgURL)), 'wb')

#write image
for chunk in r.iter_content(100000):
    imageFile.write(chunk)
    imageFile.close()
