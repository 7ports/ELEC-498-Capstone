from bs4 import BeautifulSoup
import requests
import urllib


link = "https://weather.gc.ca/radar/index_e.html?id=XSM"
link2 = 'https://uwaterloo.ca'
source = requests.get(link2).text


soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())


#iterate over all image objects on webpage
for img in soup.find_all('img'):
    temp = img.get('src')
    if temp[:1] == '/':
        image = 'https://uwaterloo.ca' + temp
    else:
        image = temp
    print(image)

    #check to see if alt tag is empty, if not make it filename otherwise give it a number
    i = 1
    nametemp = img.get('alt')
    if len(nametemp) == 0:
        filename = str(i)
        i = i + 1
    else:
        filename = nametemp


    #write the image file
    imagefile = open(filename + '.gif', 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()