pip install pygame
pip install pygbag
import asyncio
import pygame as pg
import math
import random

pygame.font.init()
pygame.init()

pygame.mixer.music.load('kashmir.wav')
pygame.mixer.music.play(-1)

# GLOBALS VARS
s_width = 450
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = play_width // 10

top_left_x = (s_width - play_width) // 2
top_left_y = 50

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


class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_positions={}):
    grid = [[(black) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == black] for i in range(20)]
    # Check if positions are within the grid bounds and not already occupied
    return all(j >= 0 and j < 10 and i < 20 and grid[i][j] == black for i, row in enumerate(shape.shape[shape.rotation % len(shape.shape)]) for j, column in enumerate(row) if column == '0')


def draw_grid(surface, row, col):
    for i in range(row):
        pygame.draw.line(surface, gray, (top_left_x, top_left_y + i * block_size),
                         (top_left_x + play_width, top_left_y + i * block_size))
        for j in range(col):
            pygame.draw.line(surface, gray, (top_left_x + j * block_size, top_left_y),
                             (top_left_x + j * block_size, top_left_y + play_height))


async def draw_window(surface, grid):
    surface.fill(black)
    pygame.font.init()
    font = pygame.font.SysFont('Sofia, sans serif', 60)
    label = font.render('Tetris', 1, white)
    surface.blit(label, (top_left_x + play_width // 2 - label.get_width() // 2, 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size))

    pygame.draw.rect(surface, red, (top_left_x, top_left_y, play_width, play_height), 4)

    draw_grid(surface, 20, 10)
    pygame.display.update()
    pygame.time.delay(50)

    await asyncio.sleep(0)


async def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = Piece(5, 0, random.choice(shapes))
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    moving_left = False
    moving_right = False
    moving_down = False

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True

        if moving_left:
            current_piece.x -= 1
            if not valid_space(current_piece, grid):
                current_piece.x += 1

        if moving_right:
            current_piece.x += 1
            if not valid_space(current_piece, grid):
                current_piece.x -= 1

        if moving_down:
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = Piece(5, 0, random.choice(shapes))
            change_piece = False

        await draw_window(surface, grid)

    pygame.quit()


if __name__ == "__main__":
    surface = pygame.display.set_mode((s_width, s_height))
    asyncio.run(main())