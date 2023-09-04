from collections import deque

class Node:
    def __init__(self, item):
        self.item = item
        self.left = self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self):
        def _preorder(node):
            print(node.item, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
    
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end=' ')
        _postorder(self.root)
        
    def levelorder(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

l=[Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7)]
d={'8':Node(8)}
BT = BinaryTree()

BT.root = l[0]
l[0].left = l[1]
l[0].right = l[2]
l[1].left = l[3]
l[1].right = l[4]
l[2].left = l[5]
l[2].right = l[6]
l[3].left = d['8']

print('preorder')
BT.preorder()

print('\ninorder')
BT.inorder()

print('\npostorder')
BT.postorder()

print('\nlevelorder')
BT.levelorder()