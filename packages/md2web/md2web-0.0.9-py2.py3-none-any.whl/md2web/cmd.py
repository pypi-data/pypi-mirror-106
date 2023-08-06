# *_*coding:utf-8 *_*
'''
Descri：
'''
import md2web
from os.path import basename
import fire


def run(md):
    with open(md, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = md2web.markdown(text)

    htmlname = basename(md).split('.')[0] + '.html'
    with open(htmlname, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)

if __name__ == '__main__':
    fire.Fire(run)