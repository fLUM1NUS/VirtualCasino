import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Виртуальное казино")  # Название приложения
    size = width, height = 1600, 900  # размеры окна
    screen = pygame.display.set_mode(size)
    programIcon = pygame.image.load('res/icon.png')  # Иконка приложения
    pygame.display.set_icon(programIcon)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
# commit1
