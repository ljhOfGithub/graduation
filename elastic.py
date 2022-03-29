from elasticsearch import Elasticsearch
import json
import paramiko
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
import os

def main():
    import paramiko
    pkey = paramiko.RSAKey.from_private_key_file(r'C:\Users\ljh\.ssh\id_bupt')
    gateway = paramiko.SSHClient()
    gateway.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    # gateway.connect(hostname="172.29.98.139", port=10085, username="bupt", timeout=5000)
    gateway.connect(hostname="121.40.17.238", port=10065, username="bupt", timeout=5000, pkey=pkey)

    # 关键就这一步了
    # sock = gateway.get_transport().open_channel('direct-tcpip', ('121.40.17.238', int(10065)), ('', 0))
    sock = gateway.get_transport().open_channel('direct-tcpip', ('172.29.98.139', int(10085)), ('', 0))

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    # ssh.connect(hostname="121.40.17.238", port=10065, username="bupt", sock=sock, timeout=5000)
    ssh.connect(hostname="172.29.98.139", port=10085, username="bupt", sock=sock, timeout=5000, pkey=pkey)

    session = ssh.get_transport().open_session()

    session.exec_command('uptime')

    exit_status = session.recv_exit_status()
    stdout = session.makefile('r').read()
    stderr = session.makefile_stderr('r').read()

    print(exit_status, stdout, stderr)

    ssh.close()
    gateway.close()


# # elastic = Elasticsearch("http://es-cn-2r42bvamz006ajce9.elasticsearch.aliyuncs.com:9200", timeout=4000, http_auth=('BUPT', 'wetfYg-gedhav-0pukje'))
# elastic = Elasticsearch("http://es-cn-2r42bvamz006ajce9.elasticsearch.aliyuncs.com:9200", timeout=4000, http_auth=('BUPT', 'wetfYg-gedhav-0pukje'))
#
# print(elastic)
#
# response = elastic.search(index="eth_block_realtime", body={
#     "_source": False,
#     "query": {"nested": {
#         "path": "Transactions",
#         "query": {"bool": {"filter": {"term": {
#         "Transactions.Hash": "0x4c24a45d972e9a59e0b8a74dc2d312e9642e66e0157725784ed0a1b1aa8cf701"
#         }}}},
#         "inner_hits": {
#         "_source": ["Transactions.CallFunction", "Transactions.CallParameter","Transactions.hash"]
#         }
#     }}
# }
# )
# print(json.dumps(response, indent=4))
if __name__ == '__main__':
    main()