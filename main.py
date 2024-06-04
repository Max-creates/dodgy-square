import pygame
from pygame.font import Font
from pygame.time import Clock
import random
import sys

class DodgySquare:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Dodgy Square')

        # Colours
        self.WHITE: tuple = (255, 255, 255)
        self.BLACK: tuple = (0, 0, 0)
        self.RED: tuple = (255, 99, 71)
        self.BLUE: tuple = (65, 105, 225)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_pos: list[int] = []
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20 # Low = lots, High = few

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0

    def create_enemy(self):
        enemy_pos: list[int] = [random.randint(0, self.screen_width - self.enemy_size), -self.enemy_size]
        self.enemy_list.append(enemy_pos)

    def update_enemy_position(self):
        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        for idx, enemy_pos in enumerate(self.enemy_list):
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                self.enemy_list.pop(idx)
                self.score += 1
                self.enemy_speed = 0.1

                if self.enemy_frequency > 10:
                    if self.score % 15 == 0:
                        self.enemy_frequency -= 2

    def detect_collision(self, player_pos, enemy_pos) -> bool:
        px, py = player_pos
        ex, ey = enemy_pos

        if (px <= ex (px + self.player_size)) or (ex <= px < (ex + self.enemy_size)):
            if (py <= ey(py + self.player_size)) or (ey <= py < (ey + self.enemy_size)):
                return True
        return False

    def show_game_over(self):
        game_over_text = self.font.render('Game Over', True, self.WHITE)
        self.screen.blit(game_over_text, (self.screen_width // 2 - 70, self.screen_height // 2 - 16))

    def replay_game(self):
        # Reset enemies
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20

        # Reset game stats
        self.game_over: bool = False
        self.frame_count: int = 0
        self.score: int = 0

    def draw_character(self, color: tuple, position: list[int], size: int):
        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))


