import pygame

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

#load sounds effects
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(.1)
sound_2.play()

#load background music
pygame.mixer.music.load('music.wav')

#play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()


#set main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
#end game
pygame.quit()
