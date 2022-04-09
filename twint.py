import twint
#configuration
c = twint.Config()
c.Search = "0x0059b14e35daB1b4EEe1e2926C7A5660dA66F747"
c.Store_csv = True
c.Proxy_host = '10.112.235.161'
c.Proxy_port = 1080
c.Proxy_type = "http"
# Run
twint.run.Search(c)