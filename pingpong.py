from pygame import *
from random import randint
import time as t
import pygame_menu
init()
win = display.set_mode((700, 500))
background = transform.scale(image.load("rab_stol.jpg"), (700, 500))
clock = time.Clock()
display.set_caption("Ping-Pong Game")

class Sprites(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprites):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 625:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 625:
            self.rect.y += self.speed

    def update3(self):
        self.rect.x += speed_x
        self.rect.y += speed_y

balls = sprite.Group() 
player1 = Player("mishka.png", 5, 50, 225, 75, 95)
player2 = Player("mishka.png", 5, 600, 225, 75, 95)
ball = Player("cursour.png", 5, 150, 50, 35, 35)
balls.add(ball)
lose2 = font.SysFont("verdava", 50).render('ИГРОК 2 ПРОИГРАЛ!', True, (255, 0, 0))
lose1 = font.SysFont("verdava", 50).render('ИГРОК 1 ПРОИГРАЛ!', True, (255, 0, 0))

speed_x = 3
speed_y = 3

def set_diff():
    pass

def start_game():
    global speed_x, speed_y
    finish = False
    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False

        if not finish:
            win.blit(background,(0, 0))
            player1.reset()
            player1.update2()
            player2.reset()
            player2.update1()
            ball.reset()
            ball.update3()

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            balls.add(ball)

        if ball.rect.y > 470 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < -40:
            win.blit(lose1, (170, 230))
            t.sleep(1)
            break

        if ball.rect.x > 710:
            win.blit(lose2, (170, 230))
            t.sleep(1)
            break

        display.update()
        clock.tick(60)

menu = pygame_menu.Menu('Ping-Pong Game', 400, 300, theme = pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Имя : ', default = 'AverLord')
#menu.add.selector('Difficulty :', [('HARD', 1), ('EASY', 2)], )
menu.add.button('ИГРАТЬ', start_game)
menu.add.button('ВЫХОД', pygame_menu.events.EXIT)

menu.mainloop(win)