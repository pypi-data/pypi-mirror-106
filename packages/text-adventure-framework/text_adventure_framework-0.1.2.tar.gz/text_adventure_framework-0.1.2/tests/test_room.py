import unittest

from text_adventure import AdventureRoom


class AdventureRoomTestCase(unittest.TestCase):
    def test_instance(self):
        room = AdventureRoom('room1', 'desc room1')
        self.assertEqual(True, isinstance(room, AdventureRoom))

    def test_connect_rooms(self):
        room1 = AdventureRoom('room1', 'you\'re in a room1')
        room2 = AdventureRoom('room2', 'you\'re in a room2')

        room1.connect(direction='left', room=room2, description='there is a doorway to another room')
        self.assertEqual(1, len(room1.connections))
        self.assertEqual(1, len(room2.connections))

        self.assertEqual({'description': 'go back where you came from', 'room': room1}, room2.connections['back'])
        self.assertEqual({'description': 'there is a doorway to another room', 'room': room2}, room1.connections['left'])

    def test_options(self):
        room1 = AdventureRoom('room1', 'desc room1')
        room2 = AdventureRoom('room2', 'desc room2')

        room1.connect(direction='left', room=room2, description='you see a doorway to your left')
        self.assertEqual(['left'], room1.options)

    def test_run(self):
        room1 = AdventureRoom('room1', 'desc room1')
        room2 = AdventureRoom('room2', 'desc room2')

        room1.connect(direction='left', room=room2, description='you see a doorway to your left')
        self.assertEqual(['left'], room1.options)

    def test_string_representation(self):
        room1 = AdventureRoom('room1', 'desc room1')
        room2 = AdventureRoom('room2', 'desc room2')
        room1.connect(direction='left', room=room2, description='you see a doorway to your left')

        expected = '''
    Name:        "room1"
    Description: "desc room1"
    is_end:      "False"
	Connections: 
	 "left -> you see a doorway to your left"'''
        str_of = str(room1)
        self.assertEqual(expected, str_of)


if __name__ == '__main__':
    unittest.main()
