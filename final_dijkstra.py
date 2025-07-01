import pygame
import final_dijkstra_helper

class grid_square():
    def __init__(self, x, y, screen):
        # TODO NOTE:
        # I'm too lazy to replace all the '50' dimensions in this class; Will change in future

        self.x = x
        self.y = y

        self.screen = screen
        self.color = 'black'
        self.border = 1

        self.collision = pygame.Rect((x, y), (50, 50))
        self.pressed = False

        self.status = 0

        self.draw()

    def draw(self):
        # Color the square
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 50), self.border)
        self.clicked()

    def redraw(self):
        # Recolor the square
        pygame.draw.rect(self.screen, 'white', (self.x, self.y, 50, 50))

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.collision.collidepoint(mouse_pos):

            key = pygame.key.get_pressed()

            # Left click; Create barrier square
            if pygame.mouse.get_pressed()[0]:
                self.redraw()
                self.pressed = True
                self.color = 'red'
                self.border = 0
                self.status = 1

            # Right click; Create empty square
            elif pygame.mouse.get_pressed()[2]:
                self.redraw()
                self.pressed = True
                self.color = 'black'
                self.border = 1
                #
                self.status = 0

            # Up arrow; Create start square
            elif key[pygame.K_UP]:
                self.redraw()
                self.pressed = True

                self.color = 'green'
                self.border = 0
                self.status = 2

            # Down arrow; Create end square
            elif key[pygame.K_DOWN]:
                self.redraw()
                self.pressed = True

                self.color = 'yellow'
                self.border = 0
                self.status = 3

            else:
                if self.pressed:
                    self.pressed = False


if __name__ == '__main__':
    pygame.init()

    # Init variables
    # Please make the grid dimension a factor of the screen dimension :)
    screen_dimension = 800
    grid_dimension = 16
    gsq_dimension = screen_dimension // grid_dimension

    screen = pygame.display.set_mode((screen_dimension, screen_dimension))
    screen.fill('white')
    pygame.display.set_caption("My Dijkstra's Algorithm")
    clock = pygame.time.Clock()

    appIcon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(appIcon)

    node_list = []
    barrier = set()
    start_end = []

    redraw = False
    running = True

    # Create initial grid
    for x in range(0, screen_dimension, gsq_dimension):

        col = []

        for y in range(0, screen_dimension, gsq_dimension):
            gsq = grid_square(x, y, screen)
            col.append(gsq)

        node_list.append(col)

    while running:
        if redraw:
            n = final_dijkstra_helper.new_grid(node_list)
            final_dijkstra_helper.dijk(n, node_list, start_end)
            redraw = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    barrier = final_dijkstra_helper.find_barriers(node_list, grid_dimension)
                    start_end = final_dijkstra_helper.find_start_end(node_list, grid_dimension)

                    if start_end:
                        node_list = final_dijkstra_helper.reconfigure_screen(screen, barrier, start_end)
                        redraw = True

                elif event.key == pygame.K_RIGHT:
                    node_list = final_dijkstra_helper.reset(screen)

        final_dijkstra_helper.check_clicked_req(node_list)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
