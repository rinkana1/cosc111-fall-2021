'''
Inst
'''
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click to draw")

keep_going = True
colors = {
  'RED': (255, 0, 0),
  'YELLOW': (255, 255, 0),
  'GREEN': (0, 255, 0),
  'BLUE': (0, 0, 255),
  'BLACK': (0, 0, 0),
  'WHITE': (255, 255, 255),
  'GREY': (127, 127, 127)
}
banner_colors = {
  'RED': (127, 0, 0),
  'YELLOW': (127, 127, 0),
  'GREEN': (0, 127, 0),
  'BLUE': (0, 0, 127),
  'BLACK': (30, 30, 30),
  'WHITE': (210, 210, 210),
  'GREY': (190, 190, 190)
}
size = [5, 10, 15, 20, 25]
radius = 15
mousedown = False
current_color = colors['RED']
current_banner = banner_colors['RED']
i = 0
current_size = size[i]

# DISPLAY INSTRUCTIONS IN CONSOLE
print('Welcome to MH Paint!\n\nYou can change the color by pressing any of the 7 colored buttons on the bottom\nYou can change the size by clicking the brown button on the left side\nFinally, you can clear the page by pressing backspace\n\nThank you for using MH Paint!')

def create_buttons(color_list):
  x_pos = 120
  for color in color_list:
    pygame.draw.circle(screen, (170, 170, 170), (x_pos, 570), 19)
    pygame.draw.circle(screen, color_list[color], (x_pos, 570), 15)
    x_pos += 86

while keep_going:
  # Creates buttons
  pygame.draw.rect(screen, current_banner, (0, 540, 800, 60))
  create_buttons(colors)
  
  #Create size change button
  pygame.draw.rect(screen, (66, 36, 4), (20, 551, 38, 38), 0, 15)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      keep_going = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_BACKSPACE:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))

    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()

      #If the y pos of the mouse is greater than 540, don't draw a dot
      if pos[1] > 540:
        mousedown = False

      else:
       mousedown = True
      
      if (pos[0] > 101 and pos[0] < 139) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['RED']
        current_banner = banner_colors['RED']

      elif (pos[0] > 187 and pos[0] < 225) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['YELLOW']
        current_banner = banner_colors['YELLOW']

      elif (pos[0] > 273 and pos[0] < 311) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['GREEN']
        current_banner = banner_colors['GREEN']

      elif (pos[0] > 359 and pos[0] < 397) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['BLUE']
        current_banner = banner_colors['BLUE']

      elif (pos[0] > 445 and pos[0] < 483) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['BLACK']
        current_banner = banner_colors['BLACK']

      elif (pos[0] > 531 and pos[0] < 569) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['WHITE']
        current_banner = banner_colors['WHITE']

      elif (pos[0] > 617 and pos[0] < 655) and (pos[1] > 551 and pos[1] < 589):
        current_color = colors['GREY']
        current_banner = banner_colors['GREY']

      elif (pos[0] > 20 and pos[0] < 58) and (pos[1] > 551 and pos[1] < 589):
        if i < 4:
          i += 1
        else:
          i = 0

        current_size = size[i]

    if event.type == pygame.MOUSEBUTTONUP:
      mousedown = False

  if mousedown:
    spot = pygame.mouse.get_pos()
    pygame.draw.circle(screen, current_color, spot, current_size)

  pygame.display.update()


pygame.quit()