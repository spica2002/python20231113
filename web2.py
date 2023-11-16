# web2.py

# 웹서버와 통신
import requests
# 크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# 파일 생성
f = open("dangn.txt", "wt", encoding="utf-8")

posts = soup.find_all("div", attrs={"class":"card-desc"})

for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    #print(title)
    price = post.find("div", attrs={"class":"card-price"})
    #print(price)
    addr = post.find("div", attrs={"class":"card-region-name"})
    #print(addr)
    print("{0},{1},{2}".format(title.text.strip().replace("\n",""),price.text.strip().replace("\n",""),addr.text.strip().replace("\n","")))
    title = title.text.strip().replace("\n", "")
    price = price.text.strip().replace("\n", "")
    addr = addr.text.strip().replace("\n", "")
    f.write(f"{title}, {price},{addr}\n")

f.close()

# <div class="card-desc">
#   <h2 class="card-title">삼성텔레비전65인치</h2>
#   <div class="card-price ">
#     150,000원
#   </div>
#   <div class="card-region-name">
#     서울 서초구 반포2동
#   </div>
