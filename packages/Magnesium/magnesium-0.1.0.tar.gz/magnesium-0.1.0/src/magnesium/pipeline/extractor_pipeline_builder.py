from .base_pipeline_builder import BasePipelineBuilder
from .pipeline import Pipeline
from .pipeline_step import PipelineStep


class ExtractorPipelineBuilder(BasePipelineBuilder):
    """"""

    def __init__(self):
        """"""

        self.post_processors = []

    def set_mapping(self, v):
        """"""

        self.mapping = v
        return self

    def set_extractor(self, v):
        """"""

        self.extractor = v
        return self

    def add_post_processor(self, v, i=None):
        """"""

        if i is None:
            self.post_processors.append(v)
        else:
            self.post_processors.insert(i, v)
        return self

    def build(self):
        """"""

        self.extractor.mapping = self.mapping

        extractor_step = PipelineStep(
            self.extractor.extract
        )

        post_processor_steps = [
            PipelineStep(post_processor.process)
            for post_processor in self.post_processors
        ]

        steps = [
            extractor_step,
            *post_processor_steps
        ]

        return Pipeline(
            steps=steps
        )
