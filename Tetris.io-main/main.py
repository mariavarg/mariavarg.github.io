import pygame
import random
import pygame.mixer


pygame.mixer.music.load("06-Kashmir.mp3")
pygame.mixer.music.play(-1)

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 450
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    pass

def create_grid(locked_positions={}):
    pass

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    pass

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pass

def main():
    pass

def main_menu():
    pass

main_menu()  # start game
# Piece Class
# Since we will be creating multiple shapes it makes sense to create a piece class that can store some information about each shape.

class Piece(object):
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3
# Creating a Grid
# The way that we will keep track of pieces in the game is using a grid data structure. We will create a multidimensional list that contains 20 lists of 10 elements (rows and columns). Each element in the lists will be a tuple representing the color of the piece in that current position. This will allow us to draw all of the colored squares quite easily as we can simply loop through the multidimensional list.

# The locked position parameter will contain a dictionary of key value pairs where each key is a position of a piece that has already fallen and each value is its color. We will loop through these locked positions and modify our blank grid to show these pieces.

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid
# Getting a Random Shape
# Since we will be dropping shapes down the screen at random we need to generate a random shape. This will be done in the get_shape() function.

def get_shape():
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))
# Drawing the Grid
# I am not going to explain all of the pygame functions and methods I use as if you are familair with pygame you should know them. However, if you'd like to learn more about the basics of pygame click here!

# We will simply be calling the function below to draw all of our objects to the screen. In this function we call some functions that we will be coding later.

    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('Agdasima-Bold.ttf', 60)
    label = font.render(\'TETRIS\', 1, (255,255,255))
 
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    pygame.display.update()
# The Game Loop
# In every game we have something called a game loop or a main loop. This is what will be running constantly and checking to see if events occur. Our game loop will go inside the main() function.

# In this function we will start by defining some variables and then move into the while loop. Inside the while loop we will check for key press events and see if the user wants to exit the game.

# When the user presses the up arrow key the piece will rotate. We can do this by simply increasing our shapes rotation attribute to be the next shape in the list we set up at the beginning of the program.

# When the user hits the left or right arrow keys we will move accordingly bu changing the x value of our piece.

# Finally when the user hist the down arrow key we will move down one square allowing the user to increase the speed at which the shape falls.

def main():
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        # draw_window(win)
# We will be adding more to this function in the future.

# Setting up The Window
# The last thing we need to do for this tutorial is setup the pygame window and give it a caption. This will go at the very end of the program, not within any function.

win = pygame.display.set_mode((s_width=450px, s_height))
pygame.display.set_caption(\'Tetris\')
Testing The Program
If you'd like to test the program you can simply call main() at the very end of the program like so.

main()

pygame.mixer.music.stop()
