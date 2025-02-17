import pygame, random

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision detection")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set game values
VELOCITY = 5

#load images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load("coin.png") 
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

#set main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY

    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY

    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    #check for collision between two rects
    if dragon_rect.colliderect(coin_rect):
        print("HIT!!!!!")
        coin_rect.x = random.randint(0,WINDOW_WIDTH-32)
        coin_rect.y = random.randint(0,WINDOW_HEIGHT-32)


    #fill display_surface
    display_surface.fill((0,0,0))

    #Draw rectangles to represent the rects of each object
    pygame.draw.rect(display_surface, (255,0,0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255,255,0), coin_rect, 1)

    #blit images
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    #update display
    pygame.display.update()

    #update clock
    clock.tick(FPS)

#end game
pygame.quit()


