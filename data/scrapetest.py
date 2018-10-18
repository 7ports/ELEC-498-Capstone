from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    #Returns True if the response seems to be HTML, False otherwise.
    
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

raw_html = simple_get("https://weather.gc.ca/radar/index_e.html?id=XSM")
#raw_html = simple_get("http://explosm.net/comics/5036/")
soup = BeautifulSoup(raw_html, 'lxml')
for link in soup.find_all('img'):
    image = "https://weather.gc.ca/radar/index_e.html?id=XSM" + link.get("src")
    image_name = os.path.split(image)[1]


    print(image)
    print(image_name)
    if '?' in image_name:
        image_name = image_name.split('?')[0]
    r2 = get(image)
    with open(image_name, "wb") as f:
        f.write(r2.content)

   
