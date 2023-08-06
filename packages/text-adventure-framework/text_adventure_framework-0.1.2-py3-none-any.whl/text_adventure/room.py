class AdventureRoom:
    def __init__(self, name, description='', is_end=False):
        self.name = name
        self.description = description
        self.connections = {}
        self.is_end = is_end

    def connect(self, direction: str, room, description=''):
        if direction not in self.connections:
            self.connections[direction] = {'room': room, 'description': description}
            if direction != 'back':
                room.connect('back', self, description='go back where you came from')
        else:
            raise RuntimeError(f'there is already a room connected to that direction: {self.connections[direction]}')

    @property
    def options(self):
        return list(self.connections.keys())

    def get_direction_description(self, direction):
        if direction in self.connections:
            return self.connections[direction].get('description')

    def get_next_room(self, direction):
        if direction in self.connections:
            return self.connections[direction].get('room')

    def __str__(self):
        output = f'''
    Name:        "{self.name}"
    Description: "{self.description}"
    is_end:      "{self.is_end}"
'''
        if self.connections:
            output += "\tConnections: \n"
            for i in self.connections:
                output += f'\t "{i} -> {self.connections[i].get("description")}"'

        return output
