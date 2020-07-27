""" This program displays the MESSAGE text as a jumbotron screen using PyGame
"""
import pygame
from pygame.locals import KEYDOWN, K_ESCAPE
from bitmap import font_bitmap, CHARACTER_WIDTH, CHARACTER_HEIGHT

MESSAGE = "Hello, World! "

LED_RADIUS = 5
LED_DIAMETER = LED_RADIUS * 2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = LED_DIAMETER * CHARACTER_HEIGHT  # 600

COLOR_BACKGROUND = (0, 0, 128)
COLOR_LED_ON = (200, 200, 0)
COLOR_LED_OFF = (150, 50, 0)


def display_message(message_txt, start_x=0):
    """ Display the actual message text starting from the COLUMN start_x """

    character_number = 0
    x_increment = LED_DIAMETER + 2
    x_start_character = LED_RADIUS
    x_position = x_start_character

    for letter in message_txt:

        ascii_code = ord(letter)

        for y_loop in range(CHARACTER_HEIGHT):

            mask = int(128)
            byte = font_bitmap[(ascii_code - 32)][CHARACTER_HEIGHT - y_loop - 1]

            x_position = x_start_character
            for _ in range(start_x, CHARACTER_WIDTH):

                y_position = ((y_loop * LED_DIAMETER) + 2) + LED_RADIUS

                led_color = COLOR_LED_OFF
                if int(byte) & int(mask):
                    led_color = COLOR_LED_ON

                pygame.draw.circle(screen, led_color, (x_position, y_position), LED_RADIUS)

                x_position = x_position + x_increment
                mask = mask / 2

        x_start_character = x_position
        start_x = 0
        character_number = character_number + 1


if __name__ == "__main__":

    pygame.init()

    infoObject = pygame.display.Info()
    print(infoObject)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    RUNNING = True
    screen.fill(COLOR_BACKGROUND)

    timer = pygame.time.Clock()

    COLUMN = 0
    while RUNNING:

        if COLUMN >= CHARACTER_WIDTH:
            COLUMN = 0
            MESSAGE = MESSAGE[1:] + MESSAGE[0]

        display_message(MESSAGE, COLUMN)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    RUNNING = False

            if event.type == pygame.QUIT:
                RUNNING = False

        COLUMN = COLUMN + 1

        timer.tick(15)
