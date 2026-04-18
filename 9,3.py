from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_path, output_path, text="Watermark"):
    img = Image.open(input_path)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()

    draw.text((img.width - 200, img.height - 50), text,
              fill=(255, 255, 255, 128), font=font)

    img.save(output_path)

add_watermark('my_image.jpg', 'watermarked.jpg')