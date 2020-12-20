import pygame, sys

pygame.init()
size = (900, 600)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Olde English", 40)
background = pygame.image.load('background.png')
playerImg = pygame.image.load('pong-player.png')
ball = pygame.image.load('ball.png')
point1 = 0
point2 = 0
x = 400
y = 300
_x = 5
_y = 5
fps = pygame.time.Clock()


class player:

    def __init__(self):
        self.x = 0
        self.y = 225
        self.up = pygame.K_w
        self.down = pygame.K_s

    def drawplayer(self):
        screen.blit(playerImg, (self.x, self.y))
        keys = pygame.key.get_pressed()
        if keys[self.up] and self.y > 0:
            self.y -= 5
        if keys[self.down] and self.y < 450:
            self.y += 5


player1 = player()
player2 = player()
player2.x = 880
player2.up = pygame.K_UP
player2.down = pygame.K_DOWN
while True:

    fps.tick(120)

    # Score Texts
    Player1_ScoreText = font.render(str(point1), True, (220, 220, 255))
    Player2_ScoreText = font.render(str(point2), True, (220, 220, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(ball, (x, y))
    player1.drawplayer()
    player2.drawplayer()
    # CREATE WALL
    if y < 1:
        _y *= -1
    if y > 549:
        _y *= -1
    if x < 21 and player1.y < y + 25 < player1.y + 175:
        _x *= -1
    if x < 0:
        x = 800
        point2 += 1
    if x > 830 and player2.y < y + 25 < player2.y + 175:
        _x *= -1
    if x > 900:
        x = 100
        point1 += 1

    x += _x
    y += _y
    screen.blit(Player1_ScoreText, (25, 10))
    screen.blit(Player2_ScoreText, (860,10))
    pygame.display.update()
