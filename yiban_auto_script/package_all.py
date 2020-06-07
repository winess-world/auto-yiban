# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/25 11:00'

#TODO:包模块

requests = __import__('requests')
re = __import__('re')
rsa = __import__('rsa')
base64 = __import__('base64')
json = __import__('json')
os=__import__('os')
time=__import__('time')
copy=__import__('copy')
random=__import__('random')
threading=__import__('threading')

from lxml import etree
from functools import wraps
from Crypto.PublicKey import RSA
from PIL import Image, ImageEnhance
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


