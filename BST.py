from itertools import count


class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key =  data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)        
            else:
                self.rchild = BST(data)
        
    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        
        if data < self.key:
            
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
                
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")
                
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
            
        print(self.key,end=" ") #printing root key
        
        if self.rchild:
            self.rchild.inorder()
            
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key,end=" ")
    
    def delete(self,data):
        if self.key is None:
            print("tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is not present in the tree")
        elif data> self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Node with smallest key is :",current.key)
        
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node maximum node : ",current.key)
        
        
            
    
def count(node):
        if node is None:
            return 0
        else:
            return 1+ count(node.lchild)+count(node.rchild)
                        
         
            
        
root = BST(10)
list1 = [20,4,30,4,1,5,4]
for i in list1:
    root.insert(i) 
    

root.search(5)
print("\nPreorder",end="\n")
root.preorder()
print("\nInorder",end='\n')
root.inorder()
print("\nPostOrder",end='\n')
root.postOrder()

if count(root)>1:
    root.delete(10)
else:
    print("Can't not delete root node")
    
    
root.delete(30)
print()
root.inorder()

root.min_node()
root.max_node()