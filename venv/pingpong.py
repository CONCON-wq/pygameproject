import pygame
import platform
import random

pygame.init()

WIDTH, HEIGHT = 800,600
PADDLE_WIDTH, PADDLE_HEIGHT = 15,90
BALL_SIZE = 15
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

DIFFICULTY_LEVELS = {
    1: {"bot_speed": 5, "ball_speed": 5, "bot_error_rate": 0.5},
    2: {"bot_speed": 7, "ball_speed": 9, "bot_error_rate": 0.4},
    3: {"bot_speed": 9, "ball_speed": 11, "bot_error_rate": 0.3}
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

player = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT //2, PADDLE_WIDTH, PADDLE_HEIGHT)
bot = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT //2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH //2 - BALL_SIZE //2, HEIGHT//2 - BALL_SIZE //2, BALL_SIZE, BALL_SIZE)

ball_speed_x, ball_speed_y = 0, 0
player_speed = 7
bot_speed = 5
game_state = "menu"
difficulty = 1
player_score = 0
bot_score = 0
font = pygame.font.Font(None,36)

menu_items = ["играть", "Уровень :1 ", "Выход"]

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH //2, HEIGHT //2)
    ball_speed_x = DIFFICULTY_LEVELS[difficulty]["ball_speed"] * random.choice((1,-1))
    ball_speed_y = DIFFICULTY_LEVELS[difficulty]["ball_speed"] * random.choice((1, -1))

def setup():
    global ball_speed_x, ball_speed_y, player_score, bot_score
    player_score = 0
    bot_score = 0
    reset_ball()
    player.center = (50, HEIGHT //2)
    bot.center = (WIDTH - 50, HEIGHT //2)

def draw_menu(mouse_pos):
    screen.fill(BLACK)
    title = font.render("ping pong", True , WHITE)
    screen.blit(title,(WIDTH //2 - title.get_width()//2, HEIGHT //4))

    for i, item in enumerate(menu_items):
        text = font.render(item, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT //2 + i *50 - 50))
        if text_rect.collidepoint(mouse_pos):
            text=font.render(item, True, RED)
        screen.blit(text, text_rect)

def update_menu():
    global game_state, difficulty
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, item in enumerate(menu_items):
                text = font.render(item, True, WHITE)
                text_rect = text.get_rect(center=(WIDTH //2 , HEIGHT //2 + i * 50 - 50))
                if text_rect.collidepoint(mouse_pos):
                    if i == 0:
                        game_state = "playing"
                        setup()
                    elif i == 1:
                        difficulty = (difficulty % 3) + 1
                        menu_items[1] = f"Уровень сложности:{difficulty}"
                    elif  i == 2:
                        pygame.quit()
                        return False

    draw_menu(mouse_pos)
    return True
