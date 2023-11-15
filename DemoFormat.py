# DemoFormat.py

for i in range(1,11):
  URL = "https://multi.com/?page=" + str(i)
  print(URL)

print("---숫자 출력---")
for x in range(1,6):
  print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
  print(x,"*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
  print(x,"*",x,"=",str(x*x).zfill(5))

  