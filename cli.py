import os, sys
from math import sqrt

from PIL import Image

from assets.objects.Palette import Palette

palette_fp = "./assets/palettes/sharpie_palette.txt"
PALETTE = Palette(palette_fp)

FILL_COLOR = (255,102,204)

im_path = "./projects/coufal_present/images/coufal_present_rounded.png"
im = Image.open(im_path)
pix = im.load()
xsize, ysize = im.size

def count_image_color(color):
    count = 0
    for yi in range(ysize):
        for xi in range(xsize):
            if pix[xi,yi] == PALETTE[color]:
                count += 1
                print(xi,yi)
    return count

def get_region(xi,yi):
    return xi//140,yi//80

def get_block(xi, yi):
    return xi//20, yi//20

def swap(color1, color2):
    count = 0
    for yi in range(ysize):
        for xi in range(xsize):
            if get_block(xi,yi) == (6,7):
                print(True)
            if pix[xi,yi] == PALETTE.pixel_lookup(color1):
                print(False)
            if pix[xi,yi] == PALETTE.pixel_lookup(color2) and get_block(xi,yi) == (6,7):
                pix[xi,yi] = PALETTE.pixel_lookup(color2)
                count += 1
    print(count)
    im.save("./projects/coufal_present/images/coufal_present_flubbed2.png")

def check_pix(x=None, y=None):
    if not(x and y):
        while True:
            coords = input("Enter coords to check: ")
            x,y = int(coords.split(" ")[0]), int(coords.split(" ")[1])
            pixel = pix[x,y]
            print(REVERSE_PALETTE[pixel])
    elif (x and y):
        print(pix[x,y])
    else:
        print("Error. Returning")

def count_region_by_folder(target_region, target_color):
    color = "12. TRANQUIL_TEAL"
    region = "[{},{}]".format(target_region[0], target_region[1])
    region_dir = "./projects/coufal_present/directions_region/{}/{}/".format(region, color)
    image_names = os.listdir(region_dir)
    color = target_color

    count = 0
    for image_name in image_names:
        this_im = Image.open(region_dir + image_name)
        this_pix = this_im.load()
        this_xsize, this_ysize = this_im.size

        for yi in range(10, this_ysize, 110):
            for xi in range(10, this_xsize, 110):
                pix1 = this_pix[xi,yi]
                pix2 = this_pix[xi+50,yi]
                pix3 = this_pix[xi,yi+50]
                pix4 = this_pix[xi++50,yi+50]
                if pix1 == FILL_COLOR:
                    count += 1
                if pix2 == FILL_COLOR:
                    count += 1
                if pix3 == FILL_COLOR:
                    count += 1
                if pix4 == FILL_COLOR:
                    count += 1
    return count

def count_region_color(target_region, color):
    count = 0
    for yi in range(ysize):
        for xi in range(xsize):
            if pix[xi,yi] == PALETTE[color] and get_region(xi, yi) == target_region:
                count += 1
    return count

def analyze_regions(target_region):
    target_region = target_region
    info_list = list()
    for color in PALETTE.keys():
        region_count = count_region_color(target_region, color)
        pixel = PALETTE[color]
        distance = sqrt(pixel[0]**2 + pixel[1]**2 + pixel[2]**2)
        entry = {"color": color, "region_count": region_count, "distance": distance}
        info_list.append(entry)

    ordered_entries = list(reversed(sorted(info_list, key=lambda entry: entry["distance"])))
    return ordered_entries

def show_region_info(region=(2,0)):
    ordered_entries = analyze_regions(region)
    for entry in ordered_entries:
        index = ordered_entries.index(entry)
        print("{}. {}: ".format(str(index).zfill(2), entry["color"]).ljust(24) + 
              "{:.2f}  ".format(entry["distance"]).ljust(9) + 
              "{} ".format(entry["region_count"]).ljust(6) + 
              "pixels")

def reorganize():
    im_path = "./projects/images/blank_direction_im.png"
    blank_im = Image.open(im_path)
    blank_im = blank_im.load()
    blank_xsize, blank_ysize = blank_im.size

def rename_folders():
    regions_dir = "./projects/coufal_present/directions_region"
    dirs = os.listdir(regions_dir)
    ordered = analyze_regions((0,0))
    for region in dirs:
        for entry in ordered:
            color = entry["color"]
            old_dir = "{}/{}/{}".format(regions_dir, region, color)
            old_dir_done = "{}/{}/{} done".format(regions_dir, region, color)

            index = ordered.index(entry)
            new_color = "{}. {}".format(str(index).zfill(2), color)
            new_dir = "{}/{}/{}".format(regions_dir, region, new_color)
            new_dir_done = "{}/{}/{} done".format(regions_dir, region, new_color)
            try:
                os.rename(old_dir, new_dir)
                print("success old {} --> {}".format(old_dir, new_dir))
            except FileNotFoundError:
                print("Trying done")
                try:
                    os.rename(old_dir_done, new_dir_done)
                    print("success new {} --> {}".format(old_dir_done, new_dir_done))
                except FileNotFoundError:
                    print("what")
            #print(old_dir)
            #print(old_dir_done)
            #print(new_dir)
            #print(new_dir_done)

def main():
    #print(count_region_color(target_region=(2,0), color="TRANQUIL_TEAL"))
    #get_region()
    
    color1 = "HONEY_BROWN"
    color2 = "WOODSY_BROWN"
    swap(color1, color2)
    #check_pix()
    #print(count_region(target_region=(2,0), color="PETAL_PINK"))
    #sort_palette()
    #show_region_info(region=(2,0))
    #reorganize()
    #rename_folders()
    #print(count_region_by_folder(target_region=(2,0), target_color="TRANQUIL_TEAL"))
    pass

main()
