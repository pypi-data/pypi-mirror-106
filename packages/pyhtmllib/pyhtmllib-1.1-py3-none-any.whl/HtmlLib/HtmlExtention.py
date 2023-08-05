from .Tool import *


class HtmlStyleSheet():
    def __init__(self, content=''):
        self.content = content
        self.name = 'style'
        self.setup()

    def setup(self):
        self.code = f'<{self.name}>{self.content}</{self.name}>'
    
    def render(self):
        self.web_lines = loadWebLines()
        head_line = getPos('/body')
        self.web_lines.insert(head_line, self.code)
        writeWebLines(self.web_lines)
    
    def addBlock(self, for_, block):
        self.block = '''%s{%s}'''%(for_, block)
        self.content += self.block
        self.setup()


class HtmlScript():
    def __init__(self, content='', type='text/javascript'):
        self.content = content
        self.name = 'script'
        self.type = type
        self.setup()

    def setup(self):
        self.code = f'<{self.name} type="{self.type}">{self.content}</{self.name}>'
    
    def render(self):
        self.web_lines = loadWebLines()
        head_line = getPos('/body')
        self.web_lines.insert(head_line, self.code)
        writeWebLines(self.web_lines)
    
    def addBlock(self, for_, block):
        self.block = '''%s{%s}'''%(for_, block)
        self.content += self.block
        self.setup()


class HtmlComment():
    def __init__(self, content=''):
        self.content = content
        self.setup()
        self.render()

    def setup(self):
        self.code = f'<!--{self.content}-->'
    
    def render(self):
        self.web_lines = loadWebLines()
        head_line = getPos('/body')
        self.web_lines.insert(head_line, self.code)
        writeWebLines(self.web_lines)