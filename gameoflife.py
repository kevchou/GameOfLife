# live cell with fewer than two live neighbours dies, as if caused by under-population.
# live cell with two or three live neighbours lives on to the next generation.
# live cell with more than three live neighbours dies, as if by overcrowding.
# dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import matplotlib.pyplot as plt

class game_grid(object):
    
    def __init__(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
          
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])
        
    def display(self):
        return plt.imshow(self.grid, interpolation="none", cmap = "binary")
        

    def count_neighbours(self, row, col):
        count = 0
        
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
            
                if not r == c == 0 and row+r>=0 and row+r<self.ROWS and col+c >=0 and col+c < self.COLS:
                    count += self.grid[row + r][col+c]
    
        return count
            
    def live_or_die(self, row, col):
        
        num_neighbours = self.count_neighbours(row, col)
        
        is_alive = self.grid[row][col]
        
        if is_alive and (num_neighbours < 2 or num_neighbours > 3):
            return 0
        
        elif (not is_alive) and (num_neighbours == 3):
            return 1
        
        return self.grid[row][col]
        
            
    def next_state(self):
        
        grid_copy = [x[:] for x in self.grid]
        
        for row in xrange(self.ROWS):
            for col in xrange(self.COLS):
                
                liveordie = self.live_or_die(row, col)                
                grid_copy[row][col] = liveordie
                
        self.grid = grid_copy
    

a = game_grid()
image = plt.imshow(a.grid)

