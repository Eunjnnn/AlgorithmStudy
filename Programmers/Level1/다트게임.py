# 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 
# 아차상(#) 당첨 시 해당 점수는 마이너스된다.

def solution(dartResult):
    answer = 0
    dartResult = dartResult.replace("10", 'A')
    square = {'S' : 1, 'D' : 2, 'T' : 3}
    stack = []
    
    for d in dartResult:
        if d.isdigit() or d == 'A':
            stack.append(10 if d == 'A' else int(d))
        elif d in square:
            stack[-1] = pow(stack[-1], square[d])
        elif d == '*':
            if len(stack) >= 2:
                stack[-1] *= 2
                stack[-2] *= 2
            else:
                stack[-1] *= 2
        elif d == '#':
            stack[-1] *= -1
            
    
    print(stack)
    return sum(stack)