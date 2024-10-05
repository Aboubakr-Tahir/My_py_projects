class Grid :
    def __init__(self):
        self.grid = [[0] * 2 for _ in range(2)]
    def solve (self , row =0 , col=0 ) : 
        I = [1 , 2]
        if row == len(self.grid) :
            print(self.grid)
            return True
        if col == len(self.grid) :
          return self.solve(row+1 , col =0)
        for guess in I :
            if self.is_valid(guess ,row , col) :
                self.grid [row] [col] = guess
                self.solve(row , col +1) 
                
                self.grid [row] [col] = 0 
                    
        return False          
                               
    def is_valid (self , guess ,  row , col) :
        if row == 0 and self.grid[row+1][col] == guess :
                return False
        elif row == 1 and self.grid[row -1][col] == guess :
                return False     
        if col == 0 and self.grid[row][col+1] == guess :
                return False
        elif col == 1 and self.grid[row][col -1 ] == guess :
                return False 
        return True                                 
gameboard =  Grid() 
gameboard.solve()          