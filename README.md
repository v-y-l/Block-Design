# Block-Design

An image model for the block design test.

Run python [main.py](https://github.com/v-y-l/Block-Design/blob/main/src/main.py) to get started.

Example:

> python main.py --puzzle puzzle_b --face_search beeline_search --piece_search sequential_search
> --puzzle_memory_loss .5 --puzzle_memory_loss_counter_limit 5 --csv stats.csv

...solves puzzle_b.png using the beeline face search and sequential puzzle piece search, with a memory loss of 50% of the puzzle every 5 puzzle pieces solved, and dump the solution list to stats.csv.

![Demo gif](https://github.com/v-y-l/Block-Design/blob/main/assets/cli_demo.gif)

### Parameters

#### --puzzle
The name of the puzzle image to solve

#### --face_search
The search algorithm to find the destination pattern on a block

#### --piece_search
The search algorithm that returns the next piece of the puzzle to solve

#### --puzzle_memory_loss
The rate of memory loss (0-100% of entire puzzle)

#### --puzzle_memory_loss_counter_limit
Memory loss kicks every time this limit of puzzle pieces is solved (resets every time the limit is achieved)

#### --csv
Dumps the full list of solution actions to the specified file

## Block image model

[block_image.py](https://github.com/v-y-l/Block-Design/blob/main/src/block_image.py)

Represents block in sprawled-out 2D form using the underlying image:

![2D block](https://github.com/v-y-l/Block-Design/blob/main/assets/labeled_block.png)

* Traverse to neighboring faces by specifying the number
* Rotations rotate the entire 2D block

### Block actions

See [enums.py](https://github.com/v-y-l/Block-Design/blob/main/src/utils/enums.py#L25)

### Forgetfulness

Forgetfulness is modeled as blotted out pixels

![50% forgetfulness](https://github.com/v-y-l/Block-Design/blob/main/assets/50_percent_forgotten_puzzle.png)

## Puzzle model

[puzzle_image_solver.py](https://github.com/v-y-l/Block-Design/blob/main/src/puzzle_image_solver.py)

* Takes in a puzzle and search strategies to solve a block design test
* Converts the image to a puzzle model by sampling from four points per block

### Search strategies

[search.py](https://github.com/v-y-l/Block-Design/blob/main/src/search.py)

* Face search functions look for some face in a block
* Puzzle piece search functions look for the next puzzle piece to solve for

![Sampled points](https://github.com/v-y-l/Block-Design/blob/main/assets/puzzle_image_marks.png)

## Testing

Test all modules
> python -m unittest test

Test an individual module
> python -m unittest test/test_search.py
