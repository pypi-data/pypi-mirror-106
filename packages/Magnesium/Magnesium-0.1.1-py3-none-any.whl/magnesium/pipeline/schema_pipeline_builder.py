from .base_pipeline_builder import BasePipelineBuilder
from .pipeline import Pipeline
from .pipeline_step import PipelineStep


class SchemaPipelineBuilder(BasePipelineBuilder):
    """"""

    def __init__(self):
        """"""

        self.post_processors = []

    def set_query_marker_strategy(self, v):
        """"""

        self.query_marker_strategy = v
        return self

    def set_text_prop_name(self, v):
        """"""

        self.text_prop_name = v
        return self

    def set_path_processor(self, v):
        """"""

        self.path_processor = v
        return self

    def set_path_interpreter(self, v):
        """"""

        self.path_interpreter = v
        return self

    def set_mapping(self, v):
        """"""

        self.mapping = v
        return self

    def build(self):
        """"""

        self.path_processor.query_marker_strategy = self.query_marker_strategy
        self.path_processor.text_prop_name = self.text_prop_name
        path_processor_step = PipelineStep(self.path_processor.process)

        self.path_interpreter.text_prop_name = self.text_prop_name
        self.mapping.path_interpreter = self.path_interpreter
        mapping_step = PipelineStep(self.mapping.create_map)

        steps = [
            path_processor_step,
            mapping_step,
        ]

        return Pipeline(steps=steps)
