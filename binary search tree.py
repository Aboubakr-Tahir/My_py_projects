class BST_node : 
    def __init__ (self , value) : 
        self.value = value 
        self.left = None 
        self.right = None 
        
    def add_child (self , value) : 
        if value == self.value :
            return 
        if value < self.value : 
            if self.left : 
                self.left.add_child (value) 
            else : 
                self.left = BST_node (value)  
        if value > self.value : 
            if self.right : 
                self.right.add_child(value)
            else :  
                self.right = BST_node (value)                 
                
    def in_order_traversal (self) : 
        elements = []
        if self.left :  
            elements += self.left.in_order_traversal()
        elements.append(self.value) 
        if self.right : 
            elements += self.right.in_order_traversal() 
        return elements  
    
    def search (self , value) :
        if value == self.value : 
            return True 
        if value < self.value : 
              if self.left : 
                  return self.left.search(value)
              else : 
                  return False 
        if value > self.value : 
            if self.right : 
                return self.right.search(value)
            else :
                return False       
        
    
def build_BST(elements) : 
        root = BST_node(elements[0])
        for i in range(1 , len(elements)) : 
           root.add_child(elements[i])
        return root         
    
elements = [17 , 25 , 99 , 28 , 14]
built_tree = build_BST(elements) 
print(built_tree.in_order_traversal()) 
print(built_tree.search(12)) 
                     