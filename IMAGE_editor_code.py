from PIL import Image, ImageEnhance, ImageFilter
import os

path = '../../images'
Pathout = './editedimgs'


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)

    factor = 1.5
    enhance = ImageEnhance.Contrast(edit)


    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{Pathout}/{clean_name}_edited.jpg")