from .base_post_processor import BasePostProcessor
import pandas as pd


class PandasDataFrameProcessor(BasePostProcessor):
    """"""
    
    def process(self, results):
        """"""
        
        processed_results = pd.DataFrame(results)        
        return processed_results
