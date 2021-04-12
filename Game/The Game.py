import pygame, sys, random


pygame.init()

screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('BG_Wood.png')
grass_bg = pygame.image.load('BG_Grass2.png')
water1 = pygame.image.load('Water1.png')
cloud1 = pygame.image.load('cloud1.png')
cloud2 = pygame.image.load('cloud2.png')
crosshair = pygame.image.load('crosshair_blue_large.png')
duck_surface = pygame.image.load('duck_target_white.png')

game_font = pygame.font.Font(None,60)
text_surface = game_font.render('You Won!',True,(0,0,0))
text_rect = text_surface.get_rect(center = (500,350))

grass_position_y = 560
grass_speed = 1

water1_position_y = 640
water1_speed = 1.5

duck_list = []
for duck in range(20):
	duck_position_x = random.randrange(50,900)
	duck_position_y = random.randrange(120,400)
	duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
	duck_list.append(duck_rect)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair.get_rect(center = event.pos)
		if event.type == pygame.MOUSEMOTION:
			for index,duck_rect in enumerate(duck_list):
				if duck_rect.collidepoint(event.pos):
					del duck_list[index]

	
	screen.blit(wood_bg,(0,0))

	for duck_rect in duck_list:
		screen.blit(duck_surface,duck_rect)

	if len(duck_list) <= 0:
		screen.blit(text_surface,text_rect)

	grass_position_y -= grass_speed

	if grass_position_y <= 520 or grass_position_y >=600:
		grass_speed *= -1
	screen.blit(grass_bg,(0,grass_position_y))

	water1_position_y -= water1_speed

	if water1_position_y <= 620 or water1_position_y >=680:
		water1_speed *= -1
	screen.blit(water1,(0,water1_position_y))

	for duck_rect in duck_list:
		screen.blit(duck_surface,duck_rect)

	screen.blit(crosshair,crosshair_rect)
	screen.blit(cloud1,(100,50))
	screen.blit(cloud2,(100,160))

	screen.blit(cloud1,(600,50))
	screen.blit(cloud2,(700,150))

	pygame.display.update()
	clock.tick(120)

