text = 'hello'

parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'\t<li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

# Forgetting a closing tag will cause issues with injection
# Need to outsource constructing HTML to Builder

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []
    
    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        
        for e in self.elements:
            lines.append(e.__str(indent + 1))
        
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)
    
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # afluent interface (allows chaining calls)
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)

    # breaking open/close principle in a way, but that is not a hard issue
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

# builder = HtmlBuilder('ul')
builder = HtmlBuilder.create('ul')
# example without chaining
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
# example with chaining
builder.add_child_fluent('li', 'hello')\
.add_child_fluent('li', 'world')
print('Ordinary builder:')
print(builder)