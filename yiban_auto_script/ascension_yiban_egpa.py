# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/28 16:21'
from yiban_auto_script.package_all import *
template=__import__("yiban_auto_script.template",fromlist=("template",))
from yiban_auto_script.bullshit import *
from yiban_auto_script.setting import *


#TODO:提升egpa
class Ascension_yiban_egpa(object,metaclass=getattr(template,"MyMetaClass")):
    '''
    刷egpa
    '''
    list1=['今日欣赏','今日推荐','','我发现了一个好的','','奔跑吧',"咆哮吧",'go']
    list2=["你对自己说早晚安了吗","今天你对自己说早晚安了吗","请收下这份祝福","请收下他"]

    @classmethod
    def get_id(cls,header,person,group_id="",puid_id=""):

        # 测试
        # header = {
        #     "Cookie":requests.utils.dict_from_cookiejar(cls.person.cookies),
            # "cookie": "UM_distinctid=17239e7ce1c97-04a4d1208b70b9-2393f61-1fa400-17239e7ce1d3ba; preview_hidden=0; MESSAGE_NEW_VERSION=1; FEED_NEW_VERSION_25106766=1; YB_SSID=11e03dd5fd6c6046156a3fa6bd82919f; waf_cookie=25169252-989a-4ddbb985735b91556f9a6d63773f8fad762d; yiban_user_token=e8db2a2eb70db0fda7d8ccb9b50b9189; timezone=-8; _YB_OPEN_V2_0=1BSnmK0l2u0eI804; CNZZDATA1253488264=12713481-1590108052-null%7C1590823565; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FMy%2Fgroup%7C1590828663510%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E9%99%95%E8%A5%BF%E5%9B%BD%E9%98%B2%E5%B7%A5%E4%B8%9A%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%7C1590828663510",
            # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        # }
        if pattern=="2":
            if group_id == "" or puid_id == "":
                raise Exception('You select 2 but you group_id and puid_id not assignment')


        global class_grade
        result = person.get('https://www.yiban.cn/my/group', headers=header).text
        print(person.get('https://www.yiban.cn/my/group', headers=header))
        all_group_id = re.findall('/newgroup/indexPub/group_id/(\d+)/puid/\d+"><span>', result)
        all_puid_id = re.findall('/newgroup/indexPub/group_id/\d+/puid/(\d+)"><span>', result)
        all_class_grade = re.findall('<a href="/newgroup/indexPub/group_id/\d+/puid/\d+"><span>(.*?)</span></a>', result)
        print(all_group_id, all_puid_id, all_class_grade)

        if pattern=="2":
            print("指定id", puid_id, group_id)
            print(group_id not in all_group_id)
            print(puid_id not in all_puid_id)
            print(all_group_id.index(group_id) != all_puid_id.index(puid_id))
            print(all_group_id.index(group_id))
            print(all_puid_id.index(puid_id))
            if group_id not in all_group_id or puid_id not in all_puid_id:
                raise Exception('You select 2 but your group_id and puid_id Seems wrong')
            else:
                yield group_id,puid_id,all_class_grade[all_group_id.index(group_id)]
        else:
            for index,i in enumerate(all_group_id):
                if pattern=="3":
                    if re.search("{}".format(sign),all_class_grade[index])==None:
                        continue
                group_id=i
                puid_id=all_puid_id[index]
                class_grade=all_class_grade[index]
                yield group_id,puid_id,class_grade

    @classmethod
    def publish_article(cls,header,person,group_id,puid_id):
        '''
        发布话题
        :return:
        '''

        result = dispath([])
        if result[0] == "":
            title = random.choice(cls.list2)
            content = result[1]
        else:
            title = random.choice(cls.list1)+result[0]
            content = result[1]
        data = {
            "puid": puid_id,
            "pubArea": group_id,
            "title": title,
            "content": "<p>{}</p>".format(content.replace(' ', '&nbsp;')),
            "isNotice": "false",
            "dom": ".js-submit",
        }

        response = person.post('https://www.yiban.cn/forum/article/addAjax', headers=header, data=data, verify=False).json()
        print(response)

    @classmethod
    def vote(cls,header,person,group_id,puid_id):
        '''
        投票
        :return:
        '''
        result=dispath([1,8])
        data = {
            "puid": puid_id,
            "scope_ids": group_id,
            "title": result[0],
            "subjectTxt": result[1],
            "subjectPic": "",
            "options_num": "3",
            "scopeMin": "1",
            "scopeMax": "1",
            "minimum": "1",
            "voteValue": time.strftime("%Y-%m-%d %H:%M", time.localtime(1893427200)),
            "voteKey": "2",
            "public_type": "0",
            "isAnonymous": "1",
            "voteIsCaptcha": "0",
            "istop": "1",
            "sysnotice": "2",
            "isshare": "1",
            "rsa": "1",
            "dom": ".js-submit",
            "group_id": group_id,
            "subjectTxt_1": "{}{}".format(random.choice(['优质','good','优秀','优','好','挺好','不错','真好','哇，优秀']),result[0]),
            "subjectTxt_2": "{}{}".format(random.choice(['一般','还好','好行','凑合','可以','common','还好啦']),result[0]),
            "subjectTxt_3": "{}{}".format(random.choice(['差劲','差','不行','low','真菜','菜鸡','菜极了','还没有我编的好']),result[0]),
        }

        result=person.post('http://www.yiban.cn/vote/vote/add',data=data,headers=header,verify=False).json()
        print(result)
        return result

    @classmethod
    def Release_the_dynamic(cls,header,person,group_id,puid_id):
        '''
        发布动态
        :return:
        '''

        result=dispath([7])
        data = {
            "content": result[1],
            "privacy": "0",
            "dom": ".js-submit",
        }
        result=person.post('http://www.yiban.cn/feed/add',headers=header,data=data,verify=False)
        print(result)




    @classmethod
    def post_Writing_blog(cls,header,person,group_id,puid_id):
        '''
            发布miao
        '''
        result = dispath([])
        if result[0] == "":
            title = random.choice(cls.list2)
            content = result[1]
        else:
            title = random.choice(cls.list1) + result[0]
            content = result[1]

        data = {
            "agree": "true",
            "content": "<p>{}</p>".format(content.replace(' ', '&nbsp;')),
            "kind": "1",
            "title": title,
        }
        response = person.post('http://ymm.yiban.cn/article/index/add', headers=header, json=data,verify=False)
        print(response.text)

    @classmethod
    def logs(cls,header,person,token,group_id,puid_id):
        '''
        发布博客
        :return:
        '''
        result = dispath([])
        if result[0] == "":
            title = random.choice(cls.list2)
            content = result[1]
        else:
            title = random.choice(cls.list1) + result[0]
            content = result[1]

        data = {
            "title": title,
            "content":content,
            "ranges": "1",
            "type": "1",
            # "f41dd412fa4224d17fe7198011e6ae06"
            "token": token,
            "ymm": "1",
            "dom": ".js-submit",
        }
        response = person.post('https://www.yiban.cn/blog/blog/addblog', headers=header, data=data,verify=False)
        print(response.text)

    @classmethod
    def sign_in(cls,header,person,group_id,puid_id):
        '''
        自动签到
        :param header:
        :param person:
        :return:
        '''

        result=person.post('https://www.yiban.cn/ajax/checkin/checkin',headers=header,verify=False).json()
        print(result)
        if result['code'] == 202:
            print("你今天已经签到过了")
        elif result['code'] == 200:
            import re
            print(re.search('\d\d+',result['data']['survey']).group())
            data={
                "optionid[]7777777777777777": re.search('\d\d+',result['data']['survey']).group(),
                "input":""
            }
            print("正在填写问卷调查")
            result=person.post('https://www.yiban.cn/ajax/checkin/answer',data=data,headers=header,verify=False).json()
            print(result)
            if result['code']==200:
                print("签到成功")

    @classmethod
    def give_a_like(cls,header,person,group_id,puid_id):
        '''
        微社区点赞
        :return:
        '''
        data={
            "puid":puid_id,
            "group_id":group_id,
        }
        #获取channel_id
        result=person.post('https://www.yiban.cn/forum/api/getListAjax',headers=header,data=data,verify=False).json()
        print(result)
        channel_id=result['data']['channel_id']
        data={
            "channel_id": channel_id,
            "puid": puid_id,
            "page": 1,
            "size": 10,
            "orderby": "updateTime",
            "Sections_id": -1,
            "need_notice": 0,
            "group_id": group_id,
            "my": 0,
        }
        #获取文章列表
        result=person.post('https://www.yiban.cn/forum/article/listAjax',data=data,headers=header,verify=False).json()
        print(result)
        if result['code']==200:
            print("成功获取最新的文章列表")
            for i in result['data']['list']:
                article_id=i['id']
                channel_id=i['Channel_id']

                data={
                    "article_id": article_id,
                    "channel_id": channel_id,
                    "puid": puid_id,
                }
                result=person.post('https://www.yiban.cn/forum/article/upArticleAjax',data=data,headers=header,verify=False).json()
                print(result)
                if result['code']==200:
                    print('点赞成功',i['author']['name']+"的"+i['title'])
                elif result['code']==201:
                    print('您已经点赞过',i['author']['name']+"的"+i['title'])
                else:
                    print("失败未知原因")

                content=dispath([1,8])

                data={
                "channel_id": channel_id,
                "puid": puid_id,
                "article_id": article_id,
                "content": content,
                "reply_id": 0,
                "syncFeed": 1,
                "isAnonymous": 0,
                }
                result=person.post('https://www.yiban.cn/forum/reply/addAjax',data=data,headers=header,verify=False).json()
                print(result)
                if result['code']==200:
                    print("评论成功：",result['data']['list'][0]['content'])
                else:
                    print("失败未知原因")
    @classmethod
    def auto_vote(cls,header,person,group_id,puid_id):
        '''
        自动投票
        :return:
        '''
        result=person.get('http://www.yiban.cn/newgroup/showMorePub/puid/{}/group_id/{}/type/3/page/1'.format(puid_id,group_id),headers=header,verify=False).text
        uid=re.findall('/user/index/index/user_id/(\d+)"><i',result)[0]
        id=re.findall('/vote/vote/showDetail/vote_id/(\d+)/puid/', result)
        print(uid)
        print(len(id))
        vote_id=[id[i-1] for i in range(1,len(id)+1) if i%2==0]
        print(vote_id)
        for index,i in enumerate(vote_id):
            data = {
                "vote_id": i,
                "uid": uid,
                "puid": puid_id,
                "pagetype": "1",
                "group_id": group_id,
                "actor_id": uid,
                "top_power": "f",
                "edit_power": "t",
                "end_power": "f",
                "del_power": "t",
                "block_power": "f",
                "isSchoolVerify": "1",
                "is_public": "f",
                "is_anonymous": "t",
                "token": "",
                "out_power": "f",
                "isMember": "",
                "url[getVoteDetail]": "vote/vote/getVoteDetail",
                "url[output]": "/vote/Expand/output",
                "url[getCommentDetail]": "vote/vote/getCommentDetail",
                "url[addComment]": "vote/vote/addComment",
                "url[editLove]": "vote/vote/editLove",
                "url[vote]": "vote/vote/act",
                "url[setIsTop]": "vote/Expand/setIsTop",
                "url[setManualEndVote]": "vote/Expand/setManualEndVote",
                "url[delVote]": "vote/Expand/delVote",
                "url[delComment]": "vote/vote/delComment",
                "url[shieldVote]": "vote/Expand/shieldVote",
                "url[getAnonymous]": "vote/Expand/getAnonymous",
                "url[userInfo]": "user/index/index",
                "isLogin": "1",
                "isOrganization": "0",
                "ispublic": "0",
            }
            # print(data)
            result=person.post('https://www.yiban.cn/vote/vote/getVoteDetail',headers=header,data=data,verify=False).json()
            print(result)
            voptions_id=result['data']['option_list'][0]['id']
            # print(voptions_id)

            data={
            "puid": puid_id,
            "group_id": group_id,
            "vote_id":  i,
            "actor_id": uid,
            "voptions_id": voptions_id,
            "minimum": "1",
            "scopeMax": "1",
            }
            # print("最终",data)
            result=person.post('https://www.yiban.cn/vote/vote/act',headers=header,data=data,verify=False).json()
            print(result)

    @classmethod
    def visit_group(cls,header,person,group_id,puid_id):
        '''
        访问群主页
        :return:
        '''
        result=person.post('http://www.yiban.cn/newgroup/indexPub/group_id/{}/puid/{}'.format(group_id,puid_id),headers=header,verify=False)
        print("访问群主页状态码",result)

    @classmethod
    def auto_like_dynamic_state(cls,header,person,group_id,puid_id):
        '''
        动态，自动点赞，评论，同情
        :param header:
        :param person:
        :return:
        '''
        for i in range(1,4):
            if i==1:
                data={
                    "num": 6,
                    "topic_content":"",
                    "scroll": i,
                }
            else:
                data={
                    "lastid": id,
                    "num": 6,
                    "topic_content":"",
                    "scroll": i,
                }
            for i in person.post('https://www.yiban.cn/feed/list', data=data, headers=header,verify=False).json()['data']:
                id = i['_id']
                #点赞
                result=person.post('https://www.yiban.cn/feed/up',headers=header,data={"id":id},verify=False).json()
                print(result)
                #同情
                result1=person.post('https://www.yiban.cn/feed/down',headers=header,data={"id":id},verify=False).json()
                print(result1)
                #评论
                result2=dispath([1,7,8])
                result3=person.post('https://www.yiban.cn/feed/createComment',headers=header,data={"id":id,"content":result2[1]},verify=False)
                print(result3)

    @classmethod
    def like_logs(cls,header,person,group_id,puid_id):
        '''
        点赞，评论，转载博客
        :param header:
        :param person:
        :return:
        '''

        response=person.get('https://www.yiban.cn/newgroup/showMore/puid/{}/group_id/{}/type/3'.format(group_id,puid_id),headers=header).text
        all_uid = [re.search('\d\d\d\d+',i).group() for i in filter(lambda x: not x.startswith('j'), etree.HTML(response).xpath('//ul[@class="user-list member-leader clearfix"]/li//@href'))]
        print(all_uid)
        for index,i in enumerate(all_uid):
            result1=person.get('https://www.yiban.cn/blog/blog/getBlogList?page=1&size=10&uid={}'.format(i),headers=header).json()
            for j in result1['data']['list']:
                blogid=j['id']
                Mount_id=j['Mount_id']
                oid=j['User_id']
                result2=person.get('https://www.yiban.cn/blog/blog/addlike?uid={}&blogid={}'.format(i,blogid),headers=header).json()
                print(result2)
                if result2['code'] == 200:
                    print("点赞成功")
                elif result2['code'] == "202" and result2['message'] == "已点赞":
                    print("已经点赞")
                else:
                    print("失败未知原因")

                result=dispath([1,8])
                data={
                    "blogid": blogid,
                    "oid": oid,
                    "mid": Mount_id,
                    "reply_user_id": 0,
                    "reply_comment_id": 0,
                    "content": result[1],
                }
                result3=person.post('https://www.yiban.cn/blog/blog/addcomment',headers=header,data=data).json()
                print(result3)
                if result3['code'] == 200:
                    print("评论成功")
                else:
                    print("失败未知原因")
                result4=person.get('https://www.yiban.cn/blog/blog/copyblog?blogid={}&suid={}&range=1'.format(i,oid)).json()
                if result4['code'] == 200:
                    print("转载成功")
                else:
                    print("失败未知原因")


if __name__ == '__main__':
    pass




