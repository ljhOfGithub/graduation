from search_engines import Google
from ast import literal_eval
import time
import argparse
import os
import traceback
# import arg
# def mysearch(csvaddr='0x5b27531228d8c65a0d2adcd8903fd3348f768a11'):
# def mysearch(csvaddr='0xb01fce059d66971fdc1e584a5cbf0116068c9048'):
# def mysearch(csvaddr='0x81e4b65b9330c5693d38430111d7eb174615bdd6'):
# def mysearch(csvaddr='0x98831a269cb88b6bfcc86e45b32c158981b34b22'):
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-q', help='query to search', default='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91')
    args = ap.parse_args()
    csvaddr = args.q
    mysearch(csvaddr)

def mysearch(csvaddr='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'):
    with open('addr.txt','r') as f:
        addrlist = literal_eval(f.read())
    # addrlist = ['0x516980e3321482b51b0e10af2770d6fbd47f6f9f']
    # addr = '0x44a7ff01f7d38c73530c279e19d31527bdcf8c78'
    # addr = '0x67dc51fca0626bcb18eaf82a0e8aa355019b8723'
    # addr = '0xaa1ea8f6cdeeb491d9cf9fcdfc8fec6b4040d1c4'
    # csvaddr = '0xc31fb4c352cb68c847715d46d97c1fa2aa2d0f00'
    # csvaddr = '0xa1b04a60a35854d0749ae39b0346bceb55247ecc'
    # csvaddr = '0x5b27531228d8c65a0d2adcd8903fd3348f768a11'
    count = 0
    myindex = addrlist.index(csvaddr)
    addrlist = addrlist[myindex:]
    engine = Google()
    for addr in addrlist:
        try:
            engine.set_search_operator('host')#设置为url将过滤
            results = engine.search(addr)
            filename = 'mycsv/' + addr
            engine.output('csv',filename)
            links = results.links()
            time.sleep(2)
        except Exception:
            print('reboot')
            time.sleep(5)
            myindex = addrlist.index(addr) - 1#
            rebootaddr = addrlist[myindex]
            count += 1
            if count >= 50:
                quit()
            # mysearch(rebootaddr)
            os.execv('/root/.miniconda3/envs/twvenv/bin/python',['python','t.py','-q',rebootaddr])
            # print(addr)
            # results = engine.search(addr)
            # engine.output('html',filename)
    # print(links)
def winsearch(csvaddr='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'):#Linux最后一个没有爬到的结果
# def winsearch(csvaddr='0x150f70875c0229daa9c46e461498f81ab9a76a81'):
# def winsearch(csvaddr='0x3047c9d8ba82571f147a8603909c6cc42fc7cd6e'):
# def winsearch(csvaddr='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'):
# def winsearch(csvaddr='0xb5f3a62e8f0468efec0a65b81c09e8b46d1f9158'):
# def winsearch(csvaddr='0xed0f9fcdf76506242f1b9f499bcc41c60ac99180'):
# def winsearch(csvaddr='0x0f65ed6419a54ea5c55d871af77aef0086287dd4'):
# def winsearch(csvaddr='0xd3ddae456004ed85639a39a9751192e80a967ed4'):
# def winsearch(csvaddr='0xf3bf6a9b4dfb2d196fdd6c8e373591ca1de58604'):#用来验证重启程序是否正常的地址，需要在重新开始爬取时进行验证，后爬取的地址是否还包含前爬取地址的结果
    with open('addr.txt','r') as f:
        addrlist = literal_eval(f.read())
        # csvaddr = '0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'
        count = 0
        myindex = addrlist.index(csvaddr)
        addrlist = addrlist[myindex:]
        addrlist.append('0x3bf351a62df57dce8512b136daa4cd6ebe2dda91')
        engine = Google()
    for addr in addrlist:
        try:
            engine.set_search_operator('url')  # 设置为将对应的host过滤掉
            results = engine.search(addr)
            filename = 'mycsv/' + addr
            engine.output('csv', filename)#如果递归处理
            time.sleep(0.5)
        except Exception:
            print('reboot')
            time.sleep(5)
            myindex = addrlist.index(addr) - 1  #
            rebootaddr = addrlist[myindex]
            count += 1
            if count >= 50:
                quit()
            traceback.print_exc()
            winsearch(rebootaddr)
            os.execv(r'C:\Users\ljh\miniconda3\python.exe', ['python', 't.py', '-q', rebootaddr])
#0x3bf351a62df57dce8512b136daa4cd6ebe2dda91
#0xd67e205a5b7a5d82b86afbc59f67f74a878d1e68
#漏掉的:
#0xb5f3a62e8f0468efec0a65b81c09e8b46d1f9158
#0xed0f9fcdf76506242f1b9f499bcc41c60ac99180
#0x0f65ed6419a54ea5c55d871af77aef0086287dd4
if __name__ == '__main__':
    # mysearch()
    # main()
    winsearch()

#python t.py -q 0x3bf351a62df57dce8512b136daa4cd6ebe2dda91