from PIL import Image

class ColorMelt():
    def __init__(self):
        self.mod_image()

    def mod_image(self):
        self.init_image()
        for modder in range(self.ysize):
            self.melt_image(modder)
            print("MODDER: ", modder)
            self.im.save("./projects/test/images/test_melt{}.png".format(
                str(modder).zfill(4)))

    def init_image(self):
        self.im_path = "./projects/test/images/test.png"
        self.im = Image.open(self.im_path)
        self.xsize, self.ysize = self.im.size
        self.pix = self.im.load()
        
    def mod_pix(self, xi, yi, modder):
        im_pix = self.pix[xi,yi]
        pixel_list = list()
        for yii in range(yi-modder, yi+1):
            pixel_list.append(self.pix[xi, yii])
        r,g,b = 0,0,0
        for pixel in pixel_list:
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]
        r = int(r/len(pixel_list))
        g = int(g/len(pixel_list))
        b = int(b/len(pixel_list))
        return r,g,b

    def melt_image(self, modder):
        for yi in range(self.ysize):
            print(yi-self.ysize)
            for xi in range(self.xsize):
                new_pix = self.mod_pix(xi, yi, modder)
                self.pix[xi,yi] = new_pix

melt = ColorMelt()
