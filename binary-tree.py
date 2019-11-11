class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.val)
  
r = Node(10) 
insert(r,Node(19)) 
insert(r,Node(6)) 
insert(r,Node(15)) 
insert(r,Node(11)) 
insert(r,Node(3)) 
insert(r,Node(2)) 
insert(r,Node(4)) 
insert(r,Node(7)) 
insert(r,Node(5)) 
  
inorder(r)
print()
preorder(r)
print()
postorder(r)
