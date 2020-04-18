from os import path
from PIL import Image
import numpy as np
import os
import random
import wikipedia
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get data directory 
currdir = path.dirname(__file__)

mask_num = random.randint(1,4)
if mask_num == 1:
    mask = np.array(Image.open(path.join(currdir, "images/flower_3.jpeg")))
elif mask_num == 2:
    mask = np.array(Image.open(path.join(currdir, "images/cloud1.png")))
elif mask_num == 3:
    mask = np.array(Image.open(path.join(currdir, "images/heart.jpg")))
elif mask_num == 4:
    mask = np.array(Image.open(path.join(currdir, "images/star.jpg")))


stopwords = set(STOPWORDS)
font_num = random.randint(1,6)
if font_num == 1:
    font = path.join(currdir, 'fonts/Fondamento/Fondamento-Regular.ttf')
elif font_num == 2:
    font = path.join(currdir, 'fonts/Vidaloka/Vidaloka-Regular.ttf')
elif font_num == 3:
    font = path.join(currdir, 'fonts/Simonetta/Simonetta-Regular.ttf')
elif font_num == 4:
    font = path.join(currdir, 'fonts/Shadows_Into_Light/ShadowsIntoLight-Regular.ttf')
elif font_num == 5:
    font = path.join(currdir, 'fonts/Libre_Baskerville/LibreBaskerville-Regular.ttf')
elif font_num == 6:
    font = path.join(currdir, 'fonts/Advent_Pro/AdventPro-Regular.ttf')

title = wikipedia.search("The Rolling Stones")

# get wikipedia page for selected title
page = wikipedia.page(title)
text = page.content

wc = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 2, 
                max_words=1000,
                mask=mask,
                font_path=font, 
                relative_scaling=.5)
# generate word cloud
wc.generate(text)

# generate random number for color scheme of wc
color_num = random.randint(1,5)
if color_num == 1:
    wc.recolor(colormap=plt.cm.cividis, random_state=3)
elif color_num == 2:
    wc.recolor(colormap=plt.cm.inferno, random_state=3)
elif color_num == 3:
    wc.recolor(colormap=plt.cm.plasma, random_state=3)
elif color_num == 4:
    wc.recolor(colormap=plt.cm.magma, random_state=3)
elif color_num == 5:
    wc.recolor(colormap=plt.cm.viridis, random_state=3)

# create coloring from image
# image_colors = ImageColorGenerator(mask)
#plt.figure(figsize=[7,7])
#wc.recolor(color_func=multi_color_func, random_state=3)

wc.to_file(path.join(currdir, "wc.png"))
