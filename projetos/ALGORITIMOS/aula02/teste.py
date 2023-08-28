import requests
from bs4 import BeautfulSoup

url = 'https:\\siga.cps.sp.gov.br/image//'
response = requests.get(url)
soup= beautifulsoup(response.text, 'html.parser')

image_links =[]

for img_tag in soup.find_all('img'):
    img_src = img_tag.get('src')
    if img_src:
        if img_src.staetswith('/'):
            imf_serc = url+ img_src
            image_links.append(img_src)

            for link in image_links:

                print(link)