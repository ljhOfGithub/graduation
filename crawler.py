from selenium import webdriver
import time
import requests
from ast import literal_eval
import csv
import xlrd
apikey = "ZF9TQA39PFPPUD7VCDK2Q9ZVD2M72N2HGZ"
def deduplicate():
    with open('bitpoint.txt','r') as f:
        list1 = literal_eval(f.read())
    with open('cryptopia.txt','r') as f:
        list2 = literal_eval(f.read())
    with open('etherdelta.txt','r') as f:
        list3 = literal_eval(f.read())
    with open('LendfMe.txt','r') as f:
        list4 = literal_eval(f.read())
    with open('phishaddr.txt','r') as f:
        list5 = literal_eval(f.read())
    with open('upbit.txt','r') as f:
        list6 = literal_eval(f.read())
    with open('scam.txt','r') as f:
        list7 = literal_eval(f.read())
    with open('db.txt','r') as f:
        list8 = literal_eval(f.read())
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
def getNtxs():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    addrlist = addrlist[0:2000]
    session = requests.Session()
    with open('ntx1.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["blockNumber","timeStamp","hash","nonce","blockHash","transactionIndex",
                         "from","to","value","gas","gasPrice","isError","txreceipt_status","input",
                         "contractAddress","cumulativeGasUsed","gasUsed","confirmations"])
        for addr in addrlist:
            url = "https://api.etherscan.io/api?module=account&action=txlist&address="+addr+"&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + apikey
            result = literal_eval(session.get(url).text)['result']
            if len(result) and result != "Error!":
                print(result)
                print(type(result))

if __name__ == '__main__':
    deduplicate()
    # readxlsx()