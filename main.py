from asyncio.windows_events import NULL
import pygame, os, random

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
time = pygame.time
screen = pygame.display.set_mode((1500, 900))


# Set the title
pygame.display.set_caption("BEst game")

# Set the title
icon = pygame.image.load(os.getcwd() + "\Media\Images\icon.png")
pygame.display.set_icon(icon)

# WASD controls
controlsGuide = pygame.image.load(os.getcwd() + '\Media\Images\ControlGuide.png')

# Change the image size
controlsGuide = pygame.transform.scale(controlsGuide, (200, 200))


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


# Load up the audio

# Correct user
Correct = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/Correct.ogg")
Correct2 = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/Correct2.ogg")

# Menu music



# Keep it running with the main game loop value
running = True

# bg color
col = 0
usrCol = 0

# Check if the user is on the menu
isOnMenu = True

# current time
ct = 0
delay = 0

# Countdown
countdown = True
Lost = False

# So the win can appear for a certain amount of time
appearfor = 0

maxTime = 2000
timer = maxTime


once = True

shill = False

if random.randint(1, 100) == 50:
  shill = True


# So the audio doesn't repeat itself
playMenuMusic = False
playFailSoundEffect = False
playCorrectSoundEffect = False


# Main gameloop
while running:
  for i in pygame.event.get():

    # Loop through all of the events, (such as keypresses or mouse movement)
    if isOnMenu == False and Lost == False:

      # Events
      if i.type == pygame.KEYDOWN:

        # WASD, which correlates to the colors
        if i.key == pygame.K_w:
          # print("w")
          usrCol = 1
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            Lost = True

        elif i.key == pygame.K_a:
          # print("a")
          usrCol = 2
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            # print("Lost")
            Lost = True

        elif i.key == pygame.K_s:
          # print("s")
          usrCol = 3
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            # print("Lost")
            Lost = True


        elif i.key == pygame.K_d:
          # print("d")
          usrCol = 4
          screen.fill((255, 255, 255))
          pygame.display.update()

          if usrCol != col:
            # print("Lost")
            Lost = True


    # Begin the game, and start up the audio

    if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
      # print("spacebar")
      if isOnMenu == True:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        # Load in the game music
        pygame.mixer.music.load(os.getcwd() + "/Media/Audio/GameAudio.ogg")
        pygame.mixer.music.play()


      isOnMenu = False

    # Quit
    if i.type == pygame.QUIT:
      # print("quit")
      running = False



  if isOnMenu == False and Lost == False:
      # Countdown that times the amount of time a color stays on the screen
      ct = pygame.time.get_ticks()
      if ct - delay > maxTime:

        # Correct
        if once == False:
          if usrCol == col:
            appearfor = 20
            

          elif usrCol != col:
            # print("Lost")
            Lost = True

        once = False
        maxTime -= 50

        timer = maxTime
        delay = pygame.time.get_ticks()
        col = random.randint(1, 4)

        playCorrectSoundEffect = False





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



  
  # Lose screen, press space to restart.
  if Lost == True:
    screen.blit(loseScreen, (10, 10))

    score = font.render("score:" + str(maxTime), True, (0, 0, 0))
    screen.blit(score, (1200, 800))

    score = font.render("Press space to restart", True, (0, 0, 0))
    screen.blit(score, (100, 700))

    if playFailSoundEffect == False:
      pygame.mixer.music.stop()
      pygame.mixer.music.unload()

      if random.randint(0, 20) == 10:
        death = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/RareDeathSound.ogg")

      elif random.randint(0, 20) == 10:
        death = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/RareDeathSound.ogg")

      else:
        death = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/Wrong.ogg")


      pygame.mixer.Sound.play(death)

    playFailSoundEffect = True


    for i in pygame.event.get():

      # Restart the game
      if i.type == pygame.KEYDOWN:

        if i.key == pygame.K_SPACE:
          print("w")

          # Restart all of the values
          running = True
          col = 0
          usrCol = 0
          isOnMenu = True
          ct = 0
          delay = 0
          countdown = True
          Lost = False
          appearfor = 0
          maxTime = 2000
          timer = maxTime
          once = True
          shill = False
          playMenuMusic = False
          playFailSoundEffect = False
          playCorrectSoundEffect = False


          # Shill my website, paxxous.com (hint hint)
          if random.randint(1, 100) == 50:
            shill = True


      # A new quit, so the game doesn't freeze on you
      elif i.type == pygame.QUIT:
        # print("quit")
        running = False


  # Blit the controls
  if isOnMenu == False:
    screen.blit(controlsGuide, (10, 10))


  if isOnMenu == True:

    # Random patreon shill???
    if shill == True:
      shill = font.render("paxxous.com :)", True, (0, 0, 0))
      screen.blit(shill, (0, 0))

    # Blit the menu screen
    screen.blit(titleScreen, (0, 0))
    screen.blit(imgFont, (375, 450))


    # Play the menu music
    if playMenuMusic == False:
      pygame.mixer.music.stop()
      pygame.mixer.music.unload()

      # Load in the game music
      if random.randint(1, 50) == 25:
        pygame.mixer.music.load(os.getcwd() + "/Media/Audio/MenuMusic2.ogg")

      else:
        pygame.mixer.music.load(os.getcwd() + "/Media/Audio/MenuMusic.ogg")

      pygame.mixer.music.play()

    playMenuMusic = True


    
  # When you win, this appears for a few minutes
  if appearfor:
    appearfor -= 1
    usrCol = 0

    delay = pygame.time.get_ticks()
    screen.fill((255, 255, 255))
    screen.blit(winScreen, (0, 0))
    pygame.display.flip()

    sound2play = NULL

    # Sound effects for when you win
    if playCorrectSoundEffect == False:
      if random.randint(1, 2) == 2:
        sound2play = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/correct2.ogg")

      elif random.randint(1, 100) == 56:
        sound2play = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/RareCorrect.ogg")

      else:
        sound2play = pygame.mixer.Sound(os.getcwd() + "/Media/Audio/correct.ogg")

      pygame.mixer.Sound.play(sound2play)

    playCorrectSoundEffect = True

  # Update the screen

  # Your score, (the lower the better) basically resembles the speed
  score = font.render("score:" + str(maxTime), True, (0, 0, 0))
  screen.blit(score, (1200, 800))


  # Cap the maxfps to 60, so nothing breaks
  clock.tick(60)

  # Update everything in the window
  pygame.display.flip()

# Quit pygame
pygame.quit()