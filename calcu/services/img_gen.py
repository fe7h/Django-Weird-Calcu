import os
import io

from PIL import Image, ImageDraw, ImageFont


def img_gen(text: str, path: str) -> io.BytesIO:

    img = Image.open(path)

    font_size = 100
    font_path = os.path.join(os.path.dirname(__file__), 'data/Impact.ttf')
    font = ImageFont.truetype(font_path, font_size)

    draw = ImageDraw.Draw(img)

    x = img.width//2 - draw.textlength(text, font=font)//2
    y = img.height - (font_size * 1.5)

    draw.text((x, y), text, font=font, fill='white')

    buf = io.BytesIO()

    img.save(buf, format='png')
    buf.seek(0)

    return buf


if __name__ == '__main__':
    img_data = img_gen('test', 'data/meme.png')
    Image.open(img_data).show()
