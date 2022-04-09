def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for l in range(i+1, len(numbers)):
            sum = numbers[i]+numbers[l]
            if sum not in answer:
                answer.append(numbers[i]+numbers[l])
            
    answer_ = sorted(answer)
    return answer_