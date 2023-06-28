from game import Game
import agent
import pygame
from copy import deepcopy


# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = {
    "background": (187, 173, 160),
    "light": (249, 246, 242),
    "dark": (119, 110, 101),
    "0": (205, 193, 180),
    "2": (238, 228, 218),
    "4": (237, 224, 200),
    "8": (242, 177, 121),
    "16": (245, 149, 99),
    "32": (246, 124, 95),
    "64": (246, 94, 59),
    "128": (237, 207, 114),
    "256": (237, 204, 97),
    "512": (237, 200, 80),
    "1024": (237, 197, 63),
    "2048": (237, 194, 46)
}
KEYS = {
    "273": "w",
    "119": "w",
    "274": "s",
    "115": "s",
    "276": "a",
    "97": "a",
    "275": "d",
    "100": "d"
}

# Define Configurations
grid_size = 4
cell_size = 100
grid_width = grid_size * cell_size
grid_height = grid_size * cell_size
window_width = grid_width + 10
window_height = grid_height + 10

# TODO: make animation for the movement


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("2024")
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        key = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if str(event.key) not in KEYS:
                    continue
                key = KEYS[str(event.key)]

        board = game.board

        key = agent.play_random(board)
        move = False
        if key == 'w':
            move = game.move_up()
        elif key == 's':
            move = game.move_down()
        elif key == 'a':
            move = game.move_left()
        elif key == 'd':
            move = game.move_right()
        if move:
            game.new_cell()

        window.fill(COLORS["background"])

        for x in range(4):
            for y in range(4):
                pos = (x * cell_size + 10, y * cell_size + 10)
                rect = pygame.Rect(pos[0], pos[1], cell_size-10, cell_size-10)
                pygame.draw.rect(window, COLORS[str(board[y][x])], rect, 0)
                if board[y][x] != 0:
                    if board[y][x] == 2 or board[y][x] == 4:
                        text = font.render(str(board[y][x]), True, COLORS["dark"])
                        text_rect = text.get_rect(center=rect.center)
                        window.blit(text, text_rect)
                    else:
                        text = font.render(str(board[y][x]), True, COLORS["light"])
                        text_rect = text.get_rect(center=rect.center)
                        window.blit(text, text_rect)







        pygame.display.flip()
        clock.tick(30)
    pygame.quit()




