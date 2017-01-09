#Author: Lee, Handong(hansleo)

from PIL import Image

img = Image.open('/your/picture').convert('LA')
img.save('grayscale_img.png')
