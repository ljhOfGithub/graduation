from selenium import webdriver
import time
import requests
from ast import literal_eval
import csv
import xlrd
import yaml
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
def test():
    with open('ntx1.csv','r') as f:
        print(len(f.readlines()))
    with open('ntx2.csv','r') as f:
        print(len(f.readlines()))
    with open('ntx3.csv','r') as f:
        print(len(f.readlines()))
    with open('ntx4.csv','r') as f:
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

    # test()

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
    try:
        print("itxs3")
        getItxs3()
    except Exception:
        print("itxs3")
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