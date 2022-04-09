from json.tool import main
import twint
import traceback
#configuration
from ast import literal_eval
def mytwint():
    with open('addr.txt','r',encoding='utf-8') as f:
        addrlist = literal_eval(f.read())
    # addrlist = ['0x0059b14e35daB1b4EEe1e2926C7A5660dA66F747']
    addr1 = '0x855f22809df5f5222d70f8df47369462c555db0d'#因为下标错误而遗漏的
    addr = '0xa484d40cfa8f82ee15b135d3d8fecd34bdc9e444'
    myindex = addrlist.index(addr)
    addrlist = addrlist[myindex:].append(addr1)
    try:
        for addr in addrlist:
            c = twint.Config()
            c.Search = addr
            # print(type(addr))
            c.Store_csv = True
            # c.Proxy_host = '47.88.50.108'
            # c.Proxy_port = 1080
            # c.Proxy_host = '10.112.235.161'
            # c.Proxy_port = 1080            
            # c.Proxy_type = "http"
            # c.Count = True
            c.Lang = "en"
            # c.Min_wait_time = 10
            c.Retries_count = 2
            c.Output = '/home/t3.csv'
            # Run
            twint.run.Search(c)
    except Exception:
        traceback.print_exc()
        print(addr)
if __name__ == '__main__':
    mytwint()
# import twint

# # 配置
# c = twint.Config()
# # 要爬取的用户
# c.Username = "realDonaldTrump"
# # 关键词
# c.Search = "great"
# c.Proxy_host = '10.112.235.161'
# c.Proxy_port = 1080            
# c.Proxy_type = "http"
# # 启动
# twint.run.Search(c)