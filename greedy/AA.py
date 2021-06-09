from sys import stdin
import heapq


N = int(stdin.readline())
meetings, heap = [], []

for i in range(N):
    start, end = map(int, stdin.readline().split())
    meetings += [[start, end]]

meetings = sorted(meetings, key = lambda k: k[0])
heapq.heappush(heap, meetings[0][1])

for meeting in meetings[1:]:
    if heap[0] <= meeting[0]:
        heapq.heappushpop(heap, meeting[1])
    else:
        heapq.heappush(heap, meeting[1])

print(len(heap))