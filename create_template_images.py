from PIL import Image


def create():
    region_xsize = 10
    region_ysize = 10
    xseps = region_xsize//2 + 1
    yseps = region_ysize//2 + 1
    minor_thickness = 10
    #major_thickness = 20
    minor_color = (128,128,128)
    #major_color = (128,0,0)
    pixel_thickness = 50

    xsize = pixel_thickness*10 + minor_thickness*xseps
    ysize = pixel_thickness*10 + minor_thickness*yseps
    
    im = Image.new("RGB", (xsize, ysize), ("GRAY"))
    pix = im.load()
    for yi in range(minor_thickness, ysize, pixel_thickness*2+minor_thickness):
        for xi in range(minor_thickness, xsize, pixel_thickness*2+minor_thickness):
            print(xsize, ysize, xi, yi)
            for yii in range(pixel_thickness*2):
                for xii in range(pixel_thickness*2):
                    pix[xi+xii, yi+yii] = (0,0,0)
            """pix[xi                , yi                ] = (0,0,0)
            pix[xi+pixel_thickness, yi                ] = (0,0,0)
            pix[xi                , yi+pixel_thickness] = (0,0,0)
            pix[xi+pixel_thickness, yi+pixel_thickness] = (0,0,0)"""
    im.save("./assets/images/70x40_template.png")

def create2():
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

def main():
    create2()

main()

