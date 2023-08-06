from lxml import etree

from .base_prefab import BasePrefab

from magnesium.query_marker import DoubleCurlyQueryMarkerStrategy
from magnesium.path_processor import SimplePathProcessor
from magnesium.path_interpreter import XPathInterpreter
from magnesium.mapping import SimpleMapping
from magnesium.pipeline import (
    SchemaPipelineBuilder,
    ExtractorPipelineBuilder
)
from magnesium.extractor import XPathExtractor
from magnesium.post_processor import (
    SpaceNormalizerProcessor,
    TailCutterProcessor,
    ListOfDictsProcessor
)


class ListOfDictsPrefab(BasePrefab):
    """"""

    def __init__(
        self,
        schema_data=None,
        query_marker_strategy=DoubleCurlyQueryMarkerStrategy(),
        path_processor=SimplePathProcessor(),
        path_interpreter=XPathInterpreter(),
        mapping=SimpleMapping(),
        extractor_processor=XPathExtractor()
    ):
        """"""

        self.query_marker_strategy = query_marker_strategy
        self.path_processor = path_processor
        self.path_interpreter = path_interpreter
        self.mapping = mapping
        self.extractor_processor = extractor_processor

        self.set_schema_data(schema_data)
        
    def set_schema_data(self, v):
        self.schema_data = v

        schema_root = etree.fromstring(self.schema_data)

        schema_pipeline_builder = SchemaPipelineBuilder()
        schema_pipeline_builder.set_query_marker_strategy(
            self.query_marker_strategy
        ).set_text_prop_name(
            'text'
        ).set_path_processor(
            self.path_processor
        ).set_path_interpreter(
            self.path_interpreter
        ).set_mapping(
            self.mapping
        )

        schema_pipeline = schema_pipeline_builder.build()
        self.fit_mapping = schema_pipeline.execute(schema_root)

    def execute(self, sample_data):
        """"""

        sample_root = etree.fromstring(sample_data)

        space_normalizer_processor = SpaceNormalizerProcessor()
        tail_cutter_processor = TailCutterProcessor()
        list_of_dicts_processor = ListOfDictsProcessor()

        extractor_pipeline_builder = ExtractorPipelineBuilder()
        extractor_pipeline_builder.set_mapping(
            self.fit_mapping
        ).set_extractor(
            self.extractor_processor
        ).add_post_processor(
            tail_cutter_processor
        ).add_post_processor(
            space_normalizer_processor
        ).add_post_processor(
            list_of_dicts_processor
        )

        extractor_pipeline = extractor_pipeline_builder.build()
        results = extractor_pipeline.execute(sample_root)

        return results
