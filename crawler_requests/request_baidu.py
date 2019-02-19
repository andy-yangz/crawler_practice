import requests
keyword = "Python"
try:
    # kv = {'user-agent': 'Mozilla/5.0'} #模拟浏览器
    kv = {'wd':keyword}
    r = requests.get("https://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    # r.encoding = r.apparent_encoding
    print(r.text[:])
except:
    print("爬取失败")