# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:59:50 2018

@author: klaus
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from argparse import ArgumentParser, RawTextHelpFormatter


class GameOfLife:
    def __init__(self, width, height, interval, seed):
        random.seed(seed)
        self.height = height
        self.width = width
        self.interval = interval
        self.epoch = 0
        
        self.board = np.zeros((self.height, self.width))
    
        for x in range(int(self.width / 2 - self.width / 4), int(self.width / 2 + self.width / 4 + 1)):
            for y in range(int(self.height / 2 - self.height / 4), int(self.height / 2 + self.height / 4 + 1)):
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
    argument_parser = ArgumentParser(description="""
Game of Life:
    - Little python implementation of Conway's game of life.
    - The game board will be visualized with matplotlib.
    - See readme.md for more informations.""", 
                                     epilog="https://github.com/WinterWonderland/Game_of_Life",
                                     formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument("--width",
                                 metavar="",
                                 type=int,
                                 default=100,
                                 help="The width of the game board (default=100)")
    argument_parser.add_argument("--height",
                                 metavar="",
                                 type=int,
                                 default=100,
                                 help="The width of the game board (default=100)")
    argument_parser.add_argument("--interval",
                                 metavar="",
                                 type=float,
                                 default=0.3,
                                 help="Interval time between each step (default=0.3)")
    argument_parser.add_argument("--seed",
                                 metavar="",
                                 type=int,
                                 default=None,
                                 help="A seed for the random number generator to get identical play boards")
    args = argument_parser.parse_args()
    
    GameOfLife(width=args.width,
               height=args.height,
               interval=args.interval,
               seed=args.seed).run()
    input("press enter to quit")
