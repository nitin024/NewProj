from PIL import Image
filename = r'C:\\IMEX255\\deploy.png'
img = Image.open(filename)
img.save('deploy.ico')

# ====================

# Optionally, you may specify the icon sizes you want:


#icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
icon_sizes = [(16,16),(32, 32),(48, 48),(64, 64), (128, 128), (255, 255)]
img.save('deploy.ico', sizes=icon_sizes)