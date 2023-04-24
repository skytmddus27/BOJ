# 시도 1: if else 구문 type() == str, int 형식 (실패)
# 시도 2: try except 구문 int() (1,2,3,14,15 런타임 에러)
# 시도 3:  숫자로 끝나는 경우 N이 0인채로 for문 종료되어 수정
# 시도 4: NUMBER는 한 글자에서 최대 "다섯" 글자 사이의 연속된 숫자

# HEAD 대소문자 구분 없이 사전 순 정렬
# NUMBER 0 무시하고 오름차순 정렬
# HEAD, NUMBER 동일할 경우 입력 순
def solution(files):
    HNT = []
    k = 0
    for file in files:
        H, N = 0, 0
        for i in range(len(file)):
            try:
                temp = int(file[i])
                H = i
                break
            except:
                continue
    
        for j in range(H, len(file)):
            try:
                temp = int(file[j])
                continue
            except:
                N = j
                break
        if N == 0:
            HEAD, NUMBER, TAIL = file[:H], file[H:], ''
        else:
            HEAD, NUMBER, TAIL = file[:H], file[H:N], file[N:]
        if len(NUMBER) > 5:
            NUMBER = NUMBER[:5]
        else:
            NUMBER = NUMBER
        HNT.append([k, HEAD.lower(), NUMBER.lstrip('0'), TAIL])
        k += 1
    # print(HNT)
    HNT = sorted(HNT, key=lambda x: (x[1], int(x[2]), x[0]))

    answer = []
    for k, HEAD, NUMBER, TAIL in HNT:
        answer.append(files[k])
    return answer

# https://school.programmers.co.kr/questions/40231
import re
def solution(file_names):
    filt = re.compile(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)')
    files = []
    for file_name in file_names:
        files.extend(filt.findall(file_name))
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in files]
    return answer