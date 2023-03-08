import os

from PIL import Image

dataset_folder = "CARPK_devkit"

os.chdir("..")
os.chdir(os.path.join(dataset_folder, "data", "Images"))

listdir = os.listdir()
for file in listdir:
    filename = file.split('.')[0]
    print(filename)
    im1 = Image.open(file)
    im1.save(f'../Images-converted/{filename}.jpg')

