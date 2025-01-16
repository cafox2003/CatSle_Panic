from classes.monster.monster import Monster
from logic.game_logic.constants import BOARD, MONSTER_DECK

class Monster_Deck():
    def __init__(self):
        self.all_monsters = Monster.generate_monsters(MONSTER_DECK.TOTAL_MONSTERS)
        self.active_monsters = []
        self.defeated_monsters = []



    def add_monster(self):
        if len(self.all_monsters) > 0:
            self.active_monsters.append(self.all_monsters.pop())
            self.recalculate_positions()


    def move_monsters(self, board=None):
        self.sort_active_monsters()
        self.unhighlight_monsters() # unhighlight all monsters
        self.handle_walls(board) # Handle collision with the walls

        for monster in self.active_monsters:
            if monster.health <= 0:
                self.active_monsters.remove(monster)  # Remove dead monsters
                continue
            monster.move()

        self.recalculate_positions() # Recalculate the position of monsters once they're in the same ring

    # Recalculates positions to divide monsters that share a space
    def recalculate_positions(self):
        processed_monsters = set()  # Keep track of monsters already moved
        for monster in self.active_monsters:

            if monster in processed_monsters:
                continue  # Skip if this monster has already been moved

            if monster.health <= 0:
                self.defeat_monster(monster)  # Remove dead monsters
                continue

            same_space_monsters = self.get_monsters(monster.coordinate.ring, monster.coordinate.color, monster.coordinate.number)
            num_monsters = len(same_space_monsters)
            
            for i, same_monster in enumerate(same_space_monsters):

                same_monster.recalculate_position(num_monsters=num_monsters, monster_pos=i + 1)
                processed_monsters.add(same_monster)  # Mark as processed


    # Handles wall collision
    def handle_walls(self, board):
        walls_destroyed = []
        proccessed_monsters = set()

        # Check if the monster will hip a wall/tower, handle movement/damage accordingly
        for monster in self.active_monsters:
            if monster.health <= 0:
                continue
            else:
                proccessed_monsters.add(monster)

            coord = monster.coordinate
            if coord.next_ring() == BOARD.RINGS[0].lower(): # If the next ring will be a castle ring
                if coord.ring == BOARD.RINGS[1].lower(): # Check the current ring

                    if not board.castles["walls"][coord.number - 1].destroyed: # Destroy the wall
                        board.castles["walls"][coord.number - 1].destroyed = True
                        monster.move(is_forward = False) #Moving monster backwards here will result in it standing still
                        walls_destroyed.append(coord.number) # Keep track of walls that have been destroyed this turn
                        monster.damage()

                    elif (not board.castles["towers"][coord.number - 1].destroyed): #Destroy the tower
                        # Only destroy the tower if the wall was destroyed on a previous turn
                        if coord.number not in walls_destroyed:
                            board.castles["towers"][coord.number - 1].destroyed = True
                            # Remove the monster if it's dead, move it if it's still alive

                            monster.damage()
                        else:
                            monster.move(is_forward = False)
                else: #If already in the castle
                    if not board.castles["towers"][((coord.number) % 6)].destroyed: #Destroy next tower
                        board.castles["towers"][((coord.number) % 6)].destroyed = True
                        monster.damage()

        for m in self.active_monsters:
            if m.health <= 0:
                self.defeat_monster(m)

    def defeat_monster(self, monster):
        self.active_monsters.remove(monster)
        self.defeated_monsters.append(monster)

    def highlight_monsters(self, warrior_card):
        highlight_monsters = self.get_monsters( ring = warrior_card.ring, color =  warrior_card.color)

        for monster in self.active_monsters:
            if monster in highlight_monsters:
                monster.is_highlighted = True
            else:
                monster.is_highlighted = False

    def unhighlight_monsters(self):
        for monster in self.active_monsters:
            monster.is_highlighted = False

    # Returns a list of monsters that are in the corresponding ring/color
    # TODO: Add constants in for the raw strings
    def get_monsters(self, ring=None, color=None, number=None):
        monsters = []
        for monster in self.active_monsters:
            # Start with True and apply each filter if it's provided
            matches = True
            
            # Ring check
            if ring is not None:
                if ring == "hero":
                    # Special case for hero ring
                    matches = matches and monster.coordinate.ring not in ["forest", "castle"]
                else:
                    matches = matches and monster.coordinate.ring == ring
            
            # Color check
            if color is not None and color != "any_color":
                matches = matches and monster.coordinate.color == color
            
            # Number check
            if number is not None:
                matches = matches and monster.coordinate.number == number
                
            if matches:
                monsters.append(monster)
                
        return monsters

    def sort_active_monsters(self):
        self.active_monsters = sorted(self.active_monsters, key=lambda monster: BOARD.RINGS.index(monster.coordinate.ring.title()))
            
    # Check if monsters remain by seeing if all have been defeated
    def monsters_remain(self):
        return (MONSTER_DECK.TOTAL_MONSTERS != len(self.defeated_monsters))
