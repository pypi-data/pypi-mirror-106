from .base_path_interpreter import BasePathInterpreter


class XPathInterpreter(BasePathInterpreter):
    """"""

    def __init__(self, text_prop_name='text'):
        """"""

        self.text_prop_name = text_prop_name

    def interpret(self, expression):
        """"""

        path = ''
        
        for tag in expression.path:
            path += f'//{tag.name}'
            for attribute in tag.attributes:
                path += f'[@{attribute.name}="{attribute.value}"]'
        
        queried_prop = expression.queried_prop

        if queried_prop == self.text_prop_name:
            path += '/text()'
        else:
            path += f'/@{queried_prop}'

        return f'{path}'
