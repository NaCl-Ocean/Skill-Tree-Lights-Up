import json
import os
import datetime
import hashlib

while True:
    user_name = input("enter user name:")
    json_file_path = os.path.join(os.path.dirname(__file__),user_name+'.json')
    f = open(json_file_path,'rb')
    user_info = json.load(f)
    f.close()

    user_passwd  = None
    try_time = 0
    expire_date = datetime.datetime.strptime(user_info['expire_date'],"%Y-%m-%d")

    if expire_date < datetime.datetime.now():
        print('Account expired')
        continue
    while try_time <=4:
        try_time += 1
        if try_time == 4:
            user_info['status'] = 1
            with open(json_file_path,'w') as f:
                json.dump(user_info,f)
            break
        if user_passwd != user_info['password']:
            user_passwd = input("enter your password:")
            m = hashlib.md5()
            m.update(user_passwd.encode('utf-8'))
            user_passwd = str(m.hexdigest())
        if user_passwd == user_info['password']:
            print('login successfully!')
            break

