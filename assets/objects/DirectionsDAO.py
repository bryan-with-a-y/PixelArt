import os

from PIL import Image

import assets.constants as CONSTANTS

class DirectionsDAO(object):
    def __init__(self, image_path, palette, project_name):
        self.project_name = project_name
        self.directions_dir = "./projects/{}/".format(project_name)
        self.palette = palette
        self.colors = self.palette.keys()
        self.grid_pattern = [3,3]
        self.load_image(image_path)
        self.create_direction_images()

    def load_image(self, image_path):
        self.im = Image.open(image_path)
        self.pix = self.im.load()
        self.xsize, self.ysize = self.im.size

    def reverse_palette(self):
        for color in self.palette.keys():
            value = self.palette[color]
            self.palette[value] = color

    def create_asset_images(self):
        gap_image = Image.new("RGB", (560,560), "blue")
        gap_image.save("./assets/gap_image.png")
        
        row_end_image = Image.new("RGB", (560,560), "red")
        row_end_image.save("./assets/gap_image.png")
        
        direction_im = Image.new("RGB", (560,560), "black")
        direction_im_pix = self.direction_im.load()
        xsize, ysize = 560,560
        for ystart in range(10, ysize, 110):
            for xstart in range(10, xsize, 110):
                for yi in range(ystart, ystart+100):
                    for xi in range(xstart, xstart+100):
                        direction_im_pix[xi,yi] = (255,255,255)
        direction_im.save("./assets/blank_direction_im.png")

        """
                if (yi>=0   and yi<10 or 
                    yi>=110 and yi<120 or
                    yi>=220 and yi<230 or
                    yi>=330 and yi<340 or
                    yi>=440 and yi<450 or
                    yi>=550 and yi<560 or

                    xi>=0   and xi<10 or 
                    xi>=110 and xi<120 or
                    xi>=220 and xi<230 or
                    xi>=330 and xi<340 or
                    xi>=440 and xi<450 or
                    xi>=550 and xi<560):
        """     
    def initialize_direction_image(self):
        self.direction_im = Image.open("./assets/blank_direction_im.png")
        self.direction_im_pix = self.direction_im.load()
    
    def create_direction_images(self, directions_type="both"):
        #save type is either "region" or "color" or "both"

        #iterates over each color to be used when saving in folder
        for color in self.colors:
            num_remaining_colors = len(self.colors) - list(self.colors).index(color)
            palette_pixel_value = self.palette[color]

            #iterates over the entire image
            for ystep in range(0, self.ysize, 10):
                for xstep in range(0, self.xsize, 10):
                    section = str([xstep//CONSTANTS.PAPER_XSIZE, ystep//CONSTANTS.PAPER_YSIZE])
                    section_str = section.replace(" ", "")
                    starting_coord = "[y-{0:03d} x-{1:03d}]".format(ystep, xstep)
                    
                    #iterates over the 10x10 graph paper
                    
                    #modified = False
                    pixel_list = []
                    for yi in range(10):
                        for xi in range(10):
                            current_pixel_value = self.pix[xstep+xi, ystep+yi]
                            
                            if palette_pixel_value == current_pixel_value:
                                #modified = True
                                xstart = xi*50 + (xi//2)*10 + 10
                                ystart = yi*50 + (yi//2)*10 + 10 #10 is the border thickness of the grid
                                pixel_list.append([xstart,ystart])
                    
                    #if modified:
                    self.create_direction_im(pixel_list)
                    #self.save_direction_im("color", color, starting_coord)
                    self.save_direction_im("region", section_str, color, starting_coord)
            print("finishing color: {}".format(color))
    
    def save_direction_im(self, directions_type, *argv):
        if directions_type == "color":
            save_location = os.path.join(self.directions_dir, "directions_color", argv[0], argv[1] + ".png")

        if directions_type == "region":
            save_location = os.path.join(
                    self.directions_dir, "directions_region", argv[0], argv[1], argv[2] + ".png")
       
        save_location = save_location.replace("\\", "/")
        self.direction_im.save(save_location)

    def create_direction_im(self, pixel_list):
        fill_color = (255,102,204)
        #iterates over a pixel on the direction image
        self.initialize_direction_image()
        
        for coord in pixel_list:
            for yi in range(50):
                for xi in range(50):
                    direction_im_x = coord[0] + xi
                    direction_im_y = coord[1] + yi
                    self.direction_im_pix[direction_im_x, direction_im_y] = fill_color

