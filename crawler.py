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
import numpy
import math
from matplotlib.pyplot import MultipleLocator
from bs4 import BeautifulSoup
apikey = "ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
apikey = "P3FE926UGARGQF8HKPM4XWJ38CJAGX5WHZ"
import json
def bloxyhack():
    pagenum = 177
    url2type = {}  # 将所有的链接和种类注解存入字典中再进行筛选
    for i in range(1,pagenum+1):
        print(i)
        url = "https://bloxy.info/tokens?annotation_page=" + str(i) + "&blockchain_id=1&q=hack"
        session = requests.session()
        resp = session.get(url)
        html = resp.text
        bs = BeautifulSoup(html,features="lxml")
        tbody = bs.select('body > div.wrapper > div:nth-child(5) > div:nth-child(8) > div > div > div.panel-body > div.table-responsive > table > tbody')[0]
        for tr in tbody:
            for tag in tr:
                if not isinstance(tag, str):#排除空行换行符等特殊的tag
                    if tag.select("a"):
                        atag = tag.select("a")[0]
                        url = atag.get('href')
                        mytype = atag.string
                        url2type[url] = mytype
        # print(url2type)
    with open('bloxy.txt','w',encoding='utf-8') as f:
        print(url2type,file=f)
    json_str = json.dumps(url2type)
    with open('bloxy.json', 'w') as json_file:
        json_file.write(json_str)
def bloxyscam():
    pagenum = 56
    url2type = {}  # 将所有的链接和种类注解存入字典中再进行筛选
    for i in range(1,pagenum+1):
        print(i)
        url = "https://bloxy.info/tokens?annotation_page=" + str(i) + "&blockchain_id=1&q=hack"
        session = requests.session()
        resp = session.get(url)
        html = resp.text
        bs = BeautifulSoup(html,features="lxml")
        tbody = bs.select('body > div.wrapper > div:nth-child(5) > div:nth-child(8) > div > div > div.panel-body > div.table-responsive > table > tbody')[0]
        for tr in tbody:
            for tag in tr:
                if not isinstance(tag, str):#排除空行换行符等特殊的tag
                    if tag.select("a"):
                        atag = tag.select("a")[0]
                        url = atag.get('href')
                        mytype = atag.string
                        url2type[url] = mytype
    with open('bloxyscam.txt','w',encoding='utf-8') as f:
        print(url2type,file=f)
    json_str = json.dumps(url2type)
    with open('bloxyscam.json', 'w') as json_file:
        json_file.write(json_str)
def bloxymalware():
    pagenum = 1
    url2type = {}  # 将所有的链接和种类注解存入字典中再进行筛选
    for i in range(1,pagenum+1):
        print(i)
        url = "https://bloxy.info/tokens?annotation_page=" + str(i) + "&blockchain_id=1&q=hack"
        session = requests.session()
        resp = session.get(url)
        html = resp.text
        bs = BeautifulSoup(html,features="lxml")
        tbody = bs.select('body > div.wrapper > div:nth-child(5) > div:nth-child(8) > div > div > div.panel-body > div.table-responsive > table > tbody')[0]
        for tr in tbody:
            for tag in tr:
                if not isinstance(tag, str):#排除空行换行符等特殊的tag
                    if tag.select("a"):
                        atag = tag.select("a")[0]
                        url = atag.get('href')
                        mytype = atag.string
                        url2type[url] = mytype
    with open('bloxymalware.txt','w',encoding='utf-8') as f:
        print(url2type,file=f)
    json_str = json.dumps(url2type)
    with open('bloxymalware.json', 'w') as json_file:
        json_file.write(json_str)

def bloxy2():
    with open('bloxy.txt','r',encoding='utf-8') as f:
        dict1 = literal_eval(f.read())
    with open('bloxyscam.txt','r',encoding='utf-8') as f:
        dict2 = literal_eval(f.read())
    with open('bloxymalware.txt','r',encoding='utf-8') as f:
        dict3 = literal_eval(f.read())
    mydict = {}
    mydict.update(dict1)
    mydict.update(dict2)
    mydict.update(dict3)
    hacktype = ['Phish', 'Coinrail', 'Cryptopia', 'EtherDelta', 'Browser', 'SpankChain', 'Upbit', 'Scam']
    notType = ['Hacking', 'HackToken', 'HackDao', 'HackerGold', 'Hacken', 'HackerSpaceBarneysToken']
    addrlist = []
    for url,type in mydict.items():
        for key in hacktype:
            for key2 in notType:
                if key.lower() in type.lower() and key.lower() not in key2:
                    if url.startswith('/address'):
                        addr = url[9:]
                    elif url.startswith('/tx'):
                        addr = url[4:]
                    if len(addr) == 42:
                        addrlist.append(addr)
    addrlist = list(set(addrlist))
    # print(addrlist)
    print(len(addrlist))
    list1 = list(set(dict1.values()))
    with open('bloxyAddr.txt','w',encoding='utf-8') as f:
        print(addrlist,file=f)
    # print(list1)
    # print(len(dict1))
def differSetNtx():
    addrlist = deduplicate()
    session = requests.Session()
    with open('bntx1.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber", "timeStamp", "hash", "nonce", "blockHash", "transactionIndex",
                         "from", "to", "value", "gas", "gasPrice", "isError", "txreceipt_status", "input",
                         "contractAddress", "cumulativeGasUsed", "gasUsed", "confirmations"])
        number = 0
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            try:
                if len(results):
                    for result in results:
                        writer.writerow([result['blockNumber'], result['timeStamp'], result['hash'], result['nonce'],
                                         result['blockHash'],
                                         result['transactionIndex'], result['from'], result['to'], result['value'],
                                         result['gas'], result['gasPrice'],
                                         result['isError'], result['txreceipt_status'], result['input'],
                                         result['contractAddress'], result['cumulativeGasUsed'],
                                         result['gasUsed'], result['confirmations']])
            except Exception:
                print(Exception)
                print(url)
                print(result)
                print(addr)
def differSetItx():
    addrlist = deduplicate()
    session = requests.Session()
    with open('bitx1.csv','w',encoding='utf-8',newline='') as f:
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
            print(url)
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
def differSetEtx():
    addrlist = deduplicate()
    session = requests.Session()
    with open('betx1.csv','w',encoding='utf-8',newline='') as f:
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
    with open('bloxyAddr.txt','r') as f:
        list9 = literal_eval(f.read())
        list9 = [addr.lower() for addr in list9]
    # print(type(list1))
    alladdr1 = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9))
    alladdr2 = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8))
    ret = [i for i in alladdr1 if i not in alladdr2]
    print(ret)
    print(len(alladdr1))
    return ret
    # with open('addr.txt','w',encoding='utf-8') as f:
    #     print(alladdr,file=f)

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
            print(url)
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
            print(url)
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
            print(url)
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
            print(url)
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
# https://api.etherscan.io/api?module=account&action=tokentx&address=0x0f3257e9513f4812bf015efc5022f16bfef0cfa8&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=YourApiKeyToken
# https://api.etherscan.io/api?module=account&action=txlist&address=0xd0b0d5a8c0b40b7272115a23a2d5e36ad190f13c&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=YourApiKeyToken
# https://api.etherscan.io/api?module=account&action=txlistinternal&address=0xe81ad9c0b999222bfe4060ef36b9fef995bad9f9&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ
#fig2:每个地址首次欺诈交易的时间
#fig3：每个月不同种交易的欺诈交易的数量
#fig5：2019年最多欺诈交易的地址，取出来分析交易数量
#fig6：不同种交易地址的存活时间
#fig7：欺诈地址的一般交易和内部交易的数量分布
def fig2():
    # A = [1,3,2]
    # B = [4,5,6]
    # zipped = zip(A, B)
    # sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    # result = zip(*sort_zipped)
    # x_axis, y_axis = [list(x) for x in result]
    # print(x_axis)
    # print(y_axis)
    # return
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    #找每个地址第一次收到钱的时间戳，包括一般交易和内部交易
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('itx1.csv')
    df6 = pandas.read_csv('itx2.csv')
    df7 = pandas.read_csv('itx3.csv')
    df8 = pandas.read_csv('itx4.csv')
    df9 = pandas.read_csv('bntx1.csv')
    df10 = pandas.read_csv('bitx1.csv')
    frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10]
    df = pandas.concat(frames)
    df = df.drop_duplicates()#去重
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    df = df.sort_values('timeStamp')
    addr2time = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2time[row['to']].append(row['timeStamp'])
    for addr,time in addr2time.items():
        time.sort()
    print(addr2time)
    addr2mon = {}
    for addr,time in addr2time.items():
        if len(time) > 0:
            addr2mon[addr] = time[0]
    print(addr2mon)
    mon2count = {}
    for addr,mon in addr2mon.items():
        mon2count[mon] = mon2count.get(mon,0) + 1
    print(mon2count)
    x = mon2count.keys()
    y = mon2count.values()
    zipped = zip(x, y)
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    print(result)
    plt.plot(x,y)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()

def nfig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('bntx1.csv')
    frames = [df1,df2,df3,df4,df5]
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
    plt.yscale('log')
    plt.show()

def ifig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    df1 = pandas.read_csv('itx1.csv')
    df2 = pandas.read_csv('itx2.csv')
    df3 = pandas.read_csv('itx3.csv')
    df4 = pandas.read_csv('itx4.csv')
    df5 = pandas.read_csv('bitx1.csv')
    frames = [df1,df2,df3,df4]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
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
    plt.yscale('log')
    plt.show()


def efig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    df1 = pandas.read_csv('etx1.csv')
    df2 = pandas.read_csv('etx2.csv')
    df3 = pandas.read_csv('etx3.csv')
    df4 = pandas.read_csv('etx4.csv')
    df5 = pandas.read_csv('betx1.csv')
    print(df1.shape[0])
    print(df2.shape[0])
    print(df3.shape[0])
    print(df4.shape[0])
    frames = [df1,df2,df3,df4]
    df = pandas.concat(frames)
    print(df.shape[0])
    df = df.drop_duplicates()
    print(df.shape[0])
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
    plt.yscale('log')
    plt.show()

#fig4：所有地址每个月欺诈交易的数量，根据txhash统计，存储to地址和txhash的列表的字典，然后去重，统计所有种类的交易
def fig4():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('itx1.csv')
    df6 = pandas.read_csv('itx2.csv')
    df7 = pandas.read_csv('itx3.csv')
    df8 = pandas.read_csv('itx4.csv')
    df9 = pandas.read_csv('etx1.csv')
    df10 = pandas.read_csv('etx2.csv')
    df11 = pandas.read_csv('etx3.csv')
    df12 = pandas.read_csv('etx4.csv')
    df13 = pandas.read_csv('bntx1.csv')
    df14 = pandas.read_csv('bitx1.csv')
    df15 = pandas.read_csv('betx1.csv')
    frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15]
    df = pandas.concat(frames)
    df = df.drop_duplicates()#去重
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    df = df.sort_values('timeStamp')
    pandas.set_option('display.max_columns', 40)  # 打印最大列数
    #月份2地址2交易数量，不同地址作为同x不同y的点
    #地址2月份还是月份2地址都可以，地址2月份2交易数量方便
    #先排序时间再统计交易数量
    mon2addr2num = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            mon2addr2num[row['timeStamp']] = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            mon2addr2num[row['timeStamp']][row['to']] = mon2addr2num[row['timeStamp']].get(row['to'],0) + 1
    #将月份和交易数量存入x轴和y轴
    x = []
    y = []
    for mon,addr2num in mon2addr2num.items():
        for addr,num in addr2num.items():
            x.append(mon)
            y.append(num)
    plt.scatter(x, y,s=9)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.show()

def nfig6():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('bntx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2time[row['to']].append(row['timeStamp'])
    for addr,time in addr2time.items():#将时间列表排序，计算时间差
        time.sort()
    x = ['<6h','6h≤time<12h','12h≤time<18h','18h≤time<24h','24h≤time<48h','48h≤time<1 week','1 week≤time<1 month','>1 month']
    y = [0,0,0,0,0,0,0,0]
    for addr, time in addr2time.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days * 24 + (end - start).seconds / 3600
    for addr,living in addr2living.items():
        if living < 6:
            y[0] += 1
        if 6 <= living and living <12:
            y[1] += 1
        if 12 <= living and living < 18:
            y[2] += 1
        if 18 <= living and living < 24:
            y[3] += 1
        if 24 <= living and living < 48:
            y[4] += 1
        if 48 <= living and living < 168:
            y[5] += 1
        if 168 <= living and living < 720:
            y[6] += 1
        if 720 <= living:
            y[7] += 1
    return x,y
    print(y)
    plt.bar(x, y)
    plt.xticks(rotation=30)
    ax = plt.gca()
    plt.yscale('log')
    plt.show()

def ifig6():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('itx1.csv')
    df2 = pandas.read_csv('itx2.csv')
    df3 = pandas.read_csv('itx3.csv')
    df4 = pandas.read_csv('itx4.csv')
    df5 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2time[row['to']].append(row['timeStamp'])
    for addr,time in addr2time.items():#将时间列表排序，计算时间差
        time.sort()
    x = ['<6h','6h≤time<12h','12h≤time<18h','18h≤time<24h','24h≤time<48h','48h≤time<1 week','1 week≤time<1 month','>1 month']
    y = [0,0,0,0,0,0,0,0]
    for addr, time in addr2time.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days * 24 + (end - start).seconds / 3600
    for addr,living in addr2living.items():
        if living < 6:
            y[0] += 1
        if 6 <= living and living <12:
            y[1] += 1
        if 12 <= living and living < 18:
            y[2] += 1
        if 18 <= living and living < 24:
            y[3] += 1
        if 24 <= living and living < 48:
            y[4] += 1
        if 48 <= living and living < 168:
            y[5] += 1
        if 168 <= living and living < 720:
            y[6] += 1
        if 720 <= living:
            y[7] += 1
    return x,y
    print(y)
    plt.bar(x, y)
    plt.xticks(rotation=30)
    ax = plt.gca()
    plt.yscale('log')
    plt.show()

def efig6():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('etx1.csv')
    df2 = pandas.read_csv('etx2.csv')
    df3 = pandas.read_csv('etx3.csv')
    df4 = pandas.read_csv('etx4.csv')
    df5 = pandas.read_csv('betx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2time[row['to']].append(row['timeStamp'])
    for addr,time in addr2time.items():#将时间列表排序，计算时间差
        time.sort()
    # print(addr2time)
    x = ['<6h','6h≤time<12h','12h≤time<18h','18h≤time<24h','24h≤time<48h','48h≤time<1 week','1 week≤time<1 month','>1 month']
    y = [0,0,0,0,0,0,0,0]
    for addr, time in addr2time.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days * 24 + (end - start).seconds / 3600
    for addr,living in addr2living.items():
        if living < 6:
            y[0] += 1
        if 6 <= living and living <12:
            y[1] += 1
        if 12 <= living and living < 18:
            y[2] += 1
        if 18 <= living and living < 24:
            y[3] += 1
        if 24 <= living and living < 48:
            y[4] += 1
        if 48 <= living and living < 168:
            y[5] += 1
        if 168 <= living and living < 720:
            y[6] += 1
        if 720 <= living:
            y[7] += 1
    return x,y
    print(y)
    plt.bar(x, y)
    plt.xticks(rotation=30)
    ax = plt.gca()
    plt.yscale('log')
    plt.show()

def fig6():
    nx,ny = nfig6()
    ny = numpy.array(ny)
    ix,iy = ifig6()
    iy = numpy.array(iy)
    ex,ey = efig6()
    ey = numpy.array(ey)
    y = numpy.array([1,1,1,1,1,1,1,1])
    x = ['<6h','6h≤time<12h','12h≤time<18h','18h≤time<24h','24h≤time<48h','48h≤time<1 week','1 week≤time<1 month','>1 month']
    x = numpy.arange(len(x))
    width = 0.2
    plt.bar(nx, ny, width, color='r', label="normal txs")
    plt.bar(x+width, iy, width, color='g', label="internal txs")
    plt.bar(x+width+width, ey, width, color='b', label="erc20 txs")
    plt.xticks(rotation=30)
    plt.yscale('log')
    plt.legend()
    plt.show()

def nfig7():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('bntx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2prof = {}
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    session = requests.Session()
    res = literal_eval(session.get(url).text)['rates']
    usd = res['usd']['value']  # 一个比特币的价格
    rates = {}
    for name, dic in res.items():
        rates[name] = usd / dic['value']
    eth = rates['eth']  # 一个以太币的价格
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2prof[row['to']] = 0
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            try:
                if isinstance(row['value'],str):
                    addr2prof[row['to']] += int(row['value']) * eth / 1000000000000000000
            except Exception:
                print(row['value'])
    print(addr2prof)
    prof2num = {}
    profaxis = ['0-1k','1k-2k','2k-3k','3k-4k','4k-5k','5k-10k','10k-15k','>15k']
    for prof in profaxis:
        prof2num[prof] = 0
    for addr,prof in addr2prof.items():
        if prof / 1000 <= 1:
            prof2num['0-1k'] += 1
        if prof / 1000 > 1 and prof / 1000 <= 2:
            prof2num['1k-2k'] += 1
        if prof / 1000 > 2 and prof / 1000 <= 3:
            prof2num['2k-3k'] += 1
        if prof / 1000 > 3 and prof / 1000 <= 4:
            prof2num['3k-4k'] += 1
        if prof / 1000 > 4 and prof / 1000 <= 5:
            prof2num['4k-5k'] += 1
        if prof / 1000 > 5 and prof / 1000 < 10:
            prof2num['5k-10k'] += 1
        if prof / 1000 > 10 and prof / 1000 < 15:
            prof2num['10k-15k'] += 1
        if prof / 1000 > 15:
            prof2num['>15k'] += 1
    x = []
    y = []
    for prof in profaxis:
        x.append(prof)
        y.append(prof2num[prof])
    plt.bar(x,y)
    plt.xticks(rotation=30)
    plt.yscale('log')
    plt.show()
    print(prof2num)

def ifig7():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('itx1.csv')
    df2 = pandas.read_csv('itx2.csv')
    df3 = pandas.read_csv('itx3.csv')
    df4 = pandas.read_csv('itx4.csv')
    df5 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2prof = {}
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    session = requests.Session()
    res = literal_eval(session.get(url).text)['rates']
    usd = res['usd']['value']  # 一个比特币的价格
    rates = {}
    for name, dic in res.items():
        rates[name] = usd / dic['value']
    eth = rates['eth']  # 一个以太币的价格
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            addr2prof[row['to']] = 0
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            try:
                if isinstance(row['value'],str):
                    addr2prof[row['to']] += int(row['value']) * eth / 1000000000000000000
            except Exception:
                print(row['value'])
    print(addr2prof)
    prof2num = {}
    profaxis = ['0-1k','1k-2k','2k-3k','3k-4k','4k-5k','5k-10k','10k-15k','>15k']
    for prof in profaxis:
        prof2num[prof] = 0
    for addr,prof in addr2prof.items():
        if prof / 1000 <= 1:
            prof2num['0-1k'] += 1
        if prof / 1000 > 1 and prof / 1000 <= 2:
            prof2num['1k-2k'] += 1
        if prof / 1000 > 2 and prof / 1000 <= 3:
            prof2num['2k-3k'] += 1
        if prof / 1000 > 3 and prof / 1000 <= 4:
            prof2num['3k-4k'] += 1
        if prof / 1000 > 4 and prof / 1000 <= 5:
            prof2num['4k-5k'] += 1
        if prof / 1000 > 5 and prof / 1000 < 10:
            prof2num['5k-10k'] += 1
        if prof / 1000 > 10 and prof / 1000 < 15:
            prof2num['10k-15k'] += 1
        if prof / 1000 > 15:
            prof2num['>15k'] += 1
    x = []
    y = []
    for prof in profaxis:
        x.append(prof)
        y.append(prof2num[prof])
    plt.bar(x,y)
    plt.xticks(rotation=30)
    plt.yscale('log')
    plt.show()
    print(prof2num)



def fig8():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    session = requests.Session()
    res = literal_eval(session.get(url).text)['rates']
    usd = res['usd']['value']#一个比特币的价格
    rates = {}
    for name,dic in res.items():
        rates[name] = usd / dic['value']
    eth = rates['eth']#一个以太币的价格
    print(res)
    print(usd)
    print(rates)
    print(eth)
    df1 = pandas.read_csv('etx1.csv')
    df2 = pandas.read_csv('etx2.csv')
    df3 = pandas.read_csv('etx3.csv')
    df4 = pandas.read_csv('etx4.csv')
    df5 = pandas.read_csv('betx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    addr2profit = {}
    for index, row in df.iterrows():
        try:
            if row['to'] != 'NaN' and row['to'] in addrlist:
                if isinstance(row['tokenSymbol'],str) and row['tokenSymbol'].lower() in rates.keys():
                    addr2profit[row['to']] = int(row['value']) * rates[row['tokenSymbol'].lower()] / 1000000000000000000
                elif not isinstance(row['tokenSymbol'],str) and not math.isnan((row['tokenSymbol'])):
                    continue
        except Exception:
            # print(index)
            print(math.isnan((row['tokenSymbol'])))
            print(row)
            print(type(row['tokenSymbol']))
            print(numpy.isnan(row['tokenSymbol']))
            # print(row['tokenSymbol'])
    print(addr2profit)
    print(len(addr2profit.keys()))

    return
    df5 = pandas.read_csv('itx1.csv')
    df6 = pandas.read_csv('itx2.csv')
    df7 = pandas.read_csv('itx3.csv')
    df8 = pandas.read_csv('itx4.csv')
    frames = [df5, df6, df7, df8]
    df = pandas.concat(frames)
    for index, row in df.iterrows():
        pass

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.distributions.empirical_distribution import ECDF

def nfig9():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('bntx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    #欺诈地址作为接收方的欺诈交易数量
    addr2num = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    # print(addr2num)
    # txnum2addrnum = {'1-10': 3447, '10-100': 1650, '100-1000': 228, '1000-5000': 24}
    # #先画直方图，横轴是交易数量区间，纵轴是欺诈地址数
    txnum2addrnum = {}
    # txnum = ['1-10','10-100','100-1000','1000-5000']#原本要分的区间，不需要分区间，需要交易数量到地址数量的映射，如果该交易数量没有则构造
    # print(list(txnum2addrnum.values()))
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # print(txnum2addrnum)
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    # y = numpy.array(y)
    # name = x

    # ecdf = ECDF(x)
    # x = numpy.linspace(min(x),max(x),len(x))
    # y = ecdf(x)

    # ysum = sum(y)
    # y = numpy.cumsum(y)
    # 构造数据
    # x = list(txnum2addrnum.keys())
    # res_freq = [value / ysum for value in y]#频率
    # print(res_freq)

    # plt.bar(list(range(len(res_freq))),res_freq,tick_label=x,width=0.6)
    # plt.xscale('log')
    # plt.xticks(rotation=30)
    # plt.show()
    # plt.plot(x,y,label=name)

    # df_participant_pair = pd.read_sql(sqls_participant_pair, db)
    # df_participant_pair['cumsum'] = numpy.cumsum(df_participant_pair['count'])
    # df_participant_pair['percentage'] = df_participant_pair['cumsum'] / list(df_participant_pair['cumsum'])[-1]
    # line2 = ax.plot(df_participant_pair['involve_pairs'], df_participant_pair['percentage'], color='black',
    #                 label='Participants')


    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x,percentage)
    plt.xscale('log')
    plt.show()

    # plt.plot(x,y)
    # plt.xticks(rotation=30)
    # plt.xscale('log')
    # plt.show()

def ifig9():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('itx1.csv')
    df2 = pandas.read_csv('itx2.csv')
    df3 = pandas.read_csv('itx3.csv')
    df4 = pandas.read_csv('itx4.csv')
    df5 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4, df5]
    df = pandas.concat(frames)
    addr2num = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # print(txnum2addrnum)
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]

    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()

    # print(x)
    # print(y)
    # # 构造数据
    # x = list(txnum2addrnum.keys())
    # res_freq = [value / sum(y) for value in y]
    # plt.bar(x, res_freq)
    # # plt.plot(x, cdf_value)
    # plt.xscale('log')
    # plt.xticks(rotation=30)
    # plt.show()

def tofig9():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('itx1.csv')
    df6 = pandas.read_csv('itx2.csv')
    df7 = pandas.read_csv('itx3.csv')
    df8 = pandas.read_csv('itx4.csv')
    df9 = pandas.read_csv('bntx1.csv')
    df10 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4,df5,df6,df7,df8,df9,df10]
    df = pandas.concat(frames)
    addr2num = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # print(txnum2addrnum)
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def fromfig9():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('itx1.csv')
    df6 = pandas.read_csv('itx2.csv')
    df7 = pandas.read_csv('itx3.csv')
    df8 = pandas.read_csv('itx4.csv')
    df9 = pandas.read_csv('bntx1.csv')
    df10 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4,df5,df6,df7,df8,df9,df10]
    df = pandas.concat(frames)
    addr2num = {}
    for index, row in df.iterrows():
        if row['to'] != 'NaN' and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2num[row['from']] = addr2num.get(row['from'],0) + 1
            except Exception:
                print(row['from'])
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def getnormaladdr():
    df = pandas.read_csv('ethereum_tagged_address.csv',encoding='ISO-8859-1')
    normalAddr = []
    hacktype = ['blacklist']
    exchangenum = 0
    for index, row in df.iterrows():
        for typeword in hacktype:
            if typeword.lower() not in row['label'].lower():
                normalAddr.append(row['addr'])
            if 'exchange' in row['label'].lower():
                exchangenum += 1
    # print(exchangenum)
    normalAddr = list(set(normalAddr))
    # print(len(normalAddr))
    with open('Peckshield.txt','w') as f:
        print(normalAddr,file=f)
def getnormaladdr2():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    with webdriver.Chrome() as w:
        w.get('https://cn.etherscan.com/login')
        username = w.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtUserName"]').send_keys('pegEth')
        passwd = w.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtPassword"]').send_keys('Asdljh0422')
        time.sleep(20)
        w.get('https://cn.etherscan.com/accounts/label/exchange?subcatid=undefined&size=10000&start=0&col=1&order=asc')
def getnormaladdrNtxs1():
    # with open('etherscanLabeledExchange1.txt','r',encoding='utf-8') as f:
    #     list1 = literal_eval(f.read())
    # with open('etherscanLabeledExchange2.txt','r',encoding='utf-8') as f:
    #     list2 = literal_eval(f.read())
    # with open('Peckshield.txt','r',encoding='utf-8') as f:
    #     list3 = literal_eval(f.read())
    # mylist = list(set(list1 + list2 + list3))
    # with open('normalAddr.txt','w',encoding='utf-8') as f:
    #     print(mylist,file=f)
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:1500]
    session = requests.Session()
    with open('normalntx1.csv','w',encoding='utf-8',newline='') as f:
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
def getnormaladdrNtxs2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[1500:3000]
    session = requests.Session()
    with open('normalntx2.csv','w',encoding='utf-8',newline='') as f:
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
def getnormaladdrNtxs3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[3000:4500]
    session = requests.Session()
    with open('normalntx3.csv','w',encoding='utf-8',newline='') as f:
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
def getnormaladdrNtxs4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4500:6000]
    session = requests.Session()
    with open('normalntx4.csv','w',encoding='utf-8',newline='') as f:
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
def getnormaladdrNtxs5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[6000:7500]
    session = requests.Session()
    with open('normalntx5.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 6000
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
def getnormaladdrNtxs6():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[7500:9000]
    session = requests.Session()
    with open('normalntx6.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 7500
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
def getnormaladdrNtxs7():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[9000:10500]
    session = requests.Session()
    with open('normalntx7.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 9000
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
def getnormaladdrNtxs8():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[10500:12000]
    session = requests.Session()
    with open('normalntx8.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 10500
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
def getnormaladdrNtxs9():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[12000:13500]
    session = requests.Session()
    with open('normalntx9.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 12000
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
def getnormaladdrNtxs10():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[13500:15000]
    session = requests.Session()
    with open('normalntx10.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 13500
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
def getnormaladdrNtxs11():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[15000:16500]
    session = requests.Session()
    with open('normalntx11.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 15000
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
def getnormaladdrNtxs12():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[16500:]
    session = requests.Session()
    with open('normalntx12.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 16500
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
def getnormaladdrNtxs13():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = ['0x7c49e1c0e33f3efb57d64b7690fa287c8d15b90a']
    session = requests.Session()
    with open('normalntx13.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        number = 16500
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
def getnormaladdrItxs1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:2000]
    session = requests.Session()
    with open('normalitx1.csv','w',encoding='utf-8',newline='') as f:
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
            # print(url)
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
def getnormaladdrItxs2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[2000:4000]
    session = requests.Session()
    with open('normalitx2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 2000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4000:6000]
    session = requests.Session()
    with open('normalitx3.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 4000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[6000:8000]
    session = requests.Session()
    with open('normalitx4.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 6000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[8000:10000]
    session = requests.Session()
    with open('normalitx5.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 8000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs6():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[10000:12000]
    session = requests.Session()
    with open('normalitx6.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 10000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs7():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[12000:14000]
    session = requests.Session()
    with open('normalitx7.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 12000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs8():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[14000:16000]
    session = requests.Session()
    with open('normalitx8.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 14000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs9():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[16000:]
    session = requests.Session()
    with open('normalitx9.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 16000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrItxs10():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = ['0x7c49e1c0e33f3efb57d64b7690fa287c8d15b90a']
    session = requests.Session()
    with open('normalitx10.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","from","to","value",
                         "contractAddress","input","type","gas","gasUsed","traceId",
                         "isError","errCode"])
        number = 16000
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            results = literal_eval(session.get(url).text)['result']
            number += 1
            print(number)
            # print(url)
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
def getnormaladdrEtxs1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:2000]
    session = requests.Session()
    with open('normaletx1.csv','w',encoding='utf-8',newline='') as f:
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
def getnormaladdrEtxs2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[2000:4000]
    session = requests.Session()
    with open('normaletx2.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 2000
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
def getnormaladdrEtxs3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[4000:6000]
    session = requests.Session()
    with open('normaletx3.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 4000
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
def getnormaladdrEtxs4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[6000:8000]
    session = requests.Session()
    with open('normaletx4.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 6000
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
def getnormaladdrEtxs5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[8000:10000]
    session = requests.Session()
    with open('normaletx5.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 8000
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
def getnormaladdrEtxs6():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[10000:12000]
    session = requests.Session()
    with open('normaletx6.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 10000
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
def getnormaladdrEtxs7():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[12000:14000]
    session = requests.Session()
    with open('normaletx7.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 12000
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
def getnormaladdrEtxs8():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[14000:16000]
    session = requests.Session()
    with open('normaletx8.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 14000
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
def getnormaladdrEtxs9():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[16000:]
    session = requests.Session()
    with open('normaletx9.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 16000
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
def getnormaladdrEtxs10():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = ['0xc46ac314fa9ce95667031a26fffe05827af6f192','0x07c0201aa56fb130a4d6cd99e9ef7efb55fc6219','0x5e44d890f52432a01d467730672325184f521ae7']
    session = requests.Session()
    with open('normaletx9.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","from",
                         "contractAddress","to","value","tokenName","tokenSymbol","tokenDecimal",
                         "transactionIndex","gas","gasPrice","gasUsed","cumulativeGasUsed","input","confirmations"])
        number = 16000
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
    # with open('ntx1.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx2.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx3.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('ntx4.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('itx1.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('itx2.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('itx3.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('itx4.csv','r') as f:
    #     print(len(f.readlines()))
    # with open('etx1.csv','r',encoding='utf-8') as f:
    #     print(len(f.readlines()))
    # with open('etx2.csv', 'r', encoding='utf-8') as f:
    #     print(len(f.readlines()))
    # with open('etx3.csv','r',encoding='utf-8') as f:
    #     print(len(f.readlines()))
    # with open('etx4.csv','r',encoding='utf-8') as f:
    #     print(len(f.readlines()))
    with open('normalAddr.txt','r') as f:
        list = literal_eval(f.read())
        print(len(list))
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
    #     getnormaladdrNtxs2()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs3")
    #     getnormaladdrNtxs3()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs4")
    #     getnormaladdrNtxs4()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs5")
    #     getnormaladdrNtxs5()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs6")
    #     getnormaladdrNtxs6()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs7")
    #     getnormaladdrNtxs7()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs8")
    #     getnormaladdrNtxs8()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs9")
    #     getnormaladdrNtxs9()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs10")
    #     getnormaladdrNtxs10()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs11")
    #     getnormaladdrNtxs11()
    # except Exception:
    #     pass
    # test()
    # try:
    #     print("ntxs12")
    #     getnormaladdrNtxs12()
    # except Exception:
    #     pass
    # try:
    #     print("ntxs13")
    #     getnormaladdrNtxs13()
    # except Exception:
    #     pass
    # try:
    #     print("itxs1")
    #     getnormaladdrItxs1()
    # except Exception:
    #     pass
    # try:
    #     print("itxs2")
    #     getnormaladdrItxs2()
    # except Exception:
    #     pass
    # try:
    #     print("itxs3")
    #     getnormaladdrItxs3()
    # except Exception:
    #     pass
    # try:
    #     print("itxs4")
    #     getnormaladdrItxs4()
    # except Exception:
    #     pass
    # try:
    #     print("itxs5")
    #     getnormaladdrItxs5()
    # except Exception:
    #     pass
    # try:
    #     print("itxs6")
    #     getnormaladdrItxs6()
    # except Exception:
    #     pass
    # try:
    #     print("itxs7")
    #     getnormaladdrItxs7()
    # except Exception:
    #     pass
    # try:
    #     print("itxs8")
    #     getnormaladdrItxs8()
    # except Exception:
    #     pass
    # try:
    #     print("itxs9")
    #     getnormaladdrItxs9()
    # except Exception:
    #     pass
    # try:
    #     print("itxs10")
    #     getnormaladdrItxs10()
    # except Exception:
    #     pass
    # try:
    #     print("etxs1")
    #     getnormaladdrEtxs1()
    # except Exception:
    #     pass
    # try:
    #     print("etxs2")
    #     getnormaladdrEtxs2()
    # except Exception:
    #     pass
    # try:
    #     print("etxs3")
    #     getnormaladdrEtxs3()
    # except Exception:
    #     pass
    # try:
    #     print("etxs4")
    #     getnormaladdrEtxs4()
    # except Exception:
    #     pass
    # try:
    #     print("etxs5")
    #     getnormaladdrEtxs5()
    # except Exception:
    #     pass
    # try:
    #     print("etxs6")
    #     getnormaladdrEtxs6()
    # except Exception:
    #     pass
    # try:
    #     print("etxs7")
    #     getnormaladdrEtxs7()
    # except Exception:
    #     pass
    # try:
    #     print("etxs8")
    #     getnormaladdrEtxs8()
    # except Exception:
    #     pass
    # try:
    #     print("etxs")
    #     getnormaladdrEtxs9()
    # except Exception:
    #     pass
    pass
    # try:
    #     print("itxs1")
    #     getItxs1()
    # except Exception:
    #     print("itxs1")
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
    # efig6()
    # nfig7()
    # ifig7()
    # nfig9()
    # tofig9()
    # bloxymalware()
    # bloxy2()
    # getnormaladdr()
    # getnormaladdrNtxs2()
    # differSetEtx()