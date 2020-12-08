from cv2 import imread, cvtColor, COLOR_BGR2RGB
from PIL import Image
from utils.enums import BlockAction, BlockPattern, BlockOrientation
from utils.data_structures import Node, FaceNode
from utils.block_actions import go_to_face, rotate_right, rotate_left
from utils.helper import is_triangle_pattern, face_to_coordinate, get_pattern

'''
A block has six faces. Each face is assigned a number.
We represent things two dimensionally by sprawling out the faces.
This simplifies tracking rotation state, as we can apply rotations
across the entire 2D image.

                        [   BlackTopRightCornerSquare (1)  ]
    [ WhiteSquare (2) ] [          WhiteSquare (3)         ] [ BlackSquare (4) ] [ BlackSquare (5) ]
                        [ BlackBottomRightCornerSquare (6) ]
'''
class BlockImage:

    def __init__(self, face=1, number=1):
        self.face = face
        self.number = number
        self.orientation = BlockOrientation.Up
        self.image = imread('./block_images/block_up.png')
        self.face_to_coordinate = face_to_coordinate
        self.r, self.c = face_to_coordinate[self.orientation][face]
        
        self._setup_block_data_structures()
        self._setup_rotation_data_structures()
        self._setup_go_to_data_structures()

    '''
    Setup the data structures that coordinate between the different
    block concepts.
    '''
    def _setup_block_data_structures(self):
        self.actions = {
            BlockAction.GoToFaceOne: lambda: go_to_face(self, 1),
            BlockAction.GoToFaceTwo: lambda: go_to_face(self, 2),
            BlockAction.GoToFaceThree: lambda: go_to_face(self, 3),
            BlockAction.GoToFaceFour: lambda: go_to_face(self, 4),
            BlockAction.GoToFaceFive: lambda: go_to_face(self, 5),
            BlockAction.GoToFaceSix: lambda: go_to_face(self, 6),
            BlockAction.RotateLeft: lambda: rotate_left(self),
            BlockAction.RotateRight: lambda: rotate_right(self)
        }

        self.go_to_face_action = {
            1: BlockAction.GoToFaceOne,
            2: BlockAction.GoToFaceTwo,
            3: BlockAction.GoToFaceThree,
            4: BlockAction.GoToFaceFour,
            5: BlockAction.GoToFaceFive,
            6: BlockAction.GoToFaceSix
        }

        self.action_to_face = {
            BlockAction.GoToFaceOne: 1,
            BlockAction.GoToFaceTwo: 2,
            BlockAction.GoToFaceThree: 3,
            BlockAction.GoToFaceFour: 4,
            BlockAction.GoToFaceFive: 5,
            BlockAction.GoToFaceSix: 6
        }

        self.action_counter = {
            BlockAction.GoToFaceOne: 0,
            BlockAction.GoToFaceTwo: 0,
            BlockAction.GoToFaceThree: 0,
            BlockAction.GoToFaceFour: 0,
            BlockAction.GoToFaceFive: 0,
            BlockAction.GoToFaceSix: 0,
            BlockAction.RotateLeft: 0,
            BlockAction.RotateRight: 0
        }
        
    ''' Sets up data structures for enabling rotation logic. '''
    def _setup_rotation_data_structures(self):
        ''' For rotating the block as whole. '''
        up = Node(BlockOrientation.Up)
        right = Node(BlockOrientation.Right)
        down = Node(BlockOrientation.Down)
        left = Node(BlockOrientation.Left)

        up.next = right
        up.prev = left
        right.next = down
        right.prev = up
        down.next = left
        down.prev = right
        left.next = up
        left.prev = down

        self.block_orientations = {
            BlockOrientation.Up: up,
            BlockOrientation.Right: right,
            BlockOrientation.Down: down,
            BlockOrientation.Left: left,
        }

        ''' For the peek operation. '''
        black_top_right_corner_square = Node(BlockPattern.BlackTopRightCornerSquare)
        black_bottom_right_corner_square = Node(BlockPattern.BlackBottomRightCornerSquare)
        black_bottom_left_corner_square = Node(BlockPattern.BlackBottomLeftCornerSquare)
        black_top_left_corner_square = Node(BlockPattern.BlackTopLeftCornerSquare)
        white_square = Node(BlockPattern.WhiteSquare)
        black_square = Node(BlockPattern.BlackSquare)

        white_square.next = white_square
        white_square.prev = white_square
        black_square.next = black_square
        black_square.prev = black_square
        black_top_right_corner_square.next = black_bottom_right_corner_square
        black_top_right_corner_square.prev = black_top_left_corner_square
        black_bottom_right_corner_square.next = black_bottom_left_corner_square
        black_bottom_right_corner_square.prev = black_top_right_corner_square
        black_bottom_left_corner_square.next = black_top_left_corner_square
        black_bottom_left_corner_square.prev = black_bottom_right_corner_square
        black_top_left_corner_square.next = black_top_right_corner_square
        black_top_left_corner_square.prev = black_bottom_left_corner_square

        self.face_orientations = {
            BlockPattern.BlackTopRightCornerSquare: black_top_right_corner_square,
            BlockPattern.BlackBottomRightCornerSquare: black_bottom_right_corner_square,
            BlockPattern.BlackBottomLeftCornerSquare: black_bottom_left_corner_square,
            BlockPattern.BlackTopLeftCornerSquare: black_top_left_corner_square,
            BlockPattern.BlackSquare: black_square,
            BlockPattern.WhiteSquare: white_square,
        }

    ''' Setup data structures that enable movement to a neighboring face. '''
    def _setup_go_to_data_structures(self):
        face_one = FaceNode(1)
        face_two = FaceNode(2)
        face_three = FaceNode(3)
        face_four = FaceNode(4)
        face_five = FaceNode(5)
        face_six = FaceNode(6)

        face_one.neighbors = {5, 4, 3, 2}
        face_two.neighbors = {1, 3, 6, 5}
        face_three.neighbors = {1, 4, 6, 2}
        face_four.neighbors = {1, 5, 6, 3}
        face_five.neighbors = {1, 2, 6, 4}
        face_six.neighbors = {3, 4, 5, 2}

        self.faces = {
            1: face_one,
            2: face_two,
            3: face_three,
            4: face_four,
            5: face_five,
            6: face_six,
        }

    def peek_action(self, action):
        if action not in self.get_valid_actions():
            raise Exception("Invalid action {} for {}".format(action, str(self)))
        if action == BlockAction.RotateLeft:
            return self.face_orientations[self.get_pattern()].prev.val
        elif action == BlockAction.RotateRight:
            return self.face_orientations[self.get_pattern()].next.val
        else:
            peek_face = self.action_to_face[action]
            peek_r, peek_c = self.face_to_coordinate[self.orientation][peek_face]
            return get_pattern(peek_r, peek_c, self.image)

    def execute_action(self, action):
        self.action_counter[action] += 1
        self.actions[action]()

    def get_action_counter(self):
        return self.action_counter

    def get_face(self):
        return self.face

    def get_go_to_actions(self):
        return [self.go_to_face_action[face] for face in self.get_neighbors()]

    def get_neighbors(self):
        return self.faces[self.face].neighbors

    def get_number(self):
        return self.number

    def get_pattern(self):
        return get_pattern(self.r, self.c, self.image)

    def get_rotate_actions(self):
        return [BlockAction.RotateLeft, BlockAction.RotateRight]

    def get_valid_actions(self):
        return self.get_rotate_actions() + self.get_go_to_actions()

    def has_triangle_pattern(self):
        return is_triangle_pattern(self.get_pattern())

    def show_image(self):
        Image.fromarray(cvtColor(self.image, COLOR_BGR2RGB), 'RGB').show()

    def __str__(self):
        return 'Block {}: face {}, pattern {}'.format(
            self.get_number(), self.get_face(), self.get_pattern())
