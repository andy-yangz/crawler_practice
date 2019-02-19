import requests
ip = "202.204.80.112"
try:
    kv = {'ip': ip}
    r = requests.get("http://www.ip138.com/ips138.asp", params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")