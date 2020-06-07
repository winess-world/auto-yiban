# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/25 10:02'
from yiban_auto_script.package_all import *

template = __import__('yiban_auto_script.template', fromlist=('template'))


# TODO:orc调度与识别模块

class ORC(object, metaclass=getattr(template, "MyMetaClass")):
    '''
    orc调度识别
    '''

    @classmethod
    def dispatch_orc(cls, img_path):
        '''
        按照1,4,4
        :return:
        '''

        num = random.randint(1, 10)

        return cls.TencentOcr_three_limit(img_path) if num == 1 else cls.baidu_orc_one_limit(img_path) if num > 1 and num < 8 else cls.UtOcrB(img_path)


    @classmethod
    # 每日五万次的调用识别接口
    def baidu_orc_one_limit(cls, img_path: str):

        '''
        百度每日5w识别次数接口
        :param img_path:
        :param client_id:
        :param client_secreat:
        :return:
        '''
        list_new=[["tczajwKLufsP4W701G6i34BN", "qqj7VBEsWddauGjYyGf3IEYDBjq36O1L"],
                               ["6lfZ2yqOApWqH2cD8esRLfgX", "PPTGVRhLGRXHOv6bqL1MLrIOXXCtrpO0"],
                               ["28pvdycYgOUaSgeDtf6ZSw51", "dwRd0Y0D7ciGXGO3V94TZw9DCLtDAu8B"]]
        result = random.randint(0,len(list_new)-1)
        result=list_new[result]
        client_id = result[0]
        client_secreat = result[1]
        print("正在调用百度识别接口")
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            client_id, client_secreat)
        response = requests.get(host, verify=False)
        if response:
            request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
            # 二进制方式打开图片文件
            f = open(img_path, 'rb')
            img = base64.b64encode(f.read())

            params = {
                "image": img,
                "detect_direction": "true"
            }
            access_token = response.json()['access_token']
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers, verify=False)
            if response:
                print(img_path, response.json())
            try:
                if len(response.json()['words_result']) == 0:
                    print("orc完全识别不到")
                    return []
            except KeyError:
                # api识别被限制
                print(response.json()['error_msg'])
            if re.search("[\u4e00-\u9fa5]", response.json()['words_result'][0]['words']) == None:
                print("orc没有识别出汉字")
                return []
            result=re.search("[\u4e00-\u9fa5+]", response.json()['words_result'][0]['words']).group()
            str1 = ""
            for j in result:
                str1 += j
            result=[i for i in str1]
            print("打印",result)
            return result
        else:
            print("请检查网络连接")

    # 调用百度免费接口
    @classmethod
    def baidu_orc_two_free(cls, img_path: str):
        '''
        百度免费识别接口
        :param img_path:
        :return:
        '''
        with open(file=img_path, mode='rb') as file:
            base64_data = base64.b64encode(file.read())
            base64_data_ex = str(base64_data).split('\'', -1)
            sss = "data:image/jpeg;base64," + base64_data_ex[1]

        form_date = {
            "image": sss,
            "image_url": "",
            "type": "commontext",
            "detect_direction": "false"
        }

        r = requests.post('https://ai.baidu.com/aidemo', verify=False, data=form_date)
        rs = json.loads(r.text)
        return rs

    @classmethod
    def TencentOcr_three_limit(self, img_path, SECRET_ID="AKIDxxhAML9PVLtAAxtmpfDTu4xYruhDtxw1",
                               SECRET_KEY="ykX3JHzPZWCfrBtaIj9IAm6ByUjKgmzv"):
        '''
        Tenxun 1k/month
        :param img_path:
        :param SECRET_ID:
        :param SECRET_KEY:
        :return:
        '''
        try:
            print("正在调用腾讯识别接口")
            cred = credential.Credential(SECRET_ID, SECRET_KEY)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "ocr.tencentcloudapi.com"
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
            req = models.GeneralBasicOCRRequest()
            with open('{}'.format(img_path), 'rb') as f:
                # 使用base64进行加密
                base64_data = base64.b64encode(f.read())
            params = '{"ImageBase64":"%s"}' % (str(base64_data)[2:-1])
            req.from_json_string(params)
            # 调用通用识别文字接口
            resp = client.GeneralBasicOCR(req)
            result = json.loads(resp.to_json_string())
            print("打印",result)
            return [i for i in result["TextDetections"][0]["DetectedText"]]
        except Exception as e:
            print("未检测到文本或者数量不足",e)
            return []

    @classmethod
    def UtOcrB(cls, imgpath:str):
        '''
        调用优图免费接口
        :param imgpath:
        :return:
        '''
        print("正在调用优图免费接口")
        files = {
            'image_file': ('file', open(imgpath, 'rb'), 'image/jpeg')
        }
        r = requests.post('https://ai.qq.com/cgi-bin/appdemo_generalocr?g_tk=5381', verify=False, files=files)
        rs = json.loads(r.text)
        print(rs)
        if rs['ret'] == 0:
            if rs['data']['item_list'] == []:
                print("OCR未识别到值")
                return []
            else:
                code_0 = rs['data']['item_list']
                code_1=""
                for i in code_0:
                    code_0=i['itemstring']
                    code_1+=code_0

                code_2 = re.findall(r'[\u4e00-\u9fa5]+',code_1)
                str1=""
                for i in code_2:
                    str1+=i
                code_2=[i for i in str1]

                if len(code_2)!=0:
                    print("打印",code_2)
                    return code_2
                else:
                    print("OCR未识别到值")
                    return []
        else:
            print("OCR未识别到值")
            return []
