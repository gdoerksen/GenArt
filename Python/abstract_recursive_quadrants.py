from PIL import Image, ImageDraw
import random # for generating random numbers


class AbstractRectangleCanvas:
    def __init__(self, image_width: int, image_height: int, background_color: tuple = (0, 0, 0)):
        self.width = image_width
        self.height = image_height
        self.color = background_color
        self.image = Image.new('RGBA', (image_width, image_height), background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.offset = 10
        self.chanceToRecurse = 0.5

        self.x_split, self.y_split = self.get_quadrant_splitter(0, 0, image_width, image_height)
        for i in range(4): 
            RecursiveRectangle( self.draw, 0, 0, self.x_split, self.y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, self.x_split, 0, self.width, self.y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, 0, self.y_split, self.x_split, self.height, self.chanceToRecurse )
            RecursiveRectangle( self.draw, self.x_split, self.y_split, self.width, self.height, self.chanceToRecurse )

    def get_quadrant_splitter(self, x1: int, y1: int, x2: int, y2: int):
        x = random.triangular(x1, x2)
        y = random.triangular(y1, y2)
        return (x, y)

    def get_image(self):
        return self.image


class RecursiveRectangle:
    def __init__(self, draw:ImageDraw.Draw, x1: int, y1:int, x2:int, y2:int, chanceToRecurse: float):
        self.draw = draw
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.chanceToRecurse = chanceToRecurse
        self.tryRecurse()

    def tryRecurse(self):
        if random.random() < self.chanceToRecurse:
            self.chanceToRecurse /= 2
            self.recurse()
        else:
            self.draw_rectangle()

    def recurse(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        x_split, y_split = self.get_quadrant_splitter(x1, y1, x2, y2)
        for i in range(4): 
            RecursiveRectangle( self.draw, x1, y1, x_split, y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, x_split, y1, x2, y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, x1, y_split, x_split, y2, self.chanceToRecurse )
            RecursiveRectangle( self.draw, x_split, y_split, x2, y2, self.chanceToRecurse )

    def get_quadrant_splitter(self, x1: int, y1: int, x2: int, y2: int):
        x = random.triangular(x1, x2)
        y = random.triangular(y1, y2)
        return (x, y)

    def draw_rectangle(self):
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.draw.rectangle((self.x1, self.y1, self.x2, self.y2), fill=color)


def main():
    image_width = 500
    image_height = 500
    canvas_color = (255, 255, 255)
    ar = AbstractRectangleCanvas(image_width, image_height, canvas_color)
    
    image = ar.get_image()
    image.show()

    # image.save('square.png')

if __name__ == '__main__':
    main()