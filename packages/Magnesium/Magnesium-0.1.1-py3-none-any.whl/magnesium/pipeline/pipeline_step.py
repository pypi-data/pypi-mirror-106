class PipelineStep(object):
    """"""

    def __init__(self, func):
        """"""

        self.func = func
    
    def execute(self, data):
        """"""

        results = self.func(data)
        return results
