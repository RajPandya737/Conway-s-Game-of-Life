#Conways Game of Life

![2023-07-12-15-10-56](https://github.com/RajPandya737/Conway-s-Game-of-Life/assets/99134716/60a62e8b-b9ff-4129-a16f-63582dbd9ece)

## Description

This is an implementation of Conway's Game of Life in Python using Pygame and NumPy. The Game of Life is a cellular automaton devised by the British mathematician John Conway. It is a "zero-player game," meaning that its evolution is determined by its initial state, requiring no further input. The game follows simple rules but exhibits complex and interesting patterns.

## Rules of the Game

The game takes place on a 2D grid of cells, where each cell can be in one of two states: alive or dead. The rules for the evolution of the cells are as follows:

1. **Underpopulation**: If a live cell has fewer than two live neighbors, it dies due to underpopulation.
2. **Survival**: If a live cell has two or three live neighbors, it survives to the next generation.
3. **Overpopulation**: If a live cell has more than three live neighbors, it dies due to overpopulation.
4. **Reproduction**: If a dead cell has exactly three live neighbors, it becomes a live cell due to reproduction.


## Prerequisites

Before running the program, ensure you have the following libraries installed:

- Pygame
- Numpy
You can install these libraries using `pip`, make sure python is installed on your machine:

```bash
pip install pygame numpy
```

## Getting Started

1. Clone this repository to your local machine:
```bash
git clone https://github.com/RajPandya737/Conway-s-Game-of-Life.git
```
2. Change to the project directory:
```bash
cd Conway-s-Game-of-Life
```
3. Run the program:
```bash
python main.py
```

## How to Play
- You don't, it is a simulation of cells that moves completely on its own!
