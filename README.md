环境
Python 3.6.3

模块
os

工具
程序员计算器

目的
通过python 实现电脑版微信中图片转码（原.dat转成JPG或PNG）


分析
据说微信图片是用异或值加密（实际就是转码）
1.先用工具打开.bat文件，但会看到一堆乱码。如下图

用notepad++的话可以，通过插件以16进制打开。（怎么用notepad打开16进制点这） 16进制打开如下图

再用 16进制打开JPG 图片如下图

由于知道了.bat的开头值为：e1 c6 .JGP的开头值为：ff d8
此时可以通过程序员计算器，计算异或值
计算公式：e1 Xor ff = 1e ;c6 Xor d8 = 1e
由此可知16进制异或值为：0x1e

知道异或值就可以撸代码：
原理就是把.bat里面的16进制都值都异或0x1e ，
例子:0xe1 ^ 0x1e = 0xff; 0xc6 ^ 0x1e = 0xd8 ……
代码如下

# weixin_Image.bat 破解
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# 微信.bat 16进制 e1 c6 e1
# key 值 1e1e 0x1e  weixin.bat-jpg

import os
#微信image文件路径
into_path = r'D:\Project0611\weixin_image\weixin1212800'
#微信图片转码后的保存位置
out_path = r'D:\Project0611\weixin_image\weixin1212800\\'

def imageDecode(f,fn):
    """
    解码
    :param f: 微信图片路径
    :param fn:微信图片目录下的.bat
    :return:
    """
    # 读取.bat
    dat_read = open(f,"rb")
    # 图片输出路径
    out = out_path + fn + ".jpg"
    # 图片写入
    png_write = open(out,"wb")
    # 循环字节
    for now in dat_read:
        for nowByte in now:
            # 转码计算
            newByte = nowByte ^ 0x1e
            # 转码后重新写入
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()
    # pass

def findFile(f):
    """
    寻找文件
    :param f:微信图片路径
    :return:
    """
    # 把路径文件夹下的文件以列表呈现
    fsinfo = os.listdir(f)
    # 逐步读取文件
    for fn in fsinfo:
        # 拼接路径：微信图片路径+图片名
        temp_path = os.path.join(f,fn)
        # 判断目录还是.bat
        if not os.path.isdir(temp_path):
            print('文件路径：{}'.format(temp_path))
            print(fn)
            # 转码函数
            imageDecode(temp_path,fn)
        else:
            pass

# 运行
findFile(into_path)
