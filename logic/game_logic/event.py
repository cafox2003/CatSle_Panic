#Chatgpt's implementation of my idea. Basically, create an object called game_state which has all needed vars, and then write methods below
# That are implemented
class Event:
    @staticmethod
    def getEvent(event_name, argument="none", game_state):
        if event_name == "Plague":
            Event.plague(game_state)
        elif event_name == "Boulder":
            Event.boulder(game_state)
        elif event_name == "Move Monsters":
            if argument == "clockwise":
                Event.move_monsters(game_state, "clockwise")
            elif argument == "counterclockwise":
                Event.move_monsters(game_state, "counterclockwise")

    @staticmethod
    def plague(game_state):
        print("Plague event: Discard all Knight cards!")
        # Implement logic to discard all knight cardsnts as needed
