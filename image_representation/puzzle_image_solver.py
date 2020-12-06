from cv2 import imread, cvtColor, COLOR_BGR2RGB
from PIL import Image
from utils.enums import BlockPattern, SearchType, BlockAction, PuzzleAction
from utils.helper import get_pattern, block_length, edge_offset
from search import random_search, sequential_search
from block_image import BlockImage
import numpy as np

class PuzzleImageSolver:

    def __init__(self,
                 image_path='./puzzle_images/puzzle_a.png',
                 solvers={
                     SearchType.Face: random_search,
                     SearchType.PuzzlePiece: sequential_search
                 },
                 config={
                     # Value from 0 to 1, represents % of memory
                     # loss on the puzzle each turn
                     'puzzle_memory_loss_factor': 0
                 }
    ):
        self.image_path = image_path
        self.image = imread(image_path)
        self.height, self.width, _ = self.image.shape
    
        self.solvers = solvers
        self.config = config
        self.problem = self.get_puzzle()
        self.block_bank = [BlockImage(1, i+1) for i in range(len(self.problem))]
        self.action_counter = {
            BlockAction.GoToFaceOne: 0,
            BlockAction.GoToFaceTwo: 0,
            BlockAction.GoToFaceThree: 0,
            BlockAction.GoToFaceFour: 0,
            BlockAction.GoToFaceFive: 0,
            BlockAction.GoToFaceSix: 0,
            BlockAction.RotateLeft: 0,
            BlockAction.RotateRight: 0,
            BlockAction.PickUpBlock: 0,
            BlockAction.PlaceInPuzzle: 0,
            PuzzleAction.LookAtPuzzle: 0,
        }

    ''' Returns the puzzle piece in image form given some r, c. '''
    def get_window(self, r, c):
        row_offset = get_row_offset(r, c, 1)
        col_offset = get_col_offset(r, c, 1)
        return self.image[self.r:row_offset][self.c:col_offset]

    ''' _returns the puzzle piece in symbolic form given some r, c. '''
    def get_pattern(self, r, c):
        return get_pattern(r, c, self.image)

    ''' _return the image puzzle in symbolic form. '''
    def get_puzzle(self):
        puzzle = []
        for r in range(0, self.height - edge_offset, block_length):
            for c in range(0, self.width - edge_offset, block_length):
                puzzle.append(self.get_pattern(r, c))
        self.r = 0
        self.c = 0
        return puzzle

    ''' _returns a numpy array with shape of height x width x bgr pixels. '''
    def get_image(self):
        return self.image

    ''' _opens the puzzle as an image. '''
    def show_image(self):
        Image.fromarray(cvtColor(self.image, COLOR_BGR2RGB), 'RGB').show()

    ''' Sets a memory_loss_factor amount of the image to black to simulate forgetfulness. '''
    def forget(self, memory_loss_factor):
        if (memory_loss_factor) == 0: return
        height, width, bgr_len = self.image.shape
        total_pixels = height * width
        total_pixels_to_forget = int(total_pixels * memory_loss_factor)
        tmp_image = self.image.reshape(total_pixels, bgr_len)
        mask = np.ones((total_pixels, bgr_len), np.uint8)
        mask[:total_pixels_to_forget] = [0, 0, 0]
        np.random.shuffle(mask)
        tmp_image *= mask
        self.image = tmp_image.reshape(height, width, bgr_len)
        self.problem = self.get_puzzle()

    ''' Take a look at the puzzle to refresh our memory of it. '''
    def remember(self):
        self.image = imread(self.image_path)
        self.problem = self.get_puzzle()

    ''' Returns a list of actions executed by each block to solve the problem. '''
    def solve(self):
        face_searcher = self.solvers[SearchType.Face]
        puzzle_piece_searcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actions_per_block = []
        puzzle_piece_indices = puzzle_piece_searcher(self.problem)
        for i in puzzle_piece_indices:
            block = self.block_bank[i]
            search_face_actions = face_searcher(
                block,
                self.problem[i],
                actions_per_block)
            if (len(search_face_actions) == 0):
                self.action_counter[PuzzleAction.LookAtPuzzle] += 1
                self.remember()
                search_face_actions = face_searcher(
                    block,
                    self.problem[i],
                    actions_per_block)
            self.forget(self.config["puzzle_memory_loss_factor"])
            self.add_block_to_stats(block)
            self.print_solved_puzzle_piece(i)
        self.print_puzzle_stats()
        return actions_per_block

    ''' _calculates the total and individual number of executed moves. '''
    def add_block_to_stats(self, block):
        for action, count in block.get_action_counter().items():
            self.action_counter[action] += count
        self.action_counter[BlockAction.PickUpBlock] += 1
        self.action_counter[BlockAction.PlaceInPuzzle] += 1

    def print_solved_puzzle_piece(self, piece_number):
        print("...[_solved puzzle piece {}] {}\n".format(
            piece_number + 1,
            str(self.block_bank[piece_number])))

    def get_action_counter(self):
        return self.action_counter

    def print_puzzle_stats(self):
        print('========================')
        print('| Puzzle statistics... |')
        print('========================')
        total_action_count = 0
        for action, count in self.get_action_counter().items():
            print(action, ": ", count)
            total_action_count += count
        print("Total actions taken: {}".format(total_action_count))

puzzle_options = {
    'a': './puzzle_images/puzzle_a.png',
    'b': './puzzle_images/puzzle_b.png',
    'c': './puzzle_images/puzzle_c.png',
}
