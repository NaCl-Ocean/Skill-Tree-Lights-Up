
import json
import sys
import os
import datetime
import hashlib
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from  core  import withdrawl

def new_main(func):
    def inner(*args,**kwargs):
        user_name = input("enter user name:")
        json_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'account',user_name + '.json')
        f = open(json_file_path, 'rb')
        user_info = json.load(f)
        f.close()

        user_passwd = None
        try_time = 0
        login = False
        expire_date = datetime.datetime.strptime(user_info['expire_date'], "%Y-%m-%d")

        if expire_date < datetime.datetime.now():
            print('Account expired')
            login = False
        while try_time <= 4:
            try_time += 1
            if try_time == 4:
                user_info['status'] = 1
                with open(json_file_path, 'w') as f:
                    json.dump(user_info, f)
                login = False
            if user_passwd != user_info['password']:
                user_passwd = input("enter your password:")
                m = hashlib.md5()
                m.update(user_passwd.encode('utf-8'))
                user_passwd = str(m.hexdigest())
            if user_passwd == user_info['password']:
                print('login successfully!')
                login = True
                break
        if login == True:
            func()

    return inner




@new_main
def main_tixian():
    info = "  ———- ICBC Bank ———— \n " \
           "1.  账户信息 \n " \
           "2.  转账 \n" \
           "3.  提现"
    print(info)

    with open('../account/alex.json', 'r') as f:
        alex_account_info = json.load(f)
        f.close()
    try :
        choice = int(input('enter your choice:'))
    except ValueError as e:
        print('please enter the choce number')

    if choice == 1:
        print(alex_account_info)
    elif choice == 2:
        fee = 950000*1.05
        with open('../account/tesla_company.json','r') as f:
            tesla_account_info = json.load(f)
            f.close()
        with open('../account/tesla_company.json', 'w') as f:
            tesla_account_info['balance'] += fee
            json.dump(tesla_account_info,f)
        with open('../account/alex.json','w') as f:
            alex_account_info['balance'] -= fee
            json.dump(alex_account_info,f)
    elif choice == 3:
        withdraw_account = int(input('enter withdrawal amount:'))
        withdrawl.withdraw(withdraw_account)


main_tixian()











