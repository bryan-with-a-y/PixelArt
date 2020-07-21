import assets.modules.pixel_functions as PF

BLACK = (0,0,0)
WHITE = (255,255,255)

class Color(object):
    def __init__(self, color, pixel_value, order):
        self.color = color
        self.pixel_value = pixel_value
        self.order = order

class Palette(object):
    """
    Things not to do:
      adding a function to add more colors to palette:
        Don't want to deal with modifying order several times
    """
    def __init__(self, textfile_path):
        self.from_textfile(textfile_path)
        self.sort_palette()
        self.make_reverse_palette()

    def _set_order(self, color, order_number):
        ###Edit this later to insert?
        self.order[color] = order_number

    def sort_palette(self):
        """ Sorts palette by pixel value's distance from (0,0,0) """
        self.order = dict()
        seq = list()
        for color in self.get_colors():
            seq.append({"distance": PF.pixel_distance(self.pixel_lookup(color), (0,0,0)),
                        "color": color,
                        "pixel_value": self.pixel_lookup(color)})
        seq = [entry for entry in reversed(sorted(
            seq, key=lambda entry: entry["distance"]))]
        
        for entry in seq:
            self._set_order(entry["color"], seq.index(entry)+1)

    def from_textfile(self, fp):
        self.palette = dict()
        with open(fp, "r") as datafile:
            for line in datafile.readlines():
                color_name, pixel_value = line.strip().split("=")
                r,g,b = [int(component) for component in pixel_value.strip("()").split(",")]
                self.add_color(color_name, (r,g,b), init=True)
        self.sort_palette()

    def add_color(self, color_name, value, init=False):
        self.palette[color_name] = value
        if not init:
            self.sort_palette()

    def make_reverse_palette(self):
        self.reverse_palette = dict()
        for color in self.get_colors():
            self.reverse_palette[self.palette[color]] = color

    def pixel_lookup(self, color):
        """Given a color string, return pixel_value tuple"""
        try:
            return self.palette[color]
        except KeyError:
            print("color name {} not found".format(color))

    def color_lookup(self, pixel_value):
        """Given a pixel_value tuple, return color string"""
        try:
            return self.reverse_palette[pixel_value]
        except KeyError:
            print("pixel value {} not found.".format(pixel_value))

    def get_order(self, color):
        """Given a color string, return the order integer of that color"""
        return self.order[color]

    def get_colors(self):
        return self.palette.keys()

    def get_pixel_values(self):
        return self.reverse_palette.keys()

    def get_closest_pixel_value(self, test_pixel):
        """Need to figure out if this should return color or pixel value"""
        best_difference = PF.pixel_difference(WHITE, BLACK)
        best_color_name = None
        best_color_value = None

        for palette_color in self.get_colors():
            palette_pixel = self.pixel_lookup(palette_color)
            test_difference = PF.pixel_difference(test_pixel, palette_pixel)
            if test_difference <= best_difference:
                best_color_name = palette_color
                best_color_value = palette_pixel
                best_difference = test_difference

        return best_color_value

