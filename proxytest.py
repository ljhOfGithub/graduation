import requests
import random
import time

http_ip = [
    # '47.88.50.108:1080',
    '10.112.235.161:1080'
]

for i in range(10):
    try:
        ip_proxy = random.choice(http_ip)
        proxy_ip = {
            'http': ip_proxy,
            'https': ip_proxy,
        }
        print('使用代理的IP:', proxy_ip)
        response = requests.get("http://httpbin.org/ip", proxies=proxy_ip).text
        print(response)
        print('当前IP有效')
        time.sleep(2)
    except Exception as e:
        print(e.args[0])
        print('当前IP无效')
        continue
#验证代理ip是否有效