import pygame


class Enemy:

    def __init__(self, start_pos, state, scroll_speed):
        self.x = start_pos[0]
        self.y = start_pos[1]
#        self.image = pygame.image.load(image)
#        self.width = self.image.get_width()
#        self.height = self.image.get_height()
#        self.scaled_image = pygame.transform.scale(self.image, (self.width * scale, self.height * scale))
#        self.width *= scale
#        self.height *= scale
        self.game_state = state
        self.radius = 20
        #self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.rect = None
        self.speed = scroll_speed
        self.clear_points = 100
        self.weapon_collision = False
        self.special_effect = None
        self.debuffs = []
        self.defense = 0
        self.stunned = ["False", 0]
        self.burned = ["False", 0]
        self.pierced = ["False", 0]
        self.air = None

    def update(self, dt, player_rect, state):
        if state == "Runner":
            self.x -= self.speed * dt
            self.rect.x = self.x
            self.rect.y = self.y
            # Collision Check
            if self.rect.colliderect(player_rect):
                collision = True
                return collision
        elif state == "Combat":
            # Add / Remove Debuffs
            if "Stun" in self.debuffs and self.stunned[0] == "False":
                self.stunned[0] = "True"
                self.stunned[1] = 3
            if self.stunned[1] == 0 and self.stunned[0] == "True":
                self.debuffs.remove("Stun")
                self.stunned[0] = "False"
            if "Burn" in self.debuffs and self.burned[0] == "False":
                self.burned[0] = "True"
                self.burned[1] = 2
            if self.burned[1] == 0 and self.burned[0] == "True":
                self.debuffs.remove("Burn")
                self.burned[0] = "False"
            if "Pierce" in self.debuffs and self.pierced[0] == "False":
                self.pierced[0] = "True"
                self.defense /= 2
                self.pierced[1] = 2
            if self.pierced[1] == 0 and self.pierced[0] == "True":
                self.debuffs.remove("Pierce")
                self.defense *= 2
                self.pierced[0] = "False"


class Slimes(Enemy):

    def __init__(self, start_pos, state, scroll_speed):
        super().__init__(start_pos, state, scroll_speed)
        self.health = 50
        self.radius = 20
        self.attack = 20
        self.defense = 10
        self.luck = 0.02
        self.dodge = 0.02
        self.air = False
        self.slime_img = pygame.image.load("images\\Slime.png")
        self.slime_small_img = pygame.image.load("images\\Slime_small.png")
        self.rect = pygame.Rect(int(self.x), int(self.y), int(self.slime_img.get_width()),int(self.slime_img.get_height()) - 10)
        self.height = int(self.slime_img.get_height()) - 10

    def draw(self, surf):
        surf.blit(self.slime_img, (int(self.x), int(self.y)))
        # Debug Collision
#        pygame.draw.rect(surf, (255, 255, 0), self.rect, 1)

    def draw_portrait(self, surf):
        surf.blit(self.slime_small_img, (700,200))


class Wolf(Enemy):

    def __init__(self, start_pos, state, scroll_speed):
        super().__init__(start_pos, state, scroll_speed)
        self.health = 80
        self.radius = 10
        self.attack = 30
        self.defense = 10
        self.luck = 0.04
        self.dodge = 0.07
        self.air = False
        self.wolf_img = pygame.image.load("images\\wolf.png")
        self.wolf_img_flip = pygame.transform.flip(self.wolf_img, True, False)
        self.wolf_small_img = pygame.image.load("images\\wolf_small.png")
        self.wolf_small_img_flip = pygame.transform.flip(self.wolf_small_img, True, False)
        self.rect = pygame.Rect(int(self.x), int(self.y + 75), int(self.wolf_img_flip.get_width()), int(self.wolf_img_flip.get_height()) - 10)
        self.height = int(self.wolf_img_flip.get_height()) - 10

    def draw(self, surf):
        surf.blit(self.wolf_img_flip, (int(self.x), int(self.y)))
        # Debug Collision
#        pygame.draw.rect(surf, (255, 255, 0), self.rect, 1)

    def draw_portrait(self, surf):
        surf.blit(self.wolf_small_img_flip, (700,180))


class Bird(Enemy):

    def __init__(self, start_pos, state, scroll_speed):
        super().__init__(start_pos, state, scroll_speed)
        self.health = 60
        self.radius = 10
        self.attack = 40
        self.defense = 10
        self.luck = 0.02
        self.dodge = 0.08
        self.air = True
        self.bird_img = pygame.image.load("images\\bird.png")
        self.bird_img_flip = pygame.transform.flip(self.bird_img, True, False)
        self.bird_small_img = pygame.image.load("images\\Bird_small.png")
        self.bird_small_img_flip = pygame.transform.flip(self.bird_small_img, True, False)
        self.rect = pygame.Rect(int(self.x), int(self.y), int(self.bird_img_flip.get_width()), int(self.bird_img_flip.get_height()) - 10)
        self.height = int(self.bird_img_flip.get_height()) + 75

    def draw(self, surf):
        surf.blit(self.bird_img_flip, (int(self.x), int(self.y)))
        # Debug Collision
#        pygame.draw.rect(surf, (255, 255, 0), self.rect, 1)

    def draw_portrait(self, surf):
        surf.blit(self.bird_small_img_flip, (700, 180))


class BasicBoss(Enemy):
    def __init__(self, start_pos, state, scroll_speed):
        super().__init__(start_pos, state, scroll_speed)
        self.health = 300
        self.radius = 50
        self.attack = 60
        self.defense = 30
        self.height = 50
        self.luck = 0
        self.dodge = 0
        self.rect = pygame.Rect(int(self.x - self.radius), int(self.y - self.radius), self.radius * 2, self.radius * 2)

    def draw(self, surf):
        pygame.draw.circle(surf, (255, 0, 0), (int(self.x), int(self.y)), self.radius)