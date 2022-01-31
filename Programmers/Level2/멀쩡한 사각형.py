### 최대공약수 사용

import math

def solution(w,h):
    answer = 1
    all_rec = w * h
    
    answer = all_rec - (w+h-math.gcd(w, h))
    
    return answer