class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def add():
    l=[4,6,7,3,8,2,5,9,1]
    root=Node(l[0])
    l.pop(0)
    for i in l:
        BST(i,root)
    return root
def BST(value,root):
    if root is None:
        root=Node(value)
    if root.value<value:
        if root.right is None:
            root.right=Node(value)
        else:
            root.right=BST(value,root.right)
    else:
        if root.left is None:
            root.left=Node(value)
        else:
            root.left=BST(value,root.left)
    return root 
#For preorder Root,Left,Right
def preorder(root):
    if root==None:
        return 
    print(root.value)
    preorder(root.left)
    preorder(root.right)
# Inorder Left,Root,Right
root=add()
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

# Postorder Left Right Root
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
def level_order(root):
    Q=[root]
    Q.append(None)
    while len(Q)!=0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
level_order(root)
def print_height(root):
    if root==None:
        return 0
    LH=print_height(root.left)
    RH=print_height(root.right)
    return max(LH,RH)+1


#               1
#            /    \
#           2      3
#          / \    / \
#         4   5  6   7
#            / \     \
#           9   10    11
#          / \
#         12  13

# preorder(root)
# print("\n")
# postorder(root)
# print("\n")
# inorder(root)
# level_order(root)
# print("\n",print_height(root))
