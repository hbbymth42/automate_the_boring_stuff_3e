#! python3
# imageSiteDownloader.py - Downloads images from Flickr as they appear on search results page

import bs4, requests, os, re
print('Please enter what images you would like to search and download:')
searchText = input()

while searchText == False:
    searchText = input()

os.makedirs('images', exist_ok=True)
print(f'Searching for {searchText}')
searchUrl = 'https://www.flickr.com/search/?text=' + searchText
res = requests.get(searchUrl)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'html.parser')

photoElems = soup.select("div[class='search-container-w-sidebar'] > div[class='search-container-w-sidebar-content'] > div[class='main search-photos-results'] > div[class='view search-photos-everyone-view requiredToShowOnServer'] > div[class='view photo-list-view requiredToShowOnServer'] > div[class='view photo-list-photo-view requiredToShowOnServer awake'] > div[class='photo-list-photo-container'] img")

for photo in photoElems:

    link = photo.get('src')
    imageName = re.findall(r'[0-9]+', link)[0]
    print(f'Downloading Image {imageName}')
    imageUrl = 'https:' + link
    imageRes = requests.get(imageUrl)
    imageRes.raise_for_status()
    
    imageFile = open(os.path.join('images', os.path.basename(f'{imageName}.jpg')), 'wb')
    for chunk in imageRes.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    print(f'Image {imageName} has been downloaded!')

print('All Result Images have been downloaded!')