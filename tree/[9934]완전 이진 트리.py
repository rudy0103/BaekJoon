# https://www.acmicpc.net/problem/9934
# 완전 이진 트리

from sys import stdin as s
from collections import deque
# s= open("input.txt","rt")

k=int(s.readline())
seq=deque(map(int,s.readline().split()))
res=deque()
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def set_item(self,item):
        self.data=item
    
    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def makeRoot(self, node, left_node, right_node):
        if self.root ==None:
            self.root = node
        node.left = left_node
        node.right = right_node

    def inorderTraversal(self, node):
        if not node.left  == None :
             self.inorderTraversal(node.left)
        
        item=seq.popleft()
        node.set_item(item)
        
        if not node.right == None :
             self.inorderTraversal(node.right)

    def BFS(self,node):
        tmp=deque()
        tmp.append(node)
        while tmp:
            n=tmp.popleft()
            res.append(n.data)
            if n.left!=None:
                tmp.append(n.left)
            if n.right!=None:
                tmp.append(n.right)
        

# 0으로 채워진 완전 이진 트리 만들기
node = []
for i in range(pow(2,k)-1):
    node.append(Node(0))

tree=Tree()
for i in range(int(len(node)/2)):
    tree.makeRoot(node[i],node[i*2+1],node[i*2+2])


# 트리를 중위순회하면서 item을 넣어 원하는 트리 만들기
tree.inorderTraversal(tree.root)


# BFS로 노드 방문하면서 res 덱에 넣기
tree.BFS(tree.root)


# 출력하기
while res:
    for i in range(k):
        for j in range(pow(2,i)):
            print(res.popleft(),end=" ")
        print()








