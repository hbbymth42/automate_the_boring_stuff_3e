#! python3
# linkVerification.py - Verifies given links on a page

import requests, os, bs4

url = 'https://passiveinvestingaustralia.com'
os.makedirs('webpages', exist_ok=True)
res = requests.get(url)
res.raise_for_status()

downloadedPageNum = 1

soup = bs4.BeautifulSoup(res.text, 'html.parser')

pageLinks = soup.select('a')

for pageLink in pageLinks:
    webPage = pageLink.get('href')
    if webPage == None:
        print('No Link Present, proceeding to next page...')
        continue
    if webPage[0] == '#':
        print('Internal Link, proceeding to next page...')
        continue
    if webPage[0] == '/':
        pageLinkConcat = url + webPage
        try:
            pageRes = requests.get(pageLinkConcat)
            pageRes.raise_for_status()
            pageContent = pageRes.content
            pageSoup = bs4.BeautifulSoup(pageContent, 'html.parser')
            with open(os.path.join('webpages',f'webPage{downloadedPageNum}.html'),'w', encoding='utf-8') as file:
                file.write(str(soup.prettify()))
            downloadedPageNum = downloadedPageNum + 1
        except:
            print(f'Broken Link: {str(pageLinkConcat)}')
    else:
        try:
            pageRes = requests.get(webPage)
            pageRes.raise_for_status()
            pageContent = pageRes.content
            pageSoup = bs4.BeautifulSoup(pageContent, 'html.parser')
            with open(os.path.join('webpages',f'webPage{downloadedPageNum}.html'),'w', encoding='utf-8') as file:
                file.write(str(soup.prettify()))
            downloadedPageNum = downloadedPageNum + 1
        except:
            print(f'Broken Link: {str(webPage)}')
print('Done!')