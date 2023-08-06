from .base_query_marker_strategy import BaseQueryMarkerStrategy


class DoubleCurlyQueryMarkerStrategy(BaseQueryMarkerStrategy):
    """"""

    def check(self, x):
        """"""

        return x.startswith('{{') and x.endswith('}}')
    
    def get(self, x):
        """"""

        return x[2:-2].strip()
