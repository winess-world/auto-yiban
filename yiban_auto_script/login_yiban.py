# _*_ coding:utf-8 -*-
__author__ = 'mystery men'
__time__ = '2020/5/25 14:51'

from yiban_auto_script.package_all import *

orc_scheduling = __import__('yiban_auto_script.orc_scheduling', fromlist=("orc_scheduling",))
template = __import__("yiban_auto_script.template", fromlist=("template",))
cope_image = __import__('yiban_auto_script.cope_image', fromlist=('cope_image',))
from yiban_auto_script.cope_image import *
from yiban_auto_script.ascension_yiban_egpa import *
from yiban_auto_script.setting import *


error_user=[]

def agency(user, passwd,puid_id="",group_id=""):
    '''
    中间代理
    :param user: 用户名
    :param passwd: 用户密码
    :return:
    '''
    Login(user, passwd,puid_id,group_id).login()


# TODO:登录模块
class Login(object, metaclass=getattr(template, "MyMetaClass")):
    '''
    登录
    '''

    def __init__(self, user: str, password: str,puid_id:str,group_id:str):
        '''
        初始化
        :param user: 用户名
        :param password: 用户密码
        '''
        self.person = requests.Session()
        self.person.headers = self.headers
        self.cookies = self.person.cookies.get_dict()
        self.ORC = getattr(orc_scheduling, "ORC")
        self.Cope_image = getattr(cope_image, "Cope_image")
        self.user = user
        self.password = password
        self.puid_id=puid_id
        self.group_id=group_id

    # 登录易班
    def login(self, login_is=False):

        '''
        进行模拟登录
        :return:
        '''

        # 将密码进行加密和获取时间戳
        rsa_pass, keys_time = self.RSA_and_time(self.__password, self.__person)

        # 保存验证码
        self.save_verification_image(self.__person)
        # 进行虚假请求
        login_data = {
            "account": self.__user,
            "password": rsa_pass,
            "captcha": None,
            "keysTime": keys_time,
            'is_rember': 1
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3938.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        login_url = "https://www.yiban.cn/login/doLoginAjax"
        login_res = self.__person.post(url=login_url, data=login_data, headers=header, cookies=self.__cookies,verify=False)
        print(login_res.json())
        if detection:
            print("正在测试账号密码")

            if login_res.json()['code'] == 422:
                print(self.__user,"账号不存在")
            elif login_res.json()['code'] == 200:
                error_user.append("账号密码正确")
                print(self.__user, "账号密码正确")
            else:
                if login_res.json()['code'] == "711":
                    print("需要验证码")
                    self.__Cope_image('./verification_image.png').__call__()
                    print("集合", set_new)
                    while True:
                        if login_is:
                            break
                        else:
                            if set_new.__len__() == 0:
                                self.save_verification_image(self.__person)
                                self.__Cope_image('./verification_image.png').__call__()
                            else:
                                login_is, login_taken, login_information = self.real_login(rsa_pass, keys_time, header)
                                set_new.clear()
                                if not login_is:
                                    self.save_verification_image(self.__person)
                                    self.__Cope_image('./verification_image.png').__call__()
                else:
                    error_user.append("账号密码出错")
                    print(self.__user, "账号密码出错")

        else:
            if login_res.json()['code'] == 422:
                print(self.__user,"账号不存在")
            elif login_res.json()['code'] == "711":
                print(login_res.text)
                print("需要验证码")
                self.__Cope_image('./verification_image.png').__call__()
                print("集合", set_new)
                while True:
                    if login_is:
                        break
                    else:
                        if set_new.__len__() == 0:
                            self.save_verification_image(self.__person)
                            self.__Cope_image('./verification_image.png').__call__()
                        else:
                            login_is, login_taken,login_information = self.real_login(rsa_pass, keys_time, header)
                            set_new.clear()
                            if not login_is:
                                self.save_verification_image(self.__person)
                                self.__Cope_image('./verification_image.png').__call__()



            elif login_res.json()['code'] == 200:
                # 获取登录结果
                getlogin_url = "http://www.yiban.cn/ajax/my/getLogin"
                getlogin_data = {
                    "": ""
                }
                getlogin_res = self.__person.post(url=getlogin_url, data=getlogin_data)
                getlogin_res_content = getlogin_res.json()
                print("无验证码获取登录结果",getlogin_res_content)
                if getlogin_res_content['code'] == 200 and getlogin_res_content['data']['isLogin'] == True:
                    print("登录成功")
                    print(login_res.json())
                    login_taken=getlogin_res_content['data']['user']['token']
                    login_is = True

                else:
                    print("状态码为{},异常信息为{}".format(getlogin_res_content['code'],
                                                  eval('u"%s"' % getlogin_res_content['message'])))
            else:
                print("异常")
                print(login_res.text)

            if not detection:
                print("登录状态", login_is)
                if login_is:
                    c = requests.cookies.RequestsCookieJar()  # 利用RequestsCookieJar获取
                    c.set('cookie-name', 'cookie-value')
                    self.__person.cookies.update(c)
                    header = self.__person.cookies.get_dict()
                    header['user-agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
                    header['x-requested-with']="XMLHttpRequest"
                    print(header)
                    print("正在获取id")

                    print("id",self.__group_id,self.__puid_id)
                    for index,i in enumerate(Ascension_yiban_egpa.get_id(header,self.__person,self.__group_id,self.__puid_id)):
                        group_id, puid_id=i[0],i[1]
                        print('大家好')
                        if pattern=="1":
                            if index==1:
                                break
                        print('id获取成功',i)
                        print('正在发布话题')
                        Ascension_yiban_egpa.publish_article(header,self.__person,group_id, puid_id)
                        print('发布话题成功')
                        print("正在发布投票")
                        Ascension_yiban_egpa.vote(header,self.__person,group_id, puid_id)
                        print("发布投票成功")
                        print("正在发布动态")
                        Ascension_yiban_egpa.Release_the_dynamic(header,self.__person,group_id, puid_id)
                        print("发布动态成功")
                        print("正在发布miao")
                        header['loginToken']=header['yiban_user_token']
                        Ascension_yiban_egpa.post_Writing_blog(header,self.__person,group_id, puid_id)
                        del header['loginToken']
                        print("发布miao成功")
                        print("正在发布博客")
                        Ascension_yiban_egpa.logs(header,self.__person,login_taken,group_id, puid_id)
                        print("发布博客成功")
                        print("正在自动签到")
                        Ascension_yiban_egpa.sign_in(header,self.__person,group_id, puid_id)
                        print("自动签到成功")
                        print("微社区进行点赞评论")
                        Ascension_yiban_egpa.give_a_like(header,self.__person,group_id, puid_id)
                        print('微社区进行点赞评论成功')
                        print("正在进行投票")
                        Ascension_yiban_egpa.auto_vote(header,self.__person,group_id, puid_id)
                        print("自动投票成功")
                        print("正在访问群主页")
                        Ascension_yiban_egpa.visit_group(header,self.__person,group_id, puid_id)
                        print("访问群主页成功")
                        print("正在进行动态文章点赞，同情，评论")
                        Ascension_yiban_egpa.auto_like_dynamic_state(header,self.__person,group_id, puid_id)
                        print("完成动态文章点赞，同情，评论")
                        print("正在对博客进行转载，点赞，评论")
                        Ascension_yiban_egpa.like_logs(header,self.__person,group_id, puid_id)
                        print("完成对博客进行转载，点赞，评论")
                    set_new.clear()


            # 正在投票

            # messages = person.post(url='http://www.yiban.cn/forum/article/listAjax',data=login_data)
            # print(messages.text)

    def real_login(self, rsa_pass, keys_time, header):
        '''
        #进行真实登录
        :param rsa_pass:
        :param keys_time:
        :param header:
        :return:
        '''
        for index, i in enumerate(set_new):
            print("进行第{}尝试,尝试的字符串{}".format(index, i))

            # 登录易班
            login_url = "https://www.yiban.cn/login/doLoginAjax"
            login_data = {
                "account": self.__user,
                "password": rsa_pass,
                "captcha": i,
                "keysTime": keys_time,
                'is_rember': 1
            }
            login_res = self.__person.post(url=login_url, data=login_data, headers=header, cookies=self.__cookies).json()
            print('登录结果')
            print(login_res)
            if set_new.__len__() != index + 1:
                if login_res['code'] == "201":
                    print("验证码输入错误")
                    continue
            import time
            time.sleep(1)
            # 获取登录结果
            getlogin_url = "http://www.yiban.cn/ajax/my/getLogin"
            getlogin_data = {
                "": ""
            }
            getlogin_res = self.__person.post(url=getlogin_url, data=getlogin_data)
            getlogin_res_content = getlogin_res.json()
            print(getlogin_res_content)
            if getlogin_res_content['code'] == 200 and getlogin_res_content['data']['isLogin'] == True:
                print("登录成功")
                login_is = True
                global token

                token = getlogin_res_content['data']['user']['token']

                return True,token, getlogin_res_content
            elif getlogin_res_content['code'] == 415:
                print("账号密码出错")
                if detection:

                    error_user.append("账号密码出错")
                    print("账号密码错误")
                    return True,"",""

            else:
                print("状态码为{},异常信息为{}".format(getlogin_res_content['code'],
                                              eval('u"%s"' % getlogin_res_content['message'])))
        return False, "",""

    @classmethod
    def save_verification_image(cls, person):
        '''
        获取保存验证码
        :param verification_code:
        :return:
        '''
        verification_code = person.get(
            'https://www.yiban.cn/captcha/index?Tue%20Dec%2004%202018%2000:01:26%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)',
            verify=False).content
        with open('./verification_image.png', 'wb') as f:
            f.write(verification_code)

    @classmethod
    def RSA_and_time(cls, password, person):
        '''
        将密码进行RSA加密,获取时间
        :param password:
        :return:
        '''

        login_page_url = "https://www.yiban.cn/login"
        login_page_res = person.get(url=login_page_url)
        print(login_page_res)
        print(re.findall(r"BEGIN PUBLIC KEY-----\sM(.*)-----END PUBLIC KEY", login_page_res.text, re.S))
        # 获取公钥并加密
        public_key = re.findall(r"BEGIN PUBLIC KEY-----\sM(.*)-----END PUBLIC KEY", login_page_res.text, re.S)[0]
        public_key = '-----BEGIN PUBLIC KEY-----\nM' + public_key + '-----END PUBLIC KEY-----'
        # 成功加密对象
        rsa_key = RSA.importKey(public_key)
        # 对密码进行加密
        x = rsa.encrypt(password.encode(), rsa_key)
        rsa_pass = base64.b64encode(x).decode()
        # 获取时间戳
        keys_time = re.findall(r"data-keys-time='(.*?)'", login_page_res.text)[0]
        return rsa_pass, keys_time

