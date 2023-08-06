# text-adventure-framework


## Why create this?
My son wanted to program a text adventure game using python. 
I didn't find any frameworks in pure python that would make that easy. 
So decided to roll my own. It's rudimentary, but functional. 

## Install:
`pip install text-adventure-framework`

Or

`pip install git+https://github.com/Caesurus/text_adventure.git`


## Usage:
```python
from text_adventure import TextAdventureEngine 
e = TextAdventureEngine()
e.add_room(name='starting room', description='you wake up in a starting room')
e.add_room(name='room 1', description='room after leaving start')
e.add_room(name='finish', description='outside world', is_end=True)

e.connect_rooms(source='starting room', destination='room 1', direction='left', description='you see a door to your left')
e.connect_rooms(source='room 1', destination='finish', direction='forward', description='the exit is right in front of you')

e.start()
```
