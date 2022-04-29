from collections import deque

# BFS


def solution(numbers, target):
    answer = 0
    l = len(numbers)
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        num, index = queue.popleft()
        # print('num: ', num, 'index: ', index)
        index += 1
        if index == l:
            if num == target:
                answer += 1
        else:
            queue.append([num + numbers[index], index])
            queue.append([num + -1*numbers[index], index])
        # print(queue)

    return answer

# DFS


def dfs(numbers, target, dep):
    answer = 0
    l = len(numbers)

    if l == dep:
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, dep+1)
        numbers[dep] *= -1
        answer += dfs(numbers, target, dep+1)
        return answer


def solution(numbers, target):
    return dfs(numbers, target, 0)
