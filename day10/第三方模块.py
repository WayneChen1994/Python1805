'''
第三方的库都需要安装

第一种：使用pip安装
命令格式：pip install 库名
若发生错误，先更新错误，再切换网络

第二种：使用pycharm进行安装
'''

from PIL import Image

# 打开图片，生成一个image对象
im = Image.open('ppp.jpg')
# 从打开的图片中获取图片信息
# im.format：图片格式信息
# im.size：图片尺寸
print(im.format, im.size)
# 设置图片的尺寸，生成缩略图
im.thumbnail((500, 200))
# 另存为，参数一：图片名，参数二：图片格式
im.save('pppp.jpg', 'JPEG')
