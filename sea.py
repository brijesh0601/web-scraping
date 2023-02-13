from bs4 import BeautifulSoup 
import requests
url="https://www.medifee.com/hospitals-in-noida"
respone=requests.get(url)
# print(respone)
htmlcontent=respone.content
soup=BeautifulSoup(htmlcontent,"html.parser")
# t=soup.td.string
# for i in t:
# print(t)
print(soup.find_all('td'))