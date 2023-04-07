def solution(name):
    answer = 0
    
    num_list = [min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name]
    #상하로 갯수 미리 세서 걍 다 더해놓기.
    answer += sum(num_list)
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        
        next_i = i+1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    
    return answer+min_move

'''
[그리디] 4월 5일 조이스틱

A가 하나면 상관없는데 여러 개면 뒤로 갔다가 다시 앞으로 오는게 더 일 아닐까..
A가 하나일 때, A가 연속일 때 : 뒤로 갔다가 앞으로 오기
A가 띄엄띄엄 있을 때 : 그냥 하나씩 차례로 진행하기

12번 TC: "AAAAABBAAAAAAABAAA"
A의 위치도 알아야 하네 어떻게 해야해...
'''
# def solution(name):
#     alpha = {"B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7,
#             "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":12,
#             "P":11, "Q":10, "R":9, "S":8, "T":7, "U":6, "V":5,
#             "W":4, "X":3, "Y":2, "Z":1, "A":0}
#     answer = 0
#     for i in name:
#         answer += alpha[i]
        
#     if "A" in name:
#         a_cnt = 0
#         for i in range(len(name)):
#             if name[i] == "A":
#                 a_cnt += 1
#         answer += len(name) - 1
#         if a_cnt == len(name):
#             answer -= len(name) - 1
#         else:
#             for i in range(a_cnt, 0, -1):
#                 if "A" * i in name:
#                     answer -= i
#                     break

#     else:
#         answer += len(name) - 1
#     return answer
