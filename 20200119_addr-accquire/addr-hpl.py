from urllib.request import urlretrieve

import requests
import re
import ssl
import os
import sys

# verify ssl
ssl._create_default_https_context = ssl._create_unverified_context

def imgDownload(url, title):
    # download imgs
    title.replace(' ', '_')

    try:
        os.makedirs('./imgs/' + title)
    except:
        pass

    url = url[0:url.index('/', 43) + 1]

    print(title, 'is downloading...')

    for i in range(1, 21):
        path = './imgs/' + title + '/' +  str(i) + '.png'
        urlretrieve(url + str(i) + '.jpg', path)
    
    return

def getImgUrl():
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        try:
            fo = open('addr.cache','r')
            url = fo.readline()
        except:
            print('Open file \"tmp.md\" failed! Please add an arg as url.')
            return

    print('Current url is', url)

    # set url & headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}

    # get true path
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'

    try:
        herf = re.findall(r'<a href=".*?" target="', res.text)[0]
        addr = herf[9:-10]
    except:
        print('True path acquiring failed!')
        return

    # get imgs' url
    res = requests.get(addr, headers=headers)
    res.encoding = 'utf-8'

    try:
        imgs = re.findall(r'<img data-original=".*?" title="', res.text)
        titles = re.findall(r'.jpg" title=".*?" alt=', res.text)
    except:
        print('Imgs\' url acquiring failed!')
        return

    try:
        os.makedirs('./imgs')
    except:
        pass

    # count for rename
    count = 0

    # loop for download
    for img in imgs:
        imgDownload(img[20:-9], titles[count][13:-6])
        count += 1

    return

if __name__ == '__main__':
    getImgUrl()