import pygame as pg
import numpy as np
import random
from config import *

class Map:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def rand_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                #Infuture, get user input and place it into here
                self.grid_array[i][j] = random.randint(0,1)
    
    def gameplay(self,on,off,area):
        for i in range(self.rows):
            for j in range(self.columns):
                y_cor = j * self.scale
                x_cor = i * self.scale

                if self.grid_array[i][j] == 1:
                    pg.draw.rect(area, on, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])
                else:
                    pg.draw.rect(area, off, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])

        updated_cells = np.ndarray(shape=(self.size))
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.grid_array[i][j]
                count = self.neighbours(i,j)
                if cell == 1 and count < 2:
                    updated_cells [i][j] = 0
                elif cell == 1 and count <= 3:
                    updated_cells [i][j] = 1
                elif cell == 1 and count >3:
                    updated_cells [i][j] = 0
                elif cell == 0 and count == 3:
                    updated_cells [i][j] = 1
                else:
                    updated_cells [i][j] = cell
        self.grid_array = updated_cells


    def neighbours (self, i, j):
        count = 0
        l = self.columns
        '''
        #Potential solution to making the number of lines for if statement go down
        for x in range(-1,2):
            for y in range(-1,2):
                if not x == y and i > 0 and j < l-1:
                    if self.grid_array[i+x][j+y] == 1:
                        count+=1

        '''
        if i < l-1:
            #check the right side
            if self.grid_array[i+1][j] == 1:
                count+=1
        if i >0:
            #check the left side
            if self.grid_array[i-1][j] == 1:
                count+=1
        if j < l-1:
            #check bottom
            if self.grid_array[i][j+1] == 1:
                count+=1
        if j >0:
            #check top
            if self.grid_array[i][j-1] == 1:
                count+=1
        if i <l-1 and j < l-1:
            #check bottom right
            if self.grid_array[i+1][j+1] == 1:
                count+=1
        if i <l-1 and j >0:
            #check top right
            if self.grid_array[i+1][j-1] == 1:
                count+=1
        if i > 0 and j >0:
            #check top left
            if self.grid_array[i-1][j-1] == 1:
                count+=1
        if i > 0 and j < l-1:
            #check bottom left
            if self.grid_array[i-1][j+1] == 1:
                count+=1
        return count
        
        

