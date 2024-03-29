## Python의 heapq 모듈 !

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while scoville[0] < K:
        result = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, result)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer