from .base_extractor import BaseExtractor


class XPathExtractor(BaseExtractor):
    """"""
    
    def __init__(self, mapping=None):
        """"""

        self.mapping = mapping

    def extract(self, data):
        """"""

        results = {}

        for k, v in self.mapping.items():
            results[k] = data.xpath(v)

        return results
