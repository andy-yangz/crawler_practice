import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(slist, url):
  html = getHTMLText(url)
  soup = BeautifulSoup(html, 'html.parser')
  a = soup.find_all('a')
  for i in a:
    try:
      href = i.attrs['href']
      slist.append(re.findall(r"[s][hz]\d{6}", href)[0])
    except:
      continue

def getStockInfo(slist, stockurl, output_file):
  count = 0
  for stock in slist:
    url = stockurl + stock + ".html"
    html = getHTMLText(url)
    try:
      if html=="":
        continue
      infoDict = {}
      soup = BeautifulSoup(html, 'html.parser')
      stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
      
      name = stockInfo.find_all('a', attrs={'class': 'bets-name'})[0]
      infoDict["股票名称"] = name.text
      print(name.text)

      keyList = stockInfo.find_all('dt')
      valueList = stockInfo.find_all('dd')
      for i in range(len(keyList)):
        key = keyList[i].text
        value = valueList[i].text
        infoDict[key] = value

      with open(output_file, 'a') as f:
        f.write(str(infoDict) + '\n')
        count += 1
        print("\r进度: {:.2f}".format(count*100/len(slist)), end="") 
    except:
      count += 1
      print("\r进度: {:.2f}".format(count*100/len(slist)), end="") 
      continue

def main():
  stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
  stock_info_url = 'https://gupiao.baidu.com/stock'
  output_file = 'C:/Users/surface/Documents/Code/crawler/BaiduStock.txt'
  
  slist = []
  getStockList(slist, stock_list_url)
  getStockInfo(slist, stock_info_url, output_file)

main()