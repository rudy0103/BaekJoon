N = int(input())
arr = list(map(int,input().split()))
result = [[] for i in range(N)]
def solve(node,d):
    L=len(node)
    if L==1:
        result[d].append(node[0])
        return
    result[d].append(node[L//2])
    left = node[:L//2]
    right = node[L//2+1:]
    solve(left,d+1)
    solve(right,d+1)
solve(arr,0)
for i in result:
    for j in i:
        print(j,end=" ")
    print()