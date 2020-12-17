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
                     'puzzle_memory_loss_factor': 0.0,
                     # Number of puzzle pieces solved before memory loss
                     # e.g. if = 4, then memory loss happens on 4th piece
                     'puzzle_memory_loss_counter_limit': 0,
                     # Value from 0 to 1, represents % of memory recovered
                     # from the puzzle
                     'glance_factor': 1.0,
                 }
    ):
        self.name = name or 'puzzle_a'
        self.solvers = config.get("solvers", {
            SearchType.Face: random_search,
            SearchType.PuzzlePiece: sequential_search
        })
        self.puzzle_memory_loss_factor = config.get("puzzle_memory_loss_factor", 0.0)
        self.puzzle_memory_loss_counter_limit = config.get(
            "puzzle_memory_loss_counter_limit", 0)
        self.glance_factor = config.get("glance_factor", 1.0)
        self.action_counter = {}
        self._setup_puzzle()

    def _setup_puzzle(self):
        self.block = None
        self.image_path = PUZZLE_OPTIONS[self.name]
        self.action_history = []
        self.num_rows, self.num_cols, self.bgr_len = (
            imread(self.image_path).shape)

        # Glance factor presumes that the puzzle is a square
        min_glance_factor = float(BLOCK_LENGTH - 10) / self.num_cols
        if not self.glance_factor >= min_glance_factor:
            raise Exception(
                "Specified glance factor {} must be at least {} to cover one square".format(
                    self.glance_factor, min_glance_factor))

        # Start with a blank slate
        self.image = np.zeros((self.num_rows,
                               self.num_cols,
                               self.bgr_len),
                              np.uint8)
        self.look_at_puzzle((0,0), self.glance_factor)

        self.unsolved_pieces = [] # Represents as top left coordinate
        for r in range(0, self.num_rows - EDGE_OFFSET, BLOCK_LENGTH):
            for c in range(0, self.num_cols - EDGE_OFFSET, BLOCK_LENGTH):
                self.unsolved_pieces.append((r, c))

        self.block_bank = [
            BlockImage(1, i+1, self) for i in
            range(len(self.unsolved_pieces))]

        self.solved_pieces = {piece:None for piece in self.unsolved_pieces}
        self.puzzle_memory_loss_counter = 0

    ''' Adds to the history of executed actions on each block. '''
    def add_to_history(self, row, action):
        self.increment_action(action)
        self.action_history.append(row)

    ''' Simulates picking up a block '''
    def pick_up_next_block(self):
        if not self.block_bank:
            raise Exception("No more blocks in block bank")
        if not self.block or self.block.is_solved:
            self.block = self.block_bank.pop()
            self.add_to_history(self.block.to_csv_row(BlockAction.PickUpFromBank),
                                BlockAction.PickUpFromBank)

    ''' Returns the puzzle piece in symbolic form given some r, c. '''
    def get_pattern(self, r, c):
        return get_pattern(r, c, self.image)

    ''' Returns a numpy array with shape of num_rows x num_cols x bgr pixels. '''
    def get_image(self):
        return self.image

    ''' For testing purposes to check if full puzzle is correctly parsed. '''
    def get_puzzle(self):
        return [self.get_pattern(r, c) for (r, c) in self.unsolved_pieces]

    ''' Get the patterns of pieces solved so far. '''
    def get_solved_pieces_patterns(self):
        solved_pieces_patterns = []
        for pieces in sorted(self.solved_pieces):
            block = self.solved_pieces[pieces]
            solved_pieces_patterns.append(block.get_pattern())
        return solved_pieces_patterns

    ''' Opens the puzzle as an image. '''
    def show_image(self, image=[]):
        if len(image) == 0: image = self.image
        Image.fromarray(cvtColor(image, COLOR_BGR2RGB), 'RGB').show()

    ''' Sets a memory_loss_factor % of image to black to simulate forgetfulness. '''
    def forget_puzzle(self):
        if (self.puzzle_memory_loss_factor) == 0: return
        num_rows, num_cols, bgr_len = self.image.shape
        total_pixels = num_rows * num_cols
        total_pixels_to_forget = int(
            total_pixels * self.puzzle_memory_loss_factor)
        tmp_image = self.image.reshape(total_pixels, bgr_len)
        mask = np.ones((total_pixels, bgr_len), np.uint8)
        mask[:total_pixels_to_forget] = [0, 0, 0]
        np.random.shuffle(mask) # Expensive
        tmp_image *= mask
        self.image = tmp_image.reshape(num_rows, num_cols, bgr_len)

    ''' Increment the action counter by an action. '''
    def increment_action(self, action):
        self.action_counter[action] = self.action_counter.get(action, 0) + 1

    ''' Increment the turn counter in turns of forgetfulness. '''
    def increment_memory_loss_counter(self):
        if self.puzzle_memory_loss_counter_limit > 0:
            self.puzzle_memory_loss_counter = (
                (self.puzzle_memory_loss_counter + 1)
                % self.puzzle_memory_loss_counter_limit
            )

    ''' Take a look at the puzzle to refresh our memory of it. '''
    def look_at_puzzle(self, point, factor):
        row, col = point
        self.add_to_history(
            self.to_csv_row(PuzzleAction.LookAtPuzzle, (row, col)),
            PuzzleAction.LookAtPuzzle)
        remembered_puzzle_pieces = (
            imread(self.image_path)[row:row + int(self.num_rows * factor),
                                    col:col + int(self.num_cols * factor)])
        self.image[row:row + int(self.num_rows * factor)
                   ,col:col + int(self.num_cols * factor)] = (
            remembered_puzzle_pieces)

    ''' If the solver is forgetting some of the puzzle on this turn '''
    def should_forget(self):
        return (self.puzzle_memory_loss_counter
                == self.puzzle_memory_loss_counter_limit - 1)

    ''' Returns a list of actions executed by each block to solve the problem. '''
    def solve(self):
        face_searcher = self.solvers[SearchType.Face]
        puzzle_piece_searcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actions_per_block = []

        while self.unsolved_pieces:
            self.pick_up_next_block()
            if self.should_forget():
                self.forget_puzzle()
            self.increment_memory_loss_counter()

            unsolved_piece_pattern, unsolved_piece = puzzle_piece_searcher(self)
            if unsolved_piece_pattern == BlockPattern.Unknown:
                continue
            search_face_actions = face_searcher(
                self.block,
                unsolved_piece_pattern,
                actions_per_block)
            self.block.is_solved = True
            self.unsolved_pieces.remove(unsolved_piece)
            self.solved_pieces[unsolved_piece] = self.block
        return actions_per_block

    ''' Prints a puzzle action in csv readable form. '''
    def to_csv_row(self, action, point):
        return str(self) + ",action," + action.name + ",point," + str(point)

    ''' Prints out all executed actions. '''
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
