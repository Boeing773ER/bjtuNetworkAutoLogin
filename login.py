import requests
import os
import json


def read_config(config_path):
    with open(config_path) as config:
        cfg = json.load(config)
        usr_name = cfg["user_name"]
        password = cfg["password"]
        if usr_name == "" or password == "":
            print("Complete config.json first")
            os.system('pause')
            os._exit(0)
        return usr_name, password


login_IP = "10.10.42.3"
login_URL = "http://"+login_IP+"/"
config_path = "./config.json"
usr_name, password = read_config(config_path)

not_sign_in_title = "上网登录页"
signed_in_title = '注销页'
result_return = '"result":1'

sign_parameter = ""
sign_parameter += login_URL
sign_parameter += "drcom/login?callback=dr1003&DDDDD="
sign_parameter += usr_name
sign_parameter += "&upass="
sign_parameter += password
sign_parameter += "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.2.1&v=2935" \
                  "&lang=zh "


if __name__ == '__main__':
    try:
        r = requests.get(login_URL, timeout=1)
        req = r.text
    except Exception as ex:
        req = 'False'
        print(ex)

    if signed_in_title in req:
        print("Logged in already")
    elif not_sign_in_title in req:
        r = requests.get(sign_parameter, timeout=1)
        req = r.text
        if result_return in req:
            print("Login Success")
        else:
            print("Login Fail")
    else:
        print("Not campus network")
    os.system('pause')
    os._exit(0)
