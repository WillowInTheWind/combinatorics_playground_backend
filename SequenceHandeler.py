import SequenceGenerator
import turtle
import sys
from PIL import Image, ImageDraw
import math

def pixelstrips_by_n_r(n, r):
    images = []
    paths = SequenceGenerator.binary_strings(n, r)
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
        images.append(im)
        im.save(f"pixelstrips/{path}.png")

    return images

def pixelstrips_by_n(n):
    row = {}
    for r in range(0, n+1):
        row[r] = SequenceGenerator.binary_strings(n, r)
    # TODO: return rendered tikz image

    return row

def pixelstrips_less_than_n(max_n):
    total = {}
    for n in range(0,max_n + 1):
        row = {}
        for r in range(0, n+1):
            row[r] = SequenceGenerator.binary_strings(n, r)
        total[n] = row

    # TODO: return rendered tikz image
    return total


def dyckpaths_by_n_r(n,r):
    images = []
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
        #im.save(f"dyck_paths/{path}.png")
        images.append(im)
    return images

def fullparentheses_by_n_r(n,r):
    images = []
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
        images.append(im)
    return images

def domino_tiling_by_n(n):
    images = []
    paths = SequenceGenerator.fibbonaci_sequence(n)
    for path in paths:
        size = 100*len(path)
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

def starfolkspaths_by_n_r(n, r):
    images = []
    paths = SequenceGenerator.binary_strings(n, r)
    for path in paths:
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
        im.save(f"starfolkspaths/{path}.png")

        images.append(im)
    return images

def nonattackingrooks_by_n_r(n, r):
    images = []
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
        images.append(im)
    return images

def binarytrees_by_n_r(n,r):
    images = []
    paths = SequenceGenerator.Nariyana_sequence(n,r)
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
        images.append(im)
    return images

for i in range(3):
    fullparentheses_by_n_r(2,i)