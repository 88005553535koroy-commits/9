from PIL import Image, ImageFilter
import os

os.makedirs('filtered_images', exist_ok=True)

for i in range(1, 6):
    img = Image.open(f'{i}.jpg')

    filtered = img.filter(ImageFilter.SHARPEN)
    filtered.save(f'filtered_images/filtered_{i}.jpg')
    print(f'Обработан {i}.jpg')

print("Все файлы обработаны")