import sys, pygame, os, math
from random import *
pygame.init()
pygame.display.set_caption('Saxton hale')

#Matrix of the map : 
# 0 = Free space
# 1 = Wall
matrix = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

#max matrix size 40/30 with 1200/720 px
squareSize = 30
shootSize = 10

size = width, height = 1200, 720

# Color definition
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
red = 255,0,0
green = 0,255,0

screen = pygame.display.set_mode(size)

# Init
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False

directions = ["left","right","up","down"]

walls = []

def draw_board():
    screen.fill(black)
    x = -1
    for xRow in matrix:
        x+=1
        y = -1
        for square in xRow:
            y+=1
            if square == 1:
                walls.append(Wall(x,y))
            if square == 2:
                pygame.draw.rect(screen,blue,(y*squareSize,x*squareSize,squareSize,squareSize))

def move(direction, object):
    if direction == "left":
        # Check if a wall is next to
        if matrix[object.positionY][object.positionX-1] != 1:
            object.rect = object.rect.move(-squareSize, 0)
            object.positionX -= 1
    if direction == "right":
        if matrix[object.positionY][object.positionX+1] != 1:
            object.rect = object.rect.move(squareSize, 0)
            object.positionX += 1
    if direction == "up":
        if matrix[object.positionY-1][object.positionX] != 1:
            object.rect = object.rect.move(0, -squareSize)
            object.positionY -= 1
    if direction == "down":
        if matrix[object.positionY+1][object.positionX] != 1:
            object.rect = object.rect.move(0, squareSize)
            object.positionY += 1

def angle_calcul_for_pnj_to_player(pnj,player):
    distancePNJPlayer = math.sqrt((abs(pnj.positionX-player.positionX))**2+(abs(pnj.positionY-player.positionY))**2)
    return math.degrees(math.acos(abs(pnj.positionX-player.positionX)/distancePNJPlayer))

class Wall(object):
    def __init__(self, positionX, positionY):
        self.rect = pygame.rect.Rect(positionY*squareSize,positionX*squareSize,squareSize,squareSize)
        self.positionX = positionX
        self.positionY = positionY
        pygame.draw.rect(screen,white,self.rect)

class Bullet(object):
    def __init__(self, shooter, directionX, directionY):
        self.rect = pygame.rect.Rect((shooter.positionX*squareSize+squareSize/2, shooter.positionY*squareSize+squareSize/2, shootSize,shootSize))
        self.shooter = shooter
        self.directionX = directionX
        self.directionY = directionY
        self.speedy = -10

    def update(self):
        if self.directionX != 0:
            self.rect.x += self.directionX*self.speedy
        if self.directionY != 0:
            self.rect.y += self.directionY*self.speedy
        pygame.draw.rect(screen, green, self.rect)
        # kill if it moves off the wall
        if self.check_collision():
            bullets.remove(self)
            del self

    def check_collision(self):
        collide = False
        positionX = round(self.rect.x / squareSize)
        positionY = round(self.rect.y / squareSize)
        if self.rect.colliderect(player.rect):
            collide = True

        # Convert the position of the bullet on the matrix and check if it's a wall
        if matrix[positionY][positionX] == 1:
            collide = True
        return collide

class PNJ(object):
    def __init__(self):
        # Rand spawn
        randPositionX = randint(5,width/squareSize-2)
        randPositionY = randint(5,height/squareSize-2)
        self.rect = pygame.rect.Rect((randPositionX*squareSize, randPositionY*squareSize, squareSize, squareSize))
        self.positionX = randPositionX
        self.positionY = randPositionY
        self.timeInDirection = 0
        self.direction = None

    def draw(self, surface):
        pygame.draw.rect(screen, blue, self.rect)

    def shoot(self):
        directionX = player.positionX - pnj.positionX
        directionY = player.positionY - pnj.positionY

        angle = angle_calcul_for_pnj_to_player(self,player)

        if directionX != 0:
            directionX = -directionX / abs(directionX)

        if directionY != 0:
            directionY = -directionY / abs(directionY)

        if angle < 22.5:
            directionY = 0
        elif angle > 67.5:
            directionX = 0

        bullet = Bullet(self, directionX,directionY)
        bullets.append(bullet)

    def random_shoot(self):
        randomDirectionX = randint(-1,1)
        randomDirectionY = randint(-1,1)
        # We wouldn't 0 x and 0 y direction
        if randomDirectionX == 0 and randomDirectionY == 0:
            randomDirectionX = 1
        bullet = Bullet(self, randomDirectionX,randomDirectionY)
        bullets.append(bullet)

    def move(self):
        # Move only if the distance between player and pnj is less 7 square
        if abs(player.positionX - self.positionX) < 7 or abs(player.positionY - self.positionY) < 7: 
            # Check where the pnj go away
            if player.positionX < self.positionX:
                move("right",self)
            elif player.positionX > self.positionX:
                move("left",self)

            if player.positionY < self.positionY:
                move("down",self)
            elif player.positionY > self.positionY:
                move("up",self)
        else:
            # Move in random direction
            if self.timeInDirection == 0 or self.timeInDirection == 3:
                self.timeInDirection = 0
                self.direction = directions[randint(0,3)]

            move(self.direction, self)
            self.timeInDirection += 1

            '''if matrix[self.positionY-1][self.positionX] + matrix[self.positionY+1][self.positionX] + matrix[self.positionY][self.positionX+1] + matrix[self.positionY][self.positionX-1] == 2:
                print("coincé")'''

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((squareSize, squareSize, squareSize, squareSize))
        self.positionX = 1
        self.positionY = 1

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            move("left",self)
        if key[pygame.K_RIGHT]:
            move("right",self)
        if key[pygame.K_UP]:
            move("up",self)
        if key[pygame.K_DOWN]:
           move("down",self)

    def draw(self, surface):
        pygame.draw.rect(screen, red, self.rect)

draw_board()
player = Player()
pnjs = [PNJ(), PNJ()]
bullets = []
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()     
        # Fullscreen toggle
        elif (event.type is pygame.KEYDOWN and event.key == pygame.K_f):
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode(size)
            else:
                pygame.display.set_mode(size, pygame.FULLSCREEN)   
    # We need to draw the board before the rest
    draw_board()

    if len(pnjs) > 0:
        for pnj in pnjs:
            # Check colision between player en pnj
            if player.positionX == pnj.positionX and player.positionY == pnj.positionY:
                pnjs.remove(pnj)
                pnjs.append(PNJ())
            else:
                pnj.move()
                pnj.shoot()
                pnj.draw(screen)

    if len(bullets) > 0:
        for bullet in bullets:
            bullet.update()

    player.draw(screen)
    player.handle_keys()
    pygame.display.update()
    # The clock tick define the movement speed
    clock.tick(20)
