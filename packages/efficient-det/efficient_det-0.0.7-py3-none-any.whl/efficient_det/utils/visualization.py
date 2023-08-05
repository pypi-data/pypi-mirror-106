from PIL import ImageDraw, ImageFont

fnt = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf")


def draw_boxes(img, box, fill_text):
    x_min, y_min, x_max, y_max = box

    draw = ImageDraw.Draw(img)
    draw.text((x_min, y_min), text=fill_text, fill="red", font=fnt)
    draw.line([(x_min, y_min), (x_min, y_max)], width=3)
    draw.line([(x_max, y_min), (x_max, y_max)], width=3)
    draw.line([(x_min, y_min), (x_max, y_min)], width=3)
    draw.line([(x_min, y_max), (x_max, y_max)], width=3)

    return img
