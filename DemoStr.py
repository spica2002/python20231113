# DemoStr.py
#print(dir(str))

strA = "python is very beautiful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.startswith("py"))
print(strA.endswith("ful"))
print("---알파벳과 숫자로 구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam", "spam egg")
print("변환 결과")
print(result)
lst = result.split()
print(lst)
print("---다시 합치기---")
print(":)".join(lst))



