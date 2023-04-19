def solution(citations):
    ## 시도 3: [0, 0, 0, 0, 0] -> 0
    if sum(citations) == 0:
        return 0
    
    citations = sorted(citations, reverse=True)
	## 시도 1
    # mean = sum(citations) // len(citations)

    ## 시도 2: [5, 6, 7] -> 3
    ## 16번 테스트 케이스 제외 모두 통과
    mean = len(citations) // 2
    
    def upper(mean):
        half = 0
        for i in citations:
            if i >= mean:
                half += 1
            else:
                break
        return half
    
    def find_max_mean_plus_i(mean):
        i = 0
        while True:
            if upper(mean+i) >= mean+i:
                i += 1
            else:
                i -= 1
                break
        return mean+i

    return find_max_mean_plus_i(mean)