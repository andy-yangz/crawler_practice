import requests
url = "https://item.jd.com/8735304.html"
try:
    # kv = {'user-agent': 'Mozilla/5.0'} #模拟浏览器
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")