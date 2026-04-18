from PIL import Image

card = Image.open('postcard.jpg')
#обрезаем текст снизу
cropped = card.crop((50, 50, card.width - 50, card.height - 100))
cropped.save('cropped_postcard.jpg')

print(f"Было: {card.size}, стало: {cropped.size}")