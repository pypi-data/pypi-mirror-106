from .base_post_processor import BasePostProcessor


class SpaceNormalizerProcessor(BasePostProcessor):
    """"""

    def process(self, results):
        """"""

        processed_results = {}

        for k, v in results.items():
            processed_results[k] = [item.strip() for item in v]

        return processed_results
