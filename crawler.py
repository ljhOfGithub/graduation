from selenium import webdriver
import time
import requests
from ast import literal_eval
import csv
import xlrd
import yaml
import pandas
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

apikey = "ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
# apikey = "P3FE926UGARGQF8HKPM4XWJ38CJAGX5WHZ"

def deduplicate():
    with open('bitpoint.txt','r') as f:
        list1 = literal_eval(f.read())
        list1 = [addr.lower() for addr in list1]
    with open('cryptopia.txt','r') as f:
        list2 = literal_eval(f.read())
        list2 = [addr.lower() for addr in list2]
    with open('etherdelta.txt','r') as f:
        list3 = literal_eval(f.read())
        list3 = [addr.lower() for addr in list3]
    with open('LendfMe.txt','r') as f:
        list4 = literal_eval(f.read())
        list4 = [addr.lower() for addr in list4]
    with open('phishaddr.txt','r') as f:
        list5 = literal_eval(f.read())
        list5 = [addr.lower() for addr in list5]
    with open('upbit.txt','r') as f:
        list6 = literal_eval(f.read())
        list6 = [addr.lower() for addr in list6]
    with open('scam.txt','r') as f:
        list7 = literal_eval(f.read())
        list7 = [addr.lower() for addr in list7]
    with open('db.txt','r') as f:
        list8 = literal_eval(f.read())
        list8 = [addr.lower() for addr in list8]
    print(type(list1))
    alladdr = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8))
    print(len(alladdr))
    with open('addr.txt','w',encoding='utf-8') as f:
        print(alladdr,file=f)

def readxlsx():
    workbook = xlrd.open_workbook('scam.xlsx')
    worksheet = workbook.sheet_by_index(0)
    objlist = worksheet.col_values(2)[1:]
    addrlist = []
    for obj in objlist:
            if len(obj) > 42:
                splitlist = obj.split(",")
                for addr in splitlist:
                    if addr.startswith('0x'):
                        addrlist.append(addr)
    with open('scam.txt','w',encoding='utf-8') as f:
        print(addrlist,file=f)

def writedb():
    with open('urls.yaml','r',encoding='utf-8') as f:
        with open('dblist.txt','w',encoding='utf-8')as f2:
            with open('temp.txt','w',encoding='utf-8') as f3:
                temp = yaml.load(f.read(),Loader=yaml.FullLoader)
                print(temp,file=f2)
                for item in temp:
                    f3.write(str(item) + '\n')
    with open('dblist.txt','r',encoding='utf-8') as f:
        itemlist = literal_eval(f.read())
        print(type(itemlist))
def readdb():
    with open('dblist.txt','r',encoding='utf-8') as f:
        itemlist = literal_eval(f.read())
        addrlist = []
        for item in itemlist:
            if 'addresses' in item.keys() and 'ETH' in item['addresses']:
                    addrs = item['addresses']['ETH']
                    for addr in addrs:
                        if len(addr) == 42:
                            addrlist.append(addr)
    addrlist = [addr.lower() for addr in addrlist]
    addrlist = list(set(addrlist))
    print(len(addrlist))
    with open('db.txt','w',encoding='utf-8') as f:
        print(addrlist,file=f)

def getNtxs1():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:1500]
    session = requests.Session()
    with open('ntx1.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 0
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],result['blockHash'],
                                        result['transactionIndex'],result['from'],result['to'],result['value'],result['gas'],result['gasPrice'],
                                        result['isError'],result['txreceipt_status'],result['input'],result['contractAddress'],result['cumulativeGasUsed'],
                                        result['gasUsed'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getNtxs2():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[1500:3000]
    session = requests.Session()
    with open('ntx2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 1500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],result['blockHash'],
                                        result['transactionIndex'],result['from'],result['to'],result['value'],result['gas'],result['gasPrice'],
                                        result['isError'],result['txreceipt_status'],result['input'],result['contractAddress'],result['cumulativeGasUsed'],
                                        result['gasUsed'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getNtxs3():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[3000:4500]
    session = requests.Session()
    with open('ntx3.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 3000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],result['blockHash'],
                                        result['transactionIndex'],result['from'],result['to'],result['value'],result['gas'],result['gasPrice'],
                                        result['isError'],result['txreceipt_status'],result['input'],result['contractAddress'],result['cumulativeGasUsed'],
                                        result['gasUsed'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)

def getNtxs4():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4500:]
    session = requests.Session()
    with open('ntx4.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 4500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],result['blockHash'],
                                        result['transactionIndex'],result['from'],result['to'],result['value'],result['gas'],result['gasPrice'],
                                        result['isError'],result['txreceipt_status'],result['input'],result['contractAddress'],result['cumulativeGasUsed'],
                                        result['gasUsed'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)

def getItxs1():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:1500]
    session = requests.Session()
    with open('itx1.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 0
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['from'],
                                         result['to'],result['value'],result['contractAddress'],result['input'],result['type'],
                                         result['gas'],result['gasUsed'],result['traceId'],result['isError'],result['errCode']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getItxs2():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[1500:3000]
    session = requests.Session()
    with open('itx2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 1500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['from'],
                                         result['to'],result['value'],result['contractAddress'],result['input'],result['type'],
                                         result['gas'],result['gasUsed'],result['traceId'],result['isError'],result['errCode']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getItxs3():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[3000:4500]
    session = requests.Session()
    with open('itx3.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 3000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['from'],
                                         result['to'],result['value'],result['contractAddress'],result['input'],result['type'],
                                         result['gas'],result['gasUsed'],result['traceId'],result['isError'],result['errCode']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)

def getItxs4():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4500:]
    session = requests.Session()
    with open('itx4.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 4500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['from'],
                                         result['to'],result['value'],result['contractAddress'],result['input'],result['type'],
                                         result['gas'],result['gasUsed'],result['traceId'],result['isError'],result['errCode']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)

def getEtxs1():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:1500]
    session = requests.Session()
    with open('etx1.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 0
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + addr + "&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],
                                         result['blockHash'],result['from'],result['contractAddress'],result['to'],result['value'],
                                         result['tokenName'],result['tokenSymbol'],result['tokenDecimal'],result['transactionIndex'],result['gas'],
                                         result['gasPrice'],result['gasUsed'],result['cumulativeGasUsed'],result['input'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getEtxs2():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[1500:3000]
    session = requests.Session()
    with open('etx2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 1500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + addr + "&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],
                                         result['blockHash'],result['from'],result['contractAddress'],result['to'],result['value'],
                                         result['tokenName'],result['tokenSymbol'],result['tokenDecimal'],result['transactionIndex'],result['gas'],
                                         result['gasPrice'],result['gasUsed'],result['cumulativeGasUsed'],result['input'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def getEtxs3():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[3000:4500]
    session = requests.Session()
    with open('etx3.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 3000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + addr + "&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],
                                         result['blockHash'],result['from'],result['contractAddress'],result['to'],result['value'],
                                         result['tokenName'],result['tokenSymbol'],result['tokenDecimal'],result['transactionIndex'],result['gas'],
                                         result['gasPrice'],result['gasUsed'],result['cumulativeGasUsed'],result['input'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)

def getEtxs4():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4500:]
    session = requests.Session()
    with open('etx4.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 4500
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + addr + "&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'],result['timeStamp'],result['hash'],result['nonce'],
                                         result['blockHash'],result['from'],result['contractAddress'],result['to'],result['value'],
                                         result['tokenName'],result['tokenSymbol'],result['tokenDecimal'],result['transactionIndex'],result['gas'],
                                         result['gasPrice'],result['gasUsed'],result['cumulativeGasUsed'],result['input'],result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
#https://api.etherscan.io/api?module=account&action=tokentx&address=0x0f3257e9513f4812bf015efc5022f16bfef0cfa8&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=YourApiKeyToken
#https://api.etherscan.io/api?module=account&action=txlist&address=0xd0b0d5a8c0b40b7272115a23a2d5e36ad190f13c&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=YourApiKeyToken
#fig2:每个地址首次欺诈交易的时间
#fig3：每个月不同种交易的欺诈交易的数量
#fig4：所有地址每个月欺诈交易的数量
#fig5：2019年最多欺诈交易的地址，取出来分析交易数量
#fig6：不同种交易地址的存活时间
#fig7：欺诈地址的一般交易和内部交易的数量分布

def fig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    frames = [df1,df2,df3,df4]
    df = pandas.concat(frames)
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    dfsort = df.sort_values('timeStamp')
    month2count = {}
    for index,row in dfsort.iterrows():#桶计数，如果当前月份还没有对应的字典则初始化为0，如果已经有对应的字典则取出对应的数量然后在此基础上加1
        month2count[row['timeStamp']] = month2count.get(row['timeStamp'],0) + 1
    print(month2count)
    x = month2count.keys()
    y = month2count.values()
    plt.plot(x,y)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()
    # print(df2)

def test():
    # with open('ntx1.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx2.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx3.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx4.csv','r') as f:
    #     print(len(f.readlines()))
    with open('itx1.csv','r') as f:
        print(len(f.readlines()))
    with open('itx2.csv','r') as f:
        print(len(f.readlines()))
    with open('itx3.csv','r') as f:
        print(len(f.readlines()))
    with open('itx4.csv','r') as f:
        print(len(f.readlines()))
    with open('etx1.csv','r',encoding='utf-8') as f:
        print(len(f.readlines()))
    with open('etx2.csv', 'r', encoding='utf-8') as f:
        print(len(f.readlines()))
    with open('etx3.csv','r',encoding='utf-8') as f:
        print(len(f.readlines()))
    with open('etx4.csv','r',encoding='utf-8') as f:
        print(len(f.readlines()))
    # with open('addr.txt','r') as f:
    #     list = literal_eval(f.read())
    #     print(len(list))

    # url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
    # session = requests.Session()
    # results = literal_eval(session.get(url).text)['result']
    # print(len(results))


if __name__ == '__main__':
    # try:
    #     print("ntxs1")
    #     getNtxs1()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs2")
    #     getNtxs2()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs3")
    #     getNtxs3()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs4")
    #     getNtxs4()
    # except Exception:
    #     pass

    fig3()
    # try:
    #     print("itxs1")
    #     getItxs1()
    # except Exception:
    #     print("itxs1")
    # getItxs2()
    # try:
    #     print("itxs2")
    #     getItxs2()
    # except Exception:
    #     print("itxs2")
    # try:
    #     print("itxs3")
    #     getItxs3()
    # except Exception:
    #     print("itxs3")
    # try:
    #     print("itxs4")
    #     getItxs4()
    # except Exception:
    #     print("itxs4")
    # try:
    #     getEtxs1()
    # except Exception:
    #     pass
    # try:
    #     print("etxs2")
    #     getEtxs2()
    # except Exception:
    #     pass
    # try:
    #     print("etxs3")
    #     getEtxs3()
    # except Exception:
    #     pass
    # try:
    #     print("etxs4")
    #     getEtxs4()
    # except Exception:
    #     pass