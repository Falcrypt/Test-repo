from PIL import Image
import os

img = Image.open("images/sample.jpg")

img.save("compressed/sample_compressed.jpg", "JPEG", quality=30)

print("Image compressed successfully!")
