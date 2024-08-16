import pygame
import numpy as np
import time
class tower():
    def __init__(self, surface, size, amount, width, height, color, gravity=10) -> None:
        self.surface = surface
        self.size = size
        self.amount = amount
        self.width = width
        self.height = height
        self.color = color
        self.gravity = gravity
    def collisiondetection(self) -> None:
        running = True
        clicked = False
        amountplaced = 0
        increase = 0
        mouse = pygame.mouse
        positions = [[0 for i in range(5)] for i in range(self.amount)]
        randomcolors = []
        for i in range(self.amount):
            randomcolors.append(np.random.randint(0,255))
        for j in range(self.amount):
            if amountplaced * self.size >= self.width:
                amountplaced = 0
                increase+=1
            try:
                positions[j][0] = amountplaced * self.size #x-positions
                positions[j][1] = self.height - (self.size)*(increase+1) #y-positions
                positions[j][2] = 0 #x-velocity
                positions[j][3] = 0 #y-velocity
                positions[j][4] = 0 #y-bound
                amountplaced+=1
            except:
                pass
        # game loop 
        while running: 
            self.surface.fill((255,255,255,255))
            current_mouse_pos = mouse.get_pos()
            sorted_positionsy = sorted(positions, key=lambda x: x[1])
            sorted_positionsx = sorted(positions, key=lambda x: x[0] )
            for i in range(self.amount):
                rectang = pygame.Rect(positions[i][0], positions[i][1], self.size, self.size)
                pygame.draw.rect(self.surface, randomcolors[i], rectang)
                if positions[i][1] > 0 and positions[i][1] < self.height - self.size: 
                    positions[i][3]+=self.gravity/10000
                else:
                    positions[i][3] = 0
                for j in range(self.amount):
                    if positions[j][0] >= positions[i][0] - self.size and positions[j][0] <= positions[i][0] + self.size:
                        if positions[i][1] >= positions[j][1] - self.size and positions[i][1] <= positions[j][1] and i != j:
                            if positions[i][0] >= positions[j][0] - self.size and positions[i][0] <= positions[j][0] + self.size and i != j:
                                positions[i][3] = 0
                    
                positions[i][1]+=positions[i][3]
                if positions[i][1] < 0 and positions[i][3] == 0:
                    positions[i][1] = 0
                elif positions[i][1] > self.height - self.size and positions[i][3] == 0:
                    positions[i][1]  = self.height - self.size

            # for loop through the event queue 
            for event in pygame.event.get(): 
            
                # Check for QUIT event	 
                if event.type == pygame.QUIT: 
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    mouse_pos = pygame.mouse.get_pos()
                    index = -1
                    for i in range(self.amount):
                         if (mouse_pos[0] >= positions[i][0] and mouse_pos[0] <= positions[i][0] + self.size) and (mouse_pos[1] >= positions[i][1] and mouse_pos[1] <= positions[i][1] + self.size):
                            index = i
                if event.type == pygame.MOUSEBUTTONUP:
                     clicked = False
                     positions[i][3] = 0
                     positions[i][2] = 0
            if clicked:
                positions[index][0] = current_mouse_pos[0]
                positions[index][1] = current_mouse_pos[1]
            pygame.display.update()
                 

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((600, 600)) 

# Set the caption of the screen 
pygame.display.set_caption('SCREEN') 

# Fill the background colour to the screen 
screen.fill(background_colour) 

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 

t = tower(screen, 60, 21, 600, 600, pygame.Color(0,0,0,255))
t.collisiondetection()