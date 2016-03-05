#!/usr/bin/env python

import pygame
import time
import random

pygame.init()

# Colors, rgb
white = (255,255,255)
black = (0,0,0)
red = (255,100,100)
gray = (100, 100, 100)
ubuntu = (48, 10, 36)
green = (169, 219, 135)
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Resolution
display_width = 800
display_height = 600

FPS = 30
block_size = 10
font = pygame.font.SysFont(None, 30)
# Clock
clock = pygame.time.Clock()
# Surface
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Gunshot Morpheus')
pygame.display.update()
# Player
def player(block_size, segments):
	for x_and_y in segments:
		pygame.draw.rect(gameDisplay, gray, [x_and_y[0], x_and_y[1], block_size, block_size])
# Function to print message to the screen
def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color) # True stands for antialiasing
	gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
# Game loop
def game_loop():
	gameOver = False
	gameExit = False
	
	lead_x = display_width / 2
	lead_y = display_height / 2
	lead_x_change = 0
	lead_y_change = 0
	center = [lead_x, lead_y]
	speed = 10
	random_x = round(random.randint(600, display_width - block_size) / 10) * 10.0
	random_y = round(random.randint(400, display_height - block_size) / 10) * 10.0
	
	print(random_x, random_y)
	
	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(ubuntu)
			message_to_screen("RETRY? Y / N", red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_y:
						game_loop()
					if event.key == pygame.K_n:
						gameExit = True
						gameOver = False

		lead_x += lead_x_change
		lead_y += lead_y_change
		# Background fill
		gameDisplay.fill(ubuntu)
		# Enemy
		pygame.draw.rect(gameDisplay, green, [random_x, random_y, block_size, block_size])
		# Player
		segments = []
		segments_head = []
		segments_head.append(lead_x)
		segments_head.append(lead_y)
		segments.append(segments_head)
		player(block_size, segments)
		#Sides
		gameDisplay.fill(red, rect=[block_size, block_size, display_width - 20, block_size])          #top
		gameDisplay.fill(red, rect=[block_size, display_height - 20, display_width - 20, block_size]) #bot
		gameDisplay.fill(red, rect=[block_size, block_size, block_size, display_height - 20])         #left
		gameDisplay.fill(red, rect=[display_width - 20, block_size, block_size, display_height - 20]) #right
		
		pygame.display.update()
		
		# If you overlap an enemy
		if lead_x == random_x and lead_y == random_y:
			random_x = round(random.randint(35, display_width - block_size) / 10) * 10.0
			random_y = round(random.randint(35, display_height - block_size) / 10) * 10.0
		
		# clock
		clock.tick(FPS)
		# Movement left/right
		for event in pygame.event.get():
			# Make it move Left Right
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -speed
					# So it won't move diagonally
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = speed
					lead_y_change = 0
				# Movement up/down
				elif event.key == pygame.K_UP:
					lead_y_change = -speed
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = speed
					lead_x_change = 0
			print(lead_x, lead_y)
			# If Player overlaps the 4 sides, quit
			if lead_x >= display_width - 20 or lead_x <= block_size or lead_y >= display_height - 20 or lead_y <= block_size:
				gameOver = True	

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
	
	pygame.quit()

	quit()

game_loop()
