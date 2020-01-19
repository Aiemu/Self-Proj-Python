# Self_Proj_Python

## 内容
包含一些用py开发的小项目

## 目录:  
### 1. 20190818_spider  
- 功能：  
  用于爬取小说网站"http://www.jingcaiyuedu.com/"上小说的爬虫

- 使用：
  ``` bash
  python3 spider.py
  ```

### 2. 20190909_ai
- 功能：  
  用于图像风格转换、分割及识别物体的ai

- 使用：
  ``` bash
  # 分割及识别直接import 对应的.py文件，调用函数即可
  # 风格转换：
  python3 StyleTransition.py <ori_img> <style_img>

### 3. 20190930_tgnb
- 功能：  
  在终端中输出点阵字

- 使用：
  ``` bash
  # 修改line 61处inpt的值
  python3 tgnb.py
  ```

### 4. 20191009_pics2pic
- 功能：  
  1. 爬取"https://pixabay.com/zh/images/search/"上的图片
  2. 利用爬取到的图片千图成像

- 使用：
  ``` bash
  # 将欲成像的图片命名为pic.jpg
  python3 spider.py # 爬取图片
  python3 transfer.py # 成像
  ```

### 5. 20200119_addr-acquire
- 功能：  
  爬取网站图片

- 使用：
  ``` bash
  python addr.py [url]
  ```