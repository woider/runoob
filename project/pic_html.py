
import urllib.request
from io import BytesIO
from PIL import Image
from PIL import ImageFilter

# HTML 模板
html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            line-height: 1em;
            letter-spacing: 0;
            font-size: 0.6rem;
            background: black;
            text-align: center;
            min-width: {size}em;
        }}
    </style>
</head>
<body>
    {body}
</body>
</html>
'''

word = '蘑菇'  # 文字块
size = 300  # 压缩率
url = 'http://img.67.com/upload/images/2014/12/14/bGlxaW5nMTQxODUxOTk0OQ==_3.jpg'
out = 'index.html'

# 获取二进制图片
binary = urllib.request.urlopen(url).read()

# 加载二进制图片
img = Image.open(BytesIO(binary))

# 压缩图像
img.thumbnail((size, size))

# 图像增强
img = img.filter(ImageFilter.DETAIL)

# 获取图像信息
width, height = img.size

body, font = '', '<font color="{color}">{word}</font>'

# 提取像素点
piexl = img.load()
for y in range(height):
    for x in range(width):
        r, g, b = piexl[x, y]
        body += font.format(
            color='#{:02x}{:02x}{:02x}'.format(r, g, b),
            word=word[((y * width + x) % len(word))]
        )
    body += '\n<br />\n'

# 文件存储
fo = open(out, 'w', encoding='utf8')
fo.write(html.format(title=word, body=body, size=size * 0.8))
fo.close()


def rgb2hex(rgbcolor):
    r, g, b = rgbcolor
    return (r << 16) + (g << 8) + b
