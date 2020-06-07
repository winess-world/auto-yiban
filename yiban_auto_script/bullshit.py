#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from 1.package_all import *
import json
import random
import requests

data = json.load(open("data.json", encoding="utf-8"))
data2 = json.load(open("title.json", encoding="utf-8"))

global sooner_later
sooner_later = []


def dispath(sign):

    while True:
        num = random.randint(1, 8)
        if num in sign:
            print("正在重新随机")
            continue
        else:
            break

    # num=7
    print(num)
    if num == 1:
        title = random.choice(data2['title'])
        # return 1," "*5+title+"\n"+generator(title)
        return title,generator(title,length=random.randint(300, 800))
    elif num == 2:
        # return 2,aphorism()
        return random.choice(["格言","格言警句","名人名言","箴言","经典语录","人生格言"]),aphorism()
    elif num == 3:
        return random.choice(["经典一句","上古佳句","绝句","美句","佳句","佳句摘录","美句摘录","句子迷"]),one_sentence()
    elif num == 4:
        return random.choice(["网易云热评","自古评论出人才","热评","经典评论"]),wangyiyun()
        # return 4,wangyiyun()
    elif num == 5:
        if sooner_later.__len__() != 0:
            result = random.choice(sooner_later)
            sooner_later.remove(result)
            # return 5,result
            return "",result
        else:
            good_single()
            print(sooner_later)
            result = random.choice(sooner_later)
            sooner_later.remove(result)
            return "",result

    elif num == 6:
        return random.choice(["英语句子",'English article','Good English article','article','well-turned phrase']),power_word()
    elif num == 7:
        return random.choice(["古诗宋词","古诗词","古代文化",'诗词鉴赏','名言古句']),sky_data()
    elif num == 8:
        return random.choice(["好文欣赏",'欣赏好文','美文','佳文','文章','好文章','好文']),random_article()
    elif num == 9:
        return 9,photo()


# TODO:狗屁不通文字生成器

def generator(title, length=800):
    """
    :param title: title.json
    :param length: 生成正文的长度
    :return: 返回正文内容
    """
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            body += "\r\n"
        elif num < 20:
            body += random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            body += random.choice(data["bosh"])
        body = body.replace("x", title)
    return body


def aphorism():
    '''
    格言生成器
    :return:
    '''
    res = requests.get('https://v1.hitokoto.cn/').json()
    return res['hitokoto'] + " " * 5 + "--《{}》".format(res['from']) + "\n" + " " * (len(res['hitokoto'])*2 + 5) + "--" + \
           res["creator"]


def one_sentence():
    '''
    一句
    :return:
    '''
    result = requests.get('http://yijuzhan.com/api/word.php?m=json').json()
    print("一句",result)
    return result['content'] + "\n" + "" * (len(result['content']) + 10) + "--" + result['source']


def wangyiyun():
    '''
    网易云热评
    :return:
    '''
    result = requests.get('https://api.nextrt.com/V1/Netease/Random/1').json()
    return result['data'][0]['content'] + "\n" + " " * (len(result['data'][0]['content'])*2 + 5) + "--" + \
           result['data'][0]['songName']


def good_single():
    '''
    好单库，早晚安问候语
    :return:
    '''
    result = requests.get('http://v2.api.haodanku.com/get_salutation_data/apikey/{}/min_id/1'.format("keysor")).json()
    for i in result['data']:
        sooner_later.append(i['content'])
    return result


def power_word():
    '''
    词霸每日一句
    :return:
    '''
    result = requests.get('http://open.iciba.com/dsapi/').json()
    return result['content'] + "\n" + result['note']


def sky_data():
    '''
    天一,古诗宋词
    :return:
    '''
    result = requests.get(
        'http://api.tianapi.com/txapi/poetry/index?key={}'.format('9b4a25946a9be23ad9f364b3c8273795')).json()
    print(result)
    return '<p style="text-align: center;"><strong style="text-align: center; white-space: normal;">{}</strong></p>'.format(result['newslist'][0]['title'])+"&nbsp;"*23 + " " * 5 + result['newslist'][0]['kind'] + " " * 2 + \
           result['newslist'][0]['author'] +"<p>"+result['newslist'][0]['content'].replace('。', '。</p><p>') +"</p>"+ "<p>"+result['newslist'][0]['intro']+"</p>"


def random_article():
    '''
    随即一文
    :return:
    '''
    result = json.loads(
        requests.get('https://interface.meiriyiwen.com/article/random?dev=1').text.encode('ascii').decode(
            'unicode_escape'))
    print(result)
    return " " * 5 + result['data']['title'] + "\n" + " " * 7 + result['data']['author'] + "\n" + result['data'][
        'content']


def photo():
    '''
    一周七图
    :return:
    '''
    result = requests.get('https://api.xygeng.cn/Bing/week/').json()
    return result['data']

if __name__ == '__main__':
    # print(one_sentence())
    # print(dispath())
    # print(sky_data())
    # print(random_article())
    pass