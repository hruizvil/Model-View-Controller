'''
    Two main tasks:
        Displaying the game, as the controller commands
        Telling the controller what the user wishes
'''
# View reports to user
import hw7_controller
import pygame
import sys
# "User input to know what user wants"

# controller = hw7_controller.Controller()
# print(controller.hello)
pygame.init()
 
size = width, height = 700, 600
 
screen = pygame.display.set_mode(size)

pygame.display.update( )
 
# while True:
#     user_column_choice = int(input("Pick a column 1 - 7: "))
#     if 1 <= user_column_choice <= 7:
#         break
       
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
     
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("")
