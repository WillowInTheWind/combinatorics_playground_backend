import math

import SequenceGenerator
from PIL import Image, ImageDraw
import io
from base64 import encodebytes

from SequenceGenerator import n_such_that_there_are_k_sequences

MAX_RESOLUTION = 2520


def pixelstrips_up_to(n_max):
    cards = []
    k=0

    for n in range(n_max+1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n,r)
            for path in paths:
                # size = 100 * len(path)
                section_increment = math.floor(MAX_RESOLUTION/len(path))
                im = Image.new("RGBA", (MAX_RESOLUTION+10, int(section_increment) +5), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 0
                current_y = 0
                for letter in path:
                # movement = ((-1)**(1+int(letter)))*100
                    draw.rectangle(xy = [current_x, current_y, current_x+section_increment, current_y+section_increment], width = 30, fill =(64,64,64,256*(int(letter))), outline = (0,0,0,256))
                    current_x += section_increment
            # write to stdout
                im.save(f'pixelstrips/pixelstrip{k}.png')
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
                section_increment = math.floor(MAX_RESOLUTION/len(path))

                im = Image.new("RGBA", (MAX_RESOLUTION+20,int(MAX_RESOLUTION/2)+20), color=(0,0,0,0))
                draw = ImageDraw.Draw(im)
                current_x= MAX_RESOLUTION+10
                current_y = int(MAX_RESOLUTION/2)+10
                draw.ellipse([current_x - 30, current_y - 30,
                              current_x + 30, current_y + 30],
                             fill=(0, 0, 0, 256))

                for letter in path:
                    # movement = ((-1)**(1+int(letter)))*100
                    if int(letter) == 1:
                        draw.line((current_x, current_y, current_x-section_increment-2, current_y - section_increment-2), fill=(0,0,0,256), width=30)
                        draw.ellipse([current_x-section_increment-30, current_y-section_increment-30, current_x-section_increment+30, current_y-section_increment+30], fill = (0,0,0,256))
                        current_y -= section_increment
                    if int(letter) == 0:
                        draw.line((current_x, current_y, current_x-section_increment-2, current_y + section_increment+2), fill=(0,0,0,256), width=30)
                        draw.ellipse([current_x-section_increment-30, current_y+section_increment-30, current_x-section_increment+30, current_y+section_increment+30], fill = (0,0,0,256))

                        current_y += section_increment
                    current_x  -= section_increment
                draw.ellipse([current_x - section_increment - 30, current_y + section_increment - 30,
                              current_x - section_increment + 30, current_y + section_increment + 30],
                             fill=(0, 0, 0, 256))

                im.save(f'Dyck/Dyck{path}.svg')
                # byte_arr = io.BytesIO()
                # im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                # encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64
                #
                # card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                # cards.append(card)
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
                section_increment = math.floor(2*MAX_RESOLUTION/len(path))
                im = Image.new("RGBA", (MAX_RESOLUTION+15, section_increment), color=(0,0,0,0))
                draw = ImageDraw.Draw(im)
                current_x= 0
                current_y = 0
                for letter in path:
                    # movement = ((-1)**(1+int(letter)))*100
                    if int(letter) == 1:
                        draw.arc((current_x, current_y, current_x+int(section_increment/2), current_y + section_increment), start = 90, end = 270, fill=(0,0,0,256), width=30)
                        current_x += int(section_increment/2)
                    if int(letter) == 0:
                        draw.arc((current_x, current_y, current_x +int(section_increment/2), current_y + section_increment), start=270, end=90,
                                 fill=(0, 0, 0, 256), width=30)

                        current_x += int(section_increment/2)
                byte_arr = io.BytesIO()
                im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

                card ={"graphic": encoded_img, "n": n, "r": r, "id":k}
                cards.append(card)
                k+=1
    return cards

def domino_tiling_up_to(n):
    cards = []
    for i in range(n):
        paths = SequenceGenerator.fibbonaci_sequence(i)
        for k in range(len(paths)):
            path = paths[k]
            # size = 100*path.count("1")+50*path.count("0")+20
            doubles = path.count("1")

            section_increment = math.floor(2*MAX_RESOLUTION / (2*doubles + (len(path)-doubles)))

            im = Image.new("RGBA", (MAX_RESOLUTION,int(MAX_RESOLUTION)), color=(0,0,0,0))
            draw = ImageDraw.Draw(im)
            current_x= 0
            current_y = 0
            for letter in path:
                # movement = ((-1)**(1+int(letter)))*100
                if letter == "1":
                    draw.rectangle(xy=[current_x, int(section_increment/2), current_x + section_increment, section_increment],width =30,fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                    draw.rectangle(xy=[current_x, 0, current_x + section_increment,  int(section_increment/2)],width =30, fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                    current_x += section_increment
                elif letter == "0":
                    draw.rectangle(xy=[current_x, 0, current_x + int(section_increment/2),  section_increment],width =30, fill=(0, 0, 0, 0), outline=(0, 0, 0, 256))
                    current_x += int(section_increment/2)
            byte_arr = io.BytesIO()
            im.save(byte_arr, format='PNG')  # convert the PIL image to byte array
            encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64

            card = {"graphic": encoded_img, "n": i, "r": 0, "id": k}
            cards.append(card)
            k += 1
    return cards

def starfolkspaths_up_to(n_max):
    cards = []
    k = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n, r)
            for path in (paths):
                ups = path.count("1")
                #size = 100 * len(path)
                major_size = max((len(path) - ups), ups)
                section_increment = math.floor(MAX_RESOLUTION/major_size)

                im = Image.new("RGBA", ((len(path) - ups)*section_increment+20, ups*section_increment+20), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 5
                current_y = 5
                draw.ellipse([current_x  - 30, current_y  - 30, current_x  + 30,
                              current_y  + 30], fill=(0, 0, 0, 256))

                for letter in path:
                    y_increase = int(letter)*section_increment
                    x_increase = section_increment - y_increase
                        # movement = ((-1)**(1+int(letter)))*100
                    draw.line(xy = [current_x, current_y, current_x+x_increase, current_y+y_increase], width =30, fill =(0,0,0,256))
                    draw.ellipse([current_x + x_increase - 30, current_y + y_increase - 30, current_x + x_increase + 30, current_y + y_increase + 30], fill=(0, 0, 0, 256))
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
    id = 0
    for n in range(n_max + 1):
        for r in range(n):
            paths = SequenceGenerator.binary_strings(n, r)
            for path in paths:
                id += 1
                size = 50 * len(path)
                im = Image.new("RGBA", (size+10, int(size+10)), color=(0, 0, 0, 0))
                draw = ImageDraw.Draw(im)
                current_x = 0
                current_y = 0
                for letter in path:
                    y_increase = int(letter)*100
                    x_increase = 100 - y_increase
                        # movement = ((-1)**(1+int(letter)))*100
                    draw.line(xy = [current_x, current_y, current_x+x_increase, current_y+y_increase], width= 30, fill =(256,256,256,256))
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


if (__name__ == "__main__"):
    pixelstrips_up_to(5);