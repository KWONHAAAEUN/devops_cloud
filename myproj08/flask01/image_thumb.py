# pip install pillow

from PIL import Image

im = Image.open("static/moon.jpg")
im.thumbnail((800, 600))
im.save("static/moon.jpg")
