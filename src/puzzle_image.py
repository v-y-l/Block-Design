from cv2 import imread, IMREAD_COLOR

class PuzzleImage:

    def __init__(self, image_path='./puzzle_images/puzzle_a.png'):
        self.image = imread(image_path)

    def getImage(self):
        print('image' + str(self.image))
        return self.image

if __name__ == '__main__':
    p = PuzzleImage()
    i = p.getImage()
