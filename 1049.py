'''
[그리디] 4/3 기타줄

6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
같은 브랜드 내에서 6줄 패키지가 낱개 6개보다 저렴할 거라는 편견을 깨라.
'''

n, m = map(int, input().split())
package, piece = [], []
for _ in range(m):
    i, j = map(int, input().split())
    package.append(i)
    piece.append(j)

result = 0
if n < 6:
    if min(piece) * n <= min(package):
        result = min(piece) * n
    else:
        result = min(package)
else:
    if min(piece) * 6 <= min(package):
        result = min(piece) * 6 * (n // 6)
    else:
        result = min(package) * (n // 6)
        
    if n % 6 != 0:
        if min(piece) * (n % 6) <= min(package):
            result += min(piece) * (n % 6)
        else:
            result += min(package)
# else:
#     result = min(package) * (n // 6)
#     if min(piece) * (n % 6) <= min(package):
#         result += min(piece) * (n % 6)
#     else:
#         result += min(package)
        
print(result)