# Block-Design

Models the block design test.

Run python [main.py](https://github.com/v-y-l/Block-Design/blob/main/src/main.py) to get started.

![Demo gif](https://github.com/v-y-l/Block-Design/blob/main/assets/demo.gif)

## Block symbolic model

[block.py](https://docs.google.com/document/d/1gwEpj-OWHED0i5rjxqZPLjMwJhysZOsv8D_8StMi4UE/edit?usp=sharing)

Represents block in sprawled-out 2D form

                        [   BlackTopRightCornerSquare (1)  ]
    [ WhiteSquare (2) ] [          WhiteSquare (3)         ] [ BlackSquare (4) ] [ BlackSquare (5) ]
                        [ BlackBottomRightCornerSquare (6) ]

* Traverse to neighboring faces by specifying the number
* Rotations rotate the entire 2D block

## Puzzle model

[puzzle_solver.py](https://github.com/v-y-l/Block-Design/blob/main/src/puzzle_solver.py)

Takes in a puzzle and search strategies to solve a block design test

### Search strategies

[search.py](https://github.com/v-y-l/Block-Design/blob/main/src/search.py)

* Face search functions look for some face in a block
* Puzzle piece search functions look for the next puzzle piece to solve for


## Puzzle image

[puzzle_image.py](https://github.com/v-y-l/Block-Design/blob/main/src/puzzle_image.py) 

Converts an image to a puzzle model by sampling from four points per block

![Sampled points](https://github.com/v-y-l/Block-Design/blob/main/assets/puzzle_image_marks.png)
