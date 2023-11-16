import re 

f=open('PV3.txt','rt')
g=open('PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()


# chatGPT가 달아준 주석
import re

# 'PV3.txt' 파일을 읽기 모드로 열고, 'PV3_copy.txt' 파일을 쓰기 모드로 열어서 인코딩을 UTF-8로 설정합니다.
f = open('PV3.txt', 'rt')
g = open('PV3_copy.txt', 'wt', encoding='utf-8')

# 'f'에서 한 줄을 읽어옵니다.
line = f.readline()

# 줄이 빈 문자열이 아닌 동안 반복합니다.
while line != '':
    # 만약 현재 줄에 "error" 문자열이 포함되어 있다면,
    if re.search("error", line):
        # 'g' 파일에 현재 줄을 쓰고 개행 문자를 추가합니다.
        g.write(line + "\n")
    
    # 다음 줄을 읽어옵니다.
    line = f.readline()

# 파일을 닫습니다.
f.close()
g.close()






