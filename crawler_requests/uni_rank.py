import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
  "Get the text information from url page"
  try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
  except:
    print("爬取失败")
  return r.text

def fillUnivList(ulist, html):
  "Parse the original html page to good structured form."
  soup = BeautifulSoup(html, "html.parser")
  for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
      tds = tr('td')
      ulist.append([tag.string for tag in tds[:4]])

def printUnivList(ulist, num):
  print("{:^10}\t{:^20}\t{:^10}\t{:^10}\n".format("排名", "学校名", "地点", "总分"))
  for uni in ulist[:num]:
    print("{:^10}\t{:^20}\t{:^10}\t{:^10}\n".format(*uni))

def main():
  uinfo = []
  url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
  html = getHTMLText(url)
  fillUnivList(uinfo, html)
  printUnivList(uinfo, 20)

main()