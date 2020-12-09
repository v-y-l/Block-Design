from cv2 import imread, cvtColor, COLOR_BGR2RGB
from PIL import Image
from utils.constants import BLOCK_LENGTH, EDGE_OFFSET, PUZZLE_OPTIONS
from utils.enums import BlockPattern, SearchType, BlockAction, PuzzleAction
from utils.helper import get_pattern
from search import random_search, sequential_search
from block_image import BlockImage
import numpy as np
import csv

class PuzzleImageSolver:

    def __init__(self,
                 name = 'puzzle_a',
                 config = {
                     'solvers': {
                         SearchType.Face: random_search,
                         SearchType.PuzzlePiece: sequential_search
                     },
                     # Value from 0 to 1, represents % of memory
                     # loss on the puzzle each turn
                     'puzzle_memory_loss_factor': 0
                 }
    ):
        self.name = name
        self.solvers = config["solvers"]
        self.puzzle_memory_loss_factor = config["puzzle_memory_loss_factor"]
        self._setup_puzzle()

    def _setup_puzzle(self):
        self.image_path = PUZZLE_OPTIONS[self.name]
        self.image = imread(self.image_path)
        self.height, self.width, _ = self.image.shape
        self.unsolved_pieces = [] # Represents as top left coordinate
        for r in range(0, self.height - EDGE_OFFSET, BLOCK_LENGTH):
            for c in range(0, self.width - EDGE_OFFSET, BLOCK_LENGTH):
                self.unsolved_pieces.append((r, c))
        self.block_bank = [
            BlockImage(1, i+1, self) for i in
            range(len(self.unsolved_pieces))]
        self.action_history = []
    
    def add_to_history(self, row):
        self.action_history.append(row)

    ''' Returns the puzzle piece in symbolic form given some r, c. '''
    def get_pattern(self, r, c):
        return get_pattern(r, c, self.image)

    ''' Returns a numpy array with shape of height x width x bgr pixels. '''
    def get_image(self):
        return self.image

    ''' Use this function for testing purposes to see if the full puzzle is correctly parsed. '''
    def get_puzzle(self):
        return [self.get_pattern(r, c) for (r, c) in self.unsolved_pieces]

    ''' Opens the puzzle as an image. '''
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
        self.add_to_history(self.to_csv_row(PuzzleAction.LookAtPuzzle))
        self.image = imread(self.image_path)
        self.problem = self.get_puzzle()

    ''' Returns a list of actions executed by each block to solve the problem. '''
    def solve(self):
        face_searcher = self.solvers[SearchType.Face]
        puzzle_piece_searcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actions_per_block = []

        while self.unsolved_pieces:
            block = self.block_bank.pop()
            self.add_to_history(block.to_csv_row(BlockAction.PickUpFromBank))
            unsolved_piece = sequential_search(self)
            search_face_actions = face_searcher(
                block,
                unsolved_piece,
                actions_per_block)
            if (len(search_face_actions) == 0):
                self.remember()
                search_face_actions = face_searcher(
                    block,
                    self.problem[i],
                    actions_per_block)
            self.add_to_history(block.to_csv_row(BlockAction.PlaceInPuzzle))
            self.forget(self.puzzle_memory_loss_factor)
        return actions_per_block

    def to_csv_row(self, action):
        return str(self) + ",action," + action.name

    def print_history(self, csv_path=''):
        csv_writer = None
        if csv_path != '':
            file = open(csv_path, 'w')
            csv_writer = csv.writer(file,
                                    delimiter=' ',
                                    quoting=csv.QUOTE_NONE)

        for i, action in enumerate(self.action_history):
            row = "{},{}".format(i+1, action)
            if csv_writer:
                csv_writer.writerow([row])
            else:
                print(row)

        if csv_writer:
            print("Solution written to {}".format(csv_path))
            file.close()

    def __str__(self):
        return 'Puzzle,{}'.format(self.name)
