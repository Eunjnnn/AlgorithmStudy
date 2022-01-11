N = int(input())
X = list(map(int, input().split()))

com_X = list(sorted(set(X)))
# set 함수
# set은 수학에서 이야기하는 집합과 비슷
# 순서가 없고, 집합안에서는 unique한 값을 가짐
# 그리고 mutable 객체입니다.
# 중복되는 값 제거해줌

com_X = { com_X[i]:i for i in range(len(com_X))}
# dictionary
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}

print(*[com_X[i] for i in X])
# * : 공백
# [표현식 for 항목 in 반복가능객체]
