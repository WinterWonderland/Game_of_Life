## Game of Life

### Abstract
Little python implementation of Conway's game of life.

[Conway's Game of Life on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

The game board will be visualized with matplotlib.

### Example
![alt text](example.png "example")

### Description
#### Initialization

A gameboard with 100x100 cells will be created.
A quarter of the fields in the middle (50x50 cells) will be filled randomly with black squares. All other fields will be filled with white squares.

#### Game Process

A black square means this cell is alive. A black square means this cell is dead.

The game runs in steps.
At each step each tile on the game board will be analyzed and updated with following rules:

* a dead cell with exactly three living neighbours will be reborn 
* a living cell with exactly two or three living neighbours keeps alive
* a living cell with less than two or more than three living neighbours dies

This implementation of the game has no real borders. A cell on the left border has its left neighbour on the right border. A cell on the top border has its upper neighbour on the bottom border. 

### Usage
#### Call
Syntax: `game_of_life.py [-h] [--width] [--height] [--interval] [--seed]`

Easiest call of the script with all parameters set to its defaults: `python game_of_life.py`

#### Optional Parameters
Name | Description
--- | ---
`-h` | show this help message and exit
`--width` | The width of the game board (default=100)
`--height` | The height of the game board (default=100)
`--interval` | Interval time between each step (default=0.3)
`--seed` | A seed for the random number generator to get identical play boards

### Dependencies
Package | Tested version
--- | ---
python | 3.7
matplotlib | 3.0.2
numpy | 1.16.1