from json.tool import main
import twint
#configuration
from ast import literal_eval
def mytwint():
    # with open('addr.txt','r',encoding='utf-8') as f:
    #     addrlist = literal_eval(f.read())
    addrlist = ['0x0059b14e35daB1b4EEe1e2926C7A5660dA66F747']
    try:
        for addr in addrlist:
            c = twint.Config()
            c.Search = addr
            print(type(addr))
            c.Store_csv = True
            # c.Proxy_host = '47.88.50.108'
            # c.Proxy_port = 1080
            # c.Proxy_type = "http"
            # c.Count = True
            c.Lang = "en"
            # c.Min_wait_time = 10
            c.Retries_count = 4
            c.Output = 't.csv'
            # Run
            twint.run.Search(c)
    except Exception:
        pass
if __name__ == '__main__':
    mytwint()