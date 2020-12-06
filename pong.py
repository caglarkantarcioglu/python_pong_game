import pygame,sys
pygame.init()
font = pygame.font.SysFont("comicsansms", 30)
point1 = 0
point2 = 0

x = 400
y = 300
xyon = 5
yyon = 5
size = (900,600)
black = (0,0,0)
screen = pygame.display.set_mode(size)
ball = pygame.image.load('ball.png')
fps = pygame.time.Clock()
class player:
    def __init__(self):
        self.x = 0
        self.y = 225
        self.h = 150
        self.w = 20
        self.color = (1,231,255)
        self.up = pygame.K_w
        self.down = pygame.K_s
    def drawplayer(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.w,self.h])
        keys = pygame.key.get_pressed()
        if keys[self.up] and self.y > 0:
            self.y -= 5
        if keys [self.down] and self.y < 450:
            self.y += 5
player1 = player()
player2 = player()
player2.x = 880
player2.up = pygame.K_UP
player2.down = pygame.K_DOWN
while True:

    fps.tick(120)

    #Point Texts
    po1 = font.render(str(point1), True, (200, 0, 200))
    po2 = font.render(str(point2), True, (200, 0, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    screen.fill(black)
    screen.blit(ball,(x,y))
    player1.drawplayer()
    player2.drawplayer()
    #CREATE WALL
    if y < 1:
        yyon *= -1
    if y > 549:
        yyon *= -1
    if x < 21 and player1.y < y+25 < player1.y+175:
        xyon *= -1
    if x < 0:
        x = 800
        point2 += 1
    if x > 830 and player2.y < y+25 < player2.y+175:
        xyon *= -1
    if x > 900:
        x = 100
        point1 += 1

    x += xyon
    y += yyon
    screen.blit(po1 , (25,0))
    screen.blit(po2 , (860,0))
    pygame.display.update()