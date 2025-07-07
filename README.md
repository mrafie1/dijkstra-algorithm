# dijkstra-algorithm
My Python implementation of Dijkstra's Algorithm.

# Introduction
**Hello!** 👋

This is my personal Python (non-heap) implementation of Dijkstra's Algorithm! The visual and interactive elements are implemented using Pygame. 

If you wish to edit the screen dimensions and grid square dimensions, read the first comment of the function ```grid_square()``` and edit the values ```screen_dimension``` and ```grid_dimension``` on lines 83 and 84.

# Instructions
**Running**

Run the file ```final_dijkstra.py```

**Creating Squares**
- Left Click: Create (red) barriers to block the path-finding algorithm
- Right Click: Reset a grid square to be blank (white)
- Up Arrow: Create a (green) starting square for the algorithm to start from
- Down Arrow: Create a (yellow) ending square for the algorithm to find

**Starting and Resetting**
- Left Arrow: Perform Dijkstra's Algorithm
- Right Arrow: Reset entire grid 

# Notes
**Too many squares!**

Having too many starting and ending squares will result in the implementation randomly selecting two squares you've highlighted yellow or green.

**No valid paths!**

Having no valid path from your start and end node will result in no path being drawn! Try removing some barriers or repositioning your start/end squares.
