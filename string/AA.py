import sys
from collections import defaultdict

input = sys.stdin.readline


def do_game():
    loc = defaultdict(list)
    count = defaultdict(int)

    for idx, letter in enumerate(W):
        loc[letter].append(idx)
        count[letter] += 1

    for k, v in count.items():
        if v < K:
            del loc[k]

    if not loc:
        return -1, -1

    diff = []
    for k, l in loc.items():
        for i in range(len(l) - K + 1):
            diff.append(l[i + K - 1] - l[i] + 1)

    return min(diff), max(diff)


T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    W, K = input().rstrip(), int(input())  # 문자열, 정수
    if K == 1:
        print(1, 1)
    else:
        l1, l2 = do_game()
        if l1 == -1:
            print(-1)
        else:
            print(l1, l2)