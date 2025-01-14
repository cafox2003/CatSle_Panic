from classes.monster.monster import Monster
from logic.game_logic.constants import BOARD

class Monster_Deck():
    def __init__(self):
        self.all_monsters = Monster.generate_monsters(100)
        self.active_monsters = []
        self.defeated_monsters = []

    def add_monster(self):
        self.active_monsters.append(self.all_monsters.pop())

    def move_monsters(self, board=None):
        monsters_to_move = list(self.active_monsters)  # Copy to prevent modification during iteration
        processed_monsters = set()  # Keep track of monsters already moved
        
        self.unhighlight_monsters()  # unhighlight all monsters
        
        for monster in monsters_to_move:
            if monster in processed_monsters:
                continue  # Skip if this monster has already been moved
            
            if monster.health <= 0:
                continue  # Skip dead monsters but don't remove them yet
            
            # Get all monsters in the same space as the current one
            same_space_monsters = self.get_monsters(
                monster.coordinate.ring, 
                monster.coordinate.color, 
                monster.coordinate.number
            )
            
            num_monsters = len(same_space_monsters)
            monsters_to_remove = set()  # Track monsters to remove after processing
            wall_attack = False  # Track if this group is attacking a wall
            
            # First check if this group is attacking a wall
            if (monster.coordinate.next_ring() == BOARD.RINGS[0].lower() and 
                monster.coordinate.ring == BOARD.RINGS[1].lower() and 
                not board.castles["walls"][monster.coordinate.number - 1].destroyed):
                wall_attack = True
                # Only the first monster takes damage
                same_space_monsters[0].damage()
                if same_space_monsters[0].health <= 0:
                    monsters_to_remove.add(same_space_monsters[0])
                board.castles["walls"][monster.coordinate.number - 1].destroyed = True
            
            for i, same_monster in enumerate(same_space_monsters):
                coord = same_monster.coordinate
                
                if coord.next_ring() == BOARD.RINGS[0].lower():  # If the next ring will be a castle ring
                    if coord.ring == BOARD.RINGS[1].lower():  # Check the current ring
                        if wall_attack:
                            # If attacking wall, all monsters stay in place
                            processed_monsters.add(same_monster)
                        elif not board.castles["towers"][coord.number - 1].destroyed:  # Destroy the tower
                            board.castles["towers"][coord.number - 1].destroyed = True
                            if i == 0:  # Only first monster takes damage
                                same_monster.damage()
                                if same_monster.health > 0:
                                    same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                                else:
                                    monsters_to_remove.add(same_monster)
                            else:
                                # Other monsters in group move without taking damage
                                same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                        else:
                            same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                    else:  # If already in the castle
                        if not board.castles["towers"][((coord.number) % 6)].destroyed:  # Destroy next tower
                            board.castles["towers"][((coord.number) % 6)].destroyed = True
                            if i == 0:  # Only first monster takes damage
                                same_monster.damage()
                        
                        if same_monster.health > 0:  # If it's still alive, move regardless of if the tower was destroyed
                            same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                        else:
                            monsters_to_remove.add(same_monster)
                else:
                    same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                
                if same_monster.health > 0:
                    processed_monsters.add(same_monster)
                else:
                    monsters_to_remove.add(same_monster)
        
            # Remove dead monsters after processing the group
            for dead_monster in monsters_to_remove:
                if dead_monster in self.active_monsters:  # Check if monster is still in the list
                    self.active_monsters.remove(dead_monster)
    # def move_monsters(self, board=None):
    #     monsters_to_move = list(self.active_monsters)  # Copy to prevent modification during iteration
    #     processed_monsters = set()  # Keep track of monsters already moved
    #
    #     self.unhighlight_monsters() # unhighlight all monsters
    #
    #     for monster in monsters_to_move:
    #         if monster in processed_monsters:
    #             continue  # Skip if this monster has already been moved
    #
    #         if monster.health <= 0:
    #             self.active_monsters.remove(monster)  # Remove dead monsters
    #             continue
    #
    #         # Get all monsters in the same space as the current one
    #         same_space_monsters = self.get_monsters(monster.coordinate.ring, monster.coordinate.color, monster.coordinate.number)
    #
    #         num_monsters = len(same_space_monsters)
    #         for i, same_monster in enumerate(same_space_monsters):
    #
    #             # Logic to detect/destroy walls and towers
    #             coord = same_monster.coordinate
    #             if coord.next_ring() == BOARD.RINGS[0].lower(): # If the next ring will be a castle ring
    #                 if coord.ring == BOARD.RINGS[1].lower(): # Check the current ring
    #
    #                     if not board.castles["walls"][coord.number - 1].destroyed: # Destroy the wall
    #                         board.castles["walls"][coord.number - 1].destroyed = True
    #                         same_monster.damage()
    #                     elif not board.castles["towers"][coord.number - 1].destroyed: #Destroy the tower
    #                         board.castles["towers"][coord.number - 1].destroyed = True
    #
    #                         # Remove the monster if it's dead, move it if it's still alive
    #                         same_monster.damage()
    #                         if same_monster.health > 0:
    #                             same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
    #                     else:
    #                         same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
    #                 else: #If already in the castle
    #                     if not board.castles["towers"][((coord.number) % 6)].destroyed: #Destroy next tower
    #                         board.castles["towers"][((coord.number) % 6)].destroyed = True
    #                         same_monster.damage()
    #
    #                     if same_monster.health > 0: #If it's still alive, move regardless of if the tower was destroyed
    #                         same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
    #
    #                 # Remove all monster that died
    #                 if same_monster.health <= 0:
    #                     self.active_monsters.remove(monster)
    #             else:
    #                 same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
    #
    #             processed_monsters.add(same_monster)  # Mark as processed

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
