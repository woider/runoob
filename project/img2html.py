from io import BytesIO
from PIL import Image
from PIL import ImageFilter
from urllib import request

TEMPLATE = '''
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


class Converter(object):
    def __init__(self, word='田', size=100):
        self.word, self.size = word, size

    # 读取url内容
    def __network(self, url):
        return request.urlopen(url).read()

    # 处理图片信息
    def __handle(self, binary):
        img = Image.open(BytesIO(binary))  # 打开制图片
        img.thumbnail((self.size, self.size))  # 压缩图片
        img.filter(ImageFilter.DETAIL)  # 图片增强
        return img

    # 分析图片像素
    def __analysis(self, img):
        width, height = img.size
        piexl = img.load()  # 提取像素点
        body, font = '', '<font color="{color}">{word}</font>'
        for y in range(height):
            for x in range(width):
                r, g, b = piexl[x, y]
                body += font.format(
                    color='#{:02x}{:02x}{:02x}'.format(r, g, b),
                    word=self.word[((y * width + x) % len(self.word))]
                )
            body += '\n<br />\n'
        return body

    # 写入文件内容
    def __writefile(self, file, str):
        fo = open(file, 'w', encoding='utf8')
        try:
            fo.write(str)
        except IOError:
            raise Exception
        finally:
            fo.close()

    # 生成html文档
    def buildDOC(self, url, output):
        try:
            binary = self.__network(url)
            img = self.__handle(binary)
            body = TEMPLATE.format(
                title=self.word,
                body=self.__analysis(img),
                size=self.size
            )  # 向模板中填充数据
            self.__writefile(output, body)
        except Exception as err:
            print('Error:', err)
            return False
        else:
            print('Successful!')
            return True
