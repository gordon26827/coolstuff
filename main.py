import pygame
#from pygame import mixer
from button import *

# initialize screen
pygame.init()

# create display
screen = pygame.display.set_mode((800, 875))

# create board
background = pygame.image.load('board.jpg')

# start background music
#mixer.music.load('gymnopedie.wav')
#mixer.music.play(-1)

# title and icon
pygame.display.set_caption("TicTacToe!")
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)

# initialize buttons
b1 = Square((11, 14))
b2 = Square((276, 14))
b3 = Square((540, 14))
b4 = Square((11, 276))
b5 = Square((276, 276))
b6 = Square((540, 276))
b7 = Square((11, 537))
b8 = Square((276, 537))
b9 = Square((540, 537))
new_game = Button((45, 175, 0), (35, 130, 0), (610, 810), (180, 55), True)

# load circles and crosses
cross = pygame.image.load('cross.png')
circle = pygame.image.load('circle.png')

# score
font = pygame.font.Font('robotomono.ttf', 32)
p1_score = 0
p2_score = 0

def check_game():
    if b1.img and b1.img == b2.img == b3.img:
        player = True if b1.img == cross else False
        return (True, player, (65, 140), (725, 140))
    if b4.img and b4.img == b5.img == b6.img:
        player = True if b4.img == cross else False
        return (True, player, (65, 410), (725, 410))
    if b7.img and b7.img == b8.img == b9.img:
        player = True if b7.img == cross else False
        return (True, player, (65, 685), (725, 685))
    if b1.img and b1.img == b4.img == b7.img:
        player = True if b1.img == cross else False
        return (True, player, (125, 65), (125, 725))
    if b2.img and b2.img == b5.img == b8.img:
        player = True if b2.img == cross else False
        return (True, player, (395, 65), (395, 725))
    if b3.img and b3.img == b6.img == b9.img:
        player = True if b3.img == cross else False
        return (True, player, (670, 65), (670, 725))
    if b1.img and b1.img == b5.img == b9.img:
        player = True if b1.img == cross else False
        return (True, player, (75, 75), (740, 740))
    if b3.img and b3.img == b5.img == b7.img:
        player = True if b3.img == cross else False
        return (True, player, (75, 740), (740, 75))
    else:
        return [False]

def show_score():
    score = font.render('Player 1: [{}]   Player 2: [{}]'.format(p1_score, p2_score), True, (0, 0, 0))
    screen.blit(score, (10, 815))

def button_message(pos, message):
    score = font.render(message, True, (0, 0, 0))
    screen.blit(score, (pos[0] + 10, pos[1] + 5))

running, turn, key_press, seen = True, True, False, False
while running:
    # RGB background
    screen.fill((240, 240, 240))
    # background
    screen.blit(background, (0, 0))

    # get mouse position
    pos = pygame.mouse.get_pos()

    # check for key press
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            key_press = True
        elif event.type == pygame.QUIT:
            running = False

    # check game
    game = check_game()

    # draw buttons and react to inputs
    for button in Button.instances:
        if button.press:
            screen.blit(button.img, (button.pos[0] + 30, button.pos[1] + 30))
        elif button.is_in(pos):
            pygame.draw.rect(screen, button.dark, button.pos + button.size)
            if key_press:
                if not game[0] and repr(button) == 'Square':
                    button.img = cross if turn else circle
                    turn = not turn
                    button.press = True
                elif repr(button) == 'Button':
                    game = [False]
                    seen = False
                    for item in Button.instances:
                        item.press = False
                        item.img = None
        elif repr(button) != 'Square':
            pygame.draw.rect(screen, button.light, button.pos + button.size)
            button_message(button.pos, 'New Game')

    # check if game over
    if game[0]:
        pygame.draw.line(screen, (255, 0, 0), game[2], game[3], 40)
        if not seen:
            if game[1]:
                p1_score += 1
            else:
                p2_score += 1
            seen = True

    # update score
    show_score()

    # update display
    pygame.display.update()

    # reset key press
    key_press = False
