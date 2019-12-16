# weixin图片转码

import os


class WeixinImageDecode(object):
    def __init__(self, into_path, out_path ,jpg_decimal=255):
        """
        初始化
        :param into_path: 文件输入路径
        :param out_path: 文件转换后存放路径
        :param jpg_decimal:jpg16进制FF 转成十进制255
        """
        self.into_path = into_path
        self.out_path = out_path
        self.jpg_decimal = jpg_decimal

    def get_dat_decimal(self):
        """
        获取微信图片的开头值
        :return: dat_decimal
        """
        fsinto = os.listdir(self.into_path)
        # print(fsinto)
        into_path = os.path.join(self.into_path, fsinto[0])
        # print(into_path)
        with open(into_path, 'rb')as f:
            dat_strs = f.readline(1)
            # print(str)
            for dat_str in dat_strs:
                # print(dat_strs)
                dat_decimal = dat_str
                # print(dat_decimal)
                return dat_decimal

    def xor_Calculate(self, dat_decimal):
        """
        根据weixin图片.bat计算xor值
        :param dat_decimal: dat_decimal
        :return: xor
        """
        xor = dat_decimal ^ self.jpg_decimal
        # xor = hex(xor)
        return xor

    def imageDecode(self, f, fn ,xor):
        """
        解码
        :param f: 微信图片路径
        :param fn:微信图片目录下的.bat
        :return:
        """
        # 读取.bat
        dat_read = open(f, "rb")
        # 图片输出路径
        out = self.out_path + fn + ".jpg"
        # 图片写入
        png_write = open(out, "wb")
        # 循环字节
        for now in dat_read:
            for nowByte in now:
                # print(xor)
                # 转码计算
                newByte = nowByte ^ xor
                # 转码后重新写入
                png_write.write(bytes([newByte]))
        dat_read.close()
        png_write.close()

    def findFile(self, f,xor):
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
            temp_path = os.path.join(f, fn)
            # 判断目录还是.bat
            if not os.path.isdir(temp_path):
                print('文件路径：{}'.format(temp_path))
                print(fn)
                # 转码函数
                weixinImageDecode.imageDecode(temp_path, fn, xor)
            else:
                pass

    def mian(self):
        dat_decimal = weixinImageDecode.get_dat_decimal()
        xor = weixinImageDecode.xor_Calculate(dat_decimal)
        weixinImageDecode.findFile(into_path, xor)



if __name__ == '__main__':
    # 录入需要转换的微信路径
    into_path = 'D:\Project0611\weixin_image\weixin1212800'
    # 录入需要保存后图片的路径
    out_path = 'D:\Project0611\weixin_image\weixin1212800\\'
    weixinImageDecode = WeixinImageDecode(into_path, out_path)
    # dat_decimal = weixinImageDecode.get_dat_decimal()
    # xor = weixinImageDecode.xor_Calculate(dat_decimal)
    # weixinImageDecode.findFile(into_path,xor)
    weixinImageDecode.mian()


