# # # _*_ coding:utf-8 -*-
# # __author__ = '鲁江洋'
# # __time__ = '2020/5/25 12:07'
# #
# # # TODO:模拟测试环境模块
# #
# # # from 1.package_all import *
# # # from 1.orc_scheduling import *
# #
# #
# # # print(ORC.baidu_orc_one_limit('./deal_wi# print(ORC.baidu_orc_two_free('./deal_with_image/image_convert.png'))th_image/image_convert.png'))
# # # print(ORC.baidu_orc_two_free('./deal_with_image/image_convert.png'))
# # # print(ORC.TencentOcr_three_limit('./deal_with_image/image_convert.png'))
# # # print(ORC.UtOcrB('./deal_with_image/image_convert.png'))
# #
# #
# # import requests
# # import re
# # import rsa
# # import time
# # from Crypto.PublicKey import RSA
# # import base64
# # import json
# # # import jsonpath
# #
# # person = requests.Session()
# # cookies = person.cookies.get_dict()  # cookies
# # person.headers = {
# #     "Accept": "application/json, text/javascript, */*; q=0.01",
# #     "Accept-Encoding": "gzip, deflate, br",
# #     "Accept-Language": "zh-CN,zh;q=0.9",
# #     "Connection": "keep-alive",
# #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
# #     # "Host": "q.yiban.cn",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
# #                   "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# # }
# #
# # def get_id(header,login_taken):
# #
# #     # 测试
# #     global puid_id
# #     global group_id
# #     global class_grade
# #     result = person.get('https://www.yiban.cn/my/group', headers=header).text
# #     group_id = re.findall('/newgroup/indexPub/group_id/(\d+)/puid/\d+"><span>', result)
# #     puid_id = re.findall('/newgroup/indexPub/group_id/\d+/puid/(\d+)"><span>', result)
# #     class_grade = re.findall('<a href="/newgroup/indexPub/group_id/\d+/puid/\d+"><span>(.*?)</span></a>', result)
# #     print(group_id, puid_id, class_grade)
# #     for index, i in enumerate(group_id):
# #         print(i, puid_id[index], class_grade[index])
# #         puid_id = i
# #         puid_id = puid_id[index]
# #         class_grade = class_grade[index]
# #         print(login_taken)
# #         data = {
# #             "title": "你好",
# #             "content": "你真好",
# #             "ranges": "1",
# #             "type": "1",
# #             # "f41dd412fa4224d17fe7198011e6ae06"
# #             "token": login_taken,
# #             "ymm": "1",
# #             "dom": ".js-submit",
# #         }
# #         response = person.post('https://www.yiban.cn/blog/blog/addblog', headers=header, data=data)
# #         print(response.text)
# # # 登录易班
# # def login(user, password):
# #     login_page_url = "https://www.yiban.cn/login"
# #     login_page_res = person.get(url=login_page_url)
# #     # print(login_page_res.text)
# #     # 获取公钥并加密
# #     public_key = re.findall(r"BEGIN PUBLIC KEY-----\sM(.*)-----END PUBLIC KEY", login_page_res.text, re.S)[0]
# #     public_key = '-----BEGIN PUBLIC KEY-----\nM' + public_key + '-----END PUBLIC KEY-----'
# #     print(public_key)
# #     rsa_key = RSA.importKey(public_key)
# #     x = rsa.encrypt(password.encode(), rsa_key)
# #     rsa_pass = base64.b64encode(x).decode()
# #     print(rsa_pass)
# #     # 获取时间戳
# #     keys_time = re.findall(r"data-keys-time='(.*?)'", login_page_res.text)[0]
# #     print(keys_time)
# #     check_in = captcha()
# #     # random = time.time()
# #     # random = round(random, 2)  # 只取两位小数
# #
# #     # 登录易班
# #     login_url = "https://www.yiban.cn/login/doLoginAjax"
# #
# #     header = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3938.0 Safari/537.36',
# #         'X-Requested-With': 'XMLHttpRequest'
# #     }
# #
# #     data = {
# #         "account": user,
# #         "password": rsa_pass,
# #         "captcha": None,
# #         "keysTime": keys_time,
# #         # 'is_rember':1
# #     }
# #
# #     login_res = person.post(url=login_url, data=data, headers=header, cookies=cookies)
# #     print('登录结果')
# #     print(login_res)
# #     print(login_res.text)
# #
# #
# #     login_data = {
# #         "account": user,
# #         "password": rsa_pass,
# #         "captcha": check_in,
# #         "keysTime": keys_time,
# #         # 'is_rember': 1
# #     }
# #
# #     login_res = person.post(url=login_url, data=login_data, headers=header,cookies=cookies)
# #     print('登录结果')
# #     print(login_res)
# #
# #     # 获取登录结果
# #     getlogin_url = "http://www.yiban.cn/ajax/my/getLogin"
# #     getlogin_data = {
# #         "": ""
# #     }
# #     getlogin_res = person.post(url=getlogin_url, data=getlogin_data)
# #     print(getlogin_res)
# #     getlogin_res_content = getlogin_res.json()
# #     print(getlogin_res_content)
# #     messages = person.post(url='http://www.yiban.cn/forum/article/listAjax',data=login_data)
# #     print(messages.text)
# #
# #     c = requests.cookies.RequestsCookieJar()  # 利用RequestsCookieJar获取
# #     print(c)
# #     c.set('cookie-name', 'cookie-value')
# #     person.cookies.update(c)
# #
# #     getlogin_url = "http://www.yiban.cn/ajax/my/getLogin"
# #     getlogin_data = {
# #         "": ""
# #     }
# #     getlogin_res = person.post(url=getlogin_url, data=getlogin_data)
# #     getlogin_res_content = getlogin_res.json()
# #     login_taken=getlogin_res_content['data']['user']['token']
# #     print(person.cookies)
# #     header=person.cookies.get_dict()
# #     header[
# #         'user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
# #     header['x-requested-with'] = "XMLHttpRequest"
# #     header['loginToken'] = login_taken
# #     print("打印",header)
# #     get_id(header,login_taken)
# #
# # def captcha():  # 图片验证码
# #     captcha_check_url = "https://www.yiban.cn/captcha/index?Tue%20Dec%2004%202018%2000:01:2" \
# #                         "6%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)"
# #     captcha_check_respond = person.get(url=captcha_check_url)
# #     print(captcha_check_respond)
# #     captcha_content = captcha_check_respond.content  # 转换类型
# #     fb = open('captcha.jpg', 'wb')  # 把字节类型转换为图片文件
# #     fb.write(captcha_content)
# #     fb.close()
# #     check_in = input("请输入图片验证码>>>:")
# #     return check_in
# #
# #
# # # login("15325488390","lujiangyang789")
# # login('15325488390','lujiangyang789')
# #
# #
# #
# #
# # # print('创建我的元类：')
# # #
# # #
# # # class MyMetaclass(type):
# # #
# # #     # 自建我们的自己的元类
# # #     def __init__(self, name, bases, dict):
# # #         print('init')
# # #         super().__init__(name, bases, dict)
# # #
# # #
# # #     def __call__(self, *args, **kwargs):
# # #         print('call')
# # #         return super().__call__(*args, **kwargs)
# # #
# # #
# # #     def __new__(cls, *args, **kwargs):
# # #         print('new')
# # #         return super().__new__(cls, *args, **kwargs)
# # #
# # #     pass
# # #
# # # print('创建People类：')
# # #
# # #
# # # class People(object, metaclass=MyMetaclass):
# # #
# # #     # 以MyMetaclass为元类创建一个类
# # #     def __init__(self):
# # #         print('sub_init')
# # #         super().__init__()
# # #
# # #
# # #     def __call__(self, *args, **kwargs):
# # #         print('sub_call')
# # #
# # #
# # #     def __new__(cls, *args, **kwargs):
# # #         print('sub_new')
# # #         return super().__new__(cls, *args, **kwargs)
# # #
# # #     def hh(self):
# # #         print("hh")
# #
# # # People()()
# #
# # class hello():
# #     def __init__(self,i):
# #         self.hello=i
# #     def jj(self):
# #         print(self.hello)
# #
# # hello(7).jj()
# # template = __import__("yiban_auto_script.template", fromlist=("template",))
# # def agency():
# #     '''
# #     中间代理
# #     :param user: 用户名
# #     :param passwd: 用户密码
# #     :return:
# #     '''
# #     Login("fsdfsdf", "fsdfse").login()
# #
# # import requests
# # # TODO:登录模块
# # class Login(object, metaclass=getattr(template, "MyMetaClass")):
# #     '''
# #     登录
# #     '''
# #
# #     def __init__(self, user: str, password: str):
# #         '''
# #         初始化
# #         :param user: 用户名
# #         :param password: 用户密码
# #         '''
# #         self.person = requests.Session()
# #         self.person.headers = self.headers
# #         self.cookies = self.person.cookies.get_dict()
# #         self.ORC = getattr(orc_scheduling, "ORC")
# #         self.Cope_image = getattr(cope_image, "Cope_image")
# #         self.user = user
# #         self.password = password
# #
# #     # 登录易班
# #     @classmethod
# #     def login(self, login_is=False):
# #
# #         '''
# #         进行模拟登录
# #         :return:
# #         '''
# #         print(self.person)
# # agency()
# import re
# import requests
# puid_id=24994856
# group_id=1119233
# header={
# "Cookie": "UM_distinctid=17239e7ce1c97-04a4d1208b70b9-2393f61-1fa400-17239e7ce1d3ba; preview_hidden=0; MESSAGE_NEW_VERSION=1; FEED_NEW_VERSION_25106766=1; ticket_user_token=e8db2a2eb70db0fda7d8ccb9b50b9189; YB_SSID=df2261a9dd0351e204cf7ef5185bff36; waf_cookie=bee8956e-68ed-455abff00bf9edadafc762f770ef7fcf4009; timezone=-8; yiban_user_token=615232931e9c9f518cf5877b4a6f2f68; CNZZDATA1253488264=12713481-1590108052-null%7C1591362135; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FNewgroup%2Findexpub%7C1591364365845%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E9%99%95%E8%A5%BF%E5%9B%BD%E9%98%B2%E5%B7%A5%E4%B8%9A%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%7C1591364365845",
# # "Host": "www.yiban.cn",
# # "Referer": "http://www.yiban.cn/newgroup/indexPub/group_id/1119233/puid/24994856",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# "X-Requested-With": "XMLHttpRequest",
# }
# result=requests.get('http://www.yiban.cn/newgroup/showMorePub/puid/24994856/group_id/805698/type/1',headers=header,verify=False).text
# uid=re.findall('/user/index/index/user_id/(\d+)"><i',result)[0]
# id=re.findall('/vote/vote/showDetail/vote_id/(\d+)/puid/', result)
# print(uid)
# vote_id=[id[i-1] for i in range(1,len(id)+1) if i%2==0]
# print(vote_id)
# for index,i in enumerate(vote_id):
#     data = {
#     "vote_id": i,
#     "uid": uid,
#     "puid": puid_id,
#     "pagetype": "1",
#     "group_id": group_id,
#     "actor_id": uid,
#     "top_power": "f",
#     "edit_power": "t",
#     "end_power": "f",
#     "del_power": "t",
#     "block_power": "f",
#     "isSchoolVerify": "1",
#     "is_public": "f",
#     "is_anonymous": "t",
#     "token": "",
#     "out_power": "f",
#     "isMember": "",
#     "url[getVoteDetail]": "vote/vote/getVoteDetail",
#     "url[output]": "/vote/Expand/output",
#     "url[getCommentDetail]": "vote/vote/getCommentDetail",
#     "url[addComment]": "vote/vote/addComment",
#     "url[editLove]": "vote/vote/editLove",
#     "url[vote]": "vote/vote/act",
#     "url[setIsTop]": "vote/Expand/setIsTop",
#     "url[setManualEndVote]": "vote/Expand/setManualEndVote",
#     "url[delVote]": "vote/Expand/delVote",
#     "url[delComment]": "vote/vote/delComment",
#     "url[shieldVote]": "vote/Expand/shieldVote",
#     "url[getAnonymous]": "vote/Expand/getAnonymous",
#     "url[userInfo]": "user/index/index",
#     "isLogin": "1",
#     "isOrganization": "0",
#     "ispublic": "0",
# }
#     # print(data)
#     result=requests.post('https://www.yiban.cn/vote/vote/getVoteDetail',headers=header,data=data,verify=False).json()
#     print(result)
#     voptions_id=result['data']['option_list'][0]['id']
#     # print(voptions_id)
#
#     data={
#     "puid": puid_id,
#     "group_id": group_id,
#     "vote_id":  i,
#     "actor_id": uid,
#     "voptions_id": voptions_id,
#     "minimum": "1",
#     "scopeMax": "1",
#     }
#     print(data)
#     # print("最终",data)
#     result=requests.post('https://www.yiban.cn/vote/vote/act',headers=header,data=data,verify=False).json()
#     print(result)
#
#
#
import re
import requests
from lxml import etree

group_id=1119233
puid_id=24994856
header={
"Cookie": "UM_distinctid=17239e7ce1c97-04a4d1208b70b9-2393f61-1fa400-17239e7ce1d3ba; preview_hidden=0; MESSAGE_NEW_VERSION=1; FEED_NEW_VERSION_25106766=1; ticket_user_token=e8db2a2eb70db0fda7d8ccb9b50b9189; YB_SSID=649e13465cce1941f75010f450172aa5; waf_cookie=ccd7a816-829a-466923b41854cd9f00b56630946abe4d1988; yiban_user_token=8b427a8c526532f2991d86911ae585bc; timezone=-8; CNZZDATA1253488264=12713481-1590108052-null%7C1591402083; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FNewgroup%2Findexpub%7C1591406297551%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E9%99%95%E8%A5%BF%E5%9B%BD%E9%98%B2%E5%B7%A5%E4%B8%9A%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%7C1591406297551",
# "Host": "www.yiban.cn",
# "Referer": "http://www.yiban.cn/newgroup/indexPub/group_id/1119233/puid/24994856",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}
response=requests.get('https://www.yiban.cn/newgroup/showMore/puid/{}/group_id/{}/type/3'.format(puid_id,group_id),headers=header).text

all_uid = [re.search('\d\d\d\d+',i).group() for i in filter(lambda x: not x.startswith('j'), etree.HTML(response).xpath('//ul[@class="user-list member-leader clearfix"]/li//@href'))]
print(all_uid)
for index,i in enumerate(all_uid):
    result1=requests.get('https://www.yiban.cn/blog/blog/getBlogList?page=1&size=10&uid={}'.format(i),headers=header).json()
    for j in result1['data']['list']:
        blogid=j['id']
        Mount_id=j['Mount_id']
        oid=j['User_id']
        result2=requests.get('https://www.yiban.cn/blog/blog/addlike?uid={}&blogid={}'.format(i,blogid),headers=header).json()
        print(result2)
        if result2['code'] == 200:
            print("点赞成功")
        elif result2['code'] == "202" and result2['message'] == "已点赞":
            print("已经点赞")
        else:
            print("失败未知原因")

        result=["你好","棒"]
        data={
            "blogid": blogid,
            "oid": oid,
            "mid": Mount_id,
            "reply_user_id": 0,
            "reply_comment_id": 0,
            "content": result[1],
        }
        result3=requests.post('https://www.yiban.cn/blog/blog/addcomment',headers=header,data=data).json()
        print(result3)
        if result3['code'] == 200:
            print("评论成功")
        else:
            print("失败未知原因")
        result4=requests.get('https://www.yiban.cn/blog/blog/copyblog?blogid={}&suid={}&range=1'.format(i,oid),headers=header).json()
        print(result4)
        if result4['code'] == 200:
            print("转载成功")
        else:
            print("失败未知原因")
