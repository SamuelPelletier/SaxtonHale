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

boardSize = boardWidth, boardHeight = 1200, 720
screenSize = screenWidth, screenHeight = boardWidth+200, boardHeight

# Color definition
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
red = 255,0,0
green = 0,255,0

screen = pygame.display.set_mode(screenSize)

font = pygame.font.Font("font/VarelaRound-Regular.ttf", 26)
pygame.mixer.music.load('sound/theme.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.04)

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

def draw_text():
    textLife = font.render("Life:", True, (255, 0, 0))
    screen.blit(textLife,(boardWidth, 0))

    textLifeNumber = font.render(str(player.life), True, (255, 0, 0))
    screen.blit(textLifeNumber,(boardWidth+textLife.get_width(), 0))

    textScore = font.render("Score:", True, (255, 0, 0))
    screen.blit(textScore,(boardWidth, textLife.get_height()))

    textScoreNumber = font.render(str(player.score), True, (255, 0, 0))
    screen.blit(textScoreNumber,(boardWidth+textScore.get_width(), textLife.get_height()))

    textFullscreen = font.render("F: fullscreen", True, (255, 0, 0))
    screen.blit(textFullscreen,(boardWidth, screenHeight-textFullscreen.get_height()))

    textReload = font.render("R: reload", True, (255, 0, 0))
    screen.blit(textReload,(boardWidth, screenHeight-(textReload.get_height()+textFullscreen.get_height())))

    textPause = font.render("P: pause", True, (255, 0, 0))
    screen.blit(textPause,(boardWidth, screenHeight-(textReload.get_height()+textFullscreen.get_height()+textPause.get_height())))

    if player.life <= 0:
        textPaused = font.render("Game Over", True, (255, 0, 0))
        screen.blit(textPaused,(boardWidth/2, boardHeight/2))

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
    # The pnj is dead
    if distancePNJPlayer == 0:
        return 0
    return math.degrees(math.acos(abs(pnj.positionX-player.positionX)/distancePNJPlayer))

def pause():
    musicPosition = pygame.mixer.music.get_pos()
    pygame.mixer.music.fadeout(1500)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()  
            elif (event.type is pygame.KEYDOWN and event.key == pygame.K_r):
                init_game() 
                paused = False     
                pygame.mixer.music.play(-1)
            elif (event.type is pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE)):
                paused = False     
                pygame.mixer.music.play(-1, musicPosition/1000)
        clock.tick(15)



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
        self.damage = 10

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
            player.life -= bullet.damage
            collide = True
            if player.life <= 0:
                player.life = 0
                draw_board()
                draw_text()
                pause()
                # If the game is reload, this bullet will be destroy before the next code
                collide = False

        # Convert the position of the bullet on the matrix and check if it's a wall
        if matrix[positionY][positionX] == 1:
            collide = True
        return collide

class PNJ(object):
    def __init__(self):
        # Rand spawn
        randPositionX = randint(5,boardWidth/squareSize-2)
        randPositionY = randint(5,boardHeight/squareSize-2)
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

            # if the pnj is next to a wall
            if matrix[self.positionY-1][self.positionX] + matrix[self.positionY+1][self.positionX] + matrix[self.positionY][self.positionX+1] + matrix[self.positionY][self.positionX-1] >= 1:
                pnjCanMove = False
                while pnjCanMove==False:
                    prePositionX = self.positionX
                    prePositionY = self.positionY
                    move(self.direction, self)
                    if prePositionX != self.positionX or prePositionY != self.positionY:
                        pnjCanMove = True
                    else:
                        # Choose the best way to escape between x axe or y axe
                        if abs(player.positionX - pnj.positionX) > abs(player.positionY - pnj.positionY):
                            self.direction = directions[randint(2,3)]
                        else:
                            self.direction = directions[randint(0,1)]

            else:
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

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((squareSize, squareSize, squareSize, squareSize))
        self.positionX = 1
        self.positionY = 1
        self.life = 500
        self.score = 0

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


def init_game():
    global player
    global pnjs
    global bullets
    global clock

    draw_board()
    player = Player()
    draw_text()
    pnjs = [PNJ(), PNJ()]
    bullets = []
    clock = pygame.time.Clock()

draw_board()
player = Player()
draw_text()
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
                pygame.display.set_mode(screenSize)
            else:
                pygame.display.set_mode(screenSize, pygame.FULLSCREEN)   
        elif (event.type is pygame.KEYDOWN and event.key == pygame.K_r):
            init_game()
        elif (event.type is pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE)):
            pause()

    # We need to draw the board before the rest
    draw_board()
    draw_text()

    if len(pnjs) > 0:
        for pnj in pnjs:
            # Check colision between player en pnj
            if player.positionX == pnj.positionX and player.positionY == pnj.positionY:
                pnjs.remove(pnj)
                player.score += 50
                player.life += 100
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
