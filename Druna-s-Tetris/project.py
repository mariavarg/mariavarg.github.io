import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font("HARLOWSI.TTF", 30)
title2_font = pygame.font.Font("HARLOWSI.TTF", 40)
score_surface = title_font.render("Score", True, Colors.dark_grey)
next_surface = title_font.render("Next", True, Colors.dark_grey)
game_over_surface = title2_font.render("Game Over", True, Colors.dark_grey, 40)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Load the background image
background_image = pygame.image.load("unsplash_upscayl.png")

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Druna_s Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # Stop the music when the user closes the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

         # Drawing
    screen.blit(background_image, (0, 0))  # Blit the background image

    score_value_surface = title_font.render(str(game.score), True, Colors.dark_grey)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        pygame.mixer.music.stop()  # Stop the music when the game is over
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)