import pygame, random, os
from gamefunctions import (print_welcome, print_shop_menu, purchase_item, new_random_monster, fight_monster, sleep, shop, print_inventory, equip_item, json_save_game, json_load_game)

pygame.init()
grid_size = 32
grid_width = 10
grid_height = 10
screen_width = 320
screen_height = 320

# I couldn't make getcwd to work.
# Instead I found this file path on Stack Overflow - needed to ensure images load from the game's directory instead of where Python is run from.
GAME_DIR = os.path.dirname(os.path.abspath(__file__))

PLAYER_IMAGE = os.path.join(GAME_DIR, "player_sprite.png")
MONSTER_IMAGE = os.path.join(GAME_DIR, "monster_sprite.png")

print(f"Image directories loading from:")
print(f"Player image: {PLAYER_IMAGE}")
print(f"Monster image: {MONSTER_IMAGE}")

class WanderingMonster:
    def __init__(self, grid_width, grid_height, monster_image=None):
        self.max_width = grid_width
        self.max_height = grid_height
        self.pos_x = random.randint(0, self.max_width - 1)
        self.pos_y = random.randint(0, self.max_height - 1)
        self.stats = new_random_monster()
        self.image = monster_image

    def move(self):
        move_x = random.choice([-1, 0, 1])
        move_y = random.choice([-1, 0, 1])
        self.pos_x = (self.pos_x + move_x) % self.max_width
        self.pos_y = (self.pos_y + move_y) % self.max_height

    def check_for_player(self, player_x, player_y, player_health, player_gold, player_items):
        if self.pos_x == player_x and self.pos_y == player_y:
            return fight_monster(self.stats, player_health, player_gold, player_items)
        return player_health, player_gold

class MonsterUIHandler:
    def __init__(self):
        self.is_first_start = True
        self.player_image = None
        self.monster_image = None

        try:
            if os.path.exists(PLAYER_IMAGE):
                print(f"The image for the player was found - {PLAYER_IMAGE}")
                self.player_image = pygame.image.load(PLAYER_IMAGE)
                self.player_image = pygame.transform.scale(self.player_image, (grid_size, grid_size))
            else:
                print(f"Couldn't find player image @ {PLAYER_IMAGE}")
        except Exception as e:
            print(f"The player image didn't load properly: {e}")
            self.player_image = None

        try:
            if os.path.exists(MONSTER_IMAGE):
                print(f"Found monster image @ {MONSTER_IMAGE}")
                self.monster_image = pygame.image.load(MONSTER_IMAGE)
                self.monster_image = pygame.transform.scale(self.monster_image, (grid_size, grid_size))
            else:
                print(f"Could not find monster image @ {MONSTER_IMAGE}")
        except Exception as e:
            print(f"Error loading monster image: {e}")
            self.monster_image = None

    def update_monsters(self, monster_list, player_x, player_y, player_health, player_gold, player_items):
        for monster in monster_list[:]:
            monster.move()

            player_health, player_gold = monster.check_for_player(
                player_x, player_y,
                player_health, player_gold,
                player_items
            )
            if player_health <= 0:
                return monster_list, player_health, player_gold

            if monster.pos_x == player_x and monster.pos_y == player_y:
                monster_list.remove(monster)

        if len(monster_list) == 0:
            monster_list.extend([
                WanderingMonster(grid_width, grid_height, self.monster_image),
                WanderingMonster(grid_width, grid_height, self.monster_image)
            ])

        return monster_list, player_health, player_gold

    def run_game_ui(self):
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Ethan's monster game- v12.8.24")
        player = pygame.Rect(0, 0, grid_size, grid_size)

        player_health = 50
        player_gold = 10
        player_inventory = {}

        if self.is_first_start:
            monsters = [
                WanderingMonster(grid_width, grid_height, self.monster_image),
            ]
        else:
            monsters = [
                WanderingMonster(grid_width, grid_height, self.monster_image),
                WanderingMonster(grid_width, grid_height, self.monster_image),
            ]

        running = True
        clock = pygame.time.Clock()

        while running:
            screen.fill((0, 0, 0))

            if self.player_image:
                screen.blit(self.player_image, player)
            else:
                pygame.draw.rect(screen, (0, 255, 255), player)

            for monster in monsters:
                monster_rect = pygame.Rect(
                    monster.pos_x * grid_size,
                    monster.pos_y * grid_size,
                    grid_size,
                    grid_size
                )
                if monster.image:
                    screen.blit(monster.image, monster_rect)
                else:
                    pygame.draw.rect(screen, (255, 0, 0), monster_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                elif event.type == pygame.KEYDOWN:
                    old_x = player.x // grid_size
                    old_y = player.y // grid_size

                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_UP:
                        player.y = (player.y - grid_size) % screen_height
                    elif event.key == pygame.K_DOWN:
                        player.y = (player.y + grid_size) % screen_height
                    elif event.key == pygame.K_LEFT:
                        player.x = (player.x - grid_size) % screen_width
                    elif event.key == pygame.K_RIGHT:
                        player.x = (player.x + grid_size) % screen_width

                    new_x = player.x // grid_size
                    new_y = player.y // grid_size

                    if old_x != new_x or old_y != new_y:
                        monsters, player_health, player_gold = self.update_monsters(
                            monsters,
                            new_x, new_y,
                            player_health,
                            player_gold,
                            player_inventory
                        )

                    if player_health <= 0:
                        print("Game is over")
                        running = False
                        break

            pygame.display.flip()
            clock.tick(60)

        self.is_first_start = False
        pygame.quit()