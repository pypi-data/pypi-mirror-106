from .base_post_processor import BasePostProcessor


class TailCutterProcessor(BasePostProcessor):
    """"""

    def process(self, results):
        """"""

        processed_results = {}

        for k, v in results.items():
            processed_results[k] = [item for item in v if not item.is_tail]

        return processed_results
