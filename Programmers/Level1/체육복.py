def solution(n, lost, reserve):
    # 방법 1
    """
    _lost = sorted([l for l in lost if l not in reserve])
    _reserve = sorted([r for r in reserve if r not in lost])
    answer = n - len(_lost)
    
    for l in _lost:
        for x in [-1, 1]:
            if x + l in _reserve:
                answer += 1
                _reserve.remove(l+x)
                break
    """

    #방법 2
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
    answer = n - len(set_lost)
                
    return answer