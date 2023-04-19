def solution(array, commands):
    answer = []
    for i, j, k in commands:
        cut = array[i-1:j]
        cut = sorted(cut)
        answer.append(cut[k-1])
    return answer