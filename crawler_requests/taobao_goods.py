import requests
import re
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

def getHTMLtext(url):
  try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
  except:
    print("爬取失败")
  return r.text

def parsePage(goods, html):
  try:
    plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
    for i in range(len(plt)):
      price = eval(plt[i].split(':')[1])
      title = eval(tlt[i].split(':')[1])
      goods.append([price, title])
  except:
    print("")


def printGoodList(goods):
  print("")

def main():
  key = "书包"
  depth = 2
  start_url = "https://s.taobao.com/search?q="+key
  goodslist=[]
  for i in range(depth):
    try:
      url = start_url + '&s=' + str(44*i)
      html = getHTMLtext(url)
      print(html)
      exit()
      parsePage(goodslist, html)
    except:
      continue
  printGoodList(goodslist)

main()
