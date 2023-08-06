from xml.etree.ElementTree import XMLParser
from .dynamictreebuilder import DynamicTreeBuilder

class DynamicXmlParser(XMLParser):
    def __init__(self, *args, **kwargs):
        super(DynamicXmlParser, self).__init__(target=DynamicTreeBuilder(), *args, **kwargs)
