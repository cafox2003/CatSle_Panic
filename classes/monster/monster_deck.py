from classes.monster.monster import Monster

class Monster_Deck():
    def __init__(self):
        self.all_monsters = Monster.generate_monsters(100)
        self.active_monsters = []
        self.defeated_monsters = []

    def add_monster(self):
        self.active_monsters.append(self.all_monsters.pop())

    def move_monsters(self):
        monsters_to_move = list(self.active_monsters)  # Copy to prevent modification during iteration
        processed_monsters = set()  # Keep track of monsters already moved

        self.unhighlight_monsters() # unhighlight all monsters

        for monster in monsters_to_move:
            if monster in processed_monsters:
                continue  # Skip if this monster has already been moved

            if monster.health <= 0:
                self.active_monsters.remove(monster)  # Remove dead monsters
                continue

            # Get all monsters in the same space as the current one
            same_space_monsters = self.get_monsters(monster.coordinate.ring, monster.coordinate.color, monster.coordinate.number)

            num_monsters = len(same_space_monsters)
            for i, same_monster in enumerate(same_space_monsters):
                same_monster.move(num_monsters=num_monsters, monster_pos=i + 1)
                processed_monsters.add(same_monster)  # Mark as processed

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
