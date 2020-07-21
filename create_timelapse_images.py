from PIL import Image
from assets.palettes.sharpie_palette import PALETTE
"""
open rounded image
run once thru image with color pallete and count each pixel
sort lowest to highest

open white image
loop through by 10's
check pixel
"""

im_name = "./projects/images/coufal_present_rounded.png"
im = Image.open(im_name)
xsize, ysize = im.size
pix = im.load()

new_im = Image.new("RGB", (420, 240))
new_pix = new_im.load()

colors = list(PALETTE.keys())
reverse_palette = dict()

counter = dict()
for color in colors:
   counter[color] = 0

for color in colors:
    pixel_value = PALETTE[color]
    reverse_palette[pixel_value] = color

for yi in range(ysize):
    for xi in range(xsize):
        current_pix = pix[xi,yi]
        color_name = reverse_palette[current_pix]
        counter[color_name] += 1


reverse_counter = dict()
for color in counter.keys():
    #print(color, counter[color])
    reverse_counter[counter[color]] = color

keys = sorted(list(reverse_counter.keys()))
for key in keys:
    print(reverse_counter[key], key)
print()

counter = 0
for count in keys:
    color = reverse_counter[count]
    print(color)
    for yii in range(0, ysize, 10):
        for xii in range(0, xsize, 10):
            modified = False
            counter += 1
            for yi in range(yii, yii+10):
                for xi in range(xii, xii+10):
                    current_pixel = pix[xi,yi]
                    palette_pixel = PALETTE[color]
                    if current_pixel == palette_pixel:
                        modified = True
                        new_pix[xi,yi] = palette_pixel
            if modified:
                new_im.save("./projects/coufal_present/timelapse/computer_generated/{:05d}.png".format(counter))
    print("next color")
    #new_im.show()

