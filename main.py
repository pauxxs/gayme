import pygame, os


pygame.init()
screen = pygame.display.set_mode((1500, 900))
# Set the title
pygame.display.set_caption("BEst game")

# WASD controls
image = pygame.image.load(os.getcwd() + '\\pixil-frame-0.png')
# Change the image size
image = pygame.transform.scale(image, (200, 200))

# Keep it running
running = True
# bg color
col = 0

# it run?

# Main gameloop
while running:
  for i in pygame.event.get():

    # Events
    if i.type == pygame.KEYDOWN:
      if i.key == pygame.K_w:
        print("w")
        col = 1

      elif i.key == pygame.K_a:
        print("a")
        col = 2

      elif i.key == pygame.K_s:
        print("s")
        col = 3

      elif i.key == pygame.K_d:
        print("d")
        col = 4
    
    # Quit
    if i.type == pygame.QUIT:
      running = False



  # Change the colors based on the the number
  if col == 1:
    screen.fill((204, 72, 207))

  elif col == 2:
    screen.fill((60, 81, 201))

  elif col == 3:
    screen.fill((201, 60, 60))

  elif col == 4:
    screen.fill((23, 235, 94))

  else:
    screen.fill((255, 255, 255))


  # Update the screen no matter what
  screen.blit(image, (10, 10))

  pygame.display.flip()
  pygame.display.update()

pygame.quit()