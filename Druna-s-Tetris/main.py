import pygame
import random

pygame.font.init()
pygame.init()

# GLOBALS VARS
s_width = 450
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = play_width // 10

top_left_x = (s_width - play_width) // 2
top_left_y = 50

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

background = pygame.image.load('/front.jpg')
back = pygame.image.load('/back2.jpg')
try_again = pygame.image.load('/try.jpg')

music = pygame.mixer.music.load('kasmir.mp3')
pygame.mixer.music.play(-1)

# color
gray = (119, 118, 110)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 255, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
sea_green = (0, 255, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
light_red = (255, 0, 0)

shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
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


class Piece(object):  # *
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def game_intro():
    gameintro = False
    while not gameintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameintro = True
                game_over = True

        s_width = 450
        s_height = 700

        message('TETRIS', red, 100, (s_width / 2 - 200), 100)
        message("It Doesn't Stop Until You Die", white, 50, (s_width / 2 - 300), 200)
        # button(horizental location ,vertical location,right shift,left shift)
        button(100, 400, 70, 30, 'GO!', white, bright_red, red, 25, 106, 406, gameloop)
        button(600, 400, 70, 30, 'QUIT', white, bright_green, green, 25, 606, 406, quit1)

        pygame.display.update()


def next_game():
    gameintro = False
    while not gameintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameintro = True
                game_over = True

        s_width = 450
        s_height = 700

        message("would you like to play again", yellow, 50, (s_width[...continuation]

# Rest of your code...

def main_menu():
    pygame.init()
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')

    gameintro = True
    while gameintro:
        win.blit(background, (0, 0))

        message('TETRIS', red, 100, (s_width / 2 - 200), 100)
        message("It Doesn't Stop Until You Die", white, 50, (s_width / 2 - 300), 200)
        button(100, 400, 70, 30, 'GO!', white, bright_red, red, 25, 106, 406, gameloop, win)
        button(600, 400, 70, 30, 'QUIT', white, bright_green, green, 25, 606, 406, quit1, win)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameintro = False

    pygame.quit()

main_menu()
