from .base_post_processor import BasePostProcessor


class ListOfDictsProcessor(BasePostProcessor):
    """"""

    def process(self, results):
        """"""

        processed_results = []

        keys = list(results.keys())
        values = list(results.values())

        for j in range(len(values[0])):
            d = {}
            for i in range(len(keys)):
                d[keys[i]] = values[i][j]
            processed_results.append(d)

        return processed_results
