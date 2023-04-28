'''
[이진탐색] 4월 28일 가사 검색
queries에 해당하는 words의 수를 리스트 형태로 반환

성공은 했으나, 효율성 면에서 실패
'''

# def soltuion(words, queries):
#     answer = []
#     for qw in queries:
#         cnt = 0
#         for word in words:
#             i = 0
#             if len(qw) == len(word):
#                 for q in qw:
#                     if q == "?":
#                         i += 1
#                     elif q == word[i]:
#                         i += 1
#             if i == len(qw):
#                 cnt += 1
#         answer.append(cnt)
#     return answer

from bisect import bisect_left, bisect_right

def count_by_range(lst, left_value, right_value):
    left_index = bisect_left(lst, left_value)
    right_index = bisect_right(lst, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    words_by_length = [[] for _ in range(10001)]
    words_by_length_reversed = [[] for _ in range(10001)]

    for word in words:
        words_by_length[len(word)].append(word)
        words_by_length_reversed[len(word)].append(word[::-1])

    for i in range(10001):
        words_by_length[i].sort()
        words_by_length_reversed[i].sort()

    for query in queries:
        if query[0] == "?":
            count = count_by_range(words_by_length_reversed[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        else:
            count = count_by_range(words_by_length[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        answer.append(count)
    return answer
