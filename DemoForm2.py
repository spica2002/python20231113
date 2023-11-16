# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹서버와 통신
import requests
# 크롤링
from bs4 import BeautifulSoup

# 디자인파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼클래스 정의
class DemoForm(QMainWindow, form_class):
    # 초기화 매서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def firstClick(self):
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

        self.label.setText("당근에서 크롤링 완료.")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭하였음.")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭하였음.")

# 직접 모듈을 실행한 경우만 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec()

