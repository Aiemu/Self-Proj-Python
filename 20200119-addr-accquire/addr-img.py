from urllib.request import urlretrieve

import requests
import re
import ssl
import os
import sys
import time
import signal
import functools
import importlib
import random
import time
import signal

# verify ssl
ssl._create_default_https_context = ssl._create_unverified_context

total_dir = 0
total_full = 0
total_down = 0

class FuncTimeoutException(Exception):
    pass

def handler(signum, _):
    raise FuncTimeoutException('Timeout Signal')

def func_timeout(times=0):
    def decorator(func):
        if not times:
            return func
        def wraps(*args, **kwargs):
            signal.alarm(times)
            result = func(*args, **kwargs)
            signal.alarm(0)
            return result
        return wraps
    return decorator

signal.signal(signal.SIGALRM, handler)

@func_timeout(10)
def imgDownload(url, title, count):
    global total_full
    global total_down

    # download imgs
    title.replace(' ', '_')

    try:
        os.makedirs('./imgs/' + title)
    except:
        pass

    total_down += 1

    path = './imgs/' + title + '/' +  str(count) + '.png'
    urlretrieve(url, path)

    total_full += 1

    return

def getImgUrl(url):
    global total_dir
    print('Current url is', url)

    # set url & headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}

    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'

    title = 'title'

    try:
        imgs = re.findall(r'<img src=".*?"', res.text)
        titles = re.findall(r'<DIV class=title>.*?</DIV>', res.text)
        title = titles[0][17:-6]
    except:
        print('Imgs\' url acquiring failed!')
        return

    try:
        os.makedirs('./imgs')
    except:
        pass

    total_dir += 1
    count = 0

    print(title + ' download begins...')

    # loop for download
    for img in imgs:
        print("Downloading: %d/%d" % (count + 1, len(imgs)), end="\r")
        try:
            imgDownload(img[10:-1], title, count)
        except FuncTimeoutException:
            print('Download Timeout: ', 'download', count, 'timeout(10s), skip this img.')
        count += 1
    
    print('🍺Cheers! Download', title, 'successfully!')
    return

if __name__ == '__main__':
    loc = 0

    mode = input('Random: 0, Cache: 1, Customize: xxxx\n')

    if mode == '1':
        try:  
            fr = open('info.cache', 'r') 
            fstr = fr.readline()
            fr.close()
            print('loctent: ' + fstr)
            loc = int(fstr)

        except: 
            loc = 840000 + random.randint(0, 9999)
            print('File Open Error, random loc = %d.' % loc)

    elif mode == '0':
        loc = 840000 + random.randint(0, 9999)

    else:
        try:
            loc = 840000 + int(mode)
        
        except:
            loc = 840000 + random.randint(0, 9999)
            print('Wrong Arg, random loc = %d.' % loc)

    ori_url = 'http://www.mmff73.com/'
    url = 'http://www.mmff73.com/'

    goOn = True

    while goOn:
        try:
            url = ori_url + 'fbzf_' + str(loc) + '.html'
            getImgUrl(url)
        except KeyboardInterrupt:
            print('Download Interrupt: ', ori_url + 'fbzf_' + str(loc) + '.html download was interrupted.')

            tmp = input('Go on? Press \'s\' to stop, \'r\' to re-random loc, or any other keys to continue.\n')
            if tmp == 's':
                goOn = False
            elif tmp == 'r':
                loc = 840000 + random.randint(0, 9999)
                print('New random loc = %d.' % loc)

        loc -= 1

        fw = open('info.cache', 'w') 
        fw.write(str(loc))
        fw.close()
        print('\n')

    print('Results of the work: ' + str(total_dir) + ' dirs, ' + '%d/%d files.' % (total_full, total_down))
























'''
图片特区
/vgne_6.html 自拍偷拍
/vgne_7.html 亚洲色图
/vgne_8.html 欧美色图
/vgne_9.html 美腿丝袜
/vgne_10.html 清纯优美
/vgne_11.html 熟女乱伦
/vgne_12.html 卡通动漫
/vgne_13.html 变态另类

小说特区
/vgne_14.html 都市激情
/vgne_15.html 校园春色
/vgne_16.html 淫荡人妻
/vgne_17.html 家庭乱伦
/vgne_18.html 武侠古典
/vgne_19.html 性爱技巧
/vgne_20.html 长编小说
/vgne_21.html 情色笑话

在线电影
/ddrb_22.html 日本系列
/ddrb_28.html 日本有码
/ddrb_23.html 亚洲系列
/ddrb_24.html 国产系列
/ddrb_25.html 欧美性爱
/ddrb_27.html 视频裸聊
/ddrb_26.html 三级伦理
/ddrb_29.html 强暴迷奸

在线电影
/ddrb_30.html 临盆孕婦
/ddrb_31.html 双性人妖
/ddrb_32.html 怀旧老片
/ddrb_33.html ＳＭ另类
/ddrb_34.html 男性同志
/ddrb_35.html 包夜小姐
/ddrb_36.html 少女激情
/ddrb_37.html 领取奖金

ＢＴ磁力
/vgne_38.html 亚洲无码
/vgne_39.html 亚洲有码
/vgne_40.html 欧美无码
/vgne_41.html 国产无码
/vgne_42.html 国产三级
/vgne_43.html ＡＶ明星
/vgne_44.html 女优赌场
/vgne_45.html 本站帮助

图片精品
/vgne_57.html 邪恶内涵
/vgne_59.html 色系军团
/vgne_60.html 嘻哈军团
/vgne_61.html 乐张不入
/vgne_62.html 色小组
/vgne_63.html 棒棒冰
/vgne_64.html 套图下载
/vgne_58.html 微信涵图

在线精品
/ddrb_52.html 手机亚洲
/ddrb_65.html 手机日韩
/ddrb_66.html 手机欧美
/ddrb_67.html 手机另类
/ddrb_53.html 有声性说
'''