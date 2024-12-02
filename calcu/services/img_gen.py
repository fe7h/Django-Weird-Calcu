from PIL import Image, ImageDraw, ImageFont
import os
import io

def img_gen(text, link):

    img = Image.open(link)

    font_size = 100
    font_path = os.path.join(os.path.dirname(__file__),'data/Impact.ttf')
    font_front = ImageFont.truetype(font_path, font_size)
    font_back = ImageFont.truetype(font_path, font_size * 1.1)

    draw = ImageDraw.Draw(img)

    x_center_front = img.width//2 - draw.textlength(text, font=font_front)//2
    x_center_back = img.width//2 - draw.textlength(text, font=font_back)//2
    y_bottom_front = img.height - (font_size * 1.5)
    y_bottom_back = img.height - (font_size * 1.5 * 1.1)

    draw.text((x_center_back, y_bottom_back), text, font=font_back, fill='black')
    draw.text((x_center_front, y_bottom_front), text, font=font_front, fill='white')

    if __name__ == '__main__':
        img.show()
        return None

    buf = io.BytesIO()

    img.save(buf,format='png')
    buf.seek(0)

    return buf

if __name__ == '__main__':
    img_gen('test', '../static/calcu/img/meme.png')
