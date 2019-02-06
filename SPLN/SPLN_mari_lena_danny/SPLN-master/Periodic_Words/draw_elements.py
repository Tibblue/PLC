from subprocess import getoutput
from PIL import Image, ImageDraw, ImageFont

def main():
    'Obtenção de elementos'
    out = getoutput("cat pw.txt | awk -F \"[ \t]+\" '{print $1 \",\" $2 \",\" $4}'")
    elements = out.split("\n")
    
    for element in elements:
        elem = element.split(",")
        draw_element(elem[0], elem[1], elem[2])

def color(group):
    if group == '1': color = (171, 214, 128)
    elif group == '2': color = (255, 133, 51)
    elif group == '3': color = (0, 204, 153)
    elif group == '4': color = (51, 204, 204)
    elif group == '5': color = (128, 223, 255)
    elif group == '6': color = (0, 107, 179)
    elif group == '7': color = (230, 230, 0)
    elif group == '8': color = (102, 204, 255)
    elif group == '9': color = (255, 153, 153)
    else: color = (221, 153, 255)
    return color

def draw_element(cn, element, group):
    img = Image.new('RGB', (100, 100), color = color(group))

    d = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("fonts/coolvetica.ttf", 45)
    font_cn = ImageFont.truetype("fonts/coolvetica.ttf", 20)

    d.text((20,30), element, font=font, fill=(255,255,255))
    

    d.text((20,10), cn, font=font_cn, fill=(255,255,255))
    
    path = 'uploads/' + cn + '.png'
    
    img.save(path)

if __name__ == "__main__":
    main()
