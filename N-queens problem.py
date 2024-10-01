class Queens :
    def __init__ (self, size) :
        self.size = size 
        self.board = [[0] * self.size for _ in range(self.size)]
    
    def is_valid(self , row , col) :
        #lets check for  column first :
        for i in range(self.size) :
            if self.board[i][col] == 1 :
                return False 
        #check for row after :    
        for j in range(self.size) :
            if self.board[row][j] == 1 :
                return False    
        #top left diagonal check :
        for i , j in zip(range(row , -1 ,-1) , range(col , -1 , -1)):
            if self.board[i][j] == 1 :
                return False    
        #top right diagonal check : 
        for i , j in zip(range(row , -1 , -1) , range(col , self.size)) :
            if self.board[i][j] == 1 :
                return False
        return True     
    
    def solve (self,row=0) :
        if row == self.size :
            for row in self.board :
                print(row)
            return True
        for col in range(self.size) :
            if self.is_valid (row , col) :
                self.board [row][col] = 1
                
                self.solve(row+1)
                   
            
                self.board[row][col] = 0 
        return ''   
        
chessboard = Queens(4) 
print(chessboard.solve())         
