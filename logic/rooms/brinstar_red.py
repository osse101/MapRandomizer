from logic.areas import Area
from maze_builder.types import Room

rooms = [
    Room(
        name='Red Tower',
        map=[
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1],
        ],
        door_left=[
            [0],
            [0],
            [0],
            [0],
            [1],
            [0],
            [1],
            [0],
            [0],
            [1],
        ],
        door_right=[
            [1],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [1],
        ]
    ),
    Room(
        name='Red Brinstar Fireflea Room',
        map=[
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0],
        ],
        door_left=[
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        door_right=[
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
    ),
    Room(
        name='X-Ray Scope Room',
        map=[[1, 1]],
        door_right=[[0, 1]],
    ),
    Room(
        name='Bat Room',
        map=[[1, 1]],
        door_left=[[1, 0]],
        door_right=[[0, 1]],
    ),
    Room(
        name='Below Spazer',
        map=[
            [1, 1],
            [1, 1],
        ],
        door_left=[
            [0, 0],
            [1, 0],
        ],
        door_right=[
            [0, 1],
            [0, 1],
        ],
    ),
    Room(
        name='Spazer Room',
        map=[[1]],
        door_left=[[1]],
    ),
    Room(
        name='Hellway',
        map=[[1, 1, 1]],
        door_left=[[1, 0, 0]],
        door_right=[[0, 0, 1]],
    ),
    Room(
        name='Red Tower Elevator Room',
        map=[
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ],
        door_left=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
        ],
        door_right=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        door_up=[
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
    ),
    Room(
        name='Alpha Power Bomb Room',
        map=[[1, 1, 1]],
        door_right=[[0, 0, 1]],
    ),
    Room(
        name='Beta Power Bomb Room',
        map=[
            [1, 1],
            [1, 0],
        ],
        door_right=[
            [0, 1],
            [0, 0],
        ]
    ),
]


for room in rooms:
    room.area = Area.BRINSTAR
