from PIL import Image

img = Image.open('my_image.jpg')

new_size = (img.width // 3, img.height // 3)
small_img = img.resize(new_size)
small_img.save('small_image.jpg')

mirror_h = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_h.save('mirror_horizontal.jpg')

mirror_v = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_v.save('mirror_vertical.jpg')

print("Сохранено")