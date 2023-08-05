import os
import webbrowser
from .Tool import *

file = 'HtmlFrame.py'
path = __file__.strip(file)

class WebPage():
    def __init__(self):
        self.setup()
        
    def setup(self):
        self.web_lines = [
                '<!DOCTYPE html>',
                '<html>',
                '<head>',
                '</head>',
                '<body>',
                '</body>',
                '</html>']
        writeWebLines(self.web_lines)

    def saveHtml(self, save_path):
        self.allow_ext = ['.html', '.htm']
        if os.path.splitext(save_path)[1] in self.allow_ext:
            web_lines = loadWebLines()
            with open(save_path, 'w') as html:
                html.write('\n'.join(web_lines))
        else:
            raise ValueError('ExtError', f'File ext in argument "save_path" is not allowed. We only allow {",".join(allow_ext)}.')

    def openWeb(self):
        self.saveHtml(path+'web-tmp/tmp.html')
        webbrowser.open(os.path.realpath(path+'web-tmp/tmp.html'))

    def setTitle(self, title):
        head_line = getPos('/head')
        code = f'<title>{title}</title>'
        self.web_lines.insert(head_line, code)
        writeWebLines(self.web_lines)

    def setMeta(self, **args):
        head_line = getPos('/head')
        argstr = dictToArgs(args)
        code = f'<meta{argstr} />'
        self.web_lines.insert(head_line, code)
        writeWebLines(self.web_lines)

    def setBase(self, **args):
        head_line = getPos('/head')
        argstr = dictToArgs(args)
        code = f'<base{argstr} />'
        self.web_lines.insert(head_line, code)
        writeWebLines(self.web_lines)
    
    def setBaseFont(self, **args):
        head_line = getPos('/head')
        argstr = dictToArgs(args)
        code = f'<basefont{argstr} />'
        self.web_lines.insert(head_line, code)
        writeWebLines(self.web_lines)

    def link(self, **args):
        head_line = getPos('/head')
        argstr = dictToArgs(args)
        code = f'<link{argstr} />'
        self.web_lines.insert(head_line, code)
        writeWebLines(self.web_lines)
