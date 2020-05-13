import json

def withdraw(withdraw_account):
    with open('../account/alex.json','r') as f:
        account_info = json.load(f)
        f.close()
    withdraw_account *= 1.05
    if withdraw_account > account_info['credit']:
        print('Withdrawal amount exceeds the credit limit')
    else:
        account_info['credit'] -= withdraw_account

    with open('../account/alex.json','w') as f:
        json.dump(account_info,f)