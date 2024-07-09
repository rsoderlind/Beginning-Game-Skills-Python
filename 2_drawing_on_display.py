import pygame

pygame.init()

#create a display surface and set a caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#give a background color to the display
display_surface.fill(BLUE)

#draw various shapes on our display
#line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)

#draw a circle
#circle(surface, color, center, radius, thickness ... 0 for fill)
pygame.draw.circle(display_surface, CYAN, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 195, 0)

#draw a rectangle
#rectangle(surface, color, (top-left-x, top-left-y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

#main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
 
#end game
pygame.quit()