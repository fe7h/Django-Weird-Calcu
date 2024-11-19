from PIL import Image, ImageDraw, ImageFont
# from django.templatetags.static import static


def img_gen(text, link):

    img = Image.open(link)

    font_size = 100
    font_front = ImageFont.truetype('data/Impact.ttf', font_size)
    font_back = ImageFont.truetype('data/Impact.ttf', font_size * 1.1)

    draw = ImageDraw.Draw(img)

    x_center_front = img.width//2 - draw.textlength(text, font=font_front)//2
    x_center_back = img.width//2 - draw.textlength(text, font=font_back)//2
    y_bottom_front = img.height - (font_size * 1.5)
    y_bottom_back = img.height - (font_size * 1.5 * 1.1)

    draw.text((x_center_back, y_bottom_back), text, font=font_back, fill='black')
    draw.text((x_center_front, y_bottom_front), text, font=font_front, fill='white')

    if __name__ == '__main__':
        img.save()
        img.show()
        return None

    link = link[0:link.rfind('/')+1]+'answer.png'
    img.save(link)

    return link

if __name__ == '__main__':
    img_gen('test', '../static/calcu/img/meme.png')
