class Pipeline(object):
    """"""

    def __init__(self, steps):
        """"""

        self.steps = steps
    
    def execute(self, data):
        """"""

        results = data

        for step in self.steps:
            results = step.execute(results)

        return results
