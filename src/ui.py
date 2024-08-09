from dataclasses import dataclass

import pygame
from pygame.color import THECOLORS


@dataclass
class Button:
    x: int
    y: int
    width: int
    height: int
    button_color: str

    font: pygame.font.SysFont
    text: str
    text_color: str


class ButtonFactory:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def create(self, button: Button) -> pygame.Rect:
        rect = pygame.Rect(
            button.x, button.y, button.width, button.height
        )

        pygame.draw.rect(
            self.screen,
            THECOLORS[button.button_color],
            rect,
        )

        font = button.font
        text = font.render(button.text, True, THECOLORS[button.text_color])
        self.screen.blit(text, (button.x, button.y))

        pygame.display.flip()
        return rect
