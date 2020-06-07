# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/25 10:10'

from yiban_auto_script.package_all import *
template=__import__('yiban_auto_script.template',fromlist=('template'))
from yiban_auto_script.orc_scheduling import ORC

global set_new
set_new=set('')

# TODO:图像处理模块
class time_num(object,metaclass=getattr(template,"MyMetaClass")):
    '''
    作为装饰器使用，返回函数执行需要花费的时间
    '''

    def time_this_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, end - start)
            return result
        return wrapper



class Cope_image(object, metaclass=getattr(template,"MyMetaClass")):
    '''
    对验证码进行锐度增强,对比度增强,亮度增强,灰度处理,二值化,去干扰线算法,降噪算法
    '''

    def __init__(self, path:str):
        '''
        初始化
        :param path: 
        '''
        self.path=path
        print(self.path)

    def __call__(self, *args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        self.image_Initial()

    @classmethod
    @time_num.time_this_function
    def image_orc(cls,image_path):
        result=ORC.dispatch_orc(image_path)
        print("结果",result)
        if len(result)!=0:
            if isinstance(result, list):
                for i in result:
                    print("进入")
                    i=re.findall('[\u4e00-\u9fa5]',i)
                    if len(i)==0:
                        print(i)
                    else:
                        for j in result:
                            set_new.add(j)
                        print("成功添加")


    def image_Initial(self):
        '''
        初始图像
        :param path:
        :return:
        '''
        if not os.path.exists('./deal_with_image'):
            os.mkdir('./deal_with_image')
        images = Image.open('{}'.format(self.__path))
        images.save('./deal_with_image/image_Initial.png')
        self.image_orc('./deal_with_image/image_Initial.png')
        self.enhance_Brightness(images)


    @classmethod
    def enhance_Contrast(cls, images:str, contrast:float=1.5):
        '''
        增强亮度
        :param contrast:
        :param images:
        :return:
        '''
        enh_con = ImageEnhance.Contrast(images)
        image_contrasted = enh_con.enhance(contrast)
        image_contrasted.save('./deal_with_image/image_contrasted.png')
        cls.image_orc('./deal_with_image/image_contrasted.png')
        cls.enhance_Brightness(image_contrasted)

    # @time_num.timethis
    @classmethod
    def enhance_Brightness(cls, image_contrasted:str, brightness:float=1.5):
        '''
        增强色彩
        :param image_contrasted:
        :param images:
        :return:
        '''
        enh_bri = ImageEnhance.Brightness(image_contrasted)
        image_brightened = enh_bri.enhance(brightness)
        image_brightened.save('./deal_with_image/image_brightened.png')
        cls.image_orc('./deal_with_image/image_brightened.png')
        cls.enhance_Color(image_brightened)

    @classmethod
    def enhance_Color(cls, image_brightened:str, color:float=1.5):
        '''
        增强色度
        :param images:
        :param color:
        :return:
        '''
        enh_col = ImageEnhance.Color(image_brightened)
        image_colored = enh_col.enhance(color)
        image_colored.save('./deal_with_image/image_colored.png')
        cls.image_orc('./deal_with_image/image_colored.png')
        cls.enhance_Sharpness(image_colored)

    @classmethod
    def enhance_Sharpness(cls, image_colored, sharpness:float=3.0):
        '''
        增强锐度
        :param image_colored:
        :param sharpness:
        :return:
        '''
        enh_sha = ImageEnhance.Sharpness(image_colored)
        image_sharped = enh_sha.enhance(sharpness)
        image_sharped.save('./deal_with_image/image_sharped.png')
        cls.image_orc('./deal_with_image/image_sharped.png')
        cls.Image_gray(image_sharped)

    @classmethod
    def Image_gray(cls, image_sharped, kind="L"):
        '''
        灰度处理
        :param image_sharped:
        :param kind:
        :return:
        '''
        # 进行灰度处理
        image = image_sharped.convert(kind)
        image.save('./deal_with_image/image_gray.png')
        cls.image_orc('./deal_with_image/image_gray.png')
        cls.Image_Binary_value(image)

    @classmethod
    def Image_Binary_value(cls, image:str, threshold:float=49.0):
        '''
        二值化
        :param image:
        :param threshold:
        :return:
        '''
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, '1')
        image.save('./deal_with_image/image_binary_value.png')
        cls.image_orc('./deal_with_image/image_binary_value.png')
        cls.Image_away_line(image)

    @classmethod
    def Image_away_line(cls, image:str):
        '''
        去干扰线算法
        :param image:
        :return:
        '''
        img_array = image.load()
        width = image.size[0]
        height = image.size[1]
        print("正在进行去干扰线算法")
        for i in range(0, 1000):
            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    count = 0
                    if img_array[x, y] == img_array[x - 1, y + 1]:
                        count += 1
                    if img_array[x, y] == img_array[x, y + 1]:
                        count += 1
                    if img_array[x, y] == img_array[x + 1, y + 1]:
                        count += 1
                    if img_array[x, y] == img_array[x - 1, y]:
                        count += 1
                    if img_array[x, y] == img_array[x + 1, y]:
                        count += 1
                    if img_array[x, y] == img_array[x - 1, y - 1]:
                        count += 1
                    if img_array[x, y] == img_array[x, y - 1]:
                        count += 1
                    if img_array[x, y] == img_array[x + 1, y - 1]:
                        count += 1
                    if count <= 2 and count > 0:
                        img_array[x, y] = 1
        print("干扰线算法完成")
        image.save('./deal_with_image/image_away_line.png')
        cls.image_orc('./deal_with_image/image_away_line.png')
        cls.Image_Center_decline(image)

    @classmethod
    def Image_Center_decline(cls, image:str):
        '''
        中心降噪算法
        :param image:
        :return:
        '''
        print("进行中心降噪,使用八邻域算法")
        # 降噪算法,八邻域算法
        pixdata = image.load()
        wight, height = image.size
        for x in range(1, wight - 1):
            for y in range(1, height - 1):
                count = 0
                # 上方像素
                if pixdata[x, y + 1] == 1:
                    count += 1
                # 下方像素
                if pixdata[x, y - 1] == 1:
                    count += 1
                # 左方像素
                if pixdata[x - 1, y] == 1:
                    count += 1
                # 右方像素
                if pixdata[x + 1, y] == 1:
                    count += 1
                # 左上方像素
                if pixdata[x - 1, y + 1] == 1:
                    count += 1
                # 右上方像素
                if pixdata[x + 1, y + 1] == 1:
                    count += 1
                # 左下方像素
                if pixdata[x - 1, y - 1] == 1:
                    count += 1
                # 右下像素
                if pixdata[x + 1, y - 1] == 1:
                    count += 1
                if count > 5:
                    pixdata[x, y] = 1
        print("完成降八邻域中心降噪算法")
        image.save('./deal_with_image/image_decline.png')
        cls.image_orc('./deal_with_image/image_decline.png')
        cls.Image_frame_decline(image)

    @classmethod
    def Image_frame_decline(cls, image:str):
        '''
        边框降噪算法
        :param image:
        :return:
        '''
        print("正在进行边框去噪算法")
        # 边框去噪算法
        pixdata = image.load()
        wight, height = image.size
        for x in range(0, wight):
            for y in range(0, height):
                # 左边框
                if x == 0:
                    if pixdata[x, y] == 0 and pixdata[x + 1, y] == 1:
                        pixdata[x, y] = 1
                # 右边框
                if x == wight - 1:
                    if pixdata[x, y] == 0 and pixdata[x - 1, y] == 1:
                        pixdata[x, y] = 1
                # 下边框
                if y == 0:
                    if pixdata[x, y] == 0 and pixdata[x, y + 1] == 1:
                        pixdata[x, y] = 1
                # 上边框
                if y == height - 1:
                    if pixdata[x, y] == 0 and pixdata[x, y - 1] == 1:
                        pixdata[x, y] = 1
        print("完成边框去噪算法")
        image.save('./deal_with_image/image_frame_decline.png')
        cls.image_orc('./deal_with_image/image_frame_decline.png')



