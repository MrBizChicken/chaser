import main_block, pygame

class Enemy(main_block.Main_block):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.speed = 10

    def update(self):
        self.move()


    def move(self):

        gw = pygame.display.Info().current_w
        gh = pygame.display.Info().current_w
        self.rect = self.rect.move(self.speed, 0)

        if self.rect.right > gw or self.rect.left < 0:
            self.speed = -self.speed
