def solution(numbers, hand):
    answer = ''
    
    phone = {1: (0,0), 2: (0,1), 3: (0,2),
             4: (1,0), 5: (1,1), 6: (1,2),
             7: (2,0), 8: (2,1), 9: (2,2),
             '*': (3,0), 0: (3,1), '#': (3,2)}
    
    left_s = phone['*']
    right_s = phone['#']
    
    for num in numbers:
        current = phone[num]
        if num in [1, 4, 7]:
            answer += 'L'
            left_s = current
        elif num in [3, 6, 9]:
            answer += 'R'
            right_s = current
        else:
            left_d = abs(left_s[0] - current[0]) + abs(left_s[1] - current[1])
            right_d = abs(right_s[0] - current[0]) + abs(right_s[1] - current[1])
            if left_d == right_d:
                if hand == 'right':
                    answer += 'R'
                    right_s = current
                else: 
                    answer += 'L'
                    left_s = current
            elif left_d < right_d:
                answer += 'L'
                left_s = current
            else:
                answer += 'R'
                right_s = current
    
    return answer