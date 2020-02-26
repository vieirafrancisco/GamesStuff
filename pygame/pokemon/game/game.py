import os
import pygame

from settings import *
from game.map.map import Map, RandomMap, LoaderMap
from game.entities.player import Player

class Game:
    def __init__(self):
        self.size = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokémon")
        #self.map = RandomMap(30, 30)
        self.map = LoaderMap(os.path.join("game","resources", "img", "maps", "map01.png"))
        self.player = Player(T_WIDTH//2,T_HEIGHT//2)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.map.show(self._disp_window)
        self.player.show(self._disp_window)

    def on_loop(self):
        self.player.move(self.map)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_execute(self):
        self.on_init()
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self._disp_window.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
        self.on_cleanup()