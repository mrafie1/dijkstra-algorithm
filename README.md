# dijkstra-algorithm
My Python implementation of Dijkstra's Algorithm.

# Introduction
**Hello!** 👋

This is my personal Python (non-heap) implementation of Dijkstra's Algorithm! The visual and interactive elements are implemented using Pygame. 

If you wish to edit the screen dimensions and grid square dimensions, read the first comment of the function ```grid_square()``` and edit the values ```screen_dimension``` and ```grid_dimension``` on lines 83 and 84.

# Instructions

## Requirements and Running

This implementation requires Pygame version 2.6.1.

To install requirements, run: ```pip install pygame==2.6.1```

To run the file, run: ```final_dijkstra.py```

## Features

On a customizable square grid, the user can place a starting, ending, and wall squares for the algorithm to path-find through. The algorithm will search in the main cardinal directions (NESW); it will not create diagonal paths. The user is able to remove the squares they've placed and reset the entire grid to its original state.

**Creating Squares**
- Left Click: Create (red) barriers to block the path-finding algorithm
- Right Click: Reset a grid square to be blank (white)
- Up Arrow: Create a (green) starting square for the algorithm to start from
- Down Arrow: Create a (yellow) ending square for the algorithm to find

**Starting and Resetting**
- Left Arrow: Perform Dijkstra's Algorithm
- Right Arrow: Reset the entire grid 

# Notes
**Too many squares!**

Having too many starting and ending squares will result in the implementation randomly selecting two squares you've highlighted yellow or green.

**No valid paths!**

Having no valid path from your start and end node will result in no path being drawn! Try removing some barriers or repositioning your start/end squares.
