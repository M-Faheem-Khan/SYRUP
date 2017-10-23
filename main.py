import pygame, sys, time, random
from pygame.locals import *
# set up pygame
pygame.init()

#PUT ALL THE CODE BELOW THIS COMMENT#
#VARIABLES
height = 600
width = 800

backgroundx = 0
backgroundy = 0

logx = 801
logy = 100

playerx = 15
playery = 534
#VARIABLES
class Main(object):
  def rise(self, player_y):
      if player_y is (50):
          pass
      else:
          player_y -= 15
          return player_y

  def gravity(self, playery):
    if playery == 534:
      pass
    else:
      playery += 2
    return playery

  def background_mover(self, backgroundx):
    if backgroundx == 4200:
      backgroundx = 0
    else:
      backgroundx -= 1
    return backgroundx

  def log_x_mover(self, logx):
    if logx <= 801 or logx >= -80 or logx >= 801:
      logx -= 10
    else:
      logx = 801
    return logx

  def log_y_mover(self, logx, logy):
    if logx < -85:
      logy = random.randint(100, 500)
    else:
      pass
    return logy

windowSurface = pygame.display.set_mode((width, height),0, 32)
pygame.display.set_caption('SYRUP CHASER')

background = pygame.image.load("Chrachters/background.jpg")
character = pygame.image.load("Chrachters/polar.gif")
log = pygame.image.load("Chrachters/Log.gif")
#PUT ALL THE CODE ABOVE THIS COMMENT#

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                playery = Main().rise(playery)
    
    windowSurface.blit(background, (backgroundx, backgroundy)) # Background
    windowSurface.blit(character, (playerx, playery)) # Chrachters
    windowSurface.blit(log, (logx, logy)) # Log

    logy_list = [100, 250, 400, 550]
    logx_list = [801]
    for i in range(3):
      logx_distance = random.randint(50, 150)
      logx_list.append(logx+logx_distance)
      print(logx_list)


    x_y_coord = zip(logx_list, logy_list)
    print(x_y_coord)

    for coord in x_y_coord:
      windowSurface.blit(log, coord)

    pygame.display.update()
    pygame.time.Clock().tick(30)

    # Make the player fall
    playery = Main().gravity(playery)

    # Make the background move
    backgroundx = Main().background_mover(backgroundx)

    # Makes the log move
    logx = Main().log_x_mover(logx)
    logy = Main().log_y_mover(logx, logy)
