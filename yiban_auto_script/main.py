# _*_ coding:utf-8 -*-
__author__ = '鲁江洋'
__time__ = '2020/5/25 11:05'

from yiban_auto_script.login_yiban import *
from yiban_auto_script.package_all import *
import pandas as pd
import threading
from yiban_auto_script.ascension_yiban_egpa import *
from yiban_auto_script.setting import *

if __name__ == '__main__':
    data = pd.read_excel("user.xlsx")
    name = data.get("name")
    password = data.get("password")
    username = data.get("username")

    if not detection:
        if pattern=="1":
            print("正在采取就近模式")
        elif pattern=="2":
            print("正在采取指定id模式")
            group_id=data.get('group_id')
            puid_id=data.get('puid_id')
            if group_id.isnull().sum()+puid_id.isnull().sum()>0:
                raise Exception("You select 2 but your Group_id or puid_id information not complete")
        elif pattern=="3":
            print("正在采取特殊标识模式")
        else:
            print("正在采取全覆盖模式")

        for j in range(a_roup_of_num):
            for i in range(data.__len__()):
                try:
                    print("gogogo {},user:{}:".format(i + 1,name[i]), username[i])
                    if pattern=="2":
                        t = threading.Thread(target=agency, args=(str(int(name[i])), str(password[i]),str(puid_id[i]),str(group_id[i])))
                    else:
                        t = threading.Thread(target=agency, args=(str(int(name[i])), str(password[i])))
                    t.start()
                    t.join()

                    # Login(str(name[i]), str(password[i])).login()
                except Exception as e:
                    print("出错了：", username[i], e)
    else:
        print("测试账号密码模式")
        for j in range(1):
            for i in range(data.__len__()):
                try:
                    print("go {}:".format(i + 1), username[i])
                    print(int(name[i]), str(password[i]))
                    t = threading.Thread(target=agency, args=(str(int(name[i])), str(password[i])))
                    t.start()
                    t.join()

                    # Login(str(name[i]), str(password[i])).login()
                except Exception as e:
                    print("出错了：", username[i], e)
        data1 = pd.DataFrame(data)
        print(data1)
        print(len(error_user))
        print(error_user)
        data1['备注']=error_user
        import pandas as pd
        data1.to_excel('user.xlsx',index=False)
