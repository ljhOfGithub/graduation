from selenium import webdriver
import time
import requests
from ast import literal_eval
import csv
import xlrd
import yaml
import pandas
import datetime
import numpy
import math
from matplotlib.pyplot import MultipleLocator
from bs4 import BeautifulSoup
apikey = "ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
apikey = "P3FE926UGARGQF8HKPM4XWJ38CJAGX5WHZ"
import json
import traceback
from scipy import stats
import numpy as np
import seaborn as sns
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.distributions.empirical_distribution import ECDF
import random
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
    with open('bloxyhack.txt','w',encoding='utf-8') as f:
        print(url2type,file=f)
    json_str = json.dumps(url2type)
    with open('bloxyhack.json', 'w') as json_file:
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
    with open('bloxyhack.txt','r',encoding='utf-8') as f:
        dict1 = literal_eval(f.read())
    with open('bloxyscam.txt','r',encoding='utf-8') as f:
        dict2 = literal_eval(f.read())
    with open('bloxymalware.txt','r',encoding='utf-8') as f:
        dict3 = literal_eval(f.read())
    mydict = {}
    mydict.update(dict1)
    mydict.update(dict2)
    mydict.update(dict3)
    newdict = {}
    for key,value in mydict.items():
        newdict[key.lower()] = value.lower()
    mydict = newdict
    # print(mydict)
    hacktype = ['Phish', 'Trust-Trading', 'Hack', 'Malware', 'Upbit', 'Scam', 'hackethereumIco']
    notType = ['Hacking', 'HackToken', 'HackDao', 'HackerGold', 'Hacken', 'HackerSpaceBarneysToken', 'HackerToken', 'Gitcoin', 'VitaluckHack']
    # hacktype = 'PhishTrust-TradingTrust TradingHackMalwareUpbitScam'
    addrlist = []
    # notType = 'HackingHackTokenHackDaoHackerGoldHackenHackerSpaceBarneysToken'
    for url,type in mydict.items():
        for key in hacktype:
            if key.lower() in type.lower():
                if url.startswith('/address'):
                    addr = url[9:]
                elif url.startswith('/tx'):
                    addr = url[4:]
                if len(addr) == 42:
                    addrlist.append(addr)
    removelist = []
    for addr in addrlist:
        for nottag in notType:
            if '/tx/'+str(addr) in mydict.keys():
                if nottag.lower() in mydict['/tx/'+str(addr)].lower():
                    removelist.append(addr)
            elif '/address/'+str(addr) in mydict.keys():
                if nottag.lower() in mydict['/address/'+str(addr)].lower():
                    removelist.append(addr)
    for removeaddr in removelist:
        addrlist.remove(removeaddr)
    print(removelist)
    print(addrlist)
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
    # return ret
    with open('addr.txt','w',encoding='utf-8') as f:
        print(alladdr1,file=f)
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
# def remointeraction():
#     with open('ntx1.csv','r') as f:
#         ntx1 = literal_eval()
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
    # df1 = pandas.read_csv('ntx1.csv')
    # df2 = pandas.read_csv('ntx2.csv')
    # df3 = pandas.read_csv('ntx3.csv')
    # df4 = pandas.read_csv('ntx4.csv')
    # df5 = pandas.read_csv('itx1.csv')
    # df6 = pandas.read_csv('itx2.csv')
    # df7 = pandas.read_csv('itx3.csv')
    # df8 = pandas.read_csv('itx4.csv')
    # df9 = pandas.read_csv('bntx1.csv')
    # df10 = pandas.read_csv('bitx1.csv')
    # frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10]
    #
    # df = pandas.concat(frames)
    # df = df.drop_duplicates()#去重
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    df = df.sort_values('timeStamp')
    addr2time = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            addr2time[row['to']].append(row['timeStamp'])
    for addr,time in addr2time.items():
        time.sort()
    # print(addr2time)
    addr2mon = {}
    for addr,time in addr2time.items():
        if len(time) > 0:
            addr2mon[addr] = time[0]
    # print(addr2mon)
    with open('fig2addr2mon.txt','w',encoding='utf-8') as f:
        print(addr2mon,file=f)
    mon2count = {}
    for addr,mon in addr2mon.items():
        mon2count[mon] = mon2count.get(mon,0) + 1
    # print(mon2count)
    mon2count = sorted(mon2count.items(),key = lambda x:(x[0],x[1]))
    with open('fig2mon2count.txt','w',encoding='utf-8') as f:
        print(mon2count,file=f)
    return
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
    plt.savefig('fig2.jpg')
    plt.show()

def nfig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    # df1 = pandas.read_csv('ntx1.csv')
    # df2 = pandas.read_csv('ntx2.csv')
    # df3 = pandas.read_csv('ntx3.csv')
    # df4 = pandas.read_csv('ntx4.csv')
    # df5 = pandas.read_csv('bntx1.csv')
    # frames = [df1,df2,df3,df4,df5]
    # df = pandas.concat(frames)
    df = pandas.read_csv('ntx.csv')
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    dfsort = df.sort_values('timeStamp')
    month2count = {}
    for index,row in dfsort.iterrows():#桶计数，如果当前月份还没有对应的字典则初始化为0，如果已经有对应的字典则取出对应的数量然后在此基础上加1
        month2count[row['timeStamp']] = month2count.get(row['timeStamp'],0) + 1
    print(month2count)
    x = month2count.keys()
    y = month2count.values()
    with open('fig3N.txt','w') as f:
        print(month2count,file=f)
    return
    plt.plot(x,y)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.show()

def ifig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    # df1 = pandas.read_csv('itx1.csv')
    # df2 = pandas.read_csv('itx2.csv')
    # df3 = pandas.read_csv('itx3.csv')
    # df4 = pandas.read_csv('itx4.csv')
    # df5 = pandas.read_csv('bitx1.csv')
    # frames = [df1,df2,df3,df4]
    # df = pandas.concat(frames)
    # df = df.drop_duplicates()
    df = pandas.read_csv('itx.csv')
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    dfsort = df.sort_values('timeStamp')
    month2count = {}
    for index,row in dfsort.iterrows():#桶计数，如果当前月份还没有对应的字典则初始化为0，如果已经有对应的字典则取出对应的数量然后在此基础上加1
        month2count[row['timeStamp']] = month2count.get(row['timeStamp'],0) + 1
    print(month2count)
    x = month2count.keys()
    y = month2count.values()
    with open('fig3I.txt','w') as f:
        print(month2count,file=f)
    return
    plt.plot(x,y)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.show()

def efig3():
    #统计每个月的欺诈交易数量，取出每行的时间戳进行转换，判断时间戳的月份，月份的欺诈交易数量+1
    # df1 = pandas.read_csv('etx1.csv')
    # df2 = pandas.read_csv('etx2.csv')
    # df3 = pandas.read_csv('etx3.csv')
    # df4 = pandas.read_csv('etx4.csv')
    # df5 = pandas.read_csv('betx1.csv')
    # print(df1.shape[0])
    # print(df2.shape[0])
    # print(df3.shape[0])
    # print(df4.shape[0])
    # frames = [df1,df2,df3,df4]
    # df = pandas.concat(frames)
    df = pandas.read_csv('etx.csv')
    # print(df.shape[0])
    # df = df.drop_duplicates()
    # print(df.shape[0])
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m"))
    dfsort = df.sort_values('timeStamp')
    month2count = {}
    for index,row in dfsort.iterrows():#桶计数，如果当前月份还没有对应的字典则初始化为0，如果已经有对应的字典则取出对应的数量然后在此基础上加1
        month2count[row['timeStamp']] = month2count.get(row['timeStamp'],0) + 1
    print(month2count)
    x = month2count.keys()
    y = month2count.values()
    with open('fig3E.txt','w') as f:
        print(month2count,file=f)
    return
    plt.plot(x,y)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.show()
def mixfig3():
    with open('fig3N.txt','r') as f:
        month2count1 = literal_eval(f.read())
    with open('fig3I.txt','r') as f:
        month2count2 = literal_eval(f.read())
    with open('fig3E.txt','r') as f:
        month2count3 = literal_eval(f.read())
    x1 = month2count1.keys()
    y1 = month2count1.values()
    x2 = month2count2.keys()
    y2 = month2count2.values()
    x3 = month2count3.keys()
    y3 = month2count3.values()
    plt.plot(x1, y1, label='normal tx')
    plt.plot(x2, y2, label='internal tx')
    plt.plot(x3, y3, label='token tx')
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(3)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.legend()
    plt.savefig('fig3.jpg')
    plt.show()
def fig221():
    with open('fig2addr2mon.txt','r',encoding='utf-8') as f:
        addr2mon = literal_eval(f.read())
    addrlist21 = []
    for addr,month in addr2mon.items():
        if month[0:4] == '2021':
            addrlist21.append(addr)
    with open('fig221.txt','w',encoding='utf-8') as f:
        print(addrlist21,file=f)
def scamIOcome21():
    with open('fig221.txt','r',encoding='utf-8') as f:
        addrlist21 = literal_eval(f.read())
    with open('scamIncome.txt','r',encoding='utf-8') as f:
        scamIncome = literal_eval(f.read())
    with open('scamOutcome.txt','r',encoding='utf-8') as f:
        scamOutcome = literal_eval(f.read())
    scamIncome21 = {}
    scamOutcome21 = {}
    profit21 = {}
    maxprofit = 0
    for addr in addrlist21:
        if addr in scamIncome.keys():
            scamIncome21[addr] = scamIncome[addr]
            if scamIncome21[addr] > maxprofit:
                maxprofit = scamIncome21[addr]
            if scamIncome21[addr] > 100:
                profit21[addr] = scamIncome21[addr]
        if addr in scamIncome.keys():
            scamOutcome21[addr] = scamOutcome[addr]

    with open('scamIncome21.txt','w') as f:
        print(scamIncome21,file=f)
    with open('scamOutcome21.txt','w') as f:
        print(scamOutcome21,file=f)
#fig4：所有地址每个月欺诈交易的数量，根据txhash统计，存储to地址和txhash的列表的字典，然后去重，统计所有种类的交易
def fig4():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    # df5 = pandas.read_csv('itx1.csv')
    # df6 = pandas.read_csv('itx2.csv')
    # df7 = pandas.read_csv('itx3.csv')
    # df8 = pandas.read_csv('itx4.csv')
    # df9 = pandas.read_csv('etx1.csv')
    # df10 = pandas.read_csv('etx2.csv')
    # df11 = pandas.read_csv('etx3.csv')
    # df12 = pandas.read_csv('etx4.csv')
    # df13 = pandas.read_csv('bntx1.csv')
    # df14 = pandas.read_csv('bitx1.csv')
    # df15 = pandas.read_csv('betx1.csv')
    # frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15]
    frames = [df1,df2,df3,df4]
    df = pandas.concat(frames)
    df = df.drop_duplicates()#去重
    df['timeStamp'] = df['timeStamp'].map(lambda x:datetime.datetime.fromtimestamp(x).strftime("%Y-%m-%d"))
    df = df.sort_values('timeStamp')
    pandas.set_option('display.max_columns', 40)  # 打印最大列数
    #月份2地址2交易数量，不同地址作为同x不同y的点
    #地址2月份还是月份2地址都可以，地址2月份2交易数量方便
    #先排序时间再统计交易数量
    day2addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            day2addr2num[row['timeStamp']] = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            day2addr2num[row['timeStamp']][row['to']] = day2addr2num[row['timeStamp']].get(row['to'],0) + 1
    with open('fig4.txt','w',encoding='utf-8') as f:
        print(day2addr2num,file=f)
    # with open('fig4.txt','r',encoding='utf-8') as f:
    #     day2addr2num = literal_eval(f.read())
    #将月份和交易数量存入x轴和y轴
    x = []
    y = []
    for mon,addr2num in day2addr2num.items():
        for addr,num in addr2num.items():
            x.append(mon)
            y.append(num)
    plt.scatter(x, y,s=1)
    plt.xticks(rotation=30)
    x_major_locator = MultipleLocator(90)
    ax = plt.gca()
    ax.set_ylabel('# of transactions')
    ax.set_xlabel('Date')
    ax.set_ylim(1)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.yscale('log')
    plt.savefig('fig4.jpg')
    plt.show()

def nfig6():#欺诈地址一般交易的living小时 scamNtxliving
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    # df1 = pandas.read_csv('ntx1.csv')
    # df2 = pandas.read_csv('ntx2.csv')
    # df3 = pandas.read_csv('ntx3.csv')
    # df4 = pandas.read_csv('ntx4.csv')
    # df5 = pandas.read_csv('ntx5.csv')
    # df6 = pandas.read_csv('bntx1.csv')
    # frames = [df1, df2, df3, df4, df5, df6]
    # df = pandas.concat(frames)
    # df = df.drop_duplicates()  # 去重
    df = pandas.read_csv('ntx.csv')
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
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
    with open('scamNtxliving.txt','w') as f:
        print(addr2living,file=f)
    return
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
    # df1 = pandas.read_csv('itx1.csv')
    # df2 = pandas.read_csv('itx2.csv')
    # df3 = pandas.read_csv('itx3.csv')
    # df4 = pandas.read_csv('itx4.csv')
    # df5 = pandas.read_csv('bitx1.csv')
    # frames = [df1, df2, df3, df4, df5]
    # df = pandas.concat(frames)
    df = pandas.read_csv('itx.csv')
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
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
    with open('scamItxliving.txt','w') as f:
        print(addr2living,file=f)
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
    # df1 = pandas.read_csv('etx1.csv')
    # df2 = pandas.read_csv('etx2.csv')
    # df3 = pandas.read_csv('etx3.csv')
    # df4 = pandas.read_csv('etx4.csv')
    # df5 = pandas.read_csv('betx1.csv')
    # frames = [df1, df2, df3, df4, df5]
    # df = pandas.concat(frames)
    # df = df.drop_duplicates()  # 去重
    df = pandas.read_csv('etx.csv')
    df = df.sort_values('timeStamp')
    addr2time = {}#地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2time[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
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
    with open('scamEtxliving.txt','w') as f:
        print(addr2living,file=f)
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
def fig7n():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('ntx.csv')
    # df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2prof = {}
    # url = "https://api.coingecko.com/api/v3/exchange_rates"
    # session = requests.Session()
    # res = literal_eval(session.get(url).text)['rates']
    # usd = res['usd']['value']  # 一个比特币的价格
    # rates = {}
    # for name, dic in res.items():
    #     rates[name] = usd / dic['value']
    # eth = rates['eth']  # 一个以太币的价格
    eth = 2460.268204521556
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'].lower() in addrlist and row['from'].lower() not in addrlist:
            addr2prof[row['to']] = 0
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'].lower() in addrlist and row['from'].lower() not in addrlist:
            try:
                if isinstance(row['value'],str):
                    addr2prof[row['to']] += int(row['value']) / 1000000000000000000 * eth
            except Exception:
                print(row['value'])
    # print(addr2prof)
    # with open('scamNtxProfit.txt','w') as f:
    #     print(addr2prof,file=f)
    # print(addr2prof['0x8909cc8d294544ca2c956550edbcb59ce4f2a9ad'])
    # return
    prof2num = {}
    profaxis = ['0-100k','100k-200k','200k-300k','300k-400k','400k-500k','500k-600k','600k-700k','700k-800k','800k-900k','900k-1000k','1000k-1100k','1100k-1200k','1200k-1300k','1300k-1400k','1400k-1500k','>1500k']
    for prof in profaxis:
        prof2num[prof] = 0
    for addr,prof in addr2prof.items():
        if prof / 1000 <= 100:
            prof2num['0-100k'] += 1
        if prof / 1000 > 100 and prof / 1000 <= 200:
            prof2num['100k-200k'] += 1
        if prof / 1000 > 200 and prof / 1000 <= 300:
            prof2num['200k-300k'] += 1
        if prof / 1000 > 300 and prof / 1000 <= 400:
            prof2num['300k-400k'] += 1
        if prof / 1000 > 400 and prof / 1000 <= 500:
            prof2num['400k-500k'] += 1
        if prof / 1000 > 500 and prof / 1000 <= 600:
            prof2num['500k-600k'] += 1
        if prof / 1000 > 600 and prof / 1000 <= 700:
            prof2num['600k-700k'] += 1
        if prof / 1000 > 700 and prof / 1000 <= 800:
            prof2num['700k-800k'] += 1
        if prof / 1000 > 800 and prof / 1000 <= 900:
            prof2num['800k-900k'] += 1
        if prof / 1000 > 900 and prof / 1000 <= 1000:
            prof2num['900k-1000k'] += 1
        if prof / 1000 > 1000 and prof / 1000 <= 1100:
            prof2num['1000k-1100k'] += 1
        if prof / 1000 > 1100 and prof / 1000 <= 1200:
            prof2num['1100k-1200k'] += 1
        if prof / 1000 > 1200 and prof / 1000 <= 1300:
            prof2num['1200k-1300k'] += 1
        if prof / 1000 > 1300 and prof / 1000 < 1400:
            prof2num['1300k-1400k'] += 1
        if prof / 1000 > 1400 and prof / 1000 < 1500:
            prof2num['1400k-1500k'] += 1
        if prof / 1000 > 1500:
            prof2num['>1500k'] += 1
            print(addr)

    prof2num2 = {}
    for addr,prof in addr2prof.items():
        addr2prof[addr] = addr2prof[addr]
    for addr,prof in addr2prof.items():
        prof2num2[prof] = prof2num2.get(prof,0) + 1
    x = []
    y = []
    # with open('fig7n.txt','r') as f:
    #     prof2num = literal_eval(f.read())
    fig, ax = plt.subplots()
    for prof in profaxis:
        x.append(prof)
        y.append(prof2num[prof])
    plt.bar(x,y,width=1)
    plt.xticks(rotation=30)
    plt.yscale('log')
    x_major_locator = MultipleLocator(5)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.savefig('fig7n.jpg')
    ax.set_xlabel('The Profit of Address($)')
    ax.set_ylabel('# of normal txs')
    plt.show()

    with open('fig7n.txt','w') as f:
        print(prof2num,file=f)
    with open('fig7n2.txt','w') as f:
        print(prof2num2,file=f)
    with open('fig7n3.txt','w') as f:
        print(addr2prof,file=f)
def fig7nCdf():
    # with open('fig7n.txt','r') as f:
    #     prof2num = literal_eval(f.read())
    # # return
    # profaxis = ['0-100k','100k-200k','200k-300k','300k-400k','400k-500k','500k-600k','600k-700k','700k-800k','800k-900k','900k-1000k','1000k-1100k','1100k-1200k','1200k-1300k','1300k-1400k','1400k-1500k','>1500k']
    # x = []
    # y = []
    #
    # fig, ax = plt.subplots()
    # for prof in profaxis:
    #     x.append(prof)
    #     y.append(prof2num[prof])
    # plt.bar(x,y,width=1)
    # plt.xticks(rotation=30)
    # plt.yscale('log')
    # x_major_locator = MultipleLocator(5)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    # plt.savefig('fig7n.jpg')
    # ax.set_xlabel('The Profit of Address($)')
    # ax.set_ylabel('# of normal txs')
    # plt.show()
    prof2num = {}
    with open('fig7n2.txt','r') as f:
        prof2num = literal_eval(f.read())
    with open('fig7n3.txt','r') as f:
        addr2prof = literal_eval(f.read())
    proflist = sorted(prof2num.keys())
    print(proflist)
    print(max(proflist))
    for addr,prof in addr2prof.items():
        if prof == max(proflist):
            print(addr)
    return
    maxp = max(proflist)
    # testprofit = []
    # for profit in proflist:
    #     if profit > 1000000:
    #         testprofit.append(profit)
    for addr,prof in addr2prof.items():
        if prof == maxp:
            print(addr)

    zipped = zip(prof2num.keys(), prof2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    # for prof in profaxis:
    #     x.append(prof)
    #     y.append(prof2num[prof])
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x,percentage)
    # plt.xscale('log')
    # x_major_locator = MultipleLocator(1000)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    ax.set_ylabel('CDF of Addresses')
    ax.set_xlabel('the profit of address($)')
    ax.set_xlim(1)
    plt.savefig('fig7nCdf2.jpg')
    # ax.set_xlim(1)
    plt.show()

def fig7i():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('itx.csv')
    df = df.sort_values('timeStamp')
    addr2prof = {}
    # url = "https://api.coingecko.com/api/v3/exchange_rates"
    # session = requests.Session()
    # res = literal_eval(session.get(url).text)['rates']
    # usd = res['usd']['value']  # 一个比特币的价格
    # rates = {}
    # for name, dic in res.items():
    #     rates[name] = usd / dic['value']
    # eth = rates['eth']  # 一个以太币的价格
    eth = 2460.268204521556
    for index, row in df.iterrows():
        # if isinstance(row['to'],str):
        # if not math.isnan(row['to']):
        if isinstance(row['to'],str):
            addr2prof[row['to']] = 0
    # print(addr2prof)
    hashlist = []
    valuesum = 0
    for index, row in df.iterrows():
        # if isinstance(row['to'],str) and row['to'].lower() in addrlist and row['from'].lower() not in addrlist:
        try:
            if isinstance(row['to'],str) and row['to'].lower() in addrlist and row['from'].lower() not in addrlist:
                addr2prof[row['to']] += int(row['value']) / 1000000000000000000 * eth
            if isinstance(row['to'],str) and row['to'].lower() == '0xa9bf70a420d364e923c74448d9d817d3f2a77822' and int(row['value']) != 0 and row['from'] not in addrlist:
                # print(row)
                # print(row['value'])
                # print(row['hash'])
                hashlist.append(row['hash'])
                valuesum += int(row['value'])
        except Exception:
            print(row['value'])
    # print(addr2prof)
    # with open('scamItxProfit.txt','w') as f:
    #     print(addr2prof,file=f)
    # print(hashlist)
    # print(valuesum)

    #'0xa6074142f75502f24a050e0ed6d45a303d713051d56433f007e661d18d045900'是0xa9bf70a420d364e923c74448d9d817d3f2a77822欺诈最多的交易hash
    prof2num = {}
    profaxis = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k-600k', '600k-700k', '700k-800k',
                '800k-900k', '900k-1000k', '1000k-1100k', '1100k-1200k', '1200k-1300k', '1300k-1400k', '1400k-1500k',
                '>1500k']
    for prof in profaxis:
        prof2num[prof] = 0
    for addr, prof in addr2prof.items():
        if prof / 1000 <= 100:
            prof2num['0-100k'] += 1
        if prof / 1000 > 100 and prof / 1000 <= 200:
            prof2num['100k-200k'] += 1
        if prof / 1000 > 200 and prof / 1000 <= 300:
            prof2num['200k-300k'] += 1
        if prof / 1000 > 300 and prof / 1000 <= 400:
            prof2num['300k-400k'] += 1
        if prof / 1000 > 400 and prof / 1000 <= 500:
            prof2num['400k-500k'] += 1
        if prof / 1000 > 500 and prof / 1000 <= 600:
            prof2num['500k-600k'] += 1
        if prof / 1000 > 600 and prof / 1000 <= 700:
            prof2num['600k-700k'] += 1
        if prof / 1000 > 700 and prof / 1000 <= 800:
            prof2num['700k-800k'] += 1
        if prof / 1000 > 800 and prof / 1000 <= 900:
            prof2num['800k-900k'] += 1
        if prof / 1000 > 900 and prof / 1000 <= 1000:
            prof2num['900k-1000k'] += 1
        if prof / 1000 > 1000 and prof / 1000 <= 1100:
            prof2num['1000k-1100k'] += 1
        if prof / 1000 > 1100 and prof / 1000 <= 1200:
            prof2num['1100k-1200k'] += 1
        if prof / 1000 > 1200 and prof / 1000 <= 1300:
            prof2num['1200k-1300k'] += 1
        if prof / 1000 > 1300 and prof / 1000 < 1400:
            prof2num['1300k-1400k'] += 1
        if prof / 1000 > 1400 and prof / 1000 < 1500:
            prof2num['1400k-1500k'] += 1
        if prof / 1000 > 1500:
            prof2num['>1500k'] += 1
    prof2num2 = {}
    for addr, prof in addr2prof.items():
        addr2prof[addr] = int(addr2prof[addr])
    for addr, prof in addr2prof.items():
        prof2num2[prof] = prof2num2.get(prof, 0) + 1
    x = []
    y = []
    for prof in profaxis:
        x.append(prof)
        y.append(prof2num[prof])
    plt.bar(x,y,width=1)
    plt.xticks(rotation=30)
    plt.yscale('log')
    x_major_locator = MultipleLocator(5)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.set_ylabel('the PDF graph of internal txs')
    ax.set_xlabel('the profit of address($)')
    plt.savefig('fig7i.jpg')
    plt.show()
    with open('fig7i.txt','w') as f:
        print(prof2num,file=f)
    with open('fig7i2.txt','w') as f:
        print(prof2num2,file=f)
    with open('fig7i3.txt','w') as f:
        print(addr2prof,file=f)
def fig7iCdf():
    with open('fig7i2.txt', 'r') as f:
        prof2num = literal_eval(f.read())
    with open('fig7i3.txt', 'r') as f:
        addr2prof = literal_eval(f.read())
    # profaxis = ['0-100k','100k-200k','200k-300k','300k-400k','400k-500k']
    # ,'500k-600k','600k-700k','700k-800k','800k-900k','900k-1000k','1000k-1100k','1100k-1200k','1200k-1300k','1300k-1400k','1400k-1500k','>1500k']
    proflist = sorted(prof2num.keys())
    print(proflist)
    # print(max(proflist))
    maxp = max(proflist)
    # testprofit = []
    # for profit in proflist:
    #     if profit > 1000000:
    #         testprofit.append(profit)
    for addr, prof in addr2prof.items():
        if prof == maxp:
            print(addr)
    zipped = zip(prof2num.keys(), prof2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    # for prof in profaxis:
    #     x.append(prof)
    #     y.append(prof2num[prof])
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    # plt.xscale('log')
    # x_major_locator = MultipleLocator(1000)
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    ax.set_ylabel('CDF of Addresses')
    ax.set_xlabel('the profit of address($)')
    ax.set_xlim(1)
    plt.savefig('fig7iCdf2.jpg')
    # ax.set_xlim(1)
    plt.show()
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

    df = pandas.read_csv('etx.csv')
    addr2profit = {}
    for index, row in df.iterrows():
        try:
            if isinstance(row['to'],str) and row['to'] in addrlist:
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
def nfig9Intx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('ntx.csv')
    #欺诈地址作为接收方的欺诈交易数量
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    with open('scamInNtx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    # print(addr2num)
    # txnum2addrnum = {'1-10': 3447, '10-100': 1650, '100-1000': 228, '1000-5000': 24}
    # #先画直方图，横轴是交易数量区间，纵轴是欺诈地址数
    txnum2addrnum = {}
    # #原本要分的区间，不需要分区间，需要交易数量到地址数量的映射，如果该交易数量没有则构造
    # print(list(txnum2addrnum.values()))
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # print(txnum2addrnum)
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('scamAddrNFig9Intx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x,percentage)
    plt.xscale('log')
    plt.show()

def fig921():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist21 = literal_eval(f.read())
    with open('scamInTx.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('scamOutTx.txt','r') as f:
        addr2Outtxnum = literal_eval(f.read())
    addr2Intxnum21 = {}
    addr2Outtxnum21 = {}
    for addr in addrlist21:#不是所有21年的欺诈地址都有in tx
        if addr in addr2Intxnum.keys():
            addr2Intxnum21[addr] = addr2Intxnum[addr]
        if addr in addr2Outtxnum.keys():
            addr2Outtxnum21[addr] = addr2Outtxnum[addr]
    with open('scamInTx21.txt','w') as f:
        print(addr2Intxnum21,file=f)
    with open('scamOutTx21.txt','w') as f:
        print(addr2Outtxnum21,file=f)
def ifig9Intx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('itx.csv')
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    with open('scamInItx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('scamAddrIFig9Intx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def efig9Intx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('etx.csv')
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('scamAddrEFig9Intx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def nfig9Outtx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('ntx.csv')
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2num[row['from']] = addr2num.get(row['from'],0) + 1
            except Exception:
                print(row['from'])
    with open('scamOutNtx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('scamAddrNFig9Outtx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def ifig9Outtx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    # df1 = pandas.read_csv('itx1.csv')
    # df2 = pandas.read_csv('itx2.csv')
    # df3 = pandas.read_csv('itx3.csv')
    # df4 = pandas.read_csv('itx4.csv')
    # df5 = pandas.read_csv('bitx1.csv')
    # frames = [df1, df2, df3, df4, df5]
    # df = pandas.concat(frames)
    df = pandas.read_csv('itx.csv')

    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2num[row['from']] = addr2num.get(row['from'],0) + 1
            except Exception:
                print(row['from'])
    with open('scamOutItx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('scamAddrIFig9Outtx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
def efig9Outtx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    # df1 = pandas.read_csv('etx1.csv')
    # df2 = pandas.read_csv('etx2.csv')
    # df3 = pandas.read_csv('etx3.csv')
    # df4 = pandas.read_csv('etx4.csv')
    # df5 = pandas.read_csv('betx1.csv')
    # frames = [df1, df2, df3, df4, df5]
    # df = pandas.concat(frames)
    df = pandas.read_csv('etx.csv')
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
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
    with open('scamAddrEFig9Outtx.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()

# def tofig9():
#     with open('addr.txt','r',encoding='utf-8') as f:
#         addrlist = literal_eval(f.read())
#     df1 = pandas.read_csv('ntx1.csv')
#     df2 = pandas.read_csv('ntx2.csv')
#     df3 = pandas.read_csv('ntx3.csv')
#     df4 = pandas.read_csv('ntx4.csv')
#     df5 = pandas.read_csv('itx1.csv')
#     df6 = pandas.read_csv('itx2.csv')
#     df7 = pandas.read_csv('itx3.csv')
#     df8 = pandas.read_csv('itx4.csv')
#     df9 = pandas.read_csv('bntx1.csv')
#     df10 = pandas.read_csv('bitx1.csv')
#     frames = [df1, df2, df3, df4,df5,df6,df7,df8,df9,df10]
#     df = pandas.concat(frames)
#     addr2num = {}
#     for index, row in df.iterrows():
#         if isinstance(row['to'],str) and row['to'] in addrlist:
#             try:
#                 if isinstance(row['to'], str):
#                     addr2num[row['to']] = addr2num.get(row['to'],0) + 1
#             except Exception:
#                 print(row['to'])
#     txnum2addrnum = {}
#     for addr,num in addr2num.items():
#         txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
#     # print(txnum2addrnum)
#     zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
#     sort_zipped = sorted(zipped, key=lambda x: (x[0]))
#     result = zip(*sort_zipped)
#     x, y = [list(x) for x in result]
#     with open('scamAddrToFig9.txt','w',encoding='utf-8') as f:
#         print(txnum2addrnum,file=f)
#     fig, ax = plt.subplots()
#     cum = numpy.cumsum(y)
#     percentage = cum / list(cum)[-1]
#     line = ax.plot(x, percentage)
#     plt.xscale('log')
#     plt.show()
# def fromfig9():
#     with open('addr.txt','r',encoding='utf-8') as f:
#         addrlist = literal_eval(f.read())
#     df1 = pandas.read_csv('ntx1.csv')
#     df2 = pandas.read_csv('ntx2.csv')
#     df3 = pandas.read_csv('ntx3.csv')
#     df4 = pandas.read_csv('ntx4.csv')
#     df5 = pandas.read_csv('itx1.csv')
#     df6 = pandas.read_csv('itx2.csv')
#     df7 = pandas.read_csv('itx3.csv')
#     df8 = pandas.read_csv('itx4.csv')
#     df9 = pandas.read_csv('bntx1.csv')
#     df10 = pandas.read_csv('bitx1.csv')
#     frames = [df1, df2, df3, df4,df5,df6,df7,df8,df9,df10]
#     df = pandas.concat(frames)
#     addr2num = {}
#     for index, row in df.iterrows():
#         if isinstance(row['to'],str) and row['from'] in addrlist:
#             try:
#                 if isinstance(row['from'], str):
#                     addr2num[row['from']] = addr2num.get(row['from'],0) + 1
#             except Exception:
#                 print(row['from'])
#     txnum2addrnum = {}
#     for addr,num in addr2num.items():
#         txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
#     zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
#     sort_zipped = sorted(zipped, key=lambda x: (x[0]))
#     result = zip(*sort_zipped)
#     x, y = [list(x) for x in result]
#     with open('scamAddrFromFig9.txt','w',encoding='utf-8') as f:
#         print(txnum2addrnum,file=f)
#     fig, ax = plt.subplots()
#     cum = numpy.cumsum(y)
#     percentage = cum / list(cum)[-1]
#     line = ax.plot(x, percentage)
#     plt.xscale('log')
#     plt.show()
def normalAddrtx2csv1():#一般交易的from，to，value列
    df1 = pandas.read_csv('normalntx1.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])#hash,from,to,value
    df2 = pandas.read_csv('normalntx2.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df3 = pandas.read_csv('normalntx3.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df4 = pandas.read_csv('normalntx4.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df5 = pandas.read_csv('normalntx5.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df6 = pandas.read_csv('normalntx6.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df7 = pandas.read_csv('normalntx7.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df8 = pandas.read_csv('normalntx8.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df9 = pandas.read_csv('normalntx9.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df10 = pandas.read_csv('normalntx10.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df11 = pandas.read_csv('normalntx11.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df12 = pandas.read_csv('normalntx12.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    df13 = pandas.read_csv('normalntx13.csv', low_memory=False, usecols=[1, 2, 6, 7, 8])
    frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]
    df = pandas.concat(frames)
    df.to_csv('normalAddrntx.csv')
def normalAddrtx2csv2():#内部交易的from，to，value列
    df14 = pandas.read_csv('normalitx1.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])#hash,from,to,value
    df15 = pandas.read_csv('normalitx2.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df16 = pandas.read_csv('normalitx3.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df17 = pandas.read_csv('normalitx4.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df18 = pandas.read_csv('normalitx5.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df19 = pandas.read_csv('normalitx6.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df20 = pandas.read_csv('normalitx7.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df21 = pandas.read_csv('normalitx8.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df22 = pandas.read_csv('normalitx9.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    df23 = pandas.read_csv('normalitx10.csv', low_memory=False, usecols=[1, 2, 3, 4, 5])
    frames = [df14, df15, df16, df17, df18, df19, df20, df21, df22, df23]
    df = pandas.concat(frames)
    df.to_csv('normalAddritx.csv')
def normalAddrtx2csv3():#内部交易的from，to，value列
    df14 = pandas.read_csv('normaletx1.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])#hash,from,to,value,tokenSymbol
    df15 = pandas.read_csv('normaletx2.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df16 = pandas.read_csv('normaletx3.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df17 = pandas.read_csv('normaletx4.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df18 = pandas.read_csv('normaletx5.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df19 = pandas.read_csv('normaletx6.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df20 = pandas.read_csv('normaletx7.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df21 = pandas.read_csv('normaletx8.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    df22 = pandas.read_csv('normaletx9.csv', low_memory=False, usecols=[1, 2, 5, 7, 8, 10])
    frames = [df14, df15, df16, df17, df18, df19, df20, df21, df22]
    df = pandas.concat(frames)
    df.to_csv('normalAddretx.csv')
def norAddrNFig9Intxs1():#统计normalAddrntx.csv里面的In Txs of normal Addresses（一般交易）
    with open('normalAddr.txt','r',encoding='utf-8') as f:#正常地址的一般交易的输入交易数量
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',nrows=3000000)
    #欺诈地址作为接收方的欺诈交易数量
    addr2num = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2num[row['to']] = addr2num.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
        print(index)
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrNFig9Intxs1.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numNIntx1.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)


    # 统计交易数量和地址数量的映射
    # #先画直方图，横轴是交易数量区间，纵轴是欺诈地址数
    # txnum2addrnum = {}
    # # txnum = ['1-10','10-100','100-1000','1000-5000']#原本要分的区间，不需要分区间，需要交易数量到地址数量的映射，如果该交易数量没有则构造
    # # print(list(txnum2addrnum.values()))
    # for addr,num in addr2num.items():
    #     txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    # sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    # result = zip(*sort_zipped)
    # x, y = [list(x) for x in result]
    # with open('norAddrNFig9Intxs.txt','w',encoding='utf-8') as f:
    #     print(txnum2addrnum,file=f)
    # fig, ax = plt.subplots()
    # cum = numpy.cumsum(y)
    # percentage = cum / list(cum)[-1]
    # line = ax.plot(x,percentage)
    # plt.xscale('log')
    # plt.show()
def norAddrNFig9Intxs2():#统计normalAddrntx.csv里面的In Txs of normal Addresses（一般交易）
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv').iloc[3000000:6000000]
    # #欺诈地址作为接收方的欺诈交易数量
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     print(index)
    with open('nor2numNIntx2.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrNFig9Intxs2.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numNIntx2.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    # 统计交易数量和地址数量的映射
    # #先画直方图，横轴是交易数量区间，纵轴是欺诈地址数
    txnum2addrnum = {}
    # txnum = ['1-10','10-100','100-1000','1000-5000']#原本要分的区间，不需要分区间，需要交易数量到地址数量的映射，如果该交易数量没有则构造
    # print(list(txnum2addrnum.values()))
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('norAddrNFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x,percentage)
    plt.xscale('log')
    plt.show()
def norAddrNFig9Intxs3():#统计normalAddrntx.csv里面的In Txs of normal Addresses（一般交易）
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv')
    # df = df.iloc[6000000:9000000]
    # #欺诈地址作为接收方的欺诈交易数量
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     print(index)
    with open('nor2numNIntx3.txt', 'r', encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrNFig9Intxs3.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numNIntx3.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    # 统计交易数量和地址数量的映射
    # #先画直方图，横轴是交易数量区间，纵轴是欺诈地址数
    txnum2addrnum = {}
    # txnum = ['1-10','10-100','100-1000','1000-5000']#原本要分的区间，不需要分区间，需要交易数量到地址数量的映射，如果该交易数量没有则构造
    # print(list(txnum2addrnum.values()))
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('norAddrNFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x,percentage)
    plt.xscale('log')
    plt.show()
def norAddrNFig9Intxs4():#统计normalAddrntx.csv里面的In Txs of normal Addresses（一般交易）
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv')
    # df = df.iloc[9000000:12000000]
    # #欺诈地址作为接收方的欺诈交易数量
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     # print(index)
    with open('nor2numNIntx4.txt', 'r', encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrNFig9Intxs4.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return

    with open('nor2numNIntx4.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
def norAddrNFig9Intxs5():#统计normalAddrntx.csv里面的In Txs of normal Addresses（一般交易）
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv')
    # df = df.iloc[12000000:,[0,4]]
    # #欺诈地址作为接收方的欺诈交易数量
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     print(index)

    with open('nor2numNIntx5.txt', 'r', encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrNFig9Intxs5.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numNIntx5.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
#统计txnum2addrnum
def mixnorAddrNFig9Intxs():
    with open('norAddrNFig9Intxs1.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum1 = literal_eval(f.read())
    with open('norAddrNFig9Intxs2.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum2 = literal_eval(f.read())
    with open('norAddrNFig9Intxs3.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    with open('norAddrNFig9Intxs4.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())
    with open('norAddrNFig9Intxs5.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum5 = literal_eval(f.read())
    txnum2addrnum = {}
    txnumlist = list(txnum2addrnum1.keys()) + list(txnum2addrnum2.keys()) + list(txnum2addrnum3.keys()) + list(txnum2addrnum4.keys()) + list(txnum2addrnum5.keys())
    for txnum in txnumlist:
        if txnum in txnum2addrnum1.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum1[txnum]
        if txnum in txnum2addrnum2.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum2[txnum]
        if txnum in txnum2addrnum3.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum3[txnum]
        if txnum in txnum2addrnum4.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum4[txnum]
        if txnum in txnum2addrnum5.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum5[txnum]
    with open('norAddrNFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
def mixnorAddrNFig9Outtxs():
    with open('norAddrNFig9Outtxs1.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum1 = literal_eval(f.read())
    with open('norAddrNFig9Outtxs2.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum2 = literal_eval(f.read())
    with open('norAddrNFig9Outtxs3.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    with open('norAddrNFig9Outtxs4.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())
    with open('norAddrNFig9Outtxs5.txt', 'r', encoding='utf-8') as f:
        txnum2addrnum5 = literal_eval(f.read())
    txnum2addrnum = {}
    txnumlist = list(txnum2addrnum1.keys()) + list(txnum2addrnum2.keys()) + list(txnum2addrnum3.keys()) + list(txnum2addrnum4.keys()) + list(txnum2addrnum5.keys())
    for txnum in txnumlist:
        if txnum in txnum2addrnum1.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum1[txnum]
        if txnum in txnum2addrnum2.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum2[txnum]
        if txnum in txnum2addrnum3.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum3[txnum]
        if txnum in txnum2addrnum4.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum4[txnum]
        if txnum in txnum2addrnum5.keys():
            txnum2addrnum[txnum] = txnum2addrnum.get(txnum,0) + txnum2addrnum5[txnum]
    with open('norAddrNFig9Outtxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
#internal tx不需要分段分析交易，正常地址的内部交易的输入交易数量

def norAddrIFig9Intxs():#统计normalAddritx.csv里面的In Txs of normal Addresses（内部交易）
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddritx2.csv')
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     print(index)
    txnum2addrnum = {}
    with open('nor2numIIntx1.txt', 'r', encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrIFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numIIntx1.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    with open('norAddrIFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    plt.xscale('log')
    plt.show()
#token tx不需要分段
def norAddrEFig9Intxs():#正常地址的token交易的输入交易数量
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddretx2.csv')
    # #欺诈地址作为接收方的欺诈交易数量
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str) and row['to'] in addrlist:
    #         try:
    #             if isinstance(row['to'], str):
    #                 addr2num[row['to']] = addr2num.get(row['to'],0) + 1
    #         except Exception:
    #             print(row['to'])
    #     print(index)
    txnum2addrnum = {}
    with open('nor2numEIntx1.txt', 'r', encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('norAddrEFig9Intxs.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
    return
    with open('nor2numEIntx1.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return

def norAddrNFig9Outtxs1():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv',nrows=3000000)#读取去重交易后的正常地址交易
    # df = df.iloc[0:,[0,3]]
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    with open('nor2numNOuttx1.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrNFig9Outtxs1.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numNOuttx1.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    # for addr,num in addr2num.items():
    #     txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    # with open('normalAddrFromFig91.txt','w',encoding='utf-8') as f:
    #     print(txnum2addrnum,file=f)
    # zipped = zip(txnum2addrnum.keys(), txnum2addrnum.values())
    # sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    # result = zip(*sort_zipped)
    # x, y = [list(x) for x in result]
    # fig, ax = plt.subplots()
    # cum = numpy.cumsum(y)
    # percentage = cum / list(cum)[-1]
    # line = ax.plot(x, percentage)
    # plt.xscale('log')
    # plt.show()
def norAddrNFig9Outtxs2():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3]).iloc[3000000:6000000]
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    # txnum2addrnum = {}
    with open('nor2numNOuttx2.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrNFig9Outtxs2.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numNOuttx2.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('normalAddrFromFig92.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
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
def norAddrNFig9Outtxs3():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3]).iloc[6000000:9000000]
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    # txnum2addrnum = {}
    with open('nor2numNOuttx3.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrNFig9Outtxs3.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numNOuttx3.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
    for addr,num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num,0) + 1
    with open('normalAddrFromFig92.txt','w',encoding='utf-8') as f:
        print(txnum2addrnum,file=f)
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
def norAddrNFig9Outtxs4():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3]).iloc[9000000:12000000]
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    # txnum2addrnum = {}
    with open('nor2numNOuttx4.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrNFig9Outtxs4.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numNOuttx4.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
def norAddrNFig9Outtxs5():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3]).iloc[12000000:]
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    # txnum2addrnum = {}
    with open('nor2numNOuttx5.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrNFig9Outtxs5.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numNOuttx5.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
def norAddrIFig9Outtxs():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddritx2.csv',usecols=[0,3])
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    with open('nor2numIOuttx.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrIFig9Outtxs.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    with open('nor2numIOuttx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return
def norAddrEFig9Outtxs():#统计两个文件的out txs
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # df = pandas.read_csv('normalAddretx2.csv',usecols=[0,3])
    # pandas.set_option('display.max_columns', None)
    # addr2num = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str) and row['from'] in addrlist:
    #         try:
    #             if isinstance(row['from'], str):
    #                 addr2num[row['from']] = addr2num.get(row['from'],0) + 1
    #         except Exception:
    #             print(row['from'])
    #     print(index)
    with open('nor2numEOuttx.txt','r',encoding='utf-8') as f:
        addr2num = literal_eval(f.read())
    txnum2addrnum = {}
    for addr, num in addr2num.items():
        txnum2addrnum[num] = txnum2addrnum.get(num, 0) + 1
    with open('norAddrEFig9Outtx.txt', 'w', encoding='utf-8') as f:
        print(txnum2addrnum, file=f)
    return
    # txnum2addrnum = {}
    with open('nor2numEOuttx.txt','w',encoding='utf-8') as f:
        print(addr2num,file=f)
    return

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
def scamIncome():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'],0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
    with open('scamIncome.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)

def scamOutcome():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2outcome[row['to']] = addr2outcome.get(row['to'],0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
    with open('scamOutcome.txt','w',encoding='utf-8') as f:
        print(addr2outcome,file=f)
def scamTx():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    addr2Intxnum = {}
    addr2Outtxnum = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2Intxnum[row['to']] = addr2Intxnum.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2Outtxnum[row['from']] = addr2Outtxnum.get(row['from'],0) + 1
            except Exception:
                print(row['from'])
                traceback.print_exc()
    with open('scamInTx.txt','w') as f:#欺诈地址两种交易的in txs
        print(addr2Intxnum,file=f)
    with open('scamOutTx.txt','w') as f:
        print(addr2Outtxnum,file=f)

def scamIOTxAna():
    with open('scamInTx.txt','r') as f:
        scamInTx = literal_eval(f.read())
    with open('scamOutTx.txt','r') as f:
        scamOutTx = literal_eval(f.read())
    scamInTx = sorted(scamInTx.items(),key = lambda x:(x[1]))
    scamOutTx = sorted(scamOutTx.items(),key = lambda x:(x[1]))
    print(scamInTx)
    print(scamOutTx)
    # with open('scamInNtx.txt','r') as f:
    #     scamInNtx = literal_eval(f.read())
    # with open('scamOutNtx.txt','r') as f:
    #     scamOutNtx = literal_eval(f.read())
    # scamInNtx = sorted(scamInNtx.items(),key = lambda x:(x[1]))
    # scamOutNtx = sorted(scamOutNtx.items(),key = lambda x:(x[1]))
    # with open('scamInItx.txt','r') as f:
    #     scamInItx = literal_eval(f.read())
    # with open('scamOutItx.txt','r') as f:
    #     scamOutItx = literal_eval(f.read())
    # scamInItx = sorted(scamInItx.items(),key = lambda x:(x[1]))
    # scamOutItx = sorted(scamOutItx.items(),key = lambda x:(x[1]))
    # print(scamInItx)
    # print(scamOutItx)
def scamTx2():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    addr2Intxnum = {}
    addr2Outtxnum = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist and isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2Intxnum[row['to']] = addr2Intxnum.get(row['to'],0) + 1
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist and isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2Outtxnum[row['from']] = addr2Outtxnum.get(row['from'],0) + 1
            except Exception:
                print(row['from'])
                traceback.print_exc()
    with open('scamInTx2.txt','w') as f:
        print(addr2Intxnum,file=f)
    with open('scamOutTx2.txt','w') as f:
        print(addr2Outtxnum,file=f)
def normalInNtx1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,4,5]).iloc[0:3000000]
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeNtx1.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
def normalInNtx2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,4,5]).iloc[3000000:6000000]
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeNtx2.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
def normalInNtx3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,4,5]).iloc[6000000:9000000]
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeNtx3.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
def normalInNtx4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,4,5]).iloc[9000000:12000000]
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeNtx4.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
def normalInNtx5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,4,5]).iloc[12000000:]
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeNtx5.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
#internal tx 不需要分段
def normalInItx():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv',usecols=[0,4,5])
    pandas.set_option('display.max_columns', None)
    addr2income = {}
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            try:
                if isinstance(row['to'], str):
                    addr2income[row['to']] = addr2income.get(row['to'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['to'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalIncomeItx1.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
#token tx不需要计算利润

def normalOutNtx1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3,5]).iloc[0:3000000]
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeNtx1.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
def normalAvgOutNtx2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3,5]).iloc[3000000:6000000]
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeNtx2.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
def normalOutNtx3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3,5]).iloc[6000000:9000000]
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeNtx3.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
def normalOutNtx4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3,5]).iloc[9000000:12000000]
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeNtx4.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
def normalOutNtx5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv',usecols=[0,3,5]).iloc[12000000:]
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeNtx5.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
#internal tx不需要分段
def normalOutItx():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv',usecols=[0,3,5])
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalOutcomeItx1.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)
#token tx不需要计算income outcome
def normalAvgOutEtx():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv',usecols=[0,3,5])
    addr2outcome = {}
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            try:
                if isinstance(row['from'], str):
                    addr2outcome[row['from']] = addr2outcome.get(row['from'], 0) + int(row['value']) / 1000000000000000000
            except Exception:
                print(row['from'])
                print(row['value'])
                traceback.print_exc()
        print(index)
    with open('normalAvgOutEtx1.txt', 'w', encoding='utf-8') as f:
        print(addr2outcome, file=f)

def mixScamAvg():
    with open('scamIncome.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    zipped1 = zip(addr2income.keys(), addr2income.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    cum = numpy.cumsum(y1)
    percentage1 = cum / list(cum)[-1]
    with open('scamOutcome.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    zipped2 = zip(addr2outcome.keys(), addr2outcome.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y2)
    percentage2 = cum / list(cum)[-1]
    line1 = ax.plot(x1, percentage1, label='Avg Income Of scam addresses', color='black')
    line2 = ax.plot(x2, percentage2, label='Avg Outcome Of scam addresses', linestyle="--", color='black')
    ax.set_xlabel('Average Income/Outcome of Addresses (ETH)')
    ax.set_ylabel('CDF of Addresses')
    plt.xscale('log')
    plt.legend()
    plt.show()
def mixNormalAvg():
    with open('normalAvgIn.txt', 'r', encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    zipped1 = zip(addr2income.keys(), addr2income.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    cum = numpy.cumsum(y1)
    percentage1 = cum / list(cum)[-1]
    with open('normalAvgOut.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    zipped2 = zip(addr2outcome.keys(), addr2outcome.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y2)
    percentage2 = cum / list(cum)[-1]
    # line1 = ax.plot(x1, percentage1, label='Avg Income Of normal addresses', color='black')
    line2 = ax.plot(x2, percentage2, label='Avg Outcome Of normal addresses', linestyle="--", color='black')
    ax.set_xlabel('Average Income/Outcome of Addresses (ETH)')
    ax.set_ylabel('CDF of Addresses')
    plt.xscale('log')
    plt.legend()
    plt.show()
def inteAvgInNtx():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx1.txt','r',encoding='utf-8') as f:
        dict1 = literal_eval(f.read())
    with open('normalIncomeNtx2.txt','r',encoding='utf-8') as f:
        dict2 = literal_eval(f.read())
    with open('normalIncomeNtx3.txt','r',encoding='utf-8') as f:
        dict3 = literal_eval(f.read())
    with open('normalIncomeNtx4.txt','r',encoding='utf-8') as f:
        dict4 = literal_eval(f.read())
    with open('normalIncomeNtx5.txt','r',encoding='utf-8') as f:
        dict5 = literal_eval(f.read())
    addr2income = {}
    for addr in addrlist:
        if addr in dict1.keys():
            addr2income[addr] = addr2income.get(addr,0) + dict1[addr]
        if addr in dict2.keys():
            addr2income[addr] = addr2income.get(addr,0) + dict2[addr]
        if addr in dict3.keys():
            addr2income[addr] = addr2income.get(addr,0) + dict3[addr]
        if addr in dict4.keys():
            addr2income[addr] = addr2income.get(addr,0) + dict4[addr]
        if addr in dict5.keys():
            addr2income[addr] = addr2income.get(addr,0) + dict5[addr]
    with open('normalInNtx.txt','w',encoding='utf-8') as f:
        print(addr2income,file=f)
def NtxAddrIncome():
    with open('normalInNtx.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    a = sorted(addr2income.items(), key=lambda x: x[1], reverse=True)
    with open('Ntxaddr2income.txt','w',encoding='utf-8') as f:
        print(a,file=f)
def ItxAddrIncome():
    with open('normalIncomeItx1.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    a = sorted(addr2income.items(), key=lambda x: x[1], reverse=True)
    with open('Itxaddr2income.txt','w',encoding='utf-8') as f:
        print(a,file=f)
def normalAddrAvgIn():
    with open('normalInNtx.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    #打开存储有地址到交易数量的映射文件
    with open('txtypenum.txt','w') as f:
        addr2txnum = literal_eval(f.read())
#欺诈地址的前1/3生命周期的时间戳
#有的欺诈地址可能livingtime为0，因为不是所有欺诈地址都发出交易
def scamAthirdLivingtime():
    with open('addr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)  # 拼接所有交易
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')  # 将所有交易按时间戳排序
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    addr2living3 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
        addr2living1[addr] = 0
        addr2living2[addr] = 0
        addr2living3[addr] = 0
    for index, row in df.iterrows():
        if isinstance(row['to'], str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
            addr2living3[addr] = livingtime
    with open('scam2athirdLivingtime1.txt','w') as f:
        print(addr2living1,file=f)
    with open('scam2athirdLivingtime2.txt','w') as f:
        print(addr2living2,file=f)
    with open('scam2athirdLivingtime3.txt','w') as f:
        print(addr2living3,file=f)
def scamAthirdIntime():
    with open('addr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)#拼接所有交易
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')#将所有交易按时间戳排序
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('scam2athirdIntime1.txt','w') as f:
        print(addr2living1,file=f)
    with open('scam2athirdIntime2.txt','w') as f:
        print(addr2living2,file=f)

def scamAthirdOuttime():
    with open('addr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)#拼接所有交易
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')#将所有交易按时间戳排序
    addr2day = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2day[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:#统计每个地址的时间戳
            addr2day[row['from']].append(row['timeStamp'])
    for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
        time.sort()
    for addr, time in addr2day.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start

    with open('scam2athirdOuttime1.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('scam2athirdOuttime2.txt', 'w') as f:
        print(addr2living2, file=f)
#如何筛选某个时间戳之间的交易并统计其数量，小于指定时间戳的才统计，根据爬到的交易进行统计
def scamAthirdInTxnum():
    with open('addr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('scam2athirdLivingtime1.txt','r') as f:
        addr2end1 = literal_eval(f.read())
    with open('scam2athirdLivingtime2.txt','r') as f:
        addr2end2 = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')#统计每个地址的符合时间戳条件的交易
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:#初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]  # 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])#每一个地址的满足对应条件的交易hash值列表
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('scam2athirdIntxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('scam2athirdIntxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('scam2athirdIntxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def scamAthirdOutTxnum():
    with open('addr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('scam2athirdLivingtime1.txt','r') as f:
        addr2end1 = literal_eval(f.read())
    with open('scam2athirdLivingtime2.txt','r') as f:
        addr2end2 = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    df2 = pandas.read_csv('itx.csv')
    frames = [df1,df2]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')#统计每个地址的符合时间戳条件的交易
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:#初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])#每一个地址的满足对应条件的交易hash值列表
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('scam2athirdOuttxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('scam2athirdOuttxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('scam2athirdOuttxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3LivingTime():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read()) # 读取去重交易后的正常地址交易
    df1 = pandas.read_csv('normalAddrntx2.csv')
    df2 = pandas.read_csv('normalAddritx2.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    addr2living3 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
        addr2living1[addr] = 0
        addr2living2[addr] = 0
        addr2living3[addr] = 0
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
            addr2living3[addr] = livingtime
    with open('normal2athirdtime1.txt','w') as f:
        print(addr2living1,file=f)
    with open('normal2athirdtime2.txt','w') as f:
        print(addr2living2,file=f)
    with open('normal2athirdtime3.txt','w') as f:
        print(addr2living3,file=f)
def norAddrA3InNtxTime():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx1.txt','w') as f:
        print(addr2living1,file=f)
    with open('normal2athirdtimeInNtx2.txt','w') as f:
        print(addr2living2,file=f)
def norAddrA3InNtxTime1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[0:3000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx11.txt','w') as f:
        print(addr2living1,file=f)
    with open('normal2athirdtimeInNtx12.txt','w') as f:
        print(addr2living2,file=f)
def norAddrA3InNtxTime2():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[3000000:6000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for addr, time in addr2stamp.items():
        time.sort()
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx21.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeInNtx22.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3InNtxTime3():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[6000000:9000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx31.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeInNtx32.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3InNtxTime4():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[9000000:12000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx41.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeInNtx42.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3InNtxTime5():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[12000000:]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInNtx51.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeInNtx52.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3OutNtxTime():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx1.txt','w') as f:
        print(addr2living1,file=f)
    with open('normal2athirdtimeOutNtx2.txt','w') as f:
        print(addr2living2,file=f)
def norAddrA3OutNtxTime1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[0:3000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:#直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx11.txt','w') as f:
        print(addr2living1,file=f)
    with open('normal2athirdtimeOutNtx12.txt','w') as f:
        print(addr2living2,file=f)
def norAddrA3OutNtxTime2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[3000000:6000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    # addr2living = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx21.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeOutNtx22.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3OutNtxTime3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[6000000:9000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx31.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeOutNtx32.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3OutNtxTime4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[9000000:12000000]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx41.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeOutNtx42.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3OutNtxTime5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[12000000:]  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:#统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    addr2living1 = {}
    addr2living2 = {}
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeOutNtx51.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeOutNtx52.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3Intxnum():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtime1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtime2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df1 = pandas.read_csv('normalAddrntx2.csv')
    df2 = pandas.read_csv('normalAddritx2.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():#每一个地址的满足对应条件的交易hash值列表
        if isinstance(row['to'],str) and row['to'] in addrlist:# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdIntxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdIntxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdIntxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3InNtxTx():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():#每一个地址的满足对应条件的交易hash值列表
        if isinstance(row['to'],str) and row['to'] in addrlist:# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdInNtxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdInNtxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3InNtxTx1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx11.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx12.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():#每一个地址的满足对应条件的交易hash值列表
        if isinstance(row['to'],str) and row['to'] in addrlist:# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum11.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdInNtxnum12.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdInNtxnum13.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3InNtxTx2():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx21.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx22.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum21.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdInNtxnum22.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdInNtxnum23.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3InNtxTx3():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx31.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx32.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'], str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum31.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdInNtxnum32.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdInNtxnum33.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3InNtxTx4():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx41.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx42.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'], str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum41.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdInNtxnum42.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdInNtxnum43.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3InNtxTx5():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInNtx51.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInNtx52.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'], str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] <= end2 and row['timeStamp'] > end1:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] > end2:
                addr2athirdtxnum3[row['to']] += 1
    with open('normal2athirdInNtxnum51.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdInNtxnum52.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdInNtxnum53.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3Outtxnum():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtime1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtime2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df1 = pandas.read_csv('normalAddrntx2.csv')
    df2 = pandas.read_csv('normalAddritx2.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOuttxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOuttxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOuttxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3OutNtxTx():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum1.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOutNtxnum2.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOutNtxnum3.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3OutNtxTx1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx11.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx12.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum11.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOutNtxnum12.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOutNtxnum13.txt','w') as f:
        print(addr2athirdtxnum3,file=f)

def norAddrA3OutNtxTx2():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx21.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx22.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum21.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOutNtxnum22.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOutNtxnum23.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3OutNtxTx3():

    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx31.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx32.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'], str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum31.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdOutNtxnum32.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdOutNtxnum33.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3OutNtxTx4():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx41.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx42.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum41.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOutNtxnum42.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOutNtxnum43.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3OutNtxTx5():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx51.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutNtx52.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2tx[row['from']].append(row['hash'])
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutNtxnum51.txt','w') as f:
        print(addr2athirdtxnum1,file=f)
    with open('normal2athirdOutNtxnum52.txt','w') as f:
        print(addr2athirdtxnum2,file=f)
    with open('normal2athirdOutNtxnum53.txt','w') as f:
        print(addr2athirdtxnum3,file=f)
def norAddrA3InItxTime():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2 + start
    with open('normal2athirdtimeInItx1.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeInItx2.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3OutItxTime():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living1 = {}
    addr2living2 = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        time.sort()
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living1[addr] = livingtime / 3 + start
            addr2living2[addr] = livingtime / 3 * 2  + start
    with open('normal2athirdtimeOutItx1.txt', 'w') as f:
        print(addr2living1, file=f)
    with open('normal2athirdtimeOutItx2.txt', 'w') as f:
        print(addr2living2, file=f)
def norAddrA3InItxTx():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInItx1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeInItx2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            end1 = addr2end1[row['to']]
            end2 = addr2end2[row['to']]
            if row['timeStamp'] < end1:
                addr2tx[row['to']].append(row['hash'])
                addr2athirdtxnum1[row['to']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['to']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['to']] += 1
    return
    with open('normal2athirdInItxnum1.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdInItxnum2.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdInItxnum3.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddrA3OutItxTx():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutItx1.txt', 'r') as f:
        addr2end1 = literal_eval(f.read())
    with open('normal2athirdtimeOutItx2.txt', 'r') as f:
        addr2end2 = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum1 = {}
    addr2athirdtxnum2 = {}
    addr2athirdtxnum3 = {}
    for addr in addrlist:
        addr2athirdtxnum1[addr] = 0
        addr2athirdtxnum2[addr] = 0
        addr2athirdtxnum3[addr] = 0
    for index, row in df.iterrows():
        if isinstance(row['from'], str) and row['from'] in addrlist:
            end1 = addr2end1[row['from']]
            end2 = addr2end2[row['from']]
            if row['timeStamp'] < end1:
                addr2athirdtxnum1[row['from']] += 1
            if row['timeStamp'] >= end1 and row['timeStamp'] < end2:
                addr2athirdtxnum2[row['from']] += 1
            if row['timeStamp'] >= end2:
                addr2athirdtxnum3[row['from']] += 1
    with open('normal2athirdOutItxnum1.txt', 'w') as f:
        print(addr2athirdtxnum1, file=f)
    with open('normal2athirdOutItxnum2.txt', 'w') as f:
        print(addr2athirdtxnum2, file=f)
    with open('normal2athirdOutItxnum3.txt', 'w') as f:
        print(addr2athirdtxnum3, file=f)
def norAddr3IOTxnum():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdInItxnum1.txt', 'r') as f:
        normal2athirdInItxnum1 = literal_eval(f.read())
    with open('normal2athirdInItxnum2.txt', 'r') as f:
        normal2athirdInItxnum2 = literal_eval(f.read())
    with open('normal2athirdInItxnum3.txt', 'r') as f:
        normal2athirdInItxnum3 = literal_eval(f.read())

    with open('normal2athirdOutItxnum1.txt', 'r') as f:
        normal2athirdOutItxnum1 = literal_eval(f.read())
    with open('normal2athirdOutItxnum2.txt', 'r') as f:
        normal2athirdOutItxnum2 = literal_eval(f.read())
    with open('normal2athirdOutItxnum3.txt', 'r') as f:
        normal2athirdOutItxnum3 = literal_eval(f.read())

    with open('normal2athirdInNtxnum1.txt', 'r') as f:
        normal2athirdInNtxnum1 = literal_eval(f.read())
    with open('normal2athirdInNtxnum2.txt', 'r') as f:
        normal2athirdInNtxnum2 = literal_eval(f.read())
    with open('normal2athirdInNtxnum3.txt', 'r') as f:
        normal2athirdInNtxnum3 = literal_eval(f.read())

    with open('normal2athirdOutNtxnum1.txt', 'r') as f:
        normal2athirdOutNtxnum1 = literal_eval(f.read())
    with open('normal2athirdOutNtxnum2.txt', 'r') as f:
        normal2athirdOutNtxnum2 = literal_eval(f.read())
    with open('normal2athirdOutNtxnum3.txt', 'r') as f:
        normal2athirdOutNtxnum3 = literal_eval(f.read())
    normal2athirdIntxnum = {}
    normal2athirdIntxnum1 = {}
    normal2athirdIntxnum2 = {}
    normal2athirdIntxnum3 = {}
    normal2athirdOuttxnum = {}
    normal2athirdOuttxnum1 = {}
    normal2athirdOuttxnum2 = {}
    normal2athirdOuttxnum3 = {}
    for addr in addrlist:
        normal2athirdIntxnum[addr] = 0
        normal2athirdIntxnum1[addr] = 0
        normal2athirdIntxnum2[addr] = 0
        normal2athirdIntxnum3[addr] = 0
        normal2athirdOuttxnum[addr] = 0
        normal2athirdOuttxnum1[addr] = 0
        normal2athirdOuttxnum2[addr] = 0
        normal2athirdOuttxnum3[addr] = 0
    for addr in addrlist:
        if addr in normal2athirdInItxnum1.keys():
            normal2athirdIntxnum1[addr] += normal2athirdInItxnum1[addr]
            normal2athirdIntxnum[addr] += normal2athirdInItxnum1[addr]
        if addr in normal2athirdInNtxnum1.keys():
            normal2athirdIntxnum1[addr] += normal2athirdInNtxnum1[addr]
            normal2athirdIntxnum[addr] += normal2athirdInNtxnum1[addr]
        if addr in normal2athirdInItxnum2.keys():
            normal2athirdIntxnum2[addr] += normal2athirdInItxnum2[addr]
            normal2athirdIntxnum[addr] += normal2athirdInItxnum2[addr]
        if addr in normal2athirdInNtxnum2.keys():
            normal2athirdIntxnum2[addr] += normal2athirdInNtxnum2[addr]
            normal2athirdIntxnum[addr] += normal2athirdInNtxnum2[addr]
        if addr in normal2athirdInItxnum3.keys():
            normal2athirdIntxnum3[addr] += normal2athirdInItxnum3[addr]
            normal2athirdIntxnum[addr] += normal2athirdInItxnum3[addr]
        if addr in normal2athirdInNtxnum3.keys():
            normal2athirdIntxnum3[addr] += normal2athirdInNtxnum3[addr]
            normal2athirdIntxnum[addr] += normal2athirdInNtxnum3[addr]

        if addr in normal2athirdOutItxnum1.keys():
            normal2athirdOuttxnum1[addr] += normal2athirdOutItxnum1[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutItxnum1[addr]
        if addr in normal2athirdOutNtxnum1.keys():
            normal2athirdOuttxnum1[addr] += normal2athirdOutNtxnum1[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutNtxnum1[addr]
        if addr in normal2athirdOutItxnum2.keys():
            normal2athirdOuttxnum2[addr] += normal2athirdOutItxnum2[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutItxnum2[addr]
        if addr in normal2athirdOutNtxnum2.keys():
            normal2athirdOuttxnum2[addr] += normal2athirdOutNtxnum2[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutNtxnum2[addr]
        if addr in normal2athirdOutItxnum3.keys():
            normal2athirdOuttxnum3[addr] += normal2athirdOutItxnum3[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutItxnum3[addr]
        if addr in normal2athirdOutNtxnum3.keys():
            normal2athirdOuttxnum3[addr] += normal2athirdOutNtxnum3[addr]
            normal2athirdOuttxnum[addr] += normal2athirdOutNtxnum3[addr]
    with open('normal2athirdIntxnum.txt', 'w') as f:
        print(normal2athirdIntxnum, file=f)
    with open('normal2athirdIntxnum1.txt', 'w') as f:
        print(normal2athirdIntxnum1, file=f)
    with open('normal2athirdIntxnum2.txt', 'w') as f:
        print(normal2athirdIntxnum2, file=f)
    with open('normal2athirdIntxnum3.txt', 'w') as f:
        print(normal2athirdIntxnum3, file=f)

    with open('normal2athirdOuttxnum.txt', 'w') as f:
        print(normal2athirdOuttxnum, file=f)
    with open('normal2athirdOuttxnum1.txt', 'w') as f:
        print(normal2athirdOuttxnum1, file=f)
    with open('normal2athirdOuttxnum2.txt', 'w') as f:
        print(normal2athirdOuttxnum2, file=f)
    with open('normal2athirdOuttxnum3.txt', 'w') as f:
        print(normal2athirdOuttxnum3, file=f)

def norAddrA3InEtxTime1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['to']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living[addr] = livingtime / 3 + start
    with open('normal2athirdtimeInEtx.txt', 'w') as f:
        print(addr2living, file=f)

def norAddrA3OutEtxTime1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2stamp = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2stamp[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:  # 统计每个地址的时间戳
            addr2stamp[row['from']].append(row['timeStamp'])
    for addr, time in addr2stamp.items():
        if len(time) > 0:  # 直接用时间戳计算
            start = time[0]
            end = time[-1]
            livingtime = end - start
            addr2living[addr] = livingtime / 3 + start
    with open('normal2athirdtimeOutEtx.txt', 'w') as f:
        print(addr2living, file=f)
def norAddrA3InEtxTx1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeInEtx.txt', 'r') as f:
        addr2end = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            end = addr2end[row['to']]# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            if row['timeStamp'] < end:
                addr2tx[row['to']].append(row['hash'])#每一个地址的满足对应条件的交易hash值列表
                addr2athirdtxnum[row['to']] += 1
    with open('normal2athirdInEtxnum.txt','w') as f:
        print(addr2athirdtxnum,file=f)
def norAddrA3OutEtxTx1():
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normal2athirdtimeOutEtx.txt', 'r') as f:
        addr2end = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv')  # 读取去重交易后的正常地址交易
    df = df.drop_duplicates()
    df = df.sort_values('timeStamp')
    addr2athirdtxnum = {}
    addr2tx = {}
    for addr in addrlist:  # 初始化用于统计的字典
        addr2athirdtxnum[addr] = 0
        addr2tx[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['from'],str) and row['from'] in addrlist:
            end = addr2end[row['to']]# 每一行地址的结束时间戳，有的欺诈地址可能只是from地址而不是to地址
            if row['timeStamp'] < end:
                addr2tx[row['from']].append(row['hash'])#每一个地址的满足对应条件的交易hash值列表
                addr2athirdtxnum[row['from']] += 1
    with open('normal2athirdOutEtxnum.txt','w') as f:
        print(addr2athirdtxnum,file=f)
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
    # with open('norAddrTx.txt','r') as f:
    #     list = literal_eval(f.read())
    #     print(len(list))
    # with open('norAddrTx.csv', 'r') as f:
    #     print(len(f.readlines()))
    # with open('normalAddrntx.csv', 'r') as f:
    #     print(len(f.readlines()))
    # with open('normalAddrntx2.csv', 'r') as f:
    #     print(len(f.readlines()))
    # chunker = pandas.read_csv("normalAddrntx2.csv", nrows=7500000)
    # print(type(chunker))
    # pd = pandas.read_csv('normalAddretx2.csv')
    # print(len(pd))
    with open('NormalAddr.txt','r') as f:
        list = literal_eval(f.read())
    print(len(list))
    # print(list.index('0x8909cc8d294544ca2c956550edbcb59ce4f2a9ad'))
    # for item in chunker:
    #     print(item)
    # with open('normalAddritx.csv', 'r') as f:
    #     print(len(f.readlines()))
    # url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
    # session = requests.Session()
    # results = literal_eval(session.get(url).text)['result']
    # print(len(results))
def mixAddrFig9():
    # with open('norAddrNFig9Intxs.txt') as f:
    #     txnum2addrnum1 = literal_eval(f.read())
    # with open('norAddrIFig9Intxs.txt') as f:
    #     txnum2addrnum2 = literal_eval(f.read())
    # zipped1 = zip(txnum2addrnum1.keys(), txnum2addrnum1.values())
    # sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    # result1 = zip(*sort_zipped1)
    # x1, y1 = [list(x) for x in result1]
    # fig, ax = plt.subplots()
    # cum = numpy.cumsum(y1)
    # percentage1 = cum / list(cum)[-1]
    # zipped2 = zip(txnum2addrnum2.keys(), txnum2addrnum2.values())
    # sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    # result2 = zip(*sort_zipped2)
    # x2, y2 = [list(x) for x in result2]
    # fig, ax = plt.subplots()
    # cum = numpy.cumsum(y2)
    # percentage2 = cum / list(cum)[-1]
    with open('scamAddrNFig9Intx.txt',encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    zipped3 = zip(txnum2addrnum3.keys(), txnum2addrnum3.values())
    sort_zipped3 = sorted(zipped3, key=lambda x: (x[0]))
    result3 = zip(*sort_zipped3)
    x3, y3 = [list(x) for x in result3]
    # fig, ax = plt.subplots()
    cum = numpy.cumsum(y3)
    percentage3 = cum / list(cum)[-1]
    with open('scamAddrIFig9Intx.txt',encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())
    zipped4 = zip(txnum2addrnum4.keys(), txnum2addrnum4.values())
    sort_zipped4 = sorted(zipped4, key=lambda x: (x[0]))
    result4 = zip(*sort_zipped4)
    x4, y4 = [list(x) for x in result4]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y4)
    percentage4 = cum / list(cum)[-1]
    # line1 = ax.plot(x1, percentage1)
    # line2 = ax.plot(x2, percentage2)
    line3 = ax.plot(x3, percentage3, label='In txs Of scam addresses',color='black')
    line4 = ax.plot(x4, percentage4, label='Out txs Of scam addresses',linestyle="--",color='black')
    ax.set_xlabel('# of Transactions (Txs)')
    ax.set_ylabel('CDF of Addresses')
    plt.xscale('log')
    plt.legend()
    plt.title('test')
    plt.show()
# def scamLive():#living time
#     with open('addr.txt', 'r', encoding='utf-8') as f:
#         addrlist = literal_eval(f.read())
#     df1 = pandas.read_csv('ntx1.csv')
#     df2 = pandas.read_csv('ntx2.csv')
#     df3 = pandas.read_csv('ntx3.csv')
#     df4 = pandas.read_csv('ntx4.csv')
#     df5 = pandas.read_csv('itx1.csv')
#     df6 = pandas.read_csv('itx2.csv')
#     df7 = pandas.read_csv('itx3.csv')
#     df8 = pandas.read_csv('itx4.csv')
#     df9 = pandas.read_csv('bntx1.csv')
#     df10 = pandas.read_csv('bitx1.csv')
#     frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]
#     df = pandas.concat(frames)
#     df = df.drop_duplicates()  # 去重
#     df = df.sort_values('timeStamp')
#     addr2day = {}  # 地址到交易时间戳的字典
#     addr2living = {}
#     for addr in addrlist:
#         addr2day[addr] = []
#     for index, row in df.iterrows():
#         if isinstance(row['to'],str) and row['to'] in addrlist:
#             addr2day[row['to']].append(row['timeStamp'])
#     for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
#         time.sort()
#     for addr, time in addr2day.items():
#         if len(time) > 0:
#             start = datetime.datetime.fromtimestamp(time[0])
#             end = datetime.datetime.fromtimestamp(time[-1])
#             addr2living[addr] = (end - start).days
#     print(addr2living)
#     livingtime2num = {}
#     for addr,livingtime in addr2living.items():
#         livingtime2num[livingtime] = livingtime2num.get(livingtime,0) + 1
#     print(livingtime2num)
#     zipped = zip(livingtime2num.keys(), livingtime2num.values())
#     sort_zipped = sorted(zipped, key=lambda x: (x[0]))
#     result = zip(*sort_zipped)
#     x, y = [list(x) for x in result]
#     fig, ax = plt.subplots()
#     cum = numpy.cumsum(y)
#     percentage = cum / list(cum)[-1]
#     line = ax.plot(x, percentage)
#     x_major_locator = MultipleLocator(250)
#     ax.xaxis.set_major_locator(x_major_locator)
#     plt.show()
def scamLive():#living time
    with open('addr.txt', 'r', encoding='utf-8') as f:
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
    df11 = pandas.read_csv('etx1.csv')
    df12 = pandas.read_csv('etx2.csv')
    df13 = pandas.read_csv('etx3.csv')
    df14 = pandas.read_csv('etx4.csv')
    df15 = pandas.read_csv('betx1.csv')
    frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15]
    df = pandas.concat(frames)
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2day = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2day[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            addr2day[row['to']].append(row['timeStamp'])
    for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
        time.sort()
    for addr, time in addr2day.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days
    livingtime2num = {}
    for addr,livingtime in addr2living.items():
        livingtime2num[livingtime] = livingtime2num.get(livingtime,0) + 1
    print(livingtime2num)
    with open('scamLive1.txt','w') as f:
        print(addr2living,file=f)
    with open('scamLive2.txt','w') as f:
        print(livingtime2num,file=f)
    return
    zipped = zip(livingtime2num.keys(), livingtime2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    x_major_locator = MultipleLocator(250)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()
def normalLive1():#living time截取正常地址的前三分之一进行living time的统计
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddrntx2.csv').iloc[0:5000000]  # hash,from,to,value
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2day = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2day[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            addr2day[row['to']].append(row['timeStamp'])
    for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
        time.sort()
    for addr, time in addr2day.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days
    print(addr2living)
    livingtime2num = {}
    for addr,livingtime in addr2living.items():
        livingtime2num[livingtime] = livingtime2num.get(livingtime,0) + 1
    print(livingtime2num)
    with open('normalLiven1.txt','w') as f:
        print(addr2living,file=f)
    with open('normalLiven2.txt','w') as f:
        print(livingtime2num,file=f)
    zipped = zip(livingtime2num.keys(), livingtime2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    x_major_locator = MultipleLocator(250)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()
def normalLive2():#living time
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddritx2.csv')  # hash,from,to,value
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2day = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2day[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            addr2day[row['to']].append(row['timeStamp'])
    for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
        time.sort()
    for addr, time in addr2day.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days
    # with open('normalLivei1.txt','w') as f:
    #     print(addr2living,file=f)
    livingtime2num = {}
    for addr,livingtime in addr2living.items():
        livingtime2num[livingtime] = livingtime2num.get(livingtime,0) + 1
    print(livingtime2num)
    # with open('normalLivei2.txt','w') as f:
    #     print(livingtime2num,file=f)
    zipped = zip(livingtime2num.keys(), livingtime2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    x_major_locator = MultipleLocator(250)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()
def normalLive3():#living time
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    df = pandas.read_csv('normalAddretx2.csv')  # hash,from,to,value
    df = df.drop_duplicates()  # 去重
    df = df.sort_values('timeStamp')
    addr2day = {}  # 地址到交易时间戳的字典
    addr2living = {}
    for addr in addrlist:
        addr2day[addr] = []
    for index, row in df.iterrows():
        if isinstance(row['to'],str) and row['to'] in addrlist:
            addr2day[row['to']].append(row['timeStamp'])
    for addr, time in addr2day.items():  # 将时间列表排序，计算时间差
        time.sort()
    for addr, time in addr2day.items():
        if len(time) > 0:
            start = datetime.datetime.fromtimestamp(time[0])
            end = datetime.datetime.fromtimestamp(time[-1])
            addr2living[addr] = (end - start).days
    print(addr2living)
    livingtime2num = {}
    for addr,livingtime in addr2living.items():
        livingtime2num[livingtime] = livingtime2num.get(livingtime,0) + 1
    print(livingtime2num)
    with open('normalLivee1.txt','w') as f:
        print(addr2living,file=f)
    with open('normalLivee2.txt','w') as f:
        print(livingtime2num,file=f)
    zipped = zip(livingtime2num.keys(), livingtime2num.values())
    sort_zipped = sorted(zipped, key=lambda x: (x[0]))
    result = zip(*sort_zipped)
    x, y = [list(x) for x in result]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x, percentage)
    x_major_locator = MultipleLocator(250)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.show()
def mixnormalLive():
    with open('normalLiven1.txt','r') as f:
        addr2living1 = literal_eval(f.read())
    with open('normalLivei1.txt','r') as f:
        addr2living2 = literal_eval(f.read())
    with open('normalLivee1.txt','r') as f:
        addr2living3 = literal_eval(f.read())
    #应该重新统计，有可能某个地址同时有三种交易，但是要取最长的living time，取出地址列表
    #创建一个地址到living time的总时间字典
    #因为normal tx取的是前三分之一的交易，所以地址列表应该是全部正常地址列表的子集
    addr2living = {}
    addrlist = list(addr2living1.keys()) + list(addr2living2.keys()) + list(addr2living3.keys())
    for addr in addrlist:
        addr2living[addr] = []
    for addr in addrlist:
        if addr in addr2living1.keys():
            addr2living[addr].append(addr2living1[addr])
        if addr in addr2living2.keys():
            addr2living[addr].append(addr2living2[addr])
        if addr in addr2living3.keys():
            addr2living[addr].append(addr2living3[addr])
    for addr,livinglist in addr2living.items():
        addr2living[addr] = sorted(addr2living[addr])

    livingtime2num = {}
    for addr,livingtime in addr2living.items():
        livingtime2num[livingtime[-1]] = livingtime2num.get(livingtime[-1],0) + 1
    with open('normalLive.txt','w') as f:
        print(livingtime2num,file=f)
    return
def mixLive():
    with open('normalLive.txt','r') as f:
        livingtime2num1 = literal_eval(f.read())
    with open('scamLive2.txt','r') as f:
        livingtime2num2 = literal_eval(f.read())
    zipped1 = zip(livingtime2num1.keys(), livingtime2num1.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    zipped2 = zip(livingtime2num2.keys(), livingtime2num2.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]

    fig, ax = plt.subplots()
    cum1 = numpy.cumsum(y1)
    percentage1 = cum1 / list(cum1)[-1]
    line1 = ax.plot(x1, percentage1, label="living time of normal address", color="black", linestyle="--")
    cum2 = numpy.cumsum(y2)
    percentage2 = cum2 / list(cum2)[-1]
    line2 = ax.plot(x2, percentage2, label="living time of scam address", color="black")

    x_major_locator = MultipleLocator(250)
    ax.xaxis.set_major_locator(x_major_locator)
    plt.title('living time of addresses(Days)')
    plt.legend()
    ax.set_ylabel('CDF of Addresses')
    ax.set_xlim(1)
    plt.savefig('livingtime.jpg')
    plt.show()
def scamTxDedupN():
    df1 = pandas.read_csv('ntx1.csv')
    df2 = pandas.read_csv('ntx2.csv')
    df3 = pandas.read_csv('ntx3.csv')
    df4 = pandas.read_csv('ntx4.csv')
    df5 = pandas.read_csv('ntx5.csv')
    df6 = pandas.read_csv('bntx1.csv')
    frames = [df1, df2, df3, df4, df5, df6]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df['hash'] = df['hash'].str.lower()#对哈希值进行全小写处理，然后去重，有可能有小写后相同的地址
    df = df.drop_duplicates(subset=['hash'], keep='first')
    df.to_csv('ntx.csv')
def scamTxDedupI():
    df1 = pandas.read_csv('itx1.csv')
    df2 = pandas.read_csv('itx2.csv')
    df3 = pandas.read_csv('itx3.csv')
    df4 = pandas.read_csv('itx4.csv')
    # df5 = pandas.read_csv('itx5.csv')
    df6 = pandas.read_csv('bitx1.csv')
    frames = [df1, df2, df3, df4, df6]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df['hash'] = df['hash'].str.lower()
    df = df.drop_duplicates(subset=['hash'], keep='first')
    df.to_csv('itx.csv')
def scamTxDedupE():
    df1 = pandas.read_csv('etx1.csv')
    df2 = pandas.read_csv('etx2.csv')
    df3 = pandas.read_csv('etx3.csv')
    df4 = pandas.read_csv('etx4.csv')
    # df5 = pandas.read_csv('etx5.csv')
    df6 = pandas.read_csv('betx1.csv')
    frames = [df1, df2, df3, df4, df6]
    df = pandas.concat(frames)
    df = df.drop_duplicates()
    df['hash'] = df['hash'].str.lower()
    df = df.drop_duplicates(subset=['hash'], keep='first')
    df.to_csv('etx.csv')
def txdedupN():
    df = pandas.read_csv('normalAddrntx.csv')
    df['hash'] = df['hash'].str.lower()#根据小写哈希值去重
    df = df.drop_duplicates(subset=['hash'],keep='first')
    for index, row in df.iterrows():
        if isinstance(row['from'],str):
            row['from'] = row['from'].lower()
        if isinstance(row['to'],str):
            row['to'] = row['to'].lower()
    df.to_csv('normalAddrntx2.csv')
def txdedupI():
    df = pandas.read_csv('normalAddritx.csv')
    df['hash'] = df['hash'].str.lower()
    df = df.drop_duplicates(subset=['hash'],keep='first')
    for index, row in df.iterrows():
        if isinstance(row['from'],str):
            row['from'] = row['from'].lower()
        if isinstance(row['to'],str):
            row['to'] = row['to'].lower()
    df.to_csv('normalAddritx2.csv')
def txdedupE():
    df = pandas.read_csv('normalAddretx.csv')
    df['hash'] = df['hash'].str.lower()
    df = df.drop_duplicates(subset=['hash'],keep='first')
    for index, row in df.iterrows():
        if isinstance(row['from'], str):
            row['from'] = row['from'].lower()
        if isinstance(row['to'], str):
            row['to'] = row['to'].lower()
    df.to_csv('normalAddretx2.csv')
def bloxyaddrtax():
    #怎么处理bloxy的地址标记，从备注中获取，但是备注中有可能有多种欺诈，以etherscan的为主，因为bloxy的很少
    with open('bloxyhack.txt', 'r', encoding='utf-8') as f:
        dict1 = literal_eval(f.read())
    with open('bloxyscam.txt', 'r', encoding='utf-8') as f:
        dict2 = literal_eval(f.read())
    with open('bloxymalware.txt', 'r', encoding='utf-8') as f:
        dict3 = literal_eval(f.read())
    mydict = {}
    mydict.update(dict1)
    mydict.update(dict2)
    mydict.update(dict3)
    # print(len(mydict))
    hacktype = ['Malware', 'ICO', 'Trust-Trading', 'Trust Trading', 'Phish', 'Hack']
    notType = ['Hacking', 'HackToken', 'HackDao', 'HackerGold', 'Hacken', 'HackerSpaceBarneysToken', 'HackerToken', 'Gitcoin', 'VitaluckHack']
    wrongaddr = ['0x4b2b60175b6e070e456816fda2b01a72343d66ca', '0x451ab68bbec364b8a9e4403741d311c54e3907f6', '0x9e6b2b11542f2bc52f3029077ace37e8fd838d7f', '0xdcf59ee4803931a376a0fb6244036e49ebc7dd61', '0x433d84a1c0b650eac4fc1fb570798cf655ce24c0', '0xcd3e727275bc2f511822dc9a26bd7b0bbf161784', '0x2563c25db9d2fb94f65e7632544eb057fc3dfcf0', '0x2559f0dd36179c230443d2c3846435e52eb2b2df', '0x14f37b574242d366558db61f3335289a5035c506', '0x06044b5359d8df7886366c22c61c7ecd29becac7', '0xa62bdee2f277c2e2c0f46cba96879b263796ee1c', '0x05fb86775fd5c16290f1e838f5caaa7342bd9a63', '0xf6fe061efa2a8e15936696baf5e8cba8c3f3485b', '0x5c430fa24f782cf8156ca97208c42127b17b0494', '0x1f2e2293efa2ebd9c09211569f3d7758f0463189']
    typenum = {}
    typelist = {}
    addrlist = []
    #提前删除错误的地址
    for mytype in hacktype:
        typenum[mytype] = 0
        typelist[mytype] = []
    for addr in wrongaddr:
        if str('/tx/' + addr) in mydict.keys():
            mydict.pop(str('/tx/' + addr))
        elif str('/address/' + addr) in mydict.keys():
            mydict.pop(str('/address/' + addr))
    for url,note in mydict.items():
        note = note.split(",")
        exitflag = False
        for mytype in hacktype:
            for tip in note:
                if mytype.lower() in tip.lower():
                    exitflag = True
                    if url.startswith('/address'):
                        addr = url[9:]
                    elif url.startswith('/tx'):
                        addr = url[4:]
                    if len(addr) == 42 and addr not in addrlist:
                        typenum[mytype] += 1
                        addr = addr.lower()
                        typelist[mytype].append(addr)
                        addrlist.append(addr)
                    break
            if exitflag:
                break
    addrlist = list(set(addrlist))
    sum = 0
    for type,num in typenum.items():
        sum += num
    for type,list1 in typelist.items():
        list1 = list(set(list1))
    # print(sum)
    # print(len(addrlist))
    # print(typenum)
    return addrlist,typenum,typelist#bloxy的地址列表，类型统计，类型地址映射
def etherscanAddrTax():
    addrlist, typenum, typelist = bloxyaddrtax()
    with open('bitpoint.txt', 'r') as f:
        list1 = literal_eval(f.read())
        list1 = [addr.lower() for addr in list1]
        list1 = list(set(list1))
    with open('cryptopia.txt', 'r') as f:
        list2 = literal_eval(f.read())
        list2 = [addr.lower() for addr in list2]
        list2 = list(set(list2))
    with open('etherdelta.txt', 'r') as f:
        list3 = literal_eval(f.read())
        list3 = [addr.lower() for addr in list3]
        list3 = list(set(list3))
    with open('LendfMe.txt', 'r') as f:
        list4 = literal_eval(f.read())
        list4 = [addr.lower() for addr in list4]
        list4 = list(set(list4))
    with open('phishaddr.txt', 'r') as f:
        list5 = literal_eval(f.read())
        list5 = [addr.lower() for addr in list5]
        list5 = list(set(list5))#在etherscan的phish类
        # typenum['Phish']  += len(list5)#只有一个文件是phish类的，把这个文件中的bloxy地址去掉即可，另外的文件中专属于etherscan的地址全部统计到hack类中
    with open('upbit.txt', 'r') as f:
        list6 = literal_eval(f.read())
        list6 = [addr.lower() for addr in list6]
        list6 = list(set(list6))
    with open('scam.txt', 'r') as f:
        list7 = literal_eval(f.read())
        list7 = [addr.lower() for addr in list7]
        list7 = list(set(list7))
    with open('db.txt', 'r') as f:
        list8 = literal_eval(f.read())
        list8 = [addr.lower() for addr in list8]
        list8 = list(set(list8))
    with open('bloxyAddr.txt', 'r') as f:#在bloxy中的所有地址
        list9 = literal_eval(f.read())
        list9 = [addr.lower() for addr in list9]
        list9 = list(set(list9))#在bloxy的所有地址
    #已经分好类的地址：在bloxy中的所有地址；未分好类的地址：在scan中而不在bloxy中的地址
    scanlist = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8))#scan中的地址数
    print(len(scanlist))#6429
    hacklist = list(set(list1 + list2 + list3 + list4 + list6 + list7 + list8))#etherscan去重后的hack类地址列表
    phishlist = list5
    bloxylist = list9
    hackandphish = [addr for addr in phishlist if addr in hacklist]
    print(len(hackandphish))#2284
    onlyscan = [addr for addr in scanlist if addr not in bloxylist]
    print(len(onlyscan))#2434
    # mylist1 = [i for i in list5 if i not in list9 and i not in hacklist]  # 在etherscan不在bloxy而且不在hack类的Phish类的地址列表
    # print(len(list9))
    # print(len(addrlist))
    phishnothack = []
    for addr in onlyscan:
        if addr not in hacklist:#phish类要去除bloxy已经分好类的，并且不能是hack类
            phishnothack.append(addr)
    phishnothack = list(set(phishnothack))#去重
    typelist['Phish'] = typelist['Phish'] + phishnothack
    typelist['Phish'] = list(set(typelist['Phish']))#地址去重
    typenum['Phish'] += len(phishnothack)#分类计数增加
    # mylist2 = [i for i in hacklist if i not in list9 and i not in list5]#在etherscan不在bloxy而且不在phish类的Hack类的地址列表
    mylist2 = []
    for addr in onlyscan:
        if addr in hacklist:#hack类要去除bloxy已经分好类的，并且不能是phish类
            mylist2.append(addr)
    mylist2 = list(set(mylist2))#去重
    typelist['Hack'] = typelist['Hack'] + mylist2
    typelist['Hack'] = list(set(typelist['Hack']))#地址去重
    typenum['Hack'] += len(mylist2)#分类计数增加
    mylist3 = []
    sum = 0#分好类的地址数
    for addr in typelist.values():#mylist3是已经分好类的地址列表
        sum += len(addr)
        mylist3 += addr
    sum2 = 0#分好类的地址数
    for num in typenum.values():#6449
        sum2 += num
    mylist3 = list(set(mylist3))#去重
    print("sum："+str(sum))#6434
    print("sum2："+str(sum2))#6449
    print(len(mylist3))#6449
    alladdr = list(set(list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9))
    print(len(alladdr))#6434
    mylist5 = [addr for addr in mylist3 if addr not in alladdr]
    # print(mylist5)
    print(typenum)
    with open('addr.txt', 'r') as f:
        list10 = literal_eval(f.read())
        print(len(list10))#6434
    mylist4 = [i for i in alladdr if i not in list10]#漏掉的欺诈地址
    # print(mylist4)
    # print(typelist)
    with open('typelist.txt','w') as f:
        print(typelist,file=f)
    return typelist
# {'Malware': 2, 'ICO': 13, 'Trust-Trading': 1290, 'Trust Trading': 1, 'Phish': 3185, 'Hack': 1943}
# 不是欺诈地址的地址：
#0x1f2e2293efa2ebd9c09211569f3d7758f0463189
#0x14f37b574242d366558db61f3335289a5035c506
#['0x4b2b60175b6e070e456816fda2b01a72343d66ca', '0x451ab68bbec364b8a9e4403741d311c54e3907f6',
# '0x9e6b2b11542f2bc52f3029077ace37e8fd838d7f', '0xdcf59ee4803931a376a0fb6244036e49ebc7dd61',
# '0x433d84a1c0b650eac4fc1fb570798cf655ce24c0', '0xcd3e727275bc2f511822dc9a26bd7b0bbf161784',
# '0x2563c25db9d2fb94f65e7632544eb057fc3dfcf0', '0x2559f0dd36179c230443d2c3846435e52eb2b2df',
# '0x14f37b574242d366558db61f3335289a5035c506', '0x06044b5359d8df7886366c22c61c7ecd29becac7',
# '0xa62bdee2f277c2e2c0f46cba96879b263796ee1c', '0x05fb86775fd5c16290f1e838f5caaa7342bd9a63',
# '0xf6fe061efa2a8e15936696baf5e8cba8c3f3485b', '0x5c430fa24f782cf8156ca97208c42127b17b0494', '0x1f2e2293efa2ebd9c09211569f3d7758f0463189']
def txtax():
    with open('typelist.txt','r') as f:
        typelist = literal_eval(f.read())
    with open('addr.txt','r') as f:
        scamaddr = literal_eval(f.read())
    txtypenum = {}
    addrtxnum = {}#记录每个种类的各个地址的各种交易数量
    for addr in scamaddr:
        addrtxnum[addr] = [0,0,0]
    hacktype = ['Malware', 'ICO', 'Trust-Trading', 'Trust Trading', 'Phish', 'Hack']
    session = requests.Session()
    for mytype in hacktype:
        txtypenum[mytype] = [0,0,0]
    num = 0
    for typename,addrlist in typelist.items():
        for addr in addrlist:
            nurl = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            iurl = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + addr + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            eurl = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + addr + "&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=" + apikey
            result1 = literal_eval(session.get(nurl).text)['result']
            result2 = literal_eval(session.get(iurl).text)['result']
            result3 = literal_eval(session.get(eurl).text)['result']
            len1 = len(result1)
            len2 = len(result2)
            len3 = len(result3)
            txtypenum[typename][0] += len1
            txtypenum[typename][1] += len2
            txtypenum[typename][2] += len3
            addrtxnum[addr][0] += len1
            addrtxnum[addr][0] += len2
            addrtxnum[addr][0] += len3
            num += 1
            print(num)
    with open('txtypenum.txt','w') as f:
        print(txtypenum,file=f)
def filterAddr1():
    with open('nor2numNOuttx1.txt','r',encoding='utf-8') as f:
        addr2tx2 = literal_eval(f.read())
    with open('nor2numNOuttx2.txt','r',encoding='utf-8') as f:
        addr2tx3 = literal_eval(f.read())
    with open('nor2numNOuttx3.txt','r',encoding='utf-8') as f:
        addr2tx4 = literal_eval(f.read())
    addr2tx = addr2tx2 + addr2tx3 + addr2tx4
    addrlist = []
    for addr,tx in addr2tx.items():
        if tx > 20000:
            addrlist.append(addr)
    for addr in addrlist:
        addr2tx.pop(addr)
    with open('filterAddr.txt','w',encoding='utf-8') as f:
        print(list(addr2tx.keys()),file=f)
def filterAddr2():
    with open('nor2numNIntx.txt','r',encoding='utf-8') as f:
        addr2tx = literal_eval(f.read())
    addrlist = []
    for addr,tx in addr2tx.items():
        if tx > 20000:
            addrlist.append(addr)
    for addr in addrlist:
        addr2tx.pop(addr)
    with open('filterAddr.txt','w',encoding='utf-8') as f:
        print(list(addr2tx.keys()),file=f)
def scamAvgIncomeOutcome():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('scamIncome.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('scamOutcome.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('scamInTx.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('scamOutTx.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        addr2avgincome[addr] = 0
        addr2avgoutcome[addr] = 0
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] != 0:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] != 0:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    print(addr2avgincome)
    print(addr2avgoutcome)
    with open('scamAvgIncome.txt','w') as f:
        print(addr2avgincome,file=f)
    with open('scamAvgOutcome.txt','w') as f:
        print(addr2avgoutcome,file=f)

def norItxAvgIOcome():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeItx1.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeItx1.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numIIntx1.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numIIntx1.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numIOuttx.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalItxAvgIncome.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalItxAvgOutcome.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def norNtxAvgIOcome1():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx1.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeNtx1.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numNIntx1.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numNOuttx1.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgoutcome[addr] = 0
            else:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalNtxAvgIncome1.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalNtxAvgOutcome1.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def norNtxAvgIOcome2():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx2.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeNtx2.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numNIntx2.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numNOuttx2.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalNtxAvgIncome2.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalNtxAvgOutcome2.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def norNtxAvgIOcome3():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx3.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeNtx3.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numNIntx3.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numNOuttx3.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgoutcome[addr] = 0
            else:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalNtxAvgIncome3.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalNtxAvgOutcome3.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def norNtxAvgIOcome4():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx4.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeNtx4.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numNIntx4.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numNOuttx2.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgoutcome[addr] = 0
            else:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalNtxAvgIncome4.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalNtxAvgOutcome4.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def norNtxAvgIOcome5():
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx5.txt','r',encoding='utf-8') as f:
        addr2income = literal_eval(f.read())
    with open('normalOutcomeNtx5.txt','r',encoding='utf-8') as f:
        addr2outcome = literal_eval(f.read())
    with open('nor2numNIntx5.txt','r') as f:
        addr2Intxnum = literal_eval(f.read())
    with open('nor2numNOuttx5.txt','r',encoding='utf-8') as f:
        addr2OutTxnum = literal_eval(f.read())
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        if addr in addr2Intxnum.keys() and addr in addr2income.keys():
            if addr2Intxnum[addr] == 0:
                addr2avgincome[addr] = 0
            else:
                addr2avgincome[addr] = addr2income[addr] / addr2Intxnum[addr]
    for addr in addrlist:
        if addr in addr2OutTxnum.keys() and addr in addr2outcome.keys():
            if addr2OutTxnum[addr] == 0:
                addr2avgoutcome[addr] = 0
            else:
                addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    with open('normalNtxAvgIncome5.txt', 'w') as f:
        print(addr2avgincome, file=f)
    with open('normalNtxAvgOutcome5.txt', 'w') as f:
        print(addr2avgoutcome, file=f)
def mixnormalNtxAvgIOcome():
    # with open('normalNtxAvgIncome1.txt', 'r') as f:
    #     addr2avgincome1 = literal_eval(f.read())
    # with open('normalNtxAvgIncome2.txt', 'r') as f:
    #     addr2avgincome2 = literal_eval(f.read())
    # with open('normalNtxAvgIncome3.txt', 'r') as f:
    #     addr2avgincome3 = literal_eval(f.read())
    # with open('normalNtxAvgIncome4.txt', 'r') as f:
    #     addr2avgincome4 = literal_eval(f.read())
    # with open('normalNtxAvgIncome5.txt', 'r') as f:
    #     addr2avgincome5 = literal_eval(f.read())
    # with open('normalNtxAvgOutcome1.txt', 'r') as f:
    #     addr2avgoutcome1 = literal_eval(f.read())
    # with open('normalNtxAvgOutcome2.txt', 'r') as f:
    #     addr2avgoutcome2 = literal_eval(f.read())
    # with open('normalNtxAvgOutcome3.txt', 'r') as f:
    #     addr2avgoutcome3 = literal_eval(f.read())
    # with open('normalNtxAvgOutcome4.txt', 'r') as f:
    #     addr2avgoutcome4 = literal_eval(f.read())
    # with open('normalNtxAvgOutcome5.txt', 'r') as f:
    #     addr2avgoutcome5 = literal_eval(f.read())
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    # addr2avgincome = {}
    # addr2avgoutcome = {}
    # for addr in addrlist:
    #     addr2avgincome[addr] = 0
    #     addr2avgoutcome[addr] = 0
    # for addr in addrlist:#将每个文件里面的平均值相加得到总的平均值
    #     if addr in addr2avgincome1.keys():
    #         addr2avgincome[addr] = addr2avgincome[addr] + addr2avgincome1[addr]
    #     if addr in addr2avgincome2.keys():
    #         addr2avgincome[addr] = addr2avgincome[addr] + addr2avgincome2[addr]
    #     if addr in addr2avgincome3.keys():
    #         addr2avgincome[addr] = addr2avgincome[addr] + addr2avgincome3[addr]
    #     if addr in addr2avgincome4.keys():
    #         addr2avgincome[addr] = addr2avgincome[addr] + addr2avgincome4[addr]
    #     if addr in addr2avgincome5.keys():
    #         addr2avgincome[addr] = addr2avgincome[addr] + addr2avgincome5[addr]
    #
    #     if addr in addr2avgoutcome1.keys():
    #         addr2avgoutcome[addr] = addr2avgoutcome[addr] + addr2avgoutcome1[addr]
    #     if addr in addr2avgoutcome2.keys():
    #         addr2avgoutcome[addr] = addr2avgoutcome[addr] + addr2avgoutcome2[addr]
    #     if addr in addr2avgoutcome3.keys():
    #         addr2avgoutcome[addr] = addr2avgoutcome[addr] + addr2avgoutcome3[addr]
    #     if addr in addr2avgoutcome4.keys():
    #         addr2avgoutcome[addr] = addr2avgoutcome[addr] + addr2avgoutcome4[addr]
    #     if addr in addr2avgoutcome5.keys():
    #         addr2avgoutcome[addr] = addr2avgoutcome[addr] + addr2avgoutcome5[addr]
    # with open('normalNtxAvgIncome.txt','w') as f:
    #     print(addr2avgincome,file=f)
    # with open('normalNtxAvgOutcome.txt','w') as f:
    #     print(addr2avgoutcome,file=f)
    #
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    with open('normalIncomeNtx1.txt','r',encoding='utf-8') as f:
        addr2income1 = literal_eval(f.read())
    with open('normalOutcomeNtx1.txt','r',encoding='utf-8') as f:
        addr2outcome1 = literal_eval(f.read())
    with open('nor2numNIntx1.txt','r') as f:
        addr2InTxnum1 = literal_eval(f.read())
    with open('nor2numNOuttx1.txt','r',encoding='utf-8') as f:
        addr2OutTxnum1 = literal_eval(f.read())

    with open('normalIncomeNtx2.txt','r',encoding='utf-8') as f:
        addr2income2 = literal_eval(f.read())
    with open('normalOutcomeNtx2.txt','r',encoding='utf-8') as f:
        addr2outcome2 = literal_eval(f.read())
    with open('nor2numNIntx2.txt','r') as f:
        addr2InTxnum2 = literal_eval(f.read())
    with open('nor2numNOuttx2.txt','r',encoding='utf-8') as f:
        addr2OutTxnum2 = literal_eval(f.read())

    with open('normalIncomeNtx3.txt','r',encoding='utf-8') as f:
        addr2income3 = literal_eval(f.read())
    with open('normalOutcomeNtx3.txt','r',encoding='utf-8') as f:
        addr2outcome3 = literal_eval(f.read())
    with open('nor2numNIntx3.txt','r') as f:
        addr2InTxnum3 = literal_eval(f.read())
    with open('nor2numNOuttx3.txt','r',encoding='utf-8') as f:
        addr2OutTxnum3 = literal_eval(f.read())

    with open('normalIncomeNtx4.txt','r',encoding='utf-8') as f:
        addr2income4 = literal_eval(f.read())
    with open('normalOutcomeNtx4.txt','r',encoding='utf-8') as f:
        addr2outcome4 = literal_eval(f.read())
    with open('nor2numNIntx4.txt','r') as f:
        addr2InTxnum4 = literal_eval(f.read())
    with open('nor2numNOuttx4.txt','r',encoding='utf-8') as f:
        addr2OutTxnum4 = literal_eval(f.read())

    with open('normalIncomeNtx5.txt','r',encoding='utf-8') as f:
        addr2income5 = literal_eval(f.read())
    with open('normalOutcomeNtx5.txt','r',encoding='utf-8') as f:
        addr2outcome5 = literal_eval(f.read())
    with open('nor2numNIntx5.txt','r') as f:
        addr2InTxnum5 = literal_eval(f.read())
    with open('nor2numNOuttx5.txt','r',encoding='utf-8') as f:
        addr2OutTxnum5 = literal_eval(f.read())
    addr2income = {}
    addr2outcome = {}
    addr2InTxnum = {}
    addr2OutTxnum = {}
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        addr2income[addr] = 0
        addr2outcome[addr] = 0
        addr2InTxnum[addr] = 0
        addr2OutTxnum[addr] = 0
        addr2avgincome[addr] = 0
        addr2avgoutcome[addr] = 0
    for addr in addrlist:
        if addr in addr2income1.keys():
            addr2income[addr] += addr2income1[addr]
        if addr in addr2income2.keys():
            addr2income[addr] += addr2income2[addr]
        if addr in addr2income3.keys():
            addr2income[addr] += addr2income3[addr]
        if addr in addr2income4.keys():
            addr2income[addr] += addr2income4[addr]
        if addr in addr2income5.keys():
            addr2income[addr] += addr2income5[addr]

        if addr in addr2outcome1.keys():
            addr2outcome[addr] += addr2outcome1[addr]
        if addr in addr2outcome2.keys():
            addr2outcome[addr] += addr2outcome2[addr]
        if addr in addr2outcome3.keys():
            addr2outcome[addr] += addr2outcome3[addr]
        if addr in addr2outcome4.keys():
            addr2outcome[addr] += addr2outcome4[addr]
        if addr in addr2outcome5.keys():
            addr2outcome[addr] += addr2outcome5[addr]

        if addr in addr2InTxnum1.keys():
            addr2InTxnum[addr] += addr2InTxnum1[addr]
        if addr in addr2InTxnum2.keys():
            addr2InTxnum[addr] += addr2InTxnum2[addr]
        if addr in addr2InTxnum3.keys():
            addr2InTxnum[addr] += addr2InTxnum3[addr]
        if addr in addr2InTxnum4.keys():
            addr2InTxnum[addr] += addr2InTxnum4[addr]
        if addr in addr2InTxnum5.keys():
            addr2InTxnum[addr] += addr2InTxnum[addr]

        if addr in addr2OutTxnum1.keys():
            addr2OutTxnum[addr] += addr2OutTxnum1[addr]
        if addr in addr2OutTxnum2.keys():
            addr2OutTxnum[addr] += addr2OutTxnum2[addr]
        if addr in addr2OutTxnum3.keys():
            addr2OutTxnum[addr] += addr2OutTxnum3[addr]
        if addr in addr2OutTxnum4.keys():
            addr2OutTxnum[addr] += addr2OutTxnum4[addr]
        if addr in addr2OutTxnum5.keys():
            addr2OutTxnum[addr] += addr2OutTxnum5[addr]
    with open('normalIncomeNtx.txt','w') as f:
        print(addr2income,file=f)
    with open('normalOutcomeNtx.txt','w') as f:
        print(addr2outcome,file=f)
    with open('nor2numNIntx.txt','w') as f:
        print(addr2InTxnum,file=f)
    with open('nor2numNOuttx.txt','w') as f:
        print(addr2OutTxnum,file=f)
    return
    for addr in addrlist:
        if addr2InTxnum[addr] != 0:
            addr2avgincome[addr] = addr2income[addr] / addr2InTxnum[addr]
        if addr2OutTxnum[addr] != 0:
            addr2outcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    print(addr2avgincome)



def mixnormalAvgIOcome():
    with open('normalIncomeNtx.txt','r') as f:
        addr2income1 = literal_eval(f.read())
    with open('normalOutcomeNtx.txt','r') as f:
        addr2outcome1 = literal_eval(f.read())
    with open('nor2numNIntx.txt','r') as f:
        addr2intx1 = literal_eval(f.read())
    with open('nor2numNOuttx.txt','r') as f:
        addr2outtx1 = literal_eval(f.read())
    with open('normalIncomeItx1.txt','r') as f:
        addr2income2 = literal_eval(f.read())
    with open('normalOutcomeItx1.txt','r') as f:
        addr2outcome2 = literal_eval(f.read())
    with open('nor2numIIntx1.txt','r') as f:
        addr2intx2 = literal_eval(f.read())
    with open('nor2numIOuttx.txt','r') as f:
        addr2outtx2 = literal_eval(f.read())
    with open('normalAddr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addr2income = {}
    addr2outcome = {}
    addr2InTxnum = {}
    addr2OutTxnum = {}
    addr2avgincome = {}
    addr2avgoutcome = {}
    for addr in addrlist:
        addr2income[addr] = 0
        addr2outcome[addr] = 0
        addr2InTxnum[addr] = 0
        addr2OutTxnum[addr] = 0
        addr2avgincome[addr] = 0
        addr2avgoutcome[addr] = 0
    for addr in addrlist:
        if addr in addr2income1.keys():
            addr2income[addr] += addr2income1[addr]
        if addr in addr2income2.keys():
            addr2income[addr] += addr2income2[addr]
        if addr in addr2outcome1.keys():
            addr2outcome[addr] += addr2outcome1[addr]
        if addr in addr2outcome2.keys():
            addr2outcome[addr] += addr2outcome2[addr]
        if addr in addr2intx1.keys():
            addr2InTxnum[addr] += addr2intx1[addr]
        if addr in addr2intx2.keys():
            addr2InTxnum[addr] += addr2intx2[addr]
        if addr in addr2outtx1.keys():
            addr2OutTxnum[addr] += addr2outtx1[addr]
        if addr in addr2outtx2.keys():
            addr2OutTxnum[addr] += addr2outtx2[addr]
    # for addr in addrlist:
    #     if addr2InTxnum[addr] != 0:
    #         addr2avgincome[addr] = addr2income[addr] / addr2InTxnum[addr]
    #     if addr2OutTxnum[addr] != 0:
    #         addr2avgoutcome[addr] = addr2outcome[addr] / addr2OutTxnum[addr]
    # print(addr2avgincome)
    # print(addr2avgoutcome)
    with open('normalIncome.txt','w') as f:
        print(addr2income,file=f)
    with open('normalOutcome.txt','w') as f:
        print(addr2outcome,file=f)
    return
    with open('normalAvgIncome.txt','w') as f:
        print(addr2avgincome,file=f)
    with open('normalAvgOutcome.txt','w') as f:
        print(addr2avgoutcome,file=f)

    #如何计算每个地址的平均income和outcome，取加权平均值


def mixAvg():
    with open('scamAvgIncome.txt','r') as f:
        addr2avgincome1 = literal_eval(f.read())
    with open('scamAvgOutcome.txt','r') as f:
        addr2avgoutcome1 = literal_eval(f.read())
    with open('normalAvgIncome.txt','r') as f:
        addr2avgincome2 = literal_eval(f.read())
    with open('normalAvgOutcome.txt','r') as f:
        addr2avgoutcome2 = literal_eval(f.read())
    income2addrnum1 = {}
    income2addrnum2 = {}
    outcome2addrnum1 = {}
    outcome2addrnum2 = {}
    for addr,avgincome in addr2avgincome1.items():
        income2addrnum1[avgincome] = income2addrnum1.get(avgincome,0) + 1
    for addr,avgincome in addr2avgincome2.items():
        income2addrnum2[avgincome] = income2addrnum2.get(avgincome,0) + 1
    for addr,avgoutcome in addr2avgoutcome1.items():
        outcome2addrnum1[avgoutcome] = outcome2addrnum1.get(avgoutcome,0) + 1
    for addr,avgoutcome in addr2avgoutcome2.items():
        outcome2addrnum2[avgoutcome] = outcome2addrnum2.get(avgoutcome,0) + 1

    fig, ax = plt.subplots()

    zipped1 = zip(income2addrnum1.keys(), income2addrnum1.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    cum = numpy.cumsum(y1)
    percentage1 = cum / list(cum)[-1]

    zipped2 = zip(outcome2addrnum1.keys(), outcome2addrnum1.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    cum2 = numpy.cumsum(y2)
    percentage2 = cum2 / list(cum2)[-1]

    zipped3 = zip(income2addrnum2.keys(), income2addrnum2.values())
    sort_zipped3 = sorted(zipped3, key=lambda x: (x[0]))
    result3 = zip(*sort_zipped3)
    x3, y3 = [list(x) for x in result3]
    cum3 = numpy.cumsum(y3)
    percentage3 = cum3 / list(cum3)[-1]

    zipped4 = zip(outcome2addrnum2.keys(), outcome2addrnum2.values())
    sort_zipped4 = sorted(zipped4, key=lambda x: (x[0]))
    result4 = zip(*sort_zipped4)
    x4, y4 = [list(x) for x in result4]
    cum4 = numpy.cumsum(y4)
    percentage4 = cum4 / list(cum4)[-1]

    line1 = ax.plot(x1, percentage1, label='Avg Income Of scam addresses', color='black')
    line2 = ax.plot(x2, percentage2, label='Avg Outcome Of scam addresses', linestyle="--", color='black')
    line3 = ax.plot(x3, percentage3, label='Avg Income Of normal addresses', color='red')
    line4 = ax.plot(x4, percentage4, label='Avg Outcome Of normal addresses', linestyle="--", color='gray')
    ax.set_xlabel('Average Income/Outcome of Addresses (ETH)')
    ax.set_ylabel('CDF of Addresses')
    plt.xscale('log')
    ax.set_xlim(1)
    plt.legend()
    plt.savefig('avgIOcome.jpg')
    plt.show()
def mixfig6():
    with open('scamNtxliving.txt','r') as f:
        addr2living1 = literal_eval(f.read())
    with open('scamItxliving.txt','r') as f:
        addr2living2 = literal_eval(f.read())
    with open('scamEtxliving.txt','r') as f:
        addr2living3 = literal_eval(f.read())
    x = ['time<6h','6h≤time<12h','12h≤time<18h','18h≤time<24h','24h≤time<48h','48h≤time<1 week','1 week≤time<1 month','time>1 month']
    y1 = [0,0,0,0,0,0,0,0]
    y2 = [0,0,0,0,0,0,0,0]
    y3 = [0,0,0,0,0,0,0,0]
    index = np.arange(len(x))
    width = 0.2
    for addr,living in addr2living1.items():
        if living < 6:
            y1[0] += 1
        if 6 <= living and living <12:
            y1[1] += 1
        if 12 <= living and living < 18:
            y1[2] += 1
        if 18 <= living and living < 24:
            y1[3] += 1
        if 24 <= living and living < 48:
            y1[4] += 1
        if 48 <= living and living < 168:
            y1[5] += 1
        if 168 <= living and living < 720:
            y1[6] += 1
        if 720 <= living:
            y1[7] += 1
    for addr,living in addr2living2.items():
        if living < 6:
            y2[0] += 1
        if 6 <= living and living <12:
            y2[1] += 1
        if 12 <= living and living < 18:
            y2[2] += 1
        if 18 <= living and living < 24:
            y2[3] += 1
        if 24 <= living and living < 48:
            y2[4] += 1
        if 48 <= living and living < 168:
            y2[5] += 1
        if 168 <= living and living < 720:
            y2[6] += 1
        if 720 <= living:
            y2[7] += 1
    for addr,living in addr2living3.items():
        if living < 6:
            y3[0] += 1
        if 6 <= living and living <12:
            y3[1] += 1
        if 12 <= living and living < 18:
            y3[2] += 1
        if 18 <= living and living < 24:
            y3[3] += 1
        if 24 <= living and living < 48:
            y3[4] += 1
        if 48 <= living and living < 168:
            y3[5] += 1
        if 168 <= living and living < 720:
            y3[6] += 1
        if 720 <= living:
            y3[7] += 1
    plt.figure(figsize=(8, 4))
    plt.bar(x, y1, width, label="normal tx")
    plt.bar(index+width, y2, width, label="internal tx")
    plt.bar(index+width*2, y3, width, label="token tx")
    for a, b in zip(x, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    x = index + width
    for a, b in zip(x, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    x = index + width * 2
    for a, b in zip(x, y3):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    plt.xticks(rotation=30)
    ax = plt.gca()
    plt.yscale('log')
    ax.set_xlabel('living time of scam address')
    plt.legend(loc='best')
    plt.savefig('fig6.jpg')
    plt.show()

def mixfig7():
    with open('scamNtxProfit.txt','r') as f:
        addr2prof1 = literal_eval(f.read())
    with open('scamItxProfit.txt','r') as f:
        addr2prof2 = literal_eval(f.read())
    profaxis = ['0-1k','1k-2k','2k-3k','3k-4k','4k-5k','5k-10k','10k-15k','>15k']
    prof2num1 = {}
    prof2num2 = {}
    for prof in profaxis:
        prof2num1[prof] = 0
        prof2num2[prof] = 0
    for addr,prof in addr2prof1.items():
        if prof / 1000 <= 1:
            prof2num1['0-1k'] += 1
        if prof / 1000 > 1 and prof / 1000 <= 2:
            prof2num1['1k-2k'] += 1
        if prof / 1000 > 2 and prof / 1000 <= 3:
            prof2num1['2k-3k'] += 1
        if prof / 1000 > 3 and prof / 1000 <= 4:
            prof2num1['3k-4k'] += 1
        if prof / 1000 > 4 and prof / 1000 <= 5:
            prof2num1['4k-5k'] += 1
        if prof / 1000 > 5 and prof / 1000 < 10:
            prof2num1['5k-10k'] += 1
        if prof / 1000 > 10 and prof / 1000 < 15:
            prof2num1['10k-15k'] += 1
        if prof / 1000 > 15:
            prof2num1['>15k'] += 1
    for addr,prof in addr2prof2.items():
        if prof / 1000 <= 1:
            prof2num2['0-1k'] += 1
        if prof / 1000 > 1 and prof / 1000 <= 2:
            prof2num2['1k-2k'] += 1
        if prof / 1000 > 2 and prof / 1000 <= 3:
            prof2num2['2k-3k'] += 1
        if prof / 1000 > 3 and prof / 1000 <= 4:
            prof2num2['3k-4k'] += 1
        if prof / 1000 > 4 and prof / 1000 <= 5:
            prof2num2['4k-5k'] += 1
        if prof / 1000 > 5 and prof / 1000 < 10:
            prof2num2['5k-10k'] += 1
        if prof / 1000 > 10 and prof / 1000 < 15:
            prof2num2['10k-15k'] += 1
        if prof / 1000 > 15:
            prof2num2['>15k'] += 1
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    index = numpy.arange(len(profaxis))
    width = 0.2
    for prof in profaxis:
        x1.append(prof)
        y1.append(prof2num1[prof])
    for prof in profaxis:
        x2.append(prof)
        y2.append(prof2num2[prof])
    plt.bar(profaxis,y1,width, label="normal tx")
    plt.bar(index+width,y2,width, label="internal tx")
    plt.xticks(rotation=30)
    plt.yscale('log')
    plt.legend()
    plt.title('scam address profit')
    plt.savefig('fig7.jpg')
    plt.show()

def mixfig9Ntx():
    with open('scamAddrNFig9Intx.txt','r',encoding='utf-8') as f:
        txnum2addrnum1 = literal_eval(f.read())
    with open('norAddrNFig9Intxs.txt','r',encoding='utf-8') as f:
        txnum2addrnum2 = literal_eval(f.read())
    with open('scamAddrNFig9Outtx.txt','r',encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    with open('norAddrNFig9Outtxs.txt','r',encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())
    zipped1 = zip(txnum2addrnum1.keys(), txnum2addrnum1.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y1)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x1,percentage,label='in txs of normal txs of scam address', color='black')

    zipped2 = zip(txnum2addrnum2.keys(), txnum2addrnum2.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    cum = numpy.cumsum(y2)
    percentage2 = cum / list(cum)[-1]
    line2 = ax.plot(x2,percentage2,label='in txs of normal txs of normal address', linestyle="--", color='black')

    zipped3 = zip(txnum2addrnum3.keys(), txnum2addrnum3.values())
    sort_zipped3 = sorted(zipped3, key=lambda x: (x[0]))
    result3 = zip(*sort_zipped3)
    x3, y3 = [list(x) for x in result3]
    cum = numpy.cumsum(y3)
    percentage3 = cum / list(cum)[-1]
    line3 = ax.plot(x3, percentage3, label='out txs of normal txs of scam address', color='gray')

    zipped4 = zip(txnum2addrnum4.keys(), txnum2addrnum4.values())
    sort_zipped4 = sorted(zipped4, key=lambda x: (x[0]))
    result4 = zip(*sort_zipped4)
    x4, y4 = [list(x) for x in result4]
    cum = numpy.cumsum(y4)
    percentage4 = cum / list(cum)[-1]
    line4 = ax.plot(x4,percentage4,label='out txs of normal txs of normal address', linestyle="--", color='gray')
    ax.set_xlim(1)
    plt.xscale('log')
    plt.legend()
    ax.set_ylabel('CDF of Addresses')
    plt.title('# fo transactions')
    plt.savefig('Ntxfig9.jpg')
    plt.show()

def mixfig9Itx():
    with open('scamAddrIFig9Intx.txt','r',encoding='utf-8') as f:
        txnum2addrnum1 = literal_eval(f.read())
    with open('norAddrIFig9Intxs.txt','r',encoding='utf-8') as f:
        txnum2addrnum2 = literal_eval(f.read())
    with open('scamAddrIFig9Outtx.txt','r',encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    with open('norAddrIFig9Outtxs.txt','r',encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())

    zipped1 = zip(txnum2addrnum1.keys(), txnum2addrnum1.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y1)
    percentage = cum / list(cum)[-1]
    line = ax.plot(x1,percentage,label='in txs of internal txs of scam address', color='black')
    zipped2 = zip(txnum2addrnum2.keys(), txnum2addrnum2.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    cum = numpy.cumsum(y2)
    percentage = cum / list(cum)[-1]
    line2 = ax.plot(x2,percentage,label='in txs of internal txs of normal address', linestyle="--", color='black')
    zipped3 = zip(txnum2addrnum3.keys(), txnum2addrnum3.values())
    sort_zipped3 = sorted(zipped3, key=lambda x: (x[0]))
    result3 = zip(*sort_zipped3)
    x3, y3 = [list(x) for x in result3]
    cum = numpy.cumsum(y3)
    percentage3 = cum / list(cum)[-1]
    line3 = ax.plot(x3, percentage3, label='out txs of internal txs of scam address', color='gray')

    zipped4 = zip(txnum2addrnum4.keys(), txnum2addrnum4.values())
    sort_zipped4 = sorted(zipped4, key=lambda x: (x[0]))
    result4 = zip(*sort_zipped4)
    x4, y4 = [list(x) for x in result4]
    cum = numpy.cumsum(y4)
    percentage4 = cum / list(cum)[-1]
    line4 = ax.plot(x4, percentage4, label='out txs of internal txs of normal address', linestyle="--", color='gray')
    ax.set_xlim(1)
    plt.xscale('log')
    plt.legend()
    ax.set_ylabel('CDF of Addresses')
    plt.title('# of transactions')
    plt.savefig('Itxfig9.jpg')
    plt.show()

def mixfig9Etx():
    with open('scamAddrEFig9Intx.txt','r',encoding='utf-8') as f:
        txnum2addrnum1 = literal_eval(f.read())
    with open('norAddrEFig9Intxs.txt','r',encoding='utf-8') as f:
        txnum2addrnum2 = literal_eval(f.read())
    with open('scamAddrEFig9Outtx.txt','r',encoding='utf-8') as f:
        txnum2addrnum3 = literal_eval(f.read())
    with open('norAddrEFig9Outtx.txt','r',encoding='utf-8') as f:
        txnum2addrnum4 = literal_eval(f.read())
    zipped1 = zip(txnum2addrnum1.keys(), txnum2addrnum1.values())
    sort_zipped1 = sorted(zipped1, key=lambda x: (x[0]))
    result1 = zip(*sort_zipped1)
    x1, y1 = [list(x) for x in result1]
    cum = numpy.cumsum(y1)
    percentage1 = cum / list(cum)[-1]

    zipped2 = zip(txnum2addrnum2.keys(), txnum2addrnum2.values())
    sort_zipped2 = sorted(zipped2, key=lambda x: (x[0]))
    result2 = zip(*sort_zipped2)
    x2, y2 = [list(x) for x in result2]
    fig, ax = plt.subplots()
    cum = numpy.cumsum(y2)
    percentage2 = cum / list(cum)[-1]

    zipped3 = zip(txnum2addrnum3.keys(), txnum2addrnum3.values())
    sort_zipped3 = sorted(zipped3, key=lambda x: (x[0]))
    result3 = zip(*sort_zipped3)
    x3, y3 = [list(x) for x in result3]
    cum = numpy.cumsum(y3)
    percentage3 = cum / list(cum)[-1]

    zipped4 = zip(txnum2addrnum4.keys(), txnum2addrnum4.values())
    sort_zipped4 = sorted(zipped4, key=lambda x: (x[0]))
    result4 = zip(*sort_zipped4)
    x4, y4 = [list(x) for x in result4]
    cum = numpy.cumsum(y4)
    percentage4 = cum / list(cum)[-1]

    line1 = ax.plot(x1,percentage1,label='in txs of token txs of scam address', color='black')
    line2 = ax.plot(x2,percentage2,label='in txs of token txs of normal address', linestyle="--", color='black')
    line3 = ax.plot(x3,percentage3,label='out txs of token txs of scam address', linestyle="--", color='gray')
    line4 = ax.plot(x4,percentage4,label='out txs of token txs of normal address', linestyle="--", color='gray')
    ax.set_xlim(1)
    # ax.set_xlabel('Average Income/Outcome of Addresses (ETH)')
    # ax.set_ylabel('CDF of Addresses')
    plt.xscale('log')
    plt.legend()
    plt.savefig('Etxfig9.jpg')
    plt.show()
def graph1():
    df = pandas.read_csv('exp_group_victim.csv')
    temp_list = df['componentnumber']
    temp_dict = {}
    for each in temp_list:
        if each not in temp_dict.keys():
            temp_dict[each] = 1
        else:
            temp_dict[each] = temp_dict[each] + 1
    no_list = []
    number_list = []
    for k, v in temp_dict.items():
        no_list.append(k)
        number_list.append(v)
    df = pandas.DataFrame({'id': no_list, '#': number_list})
    df.to_csv(r'number of each group victim')
def scamNtxMFG():
    with open('addr.txt', 'r') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('ntx.csv')
    for index, row in df1.iterrows():
        if isinstance(row['from'],str):
            row['from'] = row['from'].lower()
        if isinstance(row['to'],str):
            row['to'] = row['to'].lower()
    dict1 = {}
    addrlist2 = []
    for addr in addrlist:
        dict1[addr] = {}
    for index, row in df1.iterrows():
        # if row['from'] in addrlist and row['to'] in addrlist:
        if row['from'] in addrlist:
            dict1[row['from']][row['to']] = dict1[row['from']].get(row['to'],0) + float(row['value'])
    with open('scamNtxMFG.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['from','to','value'])
        for fromaddr,to2value in dict1.items():
            for toaddr,value in dict1[fromaddr].items():
                writer.writerow([fromaddr,toaddr,value])
                addrlist2.append(toaddr)
            addrlist2.append(fromaddr)
    addrlist2 = list(set(addrlist2))
    print(addrlist2)
    solp = []
    for addr in addrlist:
        if addr not in addrlist2:
            solp.append(addr)
    with open('scamNtxSolP.txt','w',encoding='utf-8') as f:
        print(solp,file=f)
    #独立点，和没有被识别为欺诈地址的其他地址进行交易

def scamItxMFG():
    with open('addr.txt', 'r') as f:
        addrlist = literal_eval(f.read())
    df1 = pandas.read_csv('itx.csv')
    for index, row in df1.iterrows():
        if isinstance(row['from'],str):
            row['from'] = row['from'].lower()
        if isinstance(row['to'],str):
            row['to'] = row['to'].lower()
    dict1 = {}
    addrlist2 = []
    for addr in addrlist:
        dict1[addr] = {}
    for index, row in df1.iterrows():
        # if row['from'] in addrlist and row['to'] in addrlist:
        if row['from'] in addrlist:
            dict1[row['from']][row['to']] = dict1[row['from']].get(row['to'],0) + float(row['value'])#value的单位是wei
    with open('scamItxMFG.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['from','to','value'])
        for fromaddr,to2value in dict1.items():
            for toaddr,value in dict1[fromaddr].items():
                writer.writerow([fromaddr,toaddr,value])
                addrlist2.append(toaddr)
            addrlist2.append(fromaddr)
    # print(addrlist2)
    addrlist2 = list(set(addrlist2))
    print(len(addrlist2))
    solp = []
    for addr in addrlist:
        if addr not in addrlist2:
            solp.append(addr)
    with open('scamItxSolP.txt','w',encoding='utf-8') as f:
        print(solp,file=f)

#每个文件的含义
# exp_add_profit.csv 地址和利润
# exp_group_id.csv 地址和聚类后的块号
# exp_group_victim.csv 地址和聚类后的？
# extend_group_id.csv 地址和聚类后的块号
# extend_group_profit.csv 利润和块号
# final_type2_all_trans_new.csv ????
# extend_group_start_time.csv 开始时间和块号
# final_type2_in_trans_USD.csv 地址和利润
# final_type2_trans_USD.csv地址和利润
# need_to_reget.csv 地址
# node.csv 无法打开
# number of each group victim.csv 每个块的受害者
# scam group NO.csv 地址和块号
# scam group time and profit.csv 欺诈地址和时间和利润
# tx_into.csv ?
def character13():
    with open('scamIncome.txt','r',encoding='utf-8') as f:
        scamIncome = literal_eval(f.read())
    with open('scamOutcome.txt','r',encoding='utf-8') as f:
        scamOutcome = literal_eval(f.read())
    with open('scamAvgIncome.txt', 'r', encoding='utf-8') as f:
        scamAvgIncome = literal_eval(f.read())
    with open('scamAvgOutcome.txt', 'r', encoding='utf-8') as f:
        scamAvgOutcome = literal_eval(f.read())
    with open('scamInTx.txt','r') as f:
        scamInTx = literal_eval(f.read())
    with open('scamOutTx.txt','r') as f:
        scamOutTx = literal_eval(f.read())
    with open('scam2athirdLivingtime3.txt', 'r') as f:
        scamLivingtime = literal_eval(f.read())
    with open('scam2athirdIntxnum1.txt','r') as f:
        scam2athirdIntxnum1 = literal_eval(f.read())
    with open('scam2athirdIntxnum2.txt','r') as f:
        scam2athirdIntxnum2 = literal_eval(f.read())
    with open('scam2athirdIntxnum3.txt','r') as f:
        scam2athirdIntxnum3 = literal_eval(f.read())
    with open('scam2athirdOuttxnum1.txt','r') as f:
        scam2athirdOuttxnum1 = literal_eval(f.read())
    with open('scam2athirdOuttxnum2.txt','r') as f:
        scam2athirdOuttxnum2 = literal_eval(f.read())
    with open('scam2athirdOuttxnum3.txt','r') as f:
        scam2athirdOuttxnum3 = literal_eval(f.read())

    with open('normalIncome.txt','r') as f:
        normalIncome = literal_eval(f.read())
    with open('normalOutcome.txt','r') as f:
        normalOutcome = literal_eval(f.read())
    with open('normalAvgIncome.txt','r') as f:
        normalAvgIncome = literal_eval(f.read())
    with open('normalAvgOutcome.txt','r') as f:
        normalAvgOutcome = literal_eval(f.read())
    with open('normal2athirdIntxnum.txt','r') as f:
        normal2athirdIntxnum = literal_eval(f.read())
    with open('normal2athirdOuttxnum.txt','r') as f:
        normal2athirdOuttxnum = literal_eval(f.read())
    with open('normal2athirdtime3.txt', 'r') as f:
        normalLivingtime = literal_eval(f.read())
    with open('normal2athirdIntxnum1.txt','r') as f:
        normal2athirdIntxnum1 = literal_eval(f.read())
    with open('normal2athirdIntxnum2.txt','r') as f:
        normal2athirdIntxnum2 = literal_eval(f.read())
    with open('normal2athirdIntxnum3.txt','r') as f:
        normal2athirdIntxnum3 = literal_eval(f.read())
    with open('normal2athirdOuttxnum1.txt','r') as f:
        normal2athirdOuttxnum1 = literal_eval(f.read())
    with open('normal2athirdOuttxnum2.txt','r') as f:
        normal2athirdOuttxnum2 = literal_eval(f.read())
    with open('normal2athirdOuttxnum3.txt','r') as f:
        normal2athirdOuttxnum3 = literal_eval(f.read())
    with open('addr.txt', 'r', encoding='utf-8') as f:
        scamaddrlist = literal_eval(f.read())
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        noraddrlist = literal_eval(f.read())
    scamlist = []
    norlist = []
    for addr in scamaddrlist:
        scamdict = {}
        scamdict['address'] = addr
        scamdict['allIncome'] = scamIncome.get(addr,0)
        scamdict['allOutcome'] = scamOutcome.get(addr,0)
        scamdict['avgIncome'] = scamAvgIncome.get(addr,0)
        scamdict['avgOutcome'] = scamAvgOutcome.get(addr,0)
        scamdict['intxs'] = scamInTx.get(addr,0)
        scamdict['outtxs'] = scamOutTx.get(addr,0)
        scamdict['livingTime'] = scamLivingtime.get(addr,0)
        scamdict['front1/3in'] = scam2athirdIntxnum1.get(addr,0)
        scamdict['middle1/3in'] = scam2athirdIntxnum2.get(addr,0)
        scamdict['last1/3in'] = scam2athirdIntxnum3.get(addr,0)
        scamdict['front1/3out'] = scam2athirdOuttxnum1.get(addr,0)
        scamdict['middle1/3out'] = scam2athirdOuttxnum2.get(addr,0)
        scamdict['last1/3out'] = scam2athirdOuttxnum3.get(addr,0)
        scamdict['type'] = 1
        scamlist.append(scamdict)
    for addr in noraddrlist:
        nordict = {}
        nordict['address'] = addr
        nordict['allIncome'] = normalIncome.get(addr,0)
        nordict['allOutcome'] = normalOutcome.get(addr,0)
        nordict['avgIncome'] = normalAvgIncome.get(addr,0)
        nordict['avgOutcome'] = normalAvgOutcome.get(addr, 0)
        nordict['intxs'] = normal2athirdIntxnum.get(addr, 0)
        nordict['outtxs'] = normal2athirdOuttxnum.get(addr, 0)
        nordict['livingTime'] = normalLivingtime.get(addr,0)
        nordict['front1/3in'] = normal2athirdIntxnum1.get(addr, 0)
        nordict['middle1/3in'] = normal2athirdIntxnum2.get(addr, 0)
        nordict['last1/3in'] = normal2athirdIntxnum3.get(addr, 0)
        nordict['front1/3out'] = normal2athirdOuttxnum1.get(addr, 0)
        nordict['middle1/3out'] = normal2athirdOuttxnum2.get(addr, 0)
        nordict['last1/3out'] = normal2athirdOuttxnum3.get(addr, 0)
        nordict['type'] = 0
        norlist.append(nordict)
    with open('mlchar.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["address","allIncome","allOutcome","avgIncome","avgOutcome","intxs","outtxs","livingTime","front1/3in","middle1/3in","last1/3in","front1/3out","middle1/3out","last1/3out","type"])
        for scamdict in scamlist:
            if int(scamdict['intxs']) != 0 and int(scamdict['outtxs']) != 0:
                writer.writerow([scamdict['address'], scamdict['allIncome'], scamdict['allOutcome'], scamdict['avgIncome'], scamdict['avgOutcome'], scamdict['intxs'],
                                 scamdict['outtxs'], scamdict['livingTime'], scamdict['front1/3in'], scamdict['middle1/3in'], scamdict['last1/3in'], scamdict['front1/3out'], scamdict['middle1/3out'],
                                 scamdict['last1/3out'], scamdict['type']])
        for nordict in norlist:
            if int(nordict['intxs']) != 0 and int(nordict['outtxs']) != 0:
                writer.writerow([nordict['address'], nordict['allIncome'], nordict['allOutcome'], nordict['avgIncome'],
                                 nordict['avgOutcome'], nordict['intxs'],nordict['outtxs'], nordict['livingTime'], nordict['front1/3in'], nordict['middle1/3in'], nordict['last1/3in'],
                                 nordict['front1/3out'], nordict['middle1/3out'], nordict['last1/3out'], nordict['type']])

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier


def logReg():
    data = pandas.read_csv('mlchar.csv')[["allIncome","allOutcome","avgIncome","avgOutcome","intxs","outtxs","livingTime","front1/3in","middle1/3in","last1/3in","front1/3out","middle1/3out","last1/3out","type"]]
    data = shuffle(data)
    X1 = data["allIncome"].to_list()
    X2 = data["allOutcome"].to_list()
    X3 = data["avgIncome"].to_list()
    X4 = data["avgOutcome"].to_list()
    X5 = data["intxs"].to_list()
    X6 = data["outtxs"].to_list()
    X7 = data["livingTime"].to_list()
    X8 = data["front1/3in"].to_list()
    X9 = data["middle1/3in"].to_list()
    X10 = data["last1/3in"].to_list()
    X11 = data["front1/3out"].to_list()
    X12 = data["middle1/3out"].to_list()
    X13 = data["last1/3out"].to_list()
    X = numpy.array([X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13]).T
    Y = data["type"].to_list()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

    print('LogisticRegression')
    logreg = LogisticRegression()
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(logreg.coef_)
    print(classification_report(Y_test, Ypred))
    # print( mean_squared_error(Y_test, Ypred))

    print('KNeighborsClassifier')
    logreg = KNeighborsClassifier(n_neighbors=3)
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    # print(logreg.coef_)
    print(classification_report(Y_test, Ypred))
    # print( mean_squared_error(Y_test, Ypred))

    print('svm')
    logreg = svm.SVC()
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print( mean_squared_error(Y_test, Ypred))

    print('DecisionTreeClassifier')
    logreg = DecisionTreeClassifier(random_state=1,splitter="best")
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print(mean_squared_error(Y_test, Ypred))

    print('GaussianNB')
    logreg = GaussianNB()
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print(mean_squared_error(Y_test, Ypred))

    print('RandomForestClassifier')
    logreg = RandomForestClassifier()
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print(mean_squared_error(Y_test, Ypred))

    print('GradientBoostingClassifier')
    logreg = GradientBoostingClassifier()
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print(mean_squared_error(Y_test, Ypred))

    print('MLPClassifier')
    logreg = MLPClassifier(verbose=True, max_iter=300)
    logreg.fit(X_train, Y_train)
    Ypred = logreg.predict(X_test)
    print(classification_report(Y_test, Ypred))
    # print(mean_squared_error(Y_test, Ypred))
#使用相邻的节点也是欺诈节点规则判断
def getscamNodeEdgeCSV():
    # with open('addr.txt','r',encoding='utf-8') as f:
    #     scamaddrlist = literal_eval(f.read())
    # with open('normalAddr.txt','r',encoding='utf-8') as f:
    #     noraddrlist = literal_eval(f.read())
    # df1 = pandas.read_csv('ntx.csv')
    # df2 = pandas.read_csv('itx.csv')
    # frames = [df1,df2]
    # df = pandas.concat(frames)
    # print(len(df))
    # nodecsv = {}
    # edgecsv = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['from'],str):
    #         nodecsv[row['from']] = {}
    #         edgecsv[row['from']] = {}
    #     if isinstance(row['to'],str):
    #         nodecsv[row['to']] = {}
    #         edgecsv[row['to']] = {}
    # for index, row in df.iterrows():
    #     if isinstance(row['to'],str):
    #         addr = row['to']
    #         nodecsv[addr]['indegree'] = nodecsv[addr].get('indegree', 0) + 1
    #         if row['to'] in scamaddrlist:
    #             nodecsv[addr]['type'] = 'scam'
    #         elif row['to'] in noraddrlist:
    #             nodecsv[addr]['type'] = 'normal'
    #         elif row['to'] not in scamaddrlist and row['to'] not in noraddrlist:
    #             nodecsv[addr]['type'] = 'unknown'
    #     if isinstance(row['from'],str):
    #         addr = row['from']
    #         nodecsv[addr]['outdegree'] = nodecsv[addr].get('outdegree', 0) + 1
    #         if row['from'] in scamaddrlist:
    #             nodecsv[addr]['type'] = 'scam'
    #         elif row['from'] in noraddrlist:
    #             nodecsv[addr]['type'] = 'normal'
    #         elif row['from'] not in scamaddrlist and row['from'] not in noraddrlist:
    #             nodecsv[addr]['type'] = 'unknown'
    #     if isinstance(row['from'],str) and isinstance(row['to'],str):
    #         edgecsv[row['from']][row['to']] = edgecsv[row['from']].get(row['to'],0) + 1
    #     print(index)
    # with open('mlnode.txt','w',encoding='utf-8',newline='') as f:
    #     print(nodecsv,file=f)
    # with open('mledge.txt','w',encoding='utf-8',newline='') as f:
    #     print(edgecsv,file=f)

    with open('mlnode.txt', 'r', encoding='utf-8') as f:
        nodecsv = literal_eval(f.read())
    with open('mledge.txt', 'r', encoding='utf-8') as f:
        edgecsv = literal_eval(f.read())
    for addr,attr in nodecsv.items():
        nodecsv[addr]['degree'] = nodecsv[addr].get('indegree',0) + nodecsv[addr].get('outdegree',0)
    with open('mlnode.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Id','type','indegree','outdegree','degree'])
        for addr,attr in nodecsv.items():
            writer.writerow([addr,nodecsv[addr]['type'],nodecsv[addr].get('indegree',0),nodecsv[addr].get('outdegree',0),nodecsv[addr]['degree']])
    with open('mledge.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Source','Target','Weight'])
        for fromaddr,toaddr2weight in edgecsv.items():
            for toaddr,weight in toaddr2weight.items():
                writer.writerow([fromaddr,toaddr,weight])
    return
def getnorIOAddr():
    df1 = pandas.read_csv('normalAddrntx2.csv')
    df2 = pandas.read_csv('normalAddritx2.csv')
    frames = [df1, df2]
    df = pandas.concat(frames)
    addr2addr = {}
    for index, row in df.iterrows():
        if isinstance(row['from'], str):
            addr2addr[row['from']] = []
        if isinstance(row['to'], str):
            addr2addr[row['to']] = []
    for index, row in df.iterrows():
        if isinstance(row['from'], str) and isinstance(row['to'], str):
            addr2addr[row['from']].append(row['to'])
    # with open('normaladdr2addr.txt', 'w', encoding='utf-8') as f:
    #     print(addr2addr,file=f)
    with open('normaladdr2addr.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Source','Target'])
        for addr,addrlist in addr2addr.items():
            for addr2 in addrlist:
                writer.writerow([addr,addr2])
from collections import defaultdict
def getnorNodeEdgeCSV():
    addr2addr = pandas.read_csv('normaladdr2addr.csv')
    with open('addr.txt', 'r', encoding='utf-8') as f:
        scamaddrlist = literal_eval(f.read())
    with open('normalAddr.txt', 'r', encoding='utf-8') as f:
        noraddrlist = literal_eval(f.read())
    nodecsv = defaultdict(defaultdict)#
    edgecsv = defaultdict(defaultdict)
    for index,row in addr2addr.iterrows():
        nodecsv[row['Source']]['outdegree'] = nodecsv[row['Source']].setdefault('outdegree',0) + 1
        if row['Source'] in scamaddrlist:
            nodecsv[row['Source']]['type'] = nodecsv[row['Source']].setdefault('type','scam')
        if row['Source'] in noraddrlist:
            nodecsv[row['Source']]['type'] = nodecsv[row['Source']].setdefault('type','normal')
        if row['Source'] not in scamaddrlist and row['Source'] not in noraddrlist:
            nodecsv[row['Source']]['type'] = nodecsv[row['Source']].setdefault('type','unknown')

        nodecsv[row['Target']]['indegree'] = nodecsv[row['Target']].setdefault('indegree',0) + 1
        if row['Target'] in scamaddrlist:
            nodecsv[row['Target']]['type'] = nodecsv[row['Target']].setdefault('type','scam')
        if row['Target'] in noraddrlist:
            nodecsv[row['Target']]['type'] = nodecsv[row['Target']].setdefault('type','normal')
        if row['Target'] not in scamaddrlist and row['Target'] not in noraddrlist:
            nodecsv[row['Target']]['type'] = nodecsv[row['Target']].setdefault('type','unknown')
        edgecsv[row['Source']][row['Target']] = edgecsv[row['Source']].setdefault(row['Target'],0) + 1
    with open('mlnode2.txt', 'w', encoding='utf-8') as f:
        print(nodecsv, file=f)
    with open('mledge2.txt', 'w', encoding='utf-8') as f:
        print(edgecsv, file=f)
    for addr, attr in nodecsv.items():
        nodecsv[addr]['degree'] = nodecsv[addr].get('indegree', 0) + nodecsv[addr].get('outdegree', 0)
    with open('mlnode2.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Id', 'type', 'indegree', 'outdegree', 'degree'])
        for addr, attr in nodecsv.items():
            writer.writerow([addr,nodecsv[addr]['type'],nodecsv[addr].get('indegree',0),nodecsv[addr].get('outdegree',0),nodecsv[addr]['degree']])
    with open('mledge2.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Source', 'Target', 'Weight'])
        for fromaddr, toaddr2weight in edgecsv.items():
            for toaddr, weight in toaddr2weight.items():
                writer.writerow([fromaddr, toaddr, weight])
def mixNodeEdgeCsv():
    normaladdr2addr = pandas.read_csv('normaladdr2addr.csv')
    mlnode = pandas.read_csv('mlnode.csv')
    mledge = pandas.read_csv('mledge.csv')
    mlnode2 = pandas.read_csv('mlnode2.csv')
    mledge2 = pandas.read_csv('mledge2.csv')
    print(len(mlnode))
    print(len(mlnode2))
    print(len(mlnode)+len(mlnode2))
    newNorNode = mlnode2[(mlnode2['degree'] < 5)]
    newNorNode = newNorNode.sample(len(mlnode),random_state=3)#随机挑选和欺诈node相同数量的正常node，但还要算和这些正常node相连的node，根据这些正常node的地址，找直接连接的node
    newNodelist = list(newNorNode['Id'])#先随机选然后再找直接连接的，即需要迭代一次
    directNode = []
    for addr in newNodelist:
        if addr in normaladdr2addr.keys():
            directNode = directNode + normaladdr2addr[addr]#出的边
    for addr,addrlist in normaladdr2addr.items():
        for newaddr in newNodelist:
            if newaddr in addrlist:
                directNode.append(addr)#入的边
    newNodelist = newNodelist + directNode
    newNorNode = mlnode2[(mlnode2['degree'] < 5) & mlnode2['Id'].isin(newNodelist)]
    newNorEdge = mledge2[(mledge2['Source'].isin(newNodelist)) & (mledge2['Target'].isin(newNodelist))]
    newNorNode.to_csv('mlnode5.csv')#中间node
    newNorEdge.to_csv('mledge5.csv')#中间edge
    frames1 = [mlnode,newNorNode]
    frames2 = [mledge,newNorEdge]
    nodecsv = pandas.concat(frames1).drop_duplicates()
    edgecsv = pandas.concat(frames2).drop_duplicates()
    print(len(nodecsv))
    print(len(edgecsv))
    nodecsv['Label'] = ""
    nodecsv['Interval'] = ""
    nodecsv.to_csv('node3.csv')
    edgecsv.to_csv('edge3.csv')
    # nodecsv = pandas.read_csv('node.csv')
    # edgecsv = pandas.read_csv('edge.csv')
    # print(len(nodecsv))
    # print(len(edgecsv))
#node:332191 332063 332124
#edge:197687 197687 197689

def getpred():
    pred = pandas.read_csv('predict-gdc.csv')
    num = 0
    for index,row in pred.iterrows():
        if row['pred'] == 'tensor(1)':
            num += 1
    print(num)
#11249
def fig11():
    addr = '0x83053c32b7819f420dcfed2d218335fe430fe3b5'
    # addr = '0x21f74c6bbc1e3ab9f0205e12de3a9daa14351aed'
    # addr = '0x4fed1fc4144c223ae3c1553be203cdfcbd38c581'
    # addr = '0x4bf722014e54aeab05fcf1519e6e4c0c3f742e43'
    # addr = '0x536a6ba0d913d5d6a4ce2c6eb7ed0de3c0f0b89e'
    addr = '0x74886dd45da313f3d3d32235fed4595827d0865d'#没有scam
    addr = '0x917a417d938b9f9e6ae7f9e5253fb6de410343e3'#节点太少
    # addr = '0x7c9001c50ea57c1b2ec1e3e63cf04c297534bfc1'
    addr = '0xba83e9ce38b10522e3d6061a12779b7526839eda'#第二次迭代节点太多
    addr = '0x050022eba4d55d242d9568794961df5596f968f2'
    #选0x4fed1
    mledge = pandas.read_csv('mledge.csv')
    mlnode = pandas.read_csv('mlnode.csv')
    mledge2 = pandas.read_csv('mledge2.csv')
    mlnode2 = pandas.read_csv('mlnode2.csv')

    # specialNode = []
    # for index,row in mledge.iterrows():
    #     if isinstance(row['Source'],str) and row['Source'] == addr:
    #         specialNode.append(row['Target'])
    #     if isinstance(row['Target'],str) and row['Target'] == addr:
    #         specialNode.append(row['Source'])
    # for index,row in mledge2.iterrows():
    #     if isinstance(row['Source'],str) and row['Source'] == addr:
    #         specialNode.append(row['Target'])
    #     if isinstance(row['Target'],str) and row['Target'] == addr:
    #         specialNode.append(row['Source'])
    # with open('specialNode.txt','w') as f:
    #     print(specialNode,file=f)
    # # return
    #
    # specialEdge1 = mledge[(mledge['Source'].notnull()) & (mledge['Source'] == addr) | (mledge['Target'].notnull()) & (mledge['Target'] == addr)]
    # specialEdge2 = mledge2[(mledge2['Source'].notnull()) & (mledge2['Source'] == addr) | (mledge2['Target'].notnull()) & (mledge2['Target'] == addr)]
    # frames = [specialEdge1,specialEdge2]
    # specialEdge = pandas.concat(frames)
    # specialEdge.to_csv('specialEdge.csv')
    # # return
    with open('specialNode0x05002.txt','r') as f:
        specialNode = literal_eval(f.read())
    # specialNodecsv1 = mlnode[(mlnode['Id'].isin(specialNode))]#单节点的直接连接节点的全部信息
    # specialNodecsv2 = mlnode2[(mlnode2['Id'].isin(specialNode))]
    # frames = [specialNodecsv1,specialNodecsv2]
    # specialNodecsv = pandas.concat(frames)
    # specialNodecsv.reset_index(drop=True,inplace=True)

    specialEdge1 = pandas.read_csv('specialEdge0x05002.csv')
    specialEdge2csv1 = mledge[(isinstance(mledge['Source'],str))  & (mledge['Source'].isin(specialNode)) | (mledge['Target'].notnull()) & (mledge['Target'].isin(specialNode)) ]
    specialEdge2csv2 = mledge2[(isinstance(mledge2['Source'],str))  & (mledge2['Source'].isin(specialNode)) | (mledge2['Target'].notnull()) & (mledge2['Target'].isin(specialNode)) ]
    frames = [specialEdge1,specialEdge2csv1,specialEdge2csv2]
    specialEdge2 = pandas.concat(frames)
    specialEdge2.to_csv('specialEdge2.csv')
    return
    with open('norMinerAddr.txt','r') as f:#小写地址
        norMinerAddr = literal_eval(f.read())
    with open('norExchangeAddr.txt','r') as f:
        norExchangeAddr = literal_eval(f.read())
    with open('norTokenAddr.txt', 'r') as f:
        norTokenAddr = literal_eval(f.read())
    # for index,row in specialNodecsv.iterrows():
    #     if row['Id'].lower() in norMinerAddr:
    #         row['type'] = 'Miner'
    #         specialNodecsv.iloc[index] = row
    #     if row['Id'].lower() in norExchangeAddr:
    #         row['type'] = 'Exchange'
    #         specialNodecsv.iloc[index] = row
    #     if row['Id'].lower() in norTokenAddr:
    #         row['type'] = 'Token'
    #         specialNodecsv.iloc[index] = row
    # specialNodecsv.to_csv('specialNode.csv')
    # return
    #将所有的直接连接的节点添加为待添加边的节点，然后对其边进行统计
    #再迭代一次

    # with open('specialNode.txt', 'r') as f:
    #     specialNode = literal_eval(f.read())
    # with open('norMinerAddr.txt','r') as f:#小写地址
    #     norMinerAddr = literal_eval(f.read())
    # with open('norExchangeAddr.txt','r') as f:
    #     norExchangeAddr = literal_eval(f.read())
    # with open('norTokenAddr.txt', 'r') as f:
    #     norTokenAddr = literal_eval(f.read())
    # specialEdge2 = pandas.read_csv('specialEdge2.csv')
    # specialNode2list1 = list(specialEdge2['Source'])
    # specialNode2list2 = list(specialEdge2['Target'])
    # specialNode2 = list(set(specialNode2list1 + specialNode2list2 + specialNode))
    # specialNode2csv1 = mlnode[(mlnode['Id'].isin(specialNode2))]
    # specialNode2csv2 = mlnode2[(mlnode2['Id'].isin(specialNode2))]
    # frames = [specialNode2csv1,specialNode2csv2]
    # specialNode2csv = pandas.concat(frames)

    specialNode2csv = pandas.read_csv('specialNode2.csv')
    specialNode2csv.reset_index(drop=True,inplace=True)
    for index,row in specialNode2csv.iterrows():
        if row['Id'].lower() in norMinerAddr:
            row['type'] = 'Miner'
            specialNode2csv.iloc[index] = row
        if row['Id'].lower() in norExchangeAddr:
            row['type'] = 'Exchange'
            specialNode2csv.iloc[index] = row
        if row['Id'].lower() in norTokenAddr:
            row['type'] = 'Token'
            specialNode2csv.iloc[index] = row
    specialNode2csv.to_csv('specialNode2.csv')
    # with open('specialNode2.txt','w') as f:
    #     print(specialNode2,file=f)

def taxoNormalAddr():
    normalAddr = pandas.read_csv('ethereum_tagged_address.csv',encoding='ISO-8859-1')
    minerAddr = []
    tokenAddr = []
    exchangeAddr = []
    for index,row in normalAddr.iterrows():
        if 'blacklist' not in row['label'].lower() and 'miner' in row['label'].lower():
            minerAddr.append(row['addr'].lower())
        elif 'blacklist' not in row['label'].lower() and 'exchange' in row['label'].lower():
            exchangeAddr.append(row['addr'].lower())
        elif 'blacklist' not in row['label'].lower():
            tokenAddr.append(row['addr'].lower())
    with open('norMinerAddr.txt','w') as f:
        print(minerAddr,file=f)
    with open('norExchangeAddr.txt','w') as f:
        print(exchangeAddr,file=f)
    with open('norTokenAddr.txt','w') as f:
        print(tokenAddr,file=f)
def fig12():
    mledge = pandas.read_csv('mledge.csv')
    mlnode = pandas.read_csv('mlnode.csv')
    # with open('addr.txt', 'r', encoding='utf-8') as f:
    #     scamaddrlist = literal_eval(f.read())
    mlnode = mlnode[(mlnode['degree'] > 0) & (mlnode['type']=='scam')]
    degreeScamnode = list(mlnode['Id'])
    mledge = mledge[(mledge['Source'].notnull()) & (mledge['Source'].isin(degreeScamnode)) & (mledge['Target'].notnull()) & (mledge['Target'].isin(degreeScamnode))]
    mledge.to_csv('scamNodeDegreeEdge.csv')
    mledgeSource = list(mledge['Source'])
    mledgeTarget = list(mledge['Target'])
    mledgelist = mledgeSource + mledgeTarget
    mlnode = mlnode[(mlnode['Id'].isin(mledgelist))]
    mlnode.to_csv('scamNodeDegree.csv')

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
    # pass
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
    # normalLive2()
    # norAddrA3OutItxTx()
    # norAddr3IOTxnum()
    # try:
    #     print("norAddrA3InNtxTime")
    #     norAddrA3InNtxTime()
    # except Exception:
    #     traceback.print_exc()
    # try:
    #     print("norAddrA3OutNtxTime")
    #     norAddrA3OutNtxTime()
    # except Exception:
    # #     traceback.print_exc()
    # try:
    #     print("norAddrA3Intxnum")
    #     norAddrA3Intxnum()
    # except Exception:
    #     traceback.print_exc()
    # try:
    #     print("norAddrA3Outtxnum")
    #     norAddrA3Outtxnum()
    # except Exception:
    #     traceback.print_exc()
    fig11()
    # scamAvgIncomeOutcome()
    # norAddrA3LivingTime()
#gcn gdc tagcn
#收集整理大量数据时，尽量保存中间文件，即使由于机器性能原因或者ide设置原因等中断运行，也能避免效率的降低。
#涉及网络爬虫的工作中可能会出现由于当时的网络原因出现问题，包括但不限于整个代码停止运行，某个url的网站爬取失败，为此需要增加异常处理，以便于事后补充未完成的url爬取工作
