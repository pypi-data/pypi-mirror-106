import logging

from text_adventure.room import AdventureRoom


class TextAdventureEngine:
    def __init__(self, logger=None):
        self.rooms = {}
        self.starting_room = None

        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

    def add_room(self, name, description, is_end=False):
        if name not in self.rooms:
            room = AdventureRoom(name, description, is_end)

            if 0 == len(self.rooms):
                self.starting_room = room

            self.rooms[name] = room
            return room
        else:
            raise RuntimeError('That room already exists')

    @property
    def number_rooms(self):
        return len(self.rooms)

    def _get_room_by_name(self, room_name):
        if room_name not in self.rooms:
            raise RuntimeError(f'Room named: "{room_name}" doesn\'t exist')
        else:
            return self.rooms[room_name]

    def connect_rooms(self, source: str, destination: str, direction: str, description=''):
        src_room = self._get_room_by_name(source)
        dst_room = self._get_room_by_name(destination)
        src_room.connect(direction=direction, room=dst_room, description=description)

    @staticmethod
    def _player_choice_to_direction(player_choice, current_room):
        try:
            idx = int(player_choice)
        except ValueError:
            return None

        if idx < len(current_room.options):
            direction = current_room.options[idx]
            return direction

    def start(self):
        current_room = self.starting_room

        while not current_room.is_end:
            idx = 0
            for direction in current_room.options:
                desc = current_room.get_direction_description(direction)
                print(f'{idx}: {direction} -> {desc}')
                idx += 1

            player_choice = input('Chose option: ')
            direction = self._player_choice_to_direction(player_choice, current_room)

            if direction is None:
                print('try again, with a valid choice this time please')
            else:
                self.logger.debug(f'you chose: {player_choice} -> {direction}')
                new_room = current_room.get_next_room(direction)
                current_room = new_room

        print(current_room.description)
