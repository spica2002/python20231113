class MyClass:
    def __init__(self, value):
        self.Value = value 
        print("Class is created! Value = ", value)
        
    def __del__(self):
        print("Class is deleted!")
        

# 메모리관리 자동
d = MyClass(5)
#del d

print("전체 코드 실행 종료")