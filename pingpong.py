from pygame import *
import time as t
import pygame_menu

init()
win = display.set_mode((700, 500))

speed_x = 3
speed_y = 3
zifra1 = 0
zifra2 = 0

def set_diff(*args):
    global speed_x, speed_y
    print(args)
    if args[1] == 1:
        speed_x = 5
        speed_y = 5
    if args[1] == 2:
        speed_x = 4
        speed_y = 4
    if args[1] == 3:
        speed_x = 3
        speed_y = 3

def start_game():
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

    background = transform.scale(image.load("rab_stol.jpg"), (700, 500))
    clock = time.Clock()
    display.set_caption("Ping-Pong Game")

    player1 = Player("mishka.png", 5, 40, 225, 75, 95)
    player2 = Player("mishka.png", 5, 600, 225, 75, 95)
    ball = Player("cursour.png", 5, 150, 50, 35, 35)
    lose2 = font.SysFont("verdava", 50).render('ИГРОК СПРАВА ПРОИГРАЛ!', True, (255, 20, 0))
    lose1 = font.SysFont("verdava", 50).render('ИГРОК СЛЕВА ПРОИГРАЛ!', True, (255, 20, 0))
    lose2 = font.SysFont("verdava", 50).render('ИГРОК СПРАВА ПРОИГРАЛ!', True, (255, 20, 0))
    lose1 = font.SysFont("verdava", 50).render('ИГРОК СЛЕВА ПРОИГРАЛ!', True, (255, 20, 0))

    global speed_x, speed_y, zifra1, zifra2

    finish = False
    game = True
    
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    game = False

        if not finish:
            win.blit(background,(0, 0))
            player1.reset()
            player1.update2()
            player2.reset()
            player2.update1()
            ball.reset()
            ball.update3()

            schet1 = font.SysFont("verdava", 50).render(str(zifra1), True, (20, 255, 0))
            schet2 = font.SysFont("verdava", 50).render(str(zifra2), True, (20, 255, 0))

            win.blit(schet1, (200, 30))
            win.blit(schet2, (500, 30))

        if sprite.collide_rect(player1, ball):
            speed_x *= -1
            zifra1 = zifra1 + 1
        
        if sprite.collide_rect(player2, ball):
            speed_x *= -1
            zifra2 = zifra2 + 1

        if ball.rect.y > 470 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < -40:
            win.blit(lose1, (120, 230))
            finish = True

        if ball.rect.x > 710:
            win.blit(lose2, (120, 230))
            finish = True

        display.update()
        clock.tick(60)

menu = pygame_menu.Menu('Ping-Pong Game', 400, 300, theme = pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Имя : ', default = 'AverLord')
menu.add.selector('СЛОЖНОСТЬ :', [('СЛОЖНО', 1), ('СРЕДНЕ', 2), ('ЛЕГКО', 3)], onchange = set_diff)
menu.add.button('ИГРАТЬ', start_game)
menu.add.button('ВЫХОД', pygame_menu.events.EXIT)

menu.mainloop(win)