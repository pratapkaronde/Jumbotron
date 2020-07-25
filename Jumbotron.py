import pygame
from pygame.locals import KEYDOWN, K_ESCAPE
from bitmap import font_bitmap, CHARACTER_WIDTH, CHARACTER_HEIGHT

LED_RADIUS = 5
LED_DIAMETER = LED_RADIUS * 2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = LED_DIAMETER * CHARACTER_HEIGHT  # 600

COLOR_BACKGROUND = (0, 0, 128)
COLOR_LED_ON = (200, 200, 0)
COLOR_LED_OFF = (150, 50, 0)


def displayMessage(message, start_x=0):

    character_number = 0
    x_increment = LED_DIAMETER + 2
    x_start_character = LED_RADIUS
    x_position = x_start_character

    for letter in message:

        ascii = ord(letter)

        for y in range(CHARACTER_HEIGHT):

            mask = int(128)
            byte = font_bitmap[(ascii - 32)][CHARACTER_HEIGHT - y - 1]

            x_position = x_start_character
            for x in range(start_x, CHARACTER_WIDTH):

                # x_position = ((x * LED_DIAMETER) + 2) + (character_number *
                #                                         (CHARACTER_WIDTH * (LED_DIAMETER))) + LED_RADIUS

                y_position = ((y * LED_DIAMETER) + 2) + LED_RADIUS

                led_color = COLOR_LED_OFF
                if (int(byte) & int(mask)):
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
    running = True
    screen.fill(COLOR_BACKGROUND)

    message = "Pratap Karonde "
    timer = pygame.time.Clock()

    x = 0
    while running:

        if (x >= CHARACTER_WIDTH):
            x = 0
            message = message[1:] + message[0]

        displayMessage(message, x)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == pygame.QUIT:
                running = False

        x = x + 1

        timer.tick(15)
