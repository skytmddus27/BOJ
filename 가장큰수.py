# 시도 1: 문자열로 만든 후 0번째 인덱스가 큰 순서로 출력 (실패)
# 시도 2: 34 > 3 > 30 (시간 초과 및 실패)
# 시도 3: num_padded로 뒤에 모두 0으로 채움
def solution(numbers):
    num = list(map(str, numbers))
    answer = ''
	# 시도 1
    num = sorted(num, key=lambda x: x[0], reverse=True)
	# 시도 3
    max_len = len(max(num, key=lambda x: len(x)))
    num_padded = []
    for i in num:
        num_padded.append(i[::-1].zfill(max_len)[::-1])
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if int(num_padded[i]) <= int(num_padded[j]):
                if '0' in num[j]:
                    pass
                else:
                    num[i], num[j] = num[j], num[i]
                    num_padded[i], num_padded[j] = num_padded[j], num_padded[i]
	# 시도 2
    # for i in range(len(num)):
    #     for j in range(i+1, len(num)):
    #         if num[i][0] == num[j][0]:
    #             if int(num[i]) < int(num[j]):
    #                 if '0' in num[j]:
    #                     pass
    #                 else:
    #                     num[i], num[j] = num[j], num[i]
    #             else:
    #                 if '0' in num[i]:
    #                     num[i], num[j] = num[j], num[i]
    #                 else:
    #                     pass
    answer += ''.join(num)
    return answer

# 시도 4: num과 num_padded를 리스트로 zip하고,
#		 num_padded를 기준으로 내림차순, num을 기준으로 오름차순
# [818, 81, 898, 89] -> 8989881881
def solution(numbers):
    num = list(map(str, numbers))
        
    max_len = len(max(num, key=lambda x: len(x)))
    num_padded = []
    for i in num:
        num_padded.append(i[::-1].zfill(max_len)[::-1])
    dic = list(zip(num, num_padded))
    # print(dic)
    sorted_list = list(sorted(dic, key=lambda x: (-int(x[1]), int(x[0]))))
    answer = ''
    for i, j in sorted_list:
        answer += i
    return answer

# https://school.programmers.co.kr/questions/45680
# 문자열인 채로 곱하기 4하여 sort
def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer