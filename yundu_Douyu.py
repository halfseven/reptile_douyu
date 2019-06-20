import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,ImageColorGenerator

text = open('./douyu.txt', 'r').read()
cut_text = jieba.cut(text)
result = " ".join(cut_text)
wc = WordCloud(
        font_path='Pagul.ttf',
        background_color='white',
        width=1000,
        height=600,
        max_font_size=50,
        min_font_size=10,
        mask=plt.imread('douyu.jpg'),
        max_words=1000
    )
image_colors = ImageColorGenerator(plt.imread('douyu.jpg'))
wc.generate(result)
wc.to_file('wordcloudtest.png')
plt.figure('wordcloudtest')
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.show()