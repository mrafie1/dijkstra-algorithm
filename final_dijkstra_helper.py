import dijkstra_alg
import final_dijkstra

def check_clicked_req(list_of_nodes):
    # Redraw all grid squares with their respective colors

    for col in list_of_nodes:
        for box in col:
            box.draw()

def dijk(graph, node_list, start_end_list):
    # Set start and end tuple coordinate values
    start = start_end_list[0]
    end = start_end_list[1]

    # Run dijkstra alg. on our path
    tuple_val = graph.dijkstra(start, end)
    path = tuple_val[1]
    lenpath = len(path)

    # Remove start and end grid squares from path
    path = path[1: lenpath - 1]

    # Colour path
    for val in path:
        x = val[0]
        y = val[1]
        gsq = node_list[x][y]
        gsq.border = 0
        gsq.color = 'blue'


def new_grid(nlist):
    # Create new graph
    g = dijkstra_alg.Graph()

    d = len(nlist)

    # Add vertices to graph
    for x in range(d):
        for y in range(d):
            g.add_vertex((x, y))

    # Add edges to all valid vertices (status != 1)
    for x in range(d):
        for y in range(d):
            # Check if grid square is a wall
            if nlist[x][y].status == 1:
                pass
            # Check if bottom right corner
            elif y == d - 1 and x == d - 1:
                pass

            # Check if square is in the bottom row; Add edges to squares rightward
            elif y == d - 1:
                if nlist[x + 1][y].status != 1:
                    g.add_edge((x, y), (x + 1, y), 1)

            # Check if square is in the rightmost column; Add edges to squares downward
            elif x == d - 1:
                if nlist[x][y + 1].status != 1:
                    g.add_edge((x, y), (x, y + 1), 1)

            # Add edges to squares to the right and down
            else:
                if nlist[x + 1][y].status != 1:
                    g.add_edge((x, y), (x + 1, y), 1)
                if nlist[x][y + 1].status != 1:
                    g.add_edge((x, y), (x, y + 1), 1)

    return g


def reset(bg):
    # Reset a new grid and return new grid list
    bg.fill('white')
    new_list = []

    for x in range(0, 800, 50):

        col = []

        for y in range(0, 800, 50):
            gsq = final_dijkstra.grid_square(x, y, bg)
            col.append(gsq)

        new_list.append(col)

    return new_list

def find_barriers(nodelist, dimension):
    # Search through all squares in the grid; Return a set of all barrier grid coordinate tuples
    d = set()

    for x in range(dimension):
        for y in range(dimension):
            gsq = nodelist[x][y]
            if gsq.status == 1:
                d.add((x, y))

    return d


def find_start_end(nodelist, dimension):
    # Search through all squares in the grid; Return a set of all start and end square grid coordinate tuples
    st_ed = []
    for x in range(dimension):
        for y in range(dimension):
            gsq = nodelist[x][y]
            if gsq.status == 2:
                st_ed.insert(0, (x, y))
            if gsq.status == 3:
                st_ed.insert(1, (x, y))

    return st_ed


def reconfigure_screen(bg, barrier_list, start_end_list):
    # Reset the grid screen
    # Recolour all barrier, start, and end grid squares
    bg.fill('white')
    new_list = []

    for x in range(0, 800, 50):

        col = []

        for y in range(0, 800, 50):
            gsq = final_dijkstra.grid_square(x, y, bg)
            col.append(gsq)

        new_list.append(col)

    for x in range(16):
        for y in range(16):
            if (x, y) in barrier_list:
                gsq = new_list[x][y]
                gsq.status = 1
                gsq.color = 'red'
                gsq.border = 0

            elif (x, y) == start_end_list[0]:
                gsq = new_list[x][y]
                gsq.status = 2
                gsq.color = 'green'
                gsq.border = 0
            elif (x, y) == start_end_list[1]:
                gsq = new_list[x][y]
                gsq.status = 3
                gsq.color = 'yellow'
                gsq.border = 0

    return new_list
