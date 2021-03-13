import pygame
import sys

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CLOCK = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Mario')


class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('../resources/images/mario.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = WINDOW_HEIGHT / 2 - 100
        self.down = True
        self.up = False
        self.left = False
        self.right = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top >= 10 and self.up:
            self.mario_img_rect.top -= 10
        if self.mario_img_rect.bottom <= WINDOW_HEIGHT - 10 and self.down:
            self.mario_img_rect.bottom += 10
        if self.mario_img_rect.left >= 10 and self.left:
            self.mario_img_rect.left -= 10
        if self.mario_img_rect.right <= WINDOW_WIDTH - 10 and self.right:
            self.mario_img_rect.right += 10


def start_game():
    print("Hello Pan Bogdan")
    canvas.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def game_loop():
    while True:
        mario = Mario()
        while True:
            canvas.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                    elif event.key == pygame.K_LEFT:
                        mario.left = True
                        mario.right = False
                    elif event.key == pygame.K_RIGHT:
                        mario.right = True
                        mario.left = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                    elif event.key == pygame.K_LEFT:
                        mario.left = False
                    elif event.key == pygame.K_RIGHT:
                        mario.right = False


                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            mario.update()
            pygame.display.update()
            CLOCK.tick(FPS)


start_game()
