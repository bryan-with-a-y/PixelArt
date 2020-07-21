from math import sqrt

WHITE = (255,255,255)
BLACK = (0,0,0)

def pixel_difference(pix1, pix2):
   r1,g1,b1 = pix1[0:3]
   r2,g2,b2 = pix2[0:3]

   difference = (r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2
   return difference

def pixel_distance(pix1, pix2):
   return sqrt(pixel_difference(pix1,pix2))

def get_closest_palette_pixel(palette, test_pixel):
   palette_colors = palette.keys()

   best_difference = pixel_difference(WHITE, BLACK)
   best_color_name = None
   best_color_value = None

   for palette_color_name in palette_colors:
      palette_pixel = palette[palette_color_name]
      test_difference = pixel_difference(test_pixel, palette_pixel)
      if test_difference <= best_difference:
         best_color_name = palette_color_name
         best_color_value = palette_pixel
         best_difference = test_difference
   
   return best_color_value
