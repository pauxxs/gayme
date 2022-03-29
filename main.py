from turtle import delay
import pygame, os, random

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
time = pygame.time
screen = pygame.display.set_mode((1500, 900))

# Set the title
pygame.display.set_caption("BEst game")

# WASD controls
controlsGuide = pygame.image.load(os.getcwd() + '\Media\Images\ControlGuide.png')

# Change the image size
controlsGuide = pygame.transform.scale(controlsGuide, (200, 200))

# Keep it running with the main game loop value
running = True

# bg color
col = 0
usrCol = 0

# Check if the user is on the menu
isOnMenu = True

# Initialize the title screen
titleScreen = pygame.image.load(os.getcwd() + '\Media\Images\TitleScreen.png')
titleScreen = pygame.transform.scale(titleScreen, (1500, 900))

# Lose screen
loseScreen = pygame.image.load(os.getcwd() + '\Media\Images\lose.png')
loseScreen = pygame.transform.scale(loseScreen, (1500, 900))

# Win Screen
winScreen = pygame.image.load(os.getcwd() + '\Media\Images\win.png')
winScreen = pygame.transform.scale(winScreen, (1500, 900))

# Initialize font
font = pygame.font.Font(os.getcwd() + "\Media\Fonts\PaletteMosaic-Regular.ttf", 50)
imgFont = font.render("Press space to start", True, (0, 0, 0))

# current time
ct = 0
delay = 0

# Countdown
countdown = True
Lost = False

# So the win can appear for a certain amount of time
appearfor = 0

maxTime = 2000

once = True

# Main gameloop
while running:
  for i in pygame.event.get():

    if isOnMenu == False or Lost == False:

      # Events
      if i.type == pygame.KEYDOWN:

        if i.key == pygame.K_w:
          print("w")
          usrCol = 1
          screen.fill((255, 255, 255))
          pygame.display.update()



        elif i.key == pygame.K_a:
          print("a")
          usrCol = 2
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            print("Lost")
            Lost = True

        elif i.key == pygame.K_s:
          print("s")
          usrCol = 3
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            print("Lost")
            Lost = True


        elif i.key == pygame.K_d:
          print("d")
          usrCol = 4
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            print("Lost")
            Lost = True


    if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
      print("spacebar")
      isOnMenu = False

    # Quit
    if i.type == pygame.QUIT:
      print("quit")
      running = False



  if isOnMenu == False and Lost == False:
    # countdown
      ct = pygame.time.get_ticks()
      if ct - delay > maxTime:

        if once == False:
          if usrCol == col:
            appearfor = 20
            print("yes")

          elif usrCol != col:
            print("Lost")
            Lost = True


        once = False
        maxTime -= 50
        delay = pygame.time.get_ticks()
        col = random.randint(1, 4)




  # Change the colors based on the the number


  # w
  if col == 1:
    screen.fill((204, 72, 207))

  # a
  elif col == 2:
    screen.fill((60, 81, 201))

  # s
  elif col == 3:
    screen.fill((201, 60, 60))

  # d
  elif col == 4:
    screen.fill((23, 235, 94))

  else:
    screen.fill((255, 255, 255))



  
  # Blit the images
  if Lost == True:
    screen.blit(loseScreen, (10, 10))

  if isOnMenu == False:
    screen.blit(controlsGuide, (10, 10))


  if isOnMenu == True:
    screen.blit(titleScreen, (0, 0))
    screen.blit(imgFont, (375, 450))

  if appearfor:
    appearfor -= 1

    screen.blit(winScreen, (0, 0))
    pygame.display.flip()

  # Update the screen
  clock.tick(60)
  pygame.display.flip()


pygame.quit()