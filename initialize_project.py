"""
The purpose of this program is to intialize a pixel art drawing project.
The main areas that need intialized:
    How many sections (pieces of graph paper)
    How many pixels
    What color set to use
    
    Setting up the directions folder:
        set up regions folder
        in each region folder there are sub_region folders
        in each sub_region folder there are X by X squares of pixel instructions
"""

"""
***CONSIDERATIONS FOR NEXT PROJECT***
1. Create a .py file that roudns and shows the image before initializing anything.
2. Use the margins of the graph paper to write on isntead of utilzing the entire paper
   for drawing
3. When drawing on graph paper, write thicker lines, center numbers on 10x10 block
8. Create code to generate instructions for AxB.
9. When using white as a color, mark the drawing side with pencil for better visualization purposes.
10. Reverse the image before rounding it so that when i draw it, the bleed through effect
    on the paper is the original image.
"""

"""
Project timeline/outline:
    1. Select an image
    2a. Test multiple sizes
    2b. Select a size
    3. Create direction images
    4. Set up paper
    5. Draw pixels
    
"""

import os
from posixpath import join

from PIL import Image

from assets.objects.Palette import Palette
import assets.constants as CONSTANTS

#TODO make extended_sharpie_palette.txt
palette_fp = "./assets/palettes/36_sharpie_palette.txt"
PALETTE = Palette(palette_fp)

#PROJECT LEVEL VARIABLES
PROJECT_NAME = "coufal_present"
PROJECT_DIR = join("./projects", PROJECT_NAME)
BASE_IMAGE_NAME = "{}.png".format(PROJECT_NAME)
BASE_IMAGE_PATH = join(PROJECT_DIR, "images", BASE_IMAGE_NAME)
RESIZED_IMAGE_PATH = BASE_IMAGE_PATH[:-4] + "_resize.png"
ROUNDED_IMAGE_PATH = BASE_IMAGE_PATH[:-4] + "_rounded.png"
REGION_DIRECTIONS_DIR = ""
BLOCK_PATTERN_DIRECTIONS_DIR = "./projects/{}/directions/block/".format(PROJECT_NAME)

#PALETTE LEVEL VARIABLES
INCLUDE_WHITE = True
WHITE_COLOR_NAME = "WHITE"
WHITE_COLOR_VALUE = (255,255,255)
if INCLUDE_WHITE:
    PALETTE.add_color(WHITE_COLOR_NAME, WHITE_COLOR_VALUE)

#DIRECTION MAKER METHOD VARIABLES
METHODS = ["region", "block", "region_sub_region"]
DIRECTION_METHOD = "region_sub_region"
REGION_XSIZE, REGION_YSIZE = 40,24
FILL_COLOR = (255,255,255)

#CONSTANT VARIABLES
DIRECTION_IM_PIXEL_THICKNESS = 50
DIVISION_XSIZE, DIVISION_YSIZE = 20, 12
MINOR_DIVIDE_THICKNESS = 10
MAJOR_DIVIDE_THICKNESS = 10

#PAPER LEVEL VARIABLES
IMAGE_XSIZE, IMAGE_YSIZE = 420, 240 #This is actually going to change every project
PAPER_XSIZE, PAPER_YSIZE = 40, 24 #going to change every project
GRID_PATTERN = 8,8 #probably going to change every project

def init_directory_tree():
    try:
        os.makedirs("./projects/{}".format(PROJECT_NAME))
    except:
        pass
    try:
        os.makedirs("./projects/{}/images".format(PROJECT_NAME))
    except:
        pass
    try:
        os.makedirs("./projects/{}/directions".format(PROJECT_NAME))
    except:
        pass

    region_dir = "./projects/{}/directions/region".format(PROJECT_NAME)
    try:
        os.makedirs(region_dir)
    except:
        pass

    try:
        create_region_directions_directories(region_dir)
    except:
        pass

    block_dir = "./projects/{}/directions/block".format(PROJECT_NAME)
    try:
        os.makedirs(block_dir)
    except:
        pass
    try:
        create_block_pattern_directions_directories(block_dir)
    except:
        pass

    #print("{} project directory already exists. Continuing.".format(PROJECT_NAME))

def create_region_directions_directories(region_dir):
    for region_yi in range(GRID_PATTERN[1]):
        for region_xi in range(GRID_PATTERN[0]):

            region = "REGION- {},{}".format(region_xi, region_yi)
            folder_path = join(region_dir, region)
            try:
                os.makedirs(folder_path)
            except FileExistsError:
                pass
                #print("{} color directory already exists. Continuing.".format(folder_path))

def create_block_pattern_directions_directories(block_dir):
    """10x10 will have 42x24
       20x20 will have 21x12"""
    num_xblocks = IMAGE_XSIZE//BLOCK_XSIZE
    num_yblocks = IMAGE_YSIZE//BLOCK_YSIZE
    for yi in range(num_yblocks):
        for xi in range(num_xblocks):
            coord = "X-{}_Y-{}".format(xi+1, yi+1)
            os.makedirs(join(block_dir, coord))

def round_image():
    try:
        Image.open(ROUNDED_IMAGE_PATH)
        return
    except FileNotFoundError:
        pass

    input("Insert image into images folder named {}\nPress enter when done".format(
        BASE_IMAGE_NAME))
    try:
        im = Image.open(BASE_IMAGE_PATH)
    except FileNotFoundError:
        print("File incorrectly named or not found. Try again.")
        round_image()

    xsize, ysize = IMAGE_XSIZE, IMAGE_YSIZE
    im = im.resize((xsize, ysize))
    pix = im.load()
    im.save(RESIZED_IMAGE_PATH)

    for yi in range(ysize):
        print(ysize-yi)
        for xi in range(xsize):
            im_pix = pix[xi,yi]
            new_pix = PALETTE.get_closest_pixel_value(im_pix)
            pix[xi,yi] = new_pix

    im.save(ROUNDED_IMAGE_PATH)

def create_image_directions():
    if DIRECTION_METHOD == "region":
        create_reqion_directions()

def create_region_directions():
    #TODO: Experiment with different sized templates.
    # Add functionality to automatically use the differently sized templates
    
    def calculate_direction_start_coord(xii, yii):
        crossed_xdivides = (xii//2 + 1)
        division_offsetx = crossed_xdivides* MINOR_DIVIDE_THICKNESS
        if xii >= 10:
            division_offsetx += MAJOR_DIVIDE_THICKNESS
        
        crossed_ydivides = (yii//2 + 1)
        division_offsety = crossed_ydivides * MINOR_DIVIDE_THICKNESS
        if yii >= 10:
            division_offsety += MAJOR_DIVIDE_THICKNESS

        start_dix = xii*DIRECTION_IM_PIXEL_THICKNESS + division_offsetx
        start_diy = yii*DIRECTION_IM_PIXEL_THICKNESS + division_offsety
        return start_dix, start_diy

    im = Image.open(ROUNDED_IMAGE_PATH)
    pix = im.load()
    xsize, ysize = im.size

    for xi in range(0, xsize, REGION_XSIZE):
        for yi in range(0, ysize, REGION_YSIZE):
            color_set = set()

            #iterate over REGION_SIZE to determine needed colors to make directions out of
            for yii in range(REGION_YSIZE):
                for xii in range(REGION_XSIZE):
                    imx, imy = xi+xii, yi+yii
                    pixel = pix[imx, imy]
                    color = PALETTE.color_lookup(pixel)
                    color_set.add(color)
            
            #intialize set of direction ims
            direction_im_dict = dict()
            for color in color_set:
                blank_direction_im = Image.open("./assets/images/20x20_template.png")
                direction_im_dict[color] = {"im": blank_direction_im,
                                            "pix": blank_direction_im.load()}

            #draw on direction images
            for yii in range(BLOCK_YSIZE):
                for xii in range(BLOCK_XSIZE):
                    dix_start, diy_start = calculate_direction_start_coord(xii, yii)
                    imx, imy = xi+xii, yi+yii
                    pixel = pix[imx, imy]
                    color = PALETTE.color_lookup(pixel)

                    for yiii in range(DIRECTION_IM_PIXEL_THICKNESS):
                        for xiii in range(DIRECTION_IM_PIXEL_THICKNESS):
                            direction_im_dict[color]["pix"][dix_start+xiii,
                                                            diy_start+yiii] = FILL_COLOR
            block_regionx = xi//BLOCK_XSIZE + 1
            block_regiony = yi//BLOCK_YSIZE + 1
            region = "X-{}_Y-{}".format(block_regionx, block_regiony)
            print(region)
            for color in direction_im_dict.keys():
                save_fp = "{}/{}/{}-{}.png".format(BLOCK_PATTERN_DIRECTIONS_DIR,
                        region, str(PALETTE.get_order(color)).zfill(2), color)
                direction_im_dict[color]["im"].save(save_fp)

def create_region_directions():
    pass

def main():
    init_directory_tree()
    round_image()
    create_image_directions()

if sys.argv[1] == "test":
    
main()


