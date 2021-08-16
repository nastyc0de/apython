import numpy as np
from PIL import Image

# create 3d numpy array of zeros, then replace zeros
data = np.zeros((4,5,3), dtype=np.uint8)
data[:] = [255,255,0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')