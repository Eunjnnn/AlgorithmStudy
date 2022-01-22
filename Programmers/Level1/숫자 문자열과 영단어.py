def solution(s):
    answer = ''
    num_word = ''
    
    number = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for x in s:
        if x.isdigit():
            answer += x
        else:
            num_word += x
            if num_word in number.keys():
                answer += str(number[num_word])
                num_word = ''
    
    return int(answer)