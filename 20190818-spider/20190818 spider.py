import requests
import re
url = 'http://www.jingcaiyuedu.com/novel/bbQAZ.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
res = requests.get(url, headers = headers)
res.encoding = 'utf-8'
html = res.text
print(res.status_code)
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html) [0]
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>', html, re.S)[1]
aill = re.findall(r'href="(.*?)">(.*?)<',dl)
f = open("%s.txt" % title, 'w', encoding = 'utf-8')
for i in aill:
    book_url, book_name = i
    book_url = "http://www.jingcaiyuedu.com%s" % book_url
    
    book_response = requests.get(book_url, headers = headers)
    book_response.encoding = 'utf-8'
    book_html = book_response.text
    
    # print(book_name)

    book_content = re.findall(r'<div class="panel-body" id="htmlContent">(.*?)<p class="text-center pt10">', book_html, re.S)[0]
    
    book_content = book_content.replace(' ','')
    book_content = book_content.replace('&nbsp;','')
    book_content = book_content.replace('<br />','')
    book_content = book_content.replace('<br/>','')
    book_content = book_content.replace('</p>','')
    book_content = book_content.replace('<p>','\n    ')

    f.write(book_name)
    f.write(book_content)
    f.write("\n")

    print(book_url)