"""
# -*- coding: utf-8 -*-
# @Time    : 2023/4/5 下午3:10
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : Translate.py
"""
import requests
import uuid
import hashlib
import pyperclip
import json
import time
if __name__=="__main__":
    i=1
    src="en"
    tar="zh"
    appid="xxxxxxx" # replace your appid
    passwd="xxxxxx" # replace your passwd
    salt=uuid.uuid1().__str__()
    previous_clip_data=" "
    print("FastTranslator init...")
    while True:
        data=pyperclip.paste()
        if data!=previous_clip_data:
            previous_clip_data=data
            sign=hashlib.md5((appid+data+salt+passwd).encode()).hexdigest()
            url="https://fanyi-api.baidu.com/api/trans/vip/translate?"+"q="+data+"&from="+src+"&to="+tar+"&appid="+appid+"&salt="+salt+"&sign="+sign
            response=requests.get(url)
            json_string=response.text
            json_data=json.loads(json_string)
            if('error_code' in json_data.keys()):
                print(str(i)+": error_code:",json_data["error_code"],"error_msg: ",json_data["error_msg"])
                i=i+1
            else:
                print(str(i)+": "+json_data['trans_result'][0]["dst"]+"\n")
                i=i+1

        time.sleep(0.2)
