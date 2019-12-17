# weixin_Image.bat 破解
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e
# 微信.bat 16进制 97 4e 50
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
