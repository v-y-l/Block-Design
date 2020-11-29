# Block-Design

A symbolic model for the block design test.

Run python [main.py](https://github.com/v-y-l/Block-Design/blob/main/image_representation/main.py) to get started.

Example:

> python main.py -p b -f b -s s

...will solve puzzle_b.png using the beeline face search and sequential puzzle piece search.

![Demo gif](https://github.com/v-y-l/Block-Design/blob/main/assets/symbolic_rep_demo.gif)

## Block symbolic model

[block_image.py](https://github.com/v-y-l/Block-Design/blob/main/image_representation/block_image.py

Represents block in sprawled-out 2D form

![2D block](https://github.com/v-y-l/Block-Design/blob/main/image_representation/block_images/block_up.png)

* Traverse to neighboring faces by specifying the number
* Rotations rotate the entire 2D block

## Puzzle model

[puzzle_image_solver.py](https://github.com/v-y-l/Block-Design/blob/main/image_representation/puzzle_image_solver.py)

* Takes in a puzzle and search strategies to solve a block design test
* Converts the image to a puzzle model by sampling from four points per block

### Search strategies

[search.py](https://github.com/v-y-l/Block-Design/blob/main/image_representation/search.py)

* Face search functions look for some face in a block
* Puzzle piece search functions look for the next puzzle piece to solve for

![Sampled points](https://github.com/v-y-l/Block-Design/blob/main/assets/puzzle_image_marks.png)

## Testing

> python -m unittest test/test_something.py
