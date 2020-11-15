from cv2 import imread

class PuzzleImage:

    def __init__(self, image_path='./puzzle_images/puzzle_a.png'):
        self.image = imread(image_path)

    def getImage(self):
        return self.image
