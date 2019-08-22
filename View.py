'''
    Two main tasks:
        Displaying the game, as the controller commands
        Telling the controller what the user wishes
'''
# View reports to user
import pygame
import sys

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)
taro = 220, 219, 232  # white
white = 250, 250, 250 # Taro 
yellow = 255, 255, 0
red = 255, 0, 0

# For a possible rectangle in the console
# rectangle = (50, 150, 100, 500)
# pygame.draw.rect(screen, white, rectangle)
 
# For a possible circle in the console

move_dict = { '100': 1, '200': 2, '300': 3, '400': 4, '500': 5, '600': 6, '700': 7 }

def display_board():
    for row in range(0, 7):
        for column in range(0, 6):
            pygame.draw.rect(screen, taro, (row * 100, column * 100 + 100 , 100, 100))
            pygame.draw.circle(screen, white, (row * 100 + 50, column * 100 + 150), 45)
            
    pygame.display.update()
            
def update_display_board(board):    
    for row in range(1, 7):
        for column in range(0, 7):
            if board[row][column] == 'R':
                pygame.draw.circle(screen, red, (column * 100 + 50, row * 100 + 50 ), 45)
            elif board[row][column] == 'Y':
                pygame.draw.circle(screen, yellow, (column * 100 + 50, row * 100 + 50), 45)
            pygame.display.update()
            
def update_mouse_motion(current_player, mouse_pos):
    for row in range(0, 7):
        pygame.draw.rect(screen, taro, (0, 0, 700, 100))
        if current_player == 1:
            pygame.draw.circle(screen, red, (mouse_pos, 50), 45)
        else: 
            pygame.draw.circle(screen, yellow, (mouse_pos, 50), 45)

    pygame.display.update()
            
def get_winner(current_player):
        pygame.time.wait(1000)
        myfont = pygame.font.SysFont('monospace', 30)
        label = myfont.render('Player %d wins!' %(current_player), 1, red)
        screen.blit(label, (40,10))
        pygame.display.update()
        pygame.time.wait(4000)
        
def get_tied():
        pygame.time.wait(1000)
        myfont = pygame.font.SysFont('monospace', 40)
        label = myfont.render('Game Tied!, No Winner.', 1, red)
        screen.blit(label, (40,10))
        pygame.display.update()
        
def print_game_over():
    screen = pygame.display.set_mode((700, 700))
    myfont = pygame.font.SysFont('monospace', 30)
    label = myfont.render('GAME OVER, GET OUT OF HERE!', 1, red)
    screen.blit(label, (40,10))
    pygame.display.update()

def print_Invalid_Move():
    pygame.time.wait(1000)
    myfont = pygame.font.SysFont('monospace', 30)
    label = myfont.render('Invalid Move! Try Again', 1, red)
    screen.blit(label, (40,10))
    pygame.display.update()
    pygame.time.wait(2000)
            
def next_move(current_player, counter):
    while True:
        while counter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # Checks if the user wants to quit
        for event in pygame.event.get():
            # Quits the game
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos[0]
                
                update_mouse_motion(current_player, mouse_pos)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos[0]
                return mouse_pos
