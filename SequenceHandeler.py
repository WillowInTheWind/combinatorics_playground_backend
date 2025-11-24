import SequenceGenerator
from PIL import Image, ImageDraw
import io
from base64 import encodebytes

def pixelstrips_up_to(n_max):
    cards = []
    k=0
    for n in range(n_max+1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n,r)
            for path in paths:
                size = 100 * len(path)
                im = Image.new("RGBA", (size+10, 105), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 0
                current_y = 0
                for letter in path:
                # movement = ((-1)**(1+int(letter)))*100
                    draw.rectangle(xy = [current_x, current_y, current_x+100, current_y+100], fill =(0,0,0,128*(int(letter))), outline = (0,0,0,256))
                    current_x += 100
            # write to stdout
                    byte_arr = io.BytesIO()
                    im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64
                    card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                    cards.append(card)
                    k += 1
    return cards

def dyckpaths_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max+1):
        for r in range(n):
            paths = SequenceGenerator.Nariyana_sequence(n,r)
            for path in paths:
                size = 100*len(path)
                im = Image.new("RGBA", (size+20,int(size/2)+20), color=(0,0,0,0))
                draw = ImageDraw.Draw(im)
                current_x= size+10
                current_y = int(size/2)+10
                for letter in path:
                    # movement = ((-1)**(1+int(letter)))*100
                    if int(letter) == 1:
                        draw.line((current_x, current_y, current_x-102, current_y - 102), fill=(0,0,0,256), width=10)
                        draw.ellipse([current_x-110, current_y-110, current_x-90, current_y-90], fill = (0,0,0,256))
                        current_y -= 100
                    if int(letter) == 0:
                        draw.line((current_x, current_y, current_x-102, current_y + 102), fill=(0,0,0,256), width=10)
                        draw.ellipse([current_x-110, current_y+90, current_x-90, current_y+110], fill = (0,0,0,256))

                        current_y += 100
                    current_x  -= 100
                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k +=1
    return cards

def fullparentheses_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.Nariyana_sequence(n,r)
            for path in paths:

                size = 50*(len(path)+1)
                im = Image.new("RGBA", (size+5-50,105), color=(0,0,0,0))
                draw = ImageDraw.Draw(im)
                current_x= 0
                current_y = 0
                for letter in path:
                    # movement = ((-1)**(1+int(letter)))*100
                    if int(letter) == 1:
                        draw.arc((current_x, current_y, current_x+50, current_y + 100), start = 90, end = 270, fill=(0,0,0,256), width=10)
                        current_x += 50
                    if int(letter) == 0:
                        draw.arc((current_x, current_y, current_x + 50, current_y +100), start=270, end=90,
                                 fill=(0, 0, 0, 256), width=10)

                        current_x += 50
                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k+=1
    return cards

def domino_tiling_by_n(n):
    images = []
    paths = SequenceGenerator.fibbonaci_sequence(n)
    for path in paths:
        size = 100*path.count("1")+50*path.count("0")+20
        im = Image.new("RGBA", (size,int(size/2)), color=(0,0,0,0))
        draw = ImageDraw.Draw(im)
        current_x= 0
        current_y = 0
        for letter in path:
            # movement = ((-1)**(1+int(letter)))*100
            if letter == "1":
                draw.rectangle(xy=[current_x, 50, current_x + 100, 100],fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                draw.rectangle(xy=[current_x, 0, current_x + 100,  50],fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                current_x += 100
            elif letter == "0":
                draw.rectangle(xy=[current_x, 0, current_x + 50,  100],fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                current_x += 50
        images.append(im)
    return images

def starfolkspaths_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n, r)
            for path in (paths):
                ups = path.count("1")
                size = 100 * len(path)
                im = Image.new("RGBA", ((len(path) - ups)*100+20, ups*100+20), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 5
                current_y = 5
                draw.ellipse([current_x  - 5, current_y  - 5, current_x  + 5,
                              current_y  + 5], fill=(0, 0, 0, 256))

                for letter in path:
                    y_increase = int(letter)*100
                    x_increase = 100 - y_increase
                        # movement = ((-1)**(1+int(letter)))*100
                    draw.line(xy = [current_x, current_y, current_x+x_increase, current_y+y_increase], fill =(0,0,0,256))
                    draw.ellipse([current_x + x_increase - 5, current_y + y_increase - 5, current_x + x_increase + 5, current_y + y_increase + 5], fill=(0, 0, 0, 256))
                    current_x += x_increase
                    current_y += y_increase
                    # write to stdout
                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k +=1
    return cards

def nonattackingrooks_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n, r)
            for path in paths:

                size = 50 * len(path)
                im = Image.new("RGBA", (size+10, int(size+10)), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 0
                current_y = 0
                for letter in path:
                    y_increase = int(letter)*100
                    x_increase = 100 - y_increase
                        # movement = ((-1)**(1+int(letter)))*100
                    draw.line(xy = [current_x, current_y, current_x+x_increase, current_y+y_increase], fill =(256,256,256,256))
                    current_x += x_increase
                    current_y += y_increase
                    # write to stdout

                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k+=1
    return cards
def binarytrees_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.Nariyana_sequence(n, r)
            for path in paths:
                size = 100*len(path)
                im = Image.new("RGBA", (size+20,size+20), color=(0,0,0,0))
                draw = ImageDraw.Draw(im)
                current_x= size
                current_y = size

                for letter in (path):
                    current_x = int(size/2)
                    current_y = 0

                    if int(letter) == 1:
                        draw.line(xy=[current_x, current_y, current_x + 100, current_y + 100],
                                      fill=(256, 0, 256, 256))
                        current_y += 100
                        current_x += 100
                    elif int(letter) == 0:
                        current_y -= 100
                        current_x -= 100

                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k += 1
    return cards
class CardPackage:
    graphic: str
    id:int
    n:int
    r: int

    def __init__(self, graphic, n, r,identification):
        self.graphic = graphic
        self.id = identification
        self.n = n
        self.r =  r
