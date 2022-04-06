def solution(d, budget):
    answer = 0
    d_array = sorted(d)
    
    for i in d_array:
        if budget >= i:
            budget -= i
            answer +=1 
        
    return answer

# Sort() → list.sort() : 리스트를 제자리에서 수정 -> 원래 변수가 수정됨.
#                        반환값은 None -> 따라서 arr = list.sort() 실행 시 arr에는 None값 저장됨
# Sorted() → sorted(list) : 반환값이 배열값(변수에 저장 가능! 원래 변수는 수정되지 않음.)