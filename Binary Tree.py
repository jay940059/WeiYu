class Node(object):
    def __init__(self,val):
        self.parent = None
        self.left = None
        self.right = None
        self.element=val
       
class Binary Tree:
    
    def __init__(self):
        self.root=None
        self.leaf=None
        self.size=None

