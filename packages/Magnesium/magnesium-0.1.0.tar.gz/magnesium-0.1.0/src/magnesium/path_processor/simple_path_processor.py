from .base_path_processor import BasePathProcessor
from magnesium.utils import SnapshootableStack
from magnesium.node import Tag, Attribute
from magnesium.query_path import QueryPath


class SimplePathProcessor(BasePathProcessor):
    """"""
    
    def __init__(self, query_marker_strategy=None, text_prop_name='text'):
        """"""

        self.query_marker_strategy = query_marker_strategy
        self.text_prop_name = text_prop_name
    
    def process(self, element):
        """"""

        stack = SnapshootableStack()
        query_paths = {}

        self.process_element(stack, query_paths, element)

        return query_paths
    
    def process_element(
        self,
        stack: SnapshootableStack,
        query_paths: dict,
        element
    ):
        """"""

        tag_name = element.tag
        tag = Tag(tag_name)
        attributes = element.attrib
        text = element.text.strip()

        stack.push(tag)

        queried_attributes = []

        for k, v in attributes.items():
            attribute = Attribute(k, v)
            if self.query_marker_strategy.check(v):
                queried_attributes.append(attribute)
            else:
                tag.add_attribute(attribute)

        for attribute in queried_attributes:
            var_name = self.query_marker_strategy.get(attribute.value)
            snapshot = stack.snapshot()
            query_path = QueryPath(snapshot, attribute.name)
            query_paths[var_name] = query_path

        if self.query_marker_strategy.check(text):
            var_name = self.query_marker_strategy.get(text)
            snapshot = stack.snapshot()
            query_path = QueryPath(snapshot, self.text_prop_name)
            query_paths[var_name] = query_path

        for child in element:
            self.process_element(stack, query_paths, child)

        stack.pop()
