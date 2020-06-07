# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/25 10:01'
from yiban_auto_script.package_all import *


# TODO 元类模板

class MyMetaClass(type):
    '''
    对类的所有属性，私有化，以及必须写注释
    '''

    def __new__(cls, cls_name, cls_bases, cls_dict):
        '''
        添加类属性与强制要求写注释
        :param cls_name: 类的名称
        :param cls_bases: 类的基类
        :param cls_dict: 类的属性
        :return:
        '''
        # cls_dict['person'] = requests.Session()
        cls_dict['set_all'] = set('')
        cls_dict['headers'] = {
            # 'Connection': 'close',
            "referer": "http://www.yiban.cn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }

        if '__doc__' not in cls_dict or len(cls_dict['__doc__'].strip()) == 0:
            raise TypeError('类:%s 必须有文档注释,并且不能为空' % cls_name)

        for key, value in cls_dict.items():
            if not key.startswith('__'):
                continue
            if not callable(value):
                continue
            if not value.__doc__ or len(value.__doc__.strip()) == 0:
                raise TypeError('函数:%s 必须有文档注释，并且不能为空.' % (key))
        return super().__new__(cls, cls_name, cls_bases, cls_dict)

    def __call__(cls, *args, **kwargs):
        '''
        将所有实例属性进行变为私有属性
        :param args:类传参元组
        :param kwargs:类传参字典
        :return:
        '''
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        obj.__dict__ = {'_%s__%s' % (cls.__name__, key): value for key, value in obj.__dict__.items()}
        return obj


# class hello(object, metaclass=MyMetaClass):
#     '''
#     kk
#     '''
#
#     gg = 10
#
#     def __init__(self):
#         '''
#         你好
#         '''
#         self.gg = 19
#
#     def hh(self):
#         print("你真好")
#
#     @classmethod
#     def jj(cls):
#         print("你真棒")
#
#
# hello().hh()
# hello.jj()
