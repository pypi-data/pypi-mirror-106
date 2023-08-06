from .base_mapping import BaseMapping


class SimpleMapping(BaseMapping):
    """"""
    
    def __init__(self, path_interpreter=None):
        """"""

        self.path_interpreter = path_interpreter
        
    def create_map(self, query_paths):
        """"""

        results = {}
        for k, v in query_paths.items():
            results[k] = self.path_interpreter.interpret(v)
        return results
