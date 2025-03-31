import os
import io

from PIL import Image, ImageDraw, ImageFont


def draw_text_on_img_bottom(text: str, path: str) -> io.BytesIO:
    """Uses Impact font and draws text at the bottom of the image.

    Args:
        text (text)
        path (str): Path to image.

    Returns:
        io.BytesIO: Contains an image in png format.
    """
    img = Image.open(path)

    font_size = 100
    font_path = os.path.join(os.path.dirname(__file__), 'fonts/Impact.ttf')
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
    img_data = draw_text_on_img_bottom('test', 'data/meme.png')
    Image.open(img_data).show()
