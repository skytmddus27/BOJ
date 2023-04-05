'''
[그리디] 4월 5일 A와 B

- 뒤에서부터 접근해보자
- 두 코드는 동일함
   - b = b[-2::-1]
   - b = b[:-1]
     b = b[::-1]
'''

a = input()
b = input()
while len(b) != len(a):

    if (b[-1] == 'A'):
        b = b[:-1]
    elif (b[-1] == 'B'):
        b = b[-2::-1]

if b == a:
    print(1)
else:
    print(0)
    
'''
[그리디] 4월 5일 A와 B

문자열 뒤에 A를 추가한다. 문자열을 뒤집고 뒤에 B를 추가한다.
'''

# S = input()
# T = input()

# n = len(T) - len(S)
# for i in range(n):
#     if len(S) >= 2:
#         if S == T[:len(S)]:
#             if T[len(S)] == 'A':
#                 S = S + 'A'
#             else:
#                 break
#         elif S[::-1] == T[:len(S)]:
#             if T[len(S)] == 'B':
#                 S = S[::-1] + 'B'
#             else:
#                 break
#         else:
#             break
#     else:
#         if S == T[0]:
#             if T[1] == 'A':
#                 S = S + 'A'
#             elif T[:1] == 'BB':
#                 S = 'BB'
#             else:
#                 break
#         elif S == T[1]:
#             if T[0] == 'A':
#                 S = S + 'A'
#             elif T[0] == 'B':
#                 S = S + 'B'
#         else:
#             break
    

# if S == T:
#     print(1)
# else:
#     print(0)
