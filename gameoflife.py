# live cell with fewer than two live neighbours dies, as if caused by under-population.
# live cell with two or three live neighbours lives on to the next generation.
# live cell with more than three live neighbours dies, as if by overcrowding.
# dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

w = 10
l = 10
    
class game(object):

    def __init__(self, height=10, width=10):
        
        self.grid = np.zeros((height, width))

        # Sets ROWS and COLS variable to size of the grid
        self.ROWS, self.COLS = self.grid.shape        
        self.ROWS = int(self.ROWS)
        self.COLS = int(self.COLS)

    def display(self):
        plt.imshow(self.grid, interpolation="none", cmap="binary")        
        
    def set_grid(self, item, pos = (0,0)):

        item_h, item_w = item.shape
        
        if pos[0] + item_h < self.ROWS and pos[1] + item_w < self.COLS:
            # Makes sure item fits in the grid
            self.grid[pos[0]:pos[0]+item_h, pos[1]:pos[1]+item_w] = item
    
        else:
            print "item is larger than grid"
            
    def count_neighbours(self, row, col):
        count = 0
        
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
            
                if not r == c == 0 and row+r>=0 and row+r<self.ROWS and col+c >=0 and col+c < self.COLS:
                    count += self.grid[row + r, col+c]
    
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
        
        grid_copy = self.grid.copy()
        
        for row in xrange(self.ROWS):
            for col in xrange(self.COLS):
                
                liveordie = self.live_or_die(row, col)                
                grid_copy[row][col] = liveordie
                
        self.grid = grid_copy


glider = np.array([[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]])

spaceship = np.array(
    [[0, 0, 1, 1, 0],
     [1, 1, 0, 1, 1],
     [1, 1, 1, 1, 0],
     [0, 1, 1, 0, 0]]) 
                 
pulsar = np.array(
    [[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]])



# Create game object
g = game(20, 20)
g.set_grid(glider)


g = game(20, 20)
g.set_grid(spaceship, (10, 0))

g = game(19, 19)
g.set_grid(pulsar, (3,3))

plt.imshow(g.grid, interpolation="none", cmap="binary")


# Animation

fig = plt.figure()
plt.axis('off')

ims = []

for i in xrange(50):
    ims.append((plt.imshow(g.grid, interpolation="none", cmap="binary"), ))
    g.next_state()

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=0, blit = True)

im_ani.save('im.mp4')


plt.show()


