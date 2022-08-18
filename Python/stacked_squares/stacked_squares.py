from PIL import Image, ImageDraw
import random # for generating random numbers
from pathlib import Path 
import sys
from matplotlib.pyplot import sca

from pyparsing import java_style_comment

this_dir = Path(__file__).parent
sys.path.append( str(this_dir.parent) )
from colorpalette import ColorPalette




### Hacks for testing ### 

def get_random_color(): 
    #TODO this is a hack and should be removed
    global color_palette
    # color_choice = random.choice(color_palette)

    color_choice = color_palette.random_color_hex()
    return color_choice 

def draw_stacked_squares(draw: ImageDraw.Draw, image_width: int, image_height: int):
    squares_per_row = 10
    square_width = image_width // squares_per_row
    square_height = image_height // squares_per_row
    for i in range(squares_per_row):
        # x1 = square_width * i
        # x2 = square_width * (i+1)
        for j in range(10):
            x1 = square_width * i
            x2 = square_width * (i+1)
            y1 = square_height * j
            y2 = square_height * (j+1)

            stacked_squares = 5
            scaling_factor = 0.10
            for _ in range(stacked_squares):
                color = get_random_color()
                draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)

                x1 += square_width*scaling_factor 
                x2 -= square_width*scaling_factor
                y1 += square_height*scaling_factor
                y2 -= square_height*scaling_factor

def draw_wandering_stacked_squares(draw: ImageDraw.Draw, image_width: int, image_height: int):
    squares_per_row = 10
    square_width = image_width // squares_per_row
    square_height = image_height // squares_per_row
    for i in range(squares_per_row):
        for j in range(10):
            x1 = square_width * i
            x2 = square_width * (i+1)
            y1 = square_height * j
            y2 = square_height * (j+1)
            stacked_squares = 5
            scaling_factor = 0.25
            choice_x = random.triangular(0, 1, 0.5)
            choice_y = random.triangular(0, 1, 0.5)
            new_square_width = square_width
            new_square_height = square_height
            color = get_random_color()
            draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)
            for _ in range(stacked_squares-1):
                # x1 = random.randint(x1, x1+int(new_square_width*scaling_factor))
                # y1 = random.randint(y1, y1+int(new_square_height*scaling_factor))

                x1 = x1 + int(new_square_width*scaling_factor*choice_x)
                new_square_width = int(new_square_width - (new_square_width*scaling_factor))
                x2 = x1+new_square_width

                y1 = y1 + int(new_square_height*scaling_factor*choice_y)
                new_square_height = int(new_square_height - (new_square_height*scaling_factor))
                y2 = y1+new_square_height
                
                scaling_factor += 0.05

                color = get_random_color()
                draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)

def draw_scales(draw: ImageDraw.Draw, image_width: int, image_height: int):
    squares_per_row = 10
    square_width = image_width // squares_per_row
    square_height = image_height // squares_per_row
    for i in range(squares_per_row):
        for j in range(10):
            x1 = square_width * i
            x2 = square_width * (i+1)
            y1 = square_height * j
            y2 = square_height * (j+1)
            stacked_squares = 5
            scaling_factor = 0.25
            choice_x = (x1 + square_width//2) // image_width
            choice_y = (y1 + square_height//2) // image_height 
            new_square_width = square_width
            new_square_height = square_height
            color = get_random_color()
            draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)
            for _ in range(stacked_squares-1):
                # x1 = random.randint(x1, x1+int(new_square_width*scaling_factor))
                # y1 = random.randint(y1, y1+int(new_square_height*scaling_factor))

                x1 = x1 + int(new_square_width*scaling_factor*choice_x)
                new_square_width = int(new_square_width - (new_square_width*scaling_factor))
                x2 = x1+new_square_width

                y1 = y1 + int(new_square_height*scaling_factor*choice_y)
                new_square_height = int(new_square_height - (new_square_height*scaling_factor))
                y2 = y1+new_square_height
                
                scaling_factor += 0.05

                color = get_random_color()
                draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)

def draw_square_stacked_squares(draw: ImageDraw.Draw, image_width: int, image_height: int):
    '''
    * More colors is better 
    * Lighter colors is better

    '''
    #TODO the center square is not exactly in the center of the image
    squares_per_row = 11
    squares_per_column = 11
    square_width = image_width // squares_per_row
    square_height = image_height // squares_per_column
    for i in range(squares_per_row):
        for j in range(squares_per_column):
            x1 = square_width * i
            x2 = square_width * (i+1)
            y1 = square_height * j
            y2 = square_height * (j+1)
            stacked_squares = 5
            scaling_factor = 0.25
            choice_x = (x1 + square_width//2) / image_width
            choice_y = (y1 + square_height//2) / image_height 
            new_square_width = square_width
            new_square_height = square_height
            color = get_random_color()
            draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)
            for _ in range(stacked_squares-1):
                # x1 = random.randint(x1, x1+int(new_square_width*scaling_factor))
                # y1 = random.randint(y1, y1+int(new_square_height*scaling_factor))

                x1 = x1 + int(new_square_width*scaling_factor*choice_x)
                new_square_width = int(new_square_width - (new_square_width*scaling_factor))
                x2 = x1+new_square_width

                y1 = y1 + int(new_square_height*scaling_factor*choice_y)
                new_square_height = int(new_square_height - (new_square_height*scaling_factor))
                y2 = y1+new_square_height
                
                scaling_factor += 0.05

                color = get_random_color()
                draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0), width=2)

### MAIN ###

def main():
    save_directory = Path('.') / 'Python' / 'stacked_squares' / 'output'
    save_directory.mkdir(parents=True, exist_ok=True)
    # print(save_directory.absolute())
    # seed = random.randint(0, 1000000)
    # image_width = 1000
    # image_height = 1000
    # canvas_color = (255, 255, 255)
    # image = Image.new('RGB', (image_width, image_height), canvas_color)
    # draw = ImageDraw.Draw(image)

    # draw_stacked_squares(draw, image_width, image_height )
    # draw_wandering_stacked_squares(draw, image_width, image_height )

    seed = random.randint(0, 1000000)
    image_width = 1100
    image_height = 1100
    canvas_color = (255, 255, 255)
    image = Image.new('RGB', (image_width, image_height), canvas_color)
    draw = ImageDraw.Draw(image)
    draw_square_stacked_squares(draw, image_width, image_height )


    image.save(save_directory / f'seed_{seed}.png')
    image.show()




if __name__ == '__main__':
    color_palette_directory = Path('.') / 'Resources' / 'color_palettes'
    # color_path = color_palette_directory / 'FlatUI.json'
    # color_path = color_palette_directory / '817f82-ae8ca3-a2abb5-95d9da-6dd6da.json'
    # color_path = color_palette_directory / '264653-2a9d8f-e9c46a-f4a261-e76f51.json'
    # color_path = color_palette_directory / '001219-005f73-0a9396-94d2bd-e9d8a6-ee9b00-ca6702-bb3e03-ae2012-9b2226.json'
    # color_path = color_palette_directory / 'cotton_candy.json'
    # color_path = color_palette_directory / 'brown_6.json'
    # color_path = color_palette_directory / 'brown_many.json'
    color_path = color_palette_directory / 'blue_green_many.json'


    color_palette = ColorPalette(color_path)

    # print(color_palette)
    main()