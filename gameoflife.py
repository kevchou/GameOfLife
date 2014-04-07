# live cell with fewer than two live neighbours dies, as if caused by under-population.
# live cell with two or three live neighbours lives on to the next generation.
# live cell with more than three live neighbours dies, as if by overcrowding.
# dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



w = 10
l = 10

test = np.zeros((w,l))
glider = np.array([[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]])

def set_grid(grid, item, pos = (0,0)):
    
    new_grid = grid.copy()    
    
    grid_h, grid_w = grid.shape
    item_h, item_w = item.shape
    
    if pos[0] + item_h < grid_h and pos[1] + item_w < grid_w:
        new_grid[pos[0]:pos[0]+item_h, pos[1]:pos[1]+item_w] = item

    else:
        print "item is larger than grid"
        
    return new_grid    
    
        


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
    

fig = plt.figure()

ims = []

a = game_grid()

for i in xrange(100):
    ims.append((plt.imshow(a.grid, interpolation="none", cmap="binary"), ))
    a.next_state()

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=100, blit = True)
im_ani.save('im.mp4')

plt.show()


