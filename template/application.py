"""Application module"""

import logging
import time
import pygame

class App():
    """Application class"""
    def __init__(self, delay: float) -> None:
        self._delay = delay

        self._running = True
        self._display_surf = None
        self._width = 640
        self._height = 480
        self._size = (self._width, self._height)
        self._time = time.time()
        self._counter = 0
        self._complete = False
        self.font_s = None
        self.font_l = None
    def on_init(self) -> None:
        """On init."""
        pygame.init()
        pygame.display.set_caption("Title")
        self._display_surf = pygame.display.set_mode(self._size,
                                                     pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        #self.font = pygame.font.SysFont('courier.ttf', 72)
        font_name = pygame.font.get_default_font()
        logging.info("System font: %s", font_name)
        self.font_s = pygame.font.SysFont(None, 22)
        self.font_l = pygame.font.SysFont(None, 33)
        return True
    def on_event(self, event: pygame.event.Event) -> None:
        """On event."""
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                self._running = False
        else:
            logging.debug(event)
    def on_loop(self, elapsed: float) -> None:
        """On loop."""
        self._counter+=elapsed
        if self._counter > self._delay:
            logging.info("tick")
            self._counter = 0
            if self._complete is False:
                pass
    def on_render(self) -> None:
        """On render."""
        self._display_surf.fill((0,0,0))
        pygame.display.update()
    def on_cleanup(self) -> None:
        """On cleanup."""
        pygame.quit()
    def on_execute(self) -> None:
        """On execute."""
        if self.on_init() is False:
            self._running = False
        while self._running:
            current = time.time()
            elapsed = current - self._time
            self._time = current
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop(elapsed)
            self.on_render()
        self.on_cleanup()
