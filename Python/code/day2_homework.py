import pickle
#-*-encoding:utf-8


def judge_str_is_float(str):
    strs = str.split('.')
    if len(strs)>1:
        if strs[0].isdigit() and strs[1].isdigit():
            return True
        else:
            return False
    else:
        return False


def get_stockdata_from_stockname(str,data):
    for name in data['名称']:
        if name.count(str)>0:
            index = data['名称'].index(name)
    output = '代码：{}，名称：{}，最新价：{}，涨跌幅(%)：{}，涨跌额：{}，成交量（手）：{}，成交额：{}，振幅(%)：{}，最高:{}，最低:{}，今开:{}，昨收:{}，量比:{}，换手率(%):{}，市盈率:{}，市净率:{}'.format(
              int(data['代码'][index]),data['名称'][index],data['最新价'][index],data['涨跌幅'][index],data['涨跌额'][index],data['成交量(手)'][index],data['成交额'][index],data['振幅'][index],
                data['最高'][index],data['最低'][index],data['今开'][index],data['昨收'][index],data['量比'][index],data['换手率'][index],data['市盈率'][index],data['市净率'][index]
    )
    print(output)

def get_stockdata_from_condition(str,data):
    if str.count('>'):
        tag, condition = str.split('>')
        for i in range(len(data[tag])):
            element = data[tag][i]
            if element>float(condition):
                get_stockdata_from_stockname(data['名称'][i],data)
    else:
        tag, condition = str.split('<')
        for i in range(len(data[tag])):
            element = data[tag][i]
            if element<float(condition):
                get_stockdata_from_stockname(data['名称'][i],data)

if __name__ == "__main__":

    # 格式化存储数据
    f = open('stock_data.txt','r',encoding='utf-8')
    lines = f.readlines()
    head = lines[0]
    head.strip()
    head = head.split()
    data = {}
    for i in range(len(head)):
        data[head[i]] = []

    for i in range(1,len(lines)):
        stock = lines[i].strip().split()
        breakpoint = 1
        for j in range(len(head)):
            if stock[j].endswith('%'):
                data[head[j]].append(float(stock[j].strip('%')))
            elif stock[j].isdigit():
                data[head[j]].append(float(stock[j]))
            elif judge_str_is_float(stock[j]):
                data[head[j]].append(float(stock[j]))
            else:
                data[head[j]].append(stock[j])


    while(1):
        input_str = input('enter the search info:')
        if input_str.count('<') or input_str.count('>'):
            get_stockdata_from_condition(input_str,data)
        else:
            get_stockdata_from_stockname(input_str,data)