#include <iostream>
 
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print tree.value
 
 
def in_order(tree):
    stk = []
    nodeCurrent = tree                          #sets current node to the start of the tree
    isOrdered = 0                               #counter to say if element is done
    while (not isOrdered):                      
        if nodeCurrent is not None:             #Goes to the leftmost item in the tree
            stk.append(nodeCurrent)
            nodeCurrent = nodeCurrent.left      #places pointer on left before traversal
        else:
            if len(stk)> 0:                     #backtracks from empty and visits first node again
                nodeCurrent = stk.pop()
                print (nodeCurrent.data)
                nodeCurrent = nodeCurrent.right    #starts the right subtree after the left is finished
            else:
                isOrdered = 1
        
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
