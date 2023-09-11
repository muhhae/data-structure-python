# import pygame
#
# # pygame setup
# pygame.init()
#
# displayList = pygame.display.get_desktop_sizes()
#
# screen = pygame.display.set_mode(displayList[0])
# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill("purple")
#     pygame.draw.circle(screen, "red", player_pos, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_ESCAPE]:
#         running = False
#
#     pygame.display.flip()
#
#     dt = clock.tick(60) / 1000
#
# pygame.quit()
Tower1 = []
Tower2 = []
Tower3 = []

for i in range(10, 0, -1):
    Tower1.append(i)

while len(Tower2) < 10:
    
    pass