#-*-coding:utf-8-*-

import Image
import win32gui
import win32con
import win32api
import os
import threading
import urllib
import time
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

class Wallpaper:

    def __init__(self):
        self.count = 0
        self.urltemplate = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=%d&n=1&nc=1361089515117&FORM=HYLH1'
        self.baImageUrlList = []
        self.localFileName  = ''
        self.localBMPFileName  = ''
        self.imagedir = './images/'
        self.bmpdir = './bmpimage/'
        self.bmplist = []

    def statr(self):
        self.parserImageUrl()
        self.download_images()
        self.image_convert_bmp()

        self.set_wall_func()

    def parserImageUrl(self):

        for i in range(0, 18, 1):
            url = self.urltemplate % i
            content = urllib.urlopen(url).read()
            decodedjson = json.loads(content)
            imageurl = decodedjson['images'][0]['url']

            self.baImageUrlList.append(imageurl)

    def download_images(self):

        for url in self.baImageUrlList:
            imagename = os.path.basename(url)
            imagepath = self.imagedir + imagename
            f = open(imagepath, 'wb')
            conn = urllib.urlopen(url)
            f.write(conn.read())
            f.close()

    def image_convert_bmp(self):
        imaglist = os.listdir(self.imagedir)
        for imagepath in imaglist:
            file_name = os.path.basename(imagepath)
            file_name_type = os.path.splitext(file_name)
            file_name = file_name_type[0]
            newpath = self.bmpdir + file_name + '.bmp'
            imagepath  = './images/' + imagepath

            self.bmplist.append(newpath)
            bmpImage = Image.open(imagepath)
            bmpImage.save(newpath, "BMP")

    def setWallpaper(self, imagepath):
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)

    def set_wall_func(self):

        list_size = len(self.bmplist)
        index = self.count % list_size
        filename = self.bmplist[index]
        self.count += 1
        self.setWallpaper(filename)
        self.set_wall_timer()

    def set_wall_timer(self):
        timer = threading.Timer(10, self.set_wall_func)
        timer.start()



if __name__ == '__main__':
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=%d&n=1&nc=1361089515117&FORM=HYLH1'

    bing = Wallpaper()

    bing.statr()


    #content = urllib.urlopen(url).read()
    # decodedjson = json.loads(content)
    # print(decodedjson['images'][0]['url'])

    #for i in range(0, 20, 1):
    # myurl = url % 0
    #
    # content = urllib.urlopen(myurl).read()
    # decodedjson = json.loads(content)
    # imagurl = decodedjson['images'][0]['url']
    # print(decodedjson['images'][0]['url'])
    #
    # imagename = os.path.basename(imagurl)
    # conn = urllib.urlopen(imagurl)
    # f = open(imagename, 'wb')
    # f.write(conn.read())
    # f.close()




    #print(content)
    #print(content.decode("utf8"))

    # setWallPaper(StoreFolder + "/003_meitu_1.jpg")
    # get_photo_list()
    # set_wall_func()

    # imagePath = 'c:/desktop/1406557hc2m6m0h2cac07k.jpg.thumb.jpg'
    # file_name = os.path.basename(imagePath)
    # file_name_type = os.path.splitext(file_name)
    # file_type = file_name_type[1]
    # file_name = file_name_type[0]

