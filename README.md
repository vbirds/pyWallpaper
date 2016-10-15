
### pyWallpaper

#### 简介
pyWallpaper 是自动获取Bing的背景图片设置为桌面背景的python工具。
每次运行 pyWallpaper 会自动下载bing今天和前17天的壁纸，根据设置的时间自动跟换windows桌面壁纸。

#### 使用方法

设置时间跟换壁纸频率时间：

```python
	#设置频率时间为10s
	bing = Wallpaper(10)
	#启动程序
	bing.statr()
```

如果不设置时间默认频率时间为60s