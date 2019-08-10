# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:59:50 2018

@author: klaus
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random


class GameOfLife:
    def __init__(self):
        self.height = 100
        self.width = 100
        self.interval = 0.3
        self.epoch = 0
        
        self.board = np.zeros((self.height, self.width))
    
        for x in range(25, 76):
            for y in range(25, 76):
                self.board[y][x] = random.choice([0, 1])   
        
        self.fig, self.ax = plt.subplots(figsize=(10, 10), num=1)
        self.fig.show()
        self.plot_board()
        
    def run(self):
        while self.run_step():
            time.sleep(self.interval)
            
    def run_step(self):
        self.epoch += 1
        
        new_board = self.board.copy()
        
        for x in range(self.width):
            for y in range(self.height):
                living_neighbors = self.board[y - 1 if y > 0 else self.height - 1][x - 1 if x > 0 else self.width - 1] + \
                    self.board[y - 1 if y > 0 else self.height - 1][x] + \
                    self.board[y - 1 if y > 0 else self.height - 1][x + 1 if x < self.width - 1 else 0] + \
                    self.board[y][x - 1 if x > 0 else self.width - 1] + \
                    self.board[y][x + 1 if x < self.width - 1 else 0] + \
                    self.board[y + 1 if y < self.height - 1 else 0][x - 1 if x > 0 else self.width - 1] + \
                    self.board[y + 1 if y < self.height - 1 else 0][x] + \
                    self.board[y + 1 if y < self.height - 1 else 0][x + 1 if x < self.width - 1 else 0]
                                   
                if self.board[y][x] == 0 and living_neighbors == 3:
                    new_board[y][x] = 1
        
                if self.board[y][x] == 1 and (living_neighbors < 2 or living_neighbors > 3):
                    new_board[y][x] = 0
        
        if (self.board == new_board).all():
            return False
        
        self.board = new_board
        self.plot_board()
        return True
        
    def plot_board(self):
        print("Epoch:", self.epoch)
        self.ax.clear()
        self.ax.imshow(self.board, cmap="Greys", interpolation="None")
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


if __name__ == "__main__":  
    GameOfLife().run()
    input("press enter to quit")
