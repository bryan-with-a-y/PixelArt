from PIL import Image

def create_10x10():
    region_xsize = 10 #image pixels
    region_ysize = 10 #image pixels
    xseps = region_xsize//2 + 1
    yseps = region_ysize//2 + 1
    minor_thickness = 10 #real pixels
    pixel_thickness = 50 #real pixels

    xsize = pixel_thickness*10 + minor_thickness*xseps
    ysize = pixel_thickness*10 + minor_thickness*yseps
    im = Image.new("RGB", (xsize, ysize), ("GRAY"))
    pix = im.load()

    for yi in range(minor_thickness, ysize, pixel_thickness*2+minor_thickness):
        for xi in range(minor_thickness, xsize, pixel_thickness*2+minor_thickness):
            print(xi, yi)
            for yii in range(pixel_thickness*2):
                for xii in range(pixel_thickness*2):
                    pix[xi+xii, yi+yii] = (0,0,0)
    im.save("./assets/images/10x10_template.png")

def create_20x20():
    im = Image.open("./assets/images/10x10_template.png")
    xsize, ysize = im.size
    pix = im.load()
    new_im = Image.new("RGB", (xsize*2, ysize*2))
    new_im_xsize, new_im_ysize = new_im.size
    new_pix = new_im.load()
    
    for yii in range(2):
        for xii in range(2):
            for yi in range(ysize):
                for xi in range(xsize):
                    old_pix = pix[xi, yi]
                    new_pix[xi+xii*xsize, yi+yii*ysize] = old_pix
    new_im.save("./assets/images/20x20_template.png")

def create_template_images():
    create_10x10()
    create_20x20()

create_template_images()

