from PIL import Image, ImageDraw
import random # for generating random numbers
from pathlib import Path 
import json 
import sys

this_dir = Path(__file__).parent
sys.path.append( str(this_dir) )
from colorpalette import ColorPalette

#TODO turn this into a rasterizer
'''
color choices will be grabbed from the underlying image via a k-means clustering algorithm
'''

# TODO use rabatment of the rectangle to split into rectangle and square 
# TODO split square into 3 congruent rectangles
# TODO split rectangle backwards into fibonacci squares  

'''
Choices if current object is square: 
* check size to see if we should stop recursion
* split canvas into 4 rectangles 
* choose one of the three methods to split canvas into 3 similar rectangles

Choices if current object is rectangle:
* check width and height to see if we should stop recursion
* use rabatment of the rectangle to split into rectangle and square 

'''

greenBlueOcean = ['#064E40', '#0DAD8D', '#8DD8CC', '#30BFBF', '#0C98BA', '#1164B4']
# color_palette = greenBlueOcean

limit_counter = 0

def load_color_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

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
            RecursiveRectangle( self.draw, 0, 0, 0, self.x_split, self.y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, 0, self.x_split, 0, self.width, self.y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, 0, 0, self.y_split, self.x_split, self.height, self.chanceToRecurse )
            RecursiveRectangle( self.draw, 0, self.x_split, self.y_split, self.width, self.height, self.chanceToRecurse )

    def get_quadrant_splitter(self, x1: int, y1: int, x2: int, y2: int):
        x = random.triangular(x1, x2)
        y = random.triangular(y1, y2)
        return (x, y)

    def get_image(self):
        return self.image


class RecursiveRectangle(AbstractRectangleCanvas):
    def __init__(self, draw:ImageDraw.Draw, order:int, x1: int, y1:int, x2:int, y2:int, chanceToRecurse: float):
        self.draw = draw
        self.order = order+1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.chanceToRecurse = chanceToRecurse
        self.tryRecurse()

    def tryRecurse(self):
        if self.order > 4: #TODO this is dum and should be removed
            self.draw_rectangle()
        elif random.random() < self.chanceToRecurse:
            if (self.width < 50) or (self.height < 50):
                self.draw_rectangle() #TODO test if this is meme tier or not
                global limit_counter
                limit_counter += 1 #TODO for some reason limit counter is very high 
                                   # I think inheriting from AbstractRectangleCanvas is causing this? 
                self.chanceToRecurse = 1.0
            else:
                self.chanceToRecurse /= 2
                self.recurse()
        else:
            self.draw_rectangle()

    def recurse(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        x_split, y_split = self.get_quadrant_splitter(x1, y1, x2, y2)
        for i in range(4): 
            RecursiveRectangle( self.draw, self.order, x1, y1, x_split, y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, self.order, x_split, y1, x2, y_split, self.chanceToRecurse )
            RecursiveRectangle( self.draw, self.order, x1, y_split, x_split, y2, self.chanceToRecurse )
            RecursiveRectangle( self.draw, self.order, x_split, y_split, x2, y2, self.chanceToRecurse )

    def draw_rectangle(self):
        color = get_random_color()
        self.draw.rectangle((self.x1, self.y1, self.x2, self.y2), fill=color, outline=(0, 0, 0), width=5)

### Hacks for testing ### 

def get_random_color(): 
    #TODO this is a hack and should be removed
    global color_palette
    # color_choice = random.choice(color_palette)

    color_choice = color_palette.random_color_hex()
    return color_choice 


def similar_rectangle_from_square(x1:int, y1:int, x2:int, y2:int):
    #TODO implement the two other similar rectangle functions
    # See: https://en.wikipedia.org/wiki/Plastic_number
    choose_method = random.randint(0,2)
    if choose_method == 0:
        return similar_rectangle_from_square_1(x1, y1, x2, y2)

def similar_rectangle_from_square_1(x1:int, y1:int, x2:int, y2:int):
    # produces coordinates for 3 congruent rectangles from a square
    width = x2 - x1
    height = y2 - y1
    choose_method = random.randint(0,1)
    if choose_method == 0:
        rectangles = []
        rectangles.append( (x1, y1, width//3, y2) )
        rectangles.append( (x1+width//3, y1, x1+(2*width//3),y2) )
        rectangles.append( (x1+(2*width//3), y1, x2,y2) )
    else:
        rectangles = []
        rectangles.append( (x1, y1, x2, height//3) )
        rectangles.append( (x1, y1+height//3, x2, y1+(2*height//3)) )
        rectangles.append( (x1, y1+(2*height//3), x2, y2) )
    return rectangles



### MAIN ###

#TODO could make an automated coloring book generator

def main():
    save_directory = Path('.') / 'Python' / 'abstract_recursive_quadrants' / 'output'
    save_directory.mkdir(parents=True, exist_ok=True)
    # print(save_directory.absolute())
    seed = random.randint(0, 1000000)
    image_width = 1000
    image_height = 1000
    canvas_color = (255, 255, 255)
    ar = AbstractRectangleCanvas(image_width, image_height, canvas_color)
    image = ar.get_image()
    print(limit_counter)
    image.save(save_directory / f'seed_{seed}.png')
    image.show()

    # for i in range(1, 10):
    #     random.seed(i)
    #     image_width = 1000
    #     image_height = 1000
    #     canvas_color = (255, 255, 255)
    #     ar = AbstractRectangleCanvas(image_width, image_height, canvas_color)
        
    #     image = ar.get_image()

    #     image.save(save_directory / f'seed_{i}.png')



if __name__ == '__main__':
    color_palette_directory = Path('.') / 'Resources' / 'color_palettes'
    # color_path = color_palette_directory / 'FlatUI.json'
    # color_path = color_palette_directory / '817f82-ae8ca3-a2abb5-95d9da-6dd6da.json'
    color_path = color_palette_directory / '264653-2a9d8f-e9c46a-f4a261-e76f51.json'

    color_palette = ColorPalette(color_path)

    # print(color_palette)
    main()