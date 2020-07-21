import os, sys
from PIL import Image

import assets.constants as CONSTANTS
from assets.modules.palette_pixel_functions import get_closest_palette_color

class ColorWorker(object):
    def __init__(self, image_name, grid_pattern, palette):
        self.image_dir = "./projects/images/"
        self.image_name = image_name
        self.paper_width_num = grid_pattern[0]
        self.paper_height_num = grid_pattern[1]
        self.load_image()

        self.palette = palette
        self.round_image()

        self.im.show()
        self.save_image(image_name + "_rounded.png")

    def load_image(self):
        image_path = os.path.join(self.image_dir, self.image_name)
        #image_path = "{}{}".format(self.image_dir, self.image_name)
        im = Image.open(image_path + ".png")
        
        self.xsize = self.paper_width_num*CONSTANTS.PAPER_XSIZE
        self.ysize = self.paper_height_num*CONSTANTS.PAPER_YSIZE
        self.im = im.resize( (self.xsize, self.ysize) )
        self.pix = self.im.load()

    def save_image(self, save_name):
        save_path = "./projects/images/{}".format(save_name)
        self.im.save(save_path)

    def round_image(self):
        for yi in range(self.ysize):
            if yi%10 == 0:
                print(self.ysize-yi)
            for xi in range(self.xsize):
                pixel = self.pix[xi,yi]
                value = get_closest_palette_color(self.palette, pixel)
                self.pix[xi, yi] = value

