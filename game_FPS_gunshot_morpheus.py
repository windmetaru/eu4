#!/usr/bin/env python

import pygame

pygame.init()
# colors, rgb

white = (255,255,255)
black = (0,0,0)
red = (255,100,100)
gray = (100, 100, 100)
ubuntu = (48, 10, 36)
 
# clock
clock = pygame.time.Clock()

# return surface

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Gunshot Morpheus')
pygame.display.update()

# game loop

gameExit = False
lead_x = 400
lead_y = 300
lead_x_change = 0
lead_y_change = 0

while not gameExit:
	
	lead_x += lead_x_change
	lead_y += lead_y_change
	
	#ubuntu fill
	gameDisplay.fill(ubuntu)
	#dot in the middle
	pygame.draw.rect(gameDisplay, gray, [lead_x, lead_y, 10, 10])
	gameDisplay.fill(red, rect=[10, 10, 780, 10])  #top
	gameDisplay.fill(red, rect=[10, 580, 780, 10]) #bot
	gameDisplay.fill(red, rect=[10, 10, 10, 580])  #left
	gameDisplay.fill(red, rect=[780, 10, 10, 580]) #right
	
	pygame.display.update()
	# clock
	clock.tick(60)
	
	for event in pygame.event.get():
		# Make it move Left Right
		if event.type == pygame.KEYDOWN:
			#print(event)
			# Movement left/right
			if event.key == pygame.K_LEFT:
				lead_x_change = -5
				# So it won't move diagonally
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 5
				lead_y_change = 0
			# Movement up/down
			elif event.key == pygame.K_UP:
				lead_y_change = -5
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 5
				lead_x_change = 0
		print(lead_x, lead_y)
		# If Player is under the 4 lines
		if lead_x > 770 or lead_x < 10:
			gameExit = True
			
		elif lead_y > 570 or lead_y < 20:
			gameExit = True
			

		# Make it stop moving when you are not holding the key
		if event.type == pygame.KEYUP:
			print(event)
			# Movement Left Right stops after releasing the key
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				lead_x_change = 0
			# Movement Up Down stops after releasing the key
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				lead_y_change = 0
			
			
		if event.type == pygame.QUIT:
			gameExit = True
			
		#print(event)


pygame.quit()

quit()
