from PIL import Image
import os

filename = r"test.png"
im = Image.open(filename)
if im.mode == "RGBA":
    im = im.convert("RGB")
new_filename = r"dog.pdf"
if not os.path.exists(new_filename):
    im.save(new_filename,"PDF",resolution=100.0)
